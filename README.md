# ⚖️ Moteur de Recherche Juridique IA

## 🎯 Objectif

Créer un moteur de recherche intelligent pour documents juridiques, enrichi par un LLM pour résumer les résultats.

Ce projet démontre :

✅ Stack Full-Stack Python  
✅ Moteur de recherche Elastic + NLP  
✅ Interface Web simple  
✅ Conteneurisation complète → DevOps Ready  
✅ Scalable et cloud ready (Kubernetes, AWS, Terraform à venir)

---

## 🗺️ Architecture

+---------------------+                     +-------------------+
|  User (Web Browser) |  --> Port 7860 -->   |     Frontend      |
|  (Gradio UI)        |                     |    (Gradio App)   |
+---------------------+                     +-------------------+
                                                  |
                                                  | REST call
                                                  v
+---------------------+                     +-------------------+
|                     |  --> Port 8000 -->   |     Backend       |
|   Internal Network  |                     |   FastAPI App     |
+---------------------+                     +-------------------+
                                                  |
                                                  | Elasticsearch queries
                                                  v
+---------------------+                     +-------------------+
|   Elasticsearch     |  --> Port 9200 -->   | Elastic Engine    |
+---------------------+                     +-------------------+
                                                  |
                                                  |
+---------------------+                     +-------------------+
|       Kibana        |  --> Port 5601 -->   |   Visualization   |
+---------------------+                     +-------------------+



---

## 🛠️ Stack technique

| Composant      | Technologie            |
|----------------|------------------------|
| Backend API    | Python + FastAPI       |
| Frontend UI    | Gradio (simple UI)     |
| Search Engine  | Elasticsearch 8.13.4   |
| Visualisation  | Kibana 8.13.4          |
| LLM            | HuggingFace Transformers (distilbart-cnn-12-6) |
| DevOps         | Docker Compose, Networks, Volumes |
| Cloud Ready    | AWS EC2, S3, Terraform  |

---

## 🚀 Lancement local

```bash

# Arrêter et nettoyer
make down

# Construire les images
make build

# Démarrer l'application
make up

# Voir les logs
make logs



| Méthode | Route                      | Description                      |
| ------- | -------------------------- | -------------------------------- |
| GET     | `/`                        | Health check                     |
| GET     | `/search?q=query`          | Recherche basique Elastic        |
| GET     | `/search_enriched?q=query` | Recherche enrichie (LLM summary) |
| POST    | `/enrich` (body: text)     | Résumer un texte                 |


