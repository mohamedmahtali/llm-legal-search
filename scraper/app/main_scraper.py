from scraper_judilibre import scrape_judilibre
from scraper_legifrance import scrape_legifrance
from utils import save_json

OUTPUT_PATH = "/shared_data/dataset.json"

def main():
    print("🚀 Scraping Judilibre...")
    try:
        judilibre_docs = scrape_judilibre()
    except Exception as e:
        print(f"⚠️ Error scraping Judilibre: {e}")
        judilibre_docs = []

    print("🚀 Scraping Legifrance...")
    try:
        legifrance_docs = scrape_legifrance()
    except Exception as e:
        print(f"⚠️ Error scraping Legifrance: {e}")
        legifrance_docs = []

    all_documents = judilibre_docs + legifrance_docs

    print(f"📚 Total documents collected: {len(all_documents)}")

    save_json(all_documents, OUTPUT_PATH)
    print(f"✅ Dataset enregistré dans {OUTPUT_PATH}")
