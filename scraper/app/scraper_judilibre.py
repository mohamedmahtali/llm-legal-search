import requests
from datetime import datetime

# Simple scraper Judilibre (version DEMO → à améliorer)
# Voir : https://judilibre.io/

def scrape_judilibre():
    url = "https://judilibre.io/api/v1/decisions"  # endpoint public
    params = {
        "page_size": 5  # on récupère 5 décisions pour la démo
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    decisions = response.json().get("results", [])
    documents = []

    for dec in decisions:
        documents.append({
            "title": f"Judilibre: Decision {dec.get('id', '')}",
            "content": dec.get("body", "")[:2000],  # limiter le texte pour la démo
            "date": dec.get("dateDecision", datetime.now().strftime("%Y-%m-%d"))
        })

    print(f"✅ Scraped {len(documents)} documents from Judilibre")
    return documents
