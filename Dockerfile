# Autor: DAVID H. CUEVAS SALGADO
# RUT: 13.465.553-4
# Evaluación Parcial 3 - OCY1102
# Dockerfile para aplicación Flask vulnerable

FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copia archivos
COPY requirements.txt .
COPY src/ .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crea la base de datos
RUN python create_db.py

# Expone puerto
EXPOSE 5000

# Variable de entorno
ENV FLASK_APP=vulnerable_flask_app.py

# Ejecuta la aplicación
CMD ["python", "vulnerable_flask_app.py"]