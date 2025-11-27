# 1. Image Python légère
FROM python:3.10-slim

# 2. Dossier de travail
WORKDIR /app

# 3. Copier les dépendances
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du projet
COPY . .

# 6. Exposer le port
EXPOSE 8000

# 7. Lancer FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
