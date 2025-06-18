# 📦 Image de base légère avec Python 3.11
FROM python:3.11-slim

# 🔧 Installation des dépendances système (si nécessaire pour certains packages Python compilés)
RUN apt-get update && apt-get install -y \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# 📁 Répertoire de travail dans le conteneur
WORKDIR /app

# 📄 Copier les dépendances Python
COPY requirements.txt ./requirements.txt

# 📦 Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copier le code source du frontend Gradio
COPY app ./app

# 🌐 Exposer le port sur lequel Gradio écoute
EXPOSE 7860

# 🚀 Lancer le frontend Gradio
CMD ["python", "app/frontend_gradio.py"]
