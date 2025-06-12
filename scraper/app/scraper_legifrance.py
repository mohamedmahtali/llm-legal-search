import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Simple scraper Legifrance HTML
# Ex : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047666000

def scrape_legifrance():
    urls = [
        "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074069",  # Exemple 1
        "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006070721"   # Tu peux ajouter d'autres URL
    ]

    documents = []

    for url in urls:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Prendre les <p> principaux
        paragraphs = soup.select("p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs[:10]])

        documents.append({
            "title": f"Legifrance: {url}",
            "content": content,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    print(f"✅ Scraped {len(documents)} documents from Legifrance")
    return documents
