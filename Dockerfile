# 1. Usar una imagen oficial de Python ligera
FROM python:3.12-slim

# 2. Crear una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar la lista de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo tu código al contenedor
COPY . .

# 5. El comando que se ejecutará al encender el contenedor
CMD ["python", "main.py"]
