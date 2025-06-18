import os
import json
from elasticsearch import Elasticsearch

print("🚀 Début de l'indexation...")

# Connexion à Elasticsearch (dynamique selon env)
try:
    elastic_url = os.getenv("ELASTIC_URL", "http://localhost:9200")
    es = Elasticsearch(hosts=[elastic_url])
    if not es.ping():
        raise ValueError("Elasticsearch ne répond pas")
    print(f"✅ Connexion à Elasticsearch réussie ({elastic_url})")
except Exception as e:
    print(f"❌ ERREUR de connexion à Elasticsearch : {e}")
    exit(1)

# Nom de l'index
index_name = "legal_docs"

# Mapping
index_body = {
    "mappings": {
        "properties": {
            "title": {"type": "text", "analyzer": "standard"},
            "content": {"type": "text", "analyzer": "standard"},
            "date": {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time||epoch_millis"}
        }
    }
}

# Supprimer l'index s'il existe
try:
    if es.indices.exists(index=index_name):
        print(f"🧹 Suppression de l'index existant '{index_name}'...")
        es.indices.delete(index=index_name)
        print("✅ Index supprimé.")
except Exception as e:
    print(f"❌ ERREUR lors de la suppression de l'index : {e}")
    exit(1)

# Créer l'index
try:
    print(f"📦 Création de l'index '{index_name}'...")
    es.indices.create(index=index_name, body=index_body)
    print("✅ Index créé.")
except Exception as e:
    print(f"❌ ERREUR création de l'index : {e}")
    exit(1)

# Dataset path
dataset_path = os.getenv("DATASET_PATH")
if dataset_path is None:
    dataset_path = "./shared_data/dataset.json" if os.path.exists("./shared_data/dataset.json") else "/shared_data/dataset.json"

print(f"📄 Chemin du dataset utilisé : {dataset_path}")

# Charger les documents
try:
    with open(dataset_path, encoding="utf-8") as f:
        documents = json.load(f)
    print(f"✅ {len(documents)} documents chargés.")
except FileNotFoundError:
    print(f"❌ ERREUR : fichier {dataset_path} introuvable.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ ERREUR JSON dans {dataset_path} : {e}")
    exit(1)

# Indexation
for i, doc in enumerate(documents):
    try:
        es.index(index=index_name, body=doc)
        if i < 5 or i == len(documents) - 1:
            print(f"📌 Document {i+1}/{len(documents)} indexé.")
    except Exception as e:
        print(f"❌ ERREUR indexation document {i+1} : {e}")

print("🎉 Fin de l'indexation.")

