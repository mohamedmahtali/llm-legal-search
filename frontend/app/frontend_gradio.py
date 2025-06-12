import gradio as gr
import requests

def search_enriched(query):
    print(f"🔍 Nouvelle recherche: '{query}' | Mode enrichi: True")
    try:
        response = requests.get("http://127.0.0.1:8000/search_enriched", params={"q": query})
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Erreur requête API: {e}")
        return "Erreur API"

    data = response.json()
    results = data.get("results", [])

    display = ""
    for r in results:
        display += f"### {r['title']}\n"
        display += f"**Score :** {r['score']:.2f}\n"
        display += f"**Résumé :** {r['summary']}\n\n"
    if not results:
        display = "Aucun résultat trouvé."

    return display

# Interface Gradio
iface = gr.Interface(
    fn=search_enriched,
    inputs=gr.Textbox(label="Votre recherche juridique"),
    outputs=gr.Markdown(label="Résultats enrichis"),
    title="Moteur de Recherche Juridique IA",
    description="Recherche Elastic enrichie par LLM (HuggingFace)"
)

iface.launch()
