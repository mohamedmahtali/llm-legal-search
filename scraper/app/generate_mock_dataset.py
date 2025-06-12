# generate_mock_dataset.py

import json
from datetime import datetime, timedelta
import random

OUTPUT_PATH = "./shared_data/dataset.json"

titles = [
    "Décision Cour de Cassation", "Arrêt Conseil d'État", "Décision CNIL",
    "Jurisprudence droit du travail", "Décision RGPD", "Arrêté ministériel",
    "Jugement Tribunal Administratif", "Ordonnance Tribunal Judiciaire",
    "Circulaire Ministérielle", "Instruction fiscale"
]

themes = [
    "droit civil", "droit pénal", "droit commercial", "droit du travail",
    "droit administratif", "protection des données", "procédure pénale",
    "droit international privé", "droit fiscal", "droit de la santé"
]

documents = []

for i in range(1, 1001):
    title = f"{random.choice(titles)} n°{i}"
    content = f"Ceci est un contenu simulé pour la décision n°{i} concernant le thème {random.choice(themes)}. " \
              f"Le texte complet de cette décision est généré pour permettre des tests de recherche enrichie."
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")

    documents.append({
        "title": title,
        "content": content,
        "date": date
    })

# Save
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"✅ Mock dataset saved to {OUTPUT_PATH} ({len(documents)} documents)")
