# Autor: DAVID H. CUEVAS SALGADO
# RUT: [Tu RUT]
# Evaluación Parcial 3 - OCY1102
# Dockerfile para aplicación Flask CORREGIDA

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY src/ .

RUN pip install --no-cache-dir -r requirements.txt

RUN python create_db.py

EXPOSE 5000

ENV FLASK_APP=secure_flask_app.py

# CORRECCION: Usa la version corregida
CMD ["python", "secure_flask_app.py"]