# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) 
*(Nota: Cambiaremos este enlace cuando generemos el DOI real en Zenodo al final)*

## Descripción
Este proyecto analiza 10 artículos científicos de acceso abierto utilizando la herramienta Grobid. El pipeline extrae texto estructurado de PDFs y genera:
1. Una nube de palabras clave basada en los abstracts.
2. Una visualización del número de figuras por artículo.
3. Una lista de todos los enlaces (URLs) encontrados en los artículos.

## Entorno Computacional y Reproducibilidad
Para asegurar la reproducibilidad, este proyecto proporciona dos formas de ejecución:

### Opción A: Usando Docker (Recomendado)
1. Clona este repositorio.
2. Ejecuta `docker-compose up -d` para levantar el servicio de Grobid y el entorno del script.
*(Añadiremos los comandos exactos más adelante)*

### Opción B: Entorno virtual local (Python)
1. Requiere Python 3.x instalado.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta Grobid localmente en el puerto 8070.
4. Ejecuta el script principal: `python main.py`

## Metodología de Validación
*(El enunciado pide explícitamente esto)*
Para validar los resultados obtenidos:
- **Nube de palabras:** [Explicarás aquí cómo verificaste que las palabras tengan sentido, por ejemplo, eliminando 'stop words'].
- **Conteo de figuras:** [Explicarás aquí cómo abriste un par de PDFs manualmente para contar las figuras y comprobar que tu código daba el mismo número].
- **Extracción de enlaces:** [Explicarás aquí si comprobaste manualmente que las URLs extraídas son válidas].

## Limitaciones
- El análisis depende de la precisión de Grobid para parsear la estructura del PDF.
- [Añade aquí otras limitaciones que encuentres al programar].

## Licencia
Este proyecto está bajo la licencia Apache 2.0.