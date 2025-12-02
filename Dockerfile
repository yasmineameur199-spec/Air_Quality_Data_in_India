FROM python:3.10-slim

# 1. Dossier de travail
WORKDIR /app

# 2. Copier les dépendances
COPY requirements.txt .

# 3. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier tout le projet
COPY . .

# 5. Exposer le port Cloud Run
EXPOSE 8080

# 6. Démarrer FastAPI avec le port fourni par Cloud Run
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]

