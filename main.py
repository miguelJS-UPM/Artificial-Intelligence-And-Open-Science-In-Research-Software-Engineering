import os
import time
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Configuración
GROBID_URL = os.environ.get("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")
DATA_DIR = "data"

def wait_for_grobid():
    """Espera hasta que Grobid esté completamente encendido y respondiendo"""
    print("Esperando a que Grobid despierte (puede tardar unos 15 segundos)...")
    base_url = GROBID_URL.split('/api/')[0] + '/api/isalive'
    
    for i in range(30): # Intenta durante 30 segundos
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                print("¡Grobid está listo y escuchando!\n")
                return True
        except requests.ConnectionError:
            pass # Si da error de conexión, simplemente lo ignoramos y seguimos esperando
        
        time.sleep(1) # Esperamos 1 segundo antes de volver a preguntar
        
    return False

def process_pdfs():
    abstracts_text = ""
    figures_count = {}
    links_per_paper = {}

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            print(f"Procesando: {filename}...")
            filepath = os.path.join(DATA_DIR, filename)
            
            with open(filepath, "rb") as f:
                files = {"input": (filename, f, "application/pdf")}
                response = requests.post(GROBID_URL, files=files)
            
            if response.status_code == 200:
                xml_data = response.text
                soup = BeautifulSoup(xml_data, "xml")
                
                # 1. Extraer el Abstract
                abstract_tag = soup.find("abstract")
                if abstract_tag:
                    abstracts_text += abstract_tag.get_text(separator=" ", strip=True) + " "
                
                # 2. Contar Figuras
                figures = soup.find_all("figure")
                image_figures = [fig for fig in figures if fig.get("type") != "table"]
                figures_count[filename] = len(image_figures)
                
                # 3. Extraer Enlaces (Links)
                links = []
                for tag in soup.find_all(["ptr", "ref"]):
                    if tag.has_attr("target") and tag["target"].startswith("http"):
                        links.append(tag["target"])
                links_per_paper[filename] = list(set(links))
            else:
                print(f"Error procesando {filename}. Código de estado: {response.status_code}")

    return abstracts_text, figures_count, links_per_paper

def generate_wordcloud(text):
    print("\nGenerando nube de palabras...")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('wordcloud.png')
    plt.close()
    print(" -> Creado: 'wordcloud.png'")

def generate_figure_chart(figures_dict):
    print("Generando gráfico de figuras...")
    papers = list(figures_dict.keys())
    counts = list(figures_dict.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(papers, counts, color='skyblue')
    plt.xlabel('Artículos')
    plt.ylabel('Número de Figuras')
    plt.title('Número de figuras por artículo')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('figures_chart.png')
    plt.close()
    print(" -> Creado: 'figures_chart.png'")

def save_links(links_dict):
    print("Guardando lista de enlaces...")
    with open('links.txt', 'w', encoding='utf-8') as f:
        for paper, links in links_dict.items():
            f.write(f"--- Enlaces en {paper} ---\n")
            if not links:
                f.write("  (No se encontraron enlaces)\n")
            for link in links:
                f.write(f"  - {link}\n")
            f.write("\n")
    print(" -> Creado: 'links.txt'")

if __name__ == "__main__":
    print("Iniciando contenedor de análisis...\n")
    
    # 1. Obligamos a Python a esperar a Grobid
    if not wait_for_grobid():
        print("Error crítico: Grobid no respondió después de 30 segundos. Saliendo...")
        exit(1)
        
    # 2. Ejecutamos el pipeline normal
    abstracts, figures, links = process_pdfs()
    
    if abstracts:
        generate_wordcloud(abstracts)
    if figures:
        generate_figure_chart(figures)
    if links:
        save_links(links)
        
    print("\n¡Análisis completado con éxito dentro de Docker!")