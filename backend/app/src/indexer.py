from elasticsearch import Elasticsearch, exceptions
import json
import os
import time

# Lecture de l'URL Elastic
elastic_url = os.getenv("ELASTIC_URL", "http://localhost:9200")
print(f"🔗 Connecting to Elasticsearch at {elastic_url}")

# Création du client Elasticsearch
es = Elasticsearch(elastic_url)

# Fonction pour attendre qu'Elasticsearch soit prêt
def wait_for_elasticsearch(es_client, timeout=60):
    for i in range(timeout):
        try:
            health = es_client.cluster.health()
            if health["status"] in ("green", "yellow"):
                print(f"✅ Elasticsearch cluster health is OK: {health['status']}")
                return True
        except exceptions.ConnectionError:
            pass
        print(f"⏳ Waiting for Elasticsearch... ({i+1}s)")
        time.sleep(1)
    print("❌ ERROR: Elasticsearch is not reachable after timeout.")
    return False

# Attendre que ES soit prêt
if not wait_for_elasticsearch(es):
    exit(1)

# Définir le mapping
index_name = "documents"
index_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "analysis": {
            "analyzer": {
                "default": {
                    "type": "standard"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "standard"
            },
            "content": {
                "type": "text",
                "analyzer": "standard"
            },
            "date": {
                "type": "date",
                "format": "yyyy-MM-dd||strict_date_optional_time||epoch_millis"
            }
        }
    }
}

# Supprimer l'index s'il existe
try:
    if es.indices.exists(index=index_name):
        print(f"Deleting existing index '{index_name}'...")
        es.indices.delete(index=index_name)
except Exception as e:
    print(f"❌ ERROR checking/deleting index '{index_name}': {e}")
    exit(1)

# Créer l'index
try:
    print(f"📦 Creating index '{index_name}' with mapping...")
    es.indices.create(index=index_name, body=index_body)
except Exception as e:
    print(f"❌ ERROR creating index '{index_name}': {e}")
    exit(1)

# Charger les documents depuis le dataset partagé
# On rend le chemin configurable (avec fallback sur /shared_data/dataset.json)
# Détection automatique (local / container)
dataset_path = os.getenv("DATASET_PATH")

if dataset_path is None:
    if os.path.exists("./shared_data/dataset.json"):
        dataset_path = "./shared_data/dataset.json"
    else:
        dataset_path = "/shared_data/dataset.json"

print(f"📄 Using dataset from: {dataset_path}")

try:
    with open(dataset_path, encoding="utf-8") as f:
        documents = json.load(f)
    print(f"✅ Loaded {len(documents)} documents from {dataset_path}")
except FileNotFoundError:
    print(f"❌ ERROR: {dataset_path} not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ ERROR: Failed to parse JSON in {dataset_path}: {e}")
    exit(1)

# Indexer les documents
for i, doc in enumerate(documents):
    try:
        es.index(index=index_name, body=doc)
        print(f"✅ Indexed document {i+1}/{len(documents)}")
    except Exception as e:
        print(f"❌ ERROR indexing document {i+1}: {e}")

print("🎉 Indexation terminée.")
