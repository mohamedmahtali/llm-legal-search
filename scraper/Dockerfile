# Image de base légère avec Python
FROM python:3.11-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier de travail
WORKDIR /app

# Copier les dépendances Python
COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le code source
COPY app /app

# Par sécurité : marquer app/ comme package
RUN touch /app/__init__.py

# Commande de démarrage : exécuter le scraper en tant que module
CMD ["python", "main_scraper.py"]

