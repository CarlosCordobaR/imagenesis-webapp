FROM python:3.11.4-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para Pillow
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --upgrade pip && \
    pip install --only-binary=Pillow -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 10000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "app:application", "-c", "gunicorn.conf.py"]
