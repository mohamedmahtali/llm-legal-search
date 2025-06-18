# ⚖️ Moteur de Recherche Juridique IA

> Une interface intelligente pour effectuer des recherches juridiques enrichies à l'aide de LLMs (HuggingFace) et Elasticsearch.

---

## 📚 Description

Cette application permet aux utilisateurs d'effectuer des recherches juridiques en langage naturel. Les résultats sont enrichis à l'aide d'un LLM pour générer des résumés pertinents.

**Technologies utilisées :**
- 🧠 LLM (HuggingFace)
- 🔍 Elasticsearch
- 🧰 Scraper de décisions juridiques simulées
- 🧪 FastAPI (backend)
- 🖼️ Gradio (frontend)
- 🐳 Docker & Docker Compose

---

## 📦 Structure du projet

```
llm-legal-search/
├── backend/               # API FastAPI
│   └── app/
├── frontend/              # Interface Gradio
│   └── app/
├── scraper/               # Scraping et indexation
├── docker-compose.yml     # Orchestration des services
├── requirements.txt       # Dépendances
└── README.md              # Documentation
```

---

## 🚀 Lancement rapide (via Docker)

### 1. Cloner le projet

```bash
git clone https://github.com/ton-repo/llm-legal-search.git
cd llm-legal-search
```

### 2. Lancer les conteneurs

```bash
sudo docker compose up --build -d
```

Cela lancera :
- Elasticsearch
- Kibana (si activé)
- Backend FastAPI
- Frontend Gradio
- Scraper (indexation initiale)

### 3. Accéder à l'interface

Accède à Gradio via :  
👉 `http://<votre-ip-publique>:7860`  
Exemple : `http://54.81.246.252:7860`

---

## 🧪 Exemple d'utilisation

Tapez simplement :

```
Cassation
```

Et recevez un ensemble de décisions pertinentes avec :
- Titre
- Score de pertinence
- Résumé enrichi

---

## 🔧 Configuration personnalisée

- ✅ Backend : `http://backend:8000`
- ✅ Endpoint de recherche enrichie : `/search_enriched?q=...`

> ⚠️ Assurez-vous que les conteneurs se parlent en réseau Docker (ex: `http://backend:8000` depuis le frontend).

---

## 🔐 Sécurité

- Par défaut, l'accès est non sécurisé (HTTP).
- Il est recommandé d'ajouter un reverse proxy Nginx + HTTPS (Let’s Encrypt).
- Pensez à désactiver l’option `share=True` dans Gradio si vous exposez publiquement.

---

## 🛠️ Dépendances principales

```txt
gradio==4.28.3
fastapi==0.110.0
pydantic==2.6.4
```

---

## 🙌 Contributions

Pull requests bienvenues !  
Ajoutez un test ou un exemple si vous proposez une nouvelle fonctionnalité.

---

## 📄 Licence

MIT - Feel free to use and adapt.
