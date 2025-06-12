# Frontend Gradio - Dockerfile

FROM python:3.11-slim

# Installer dépendances système (optionnel si besoin de build C++ / wheels)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Créer répertoire app
WORKDIR /app

# Copier requirements
COPY requirements.txt /app/requirements.txt

# Installer requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source frontend
COPY app /app/app

# Exposer port Gradio
EXPOSE 7860

# Commande de démarrage Gradio
CMD ["python", "app/frontend_gradio.py"]
