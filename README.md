# Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering

[![Documentation Status](https://readthedocs.org/projects/ciencia-abierta-miguel/badge/?version=latest)](https://ciencia-abierta-miguel.readthedocs.io/es/latest/?v=final)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18880539.svg)](https://doi.org/10.5281/zenodo.18880539)

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

### Opción B: Entorno virtual local (Python)
1. Requiere Python 3.x instalado.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta Grobid localmente en el puerto 8070.
4. Ejecuta el script principal: `python main.py`

## Metodología de Validación
Para validar los resultados obtenidos:
- **Nube de palabras:** Buscando una de las palabras más grande, "framework" archivo por archivo, salen en numerosas ocasiones, especialmente en el "2603.03233v1.pdf" con un total de 76 veces, en el resto mantiene una media de 10/20 y algunos entre 0/5.
- **Conteo de figuras:** Si abrimos los PDFs de manera manual y contamos las figuras y las explicaciones de las mismas, vemos que coincide con la gráfica de barras generada.
- **Extracción de enlaces:** Abriendo el archivo, copiando las URLs generadas y comprobandolas, son válidas y no salta ningún tipo de error.

## Limitaciones
- El análisis depende de la precisión de Grobid para parsear la estructura del PDF.

## Licencia
Este proyecto está bajo la licencia Apache 2.0.