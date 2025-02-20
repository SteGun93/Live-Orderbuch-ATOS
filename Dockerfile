FROM python:3.9-slim

WORKDIR /app

# Kopieren der requirements.txt zuerst für besseres Layer Caching
COPY requirements.txt .

# Python-Abhängigkeiten installieren
RUN python -m venv venv && \
    . /app/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Setzen des Python-Pfads
ENV PATH="/app/venv/bin:$PATH"

# Umgebungsvariable setzen
ENV DEBUG=True

EXPOSE 5000

CMD ["python", "main.py"]