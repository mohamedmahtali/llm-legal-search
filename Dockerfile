# Image de base légère avec Python
FROM python:3.11-slim

# Installer quelques dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'app
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'app
COPY app /app

# Exposer le port
EXPOSE 8000

# Commande de lancement de l'API
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
