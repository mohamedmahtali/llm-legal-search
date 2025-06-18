import gradio as gr
import requests
import traceback

def search_enriched(query):
    print("🔍 --- Nouvelle recherche ---")
    print(f"🔎 Terme de recherche reçu : '{query}'")

    try:
        print("➡️ Envoi de la requête HTTP au backend...")
        response = requests.get("http://backend:8000/search_enriched", params={"q": query})
        print(f"✅ Réponse HTTP reçue : {response.status_code}")
        response.raise_for_status()

        print("🔄 Tentative de décodage JSON...")
        data = response.json()
        print("✅ JSON décodé avec succès.")
        print("🧪 Contenu brut reçu du backend :", data)

    except Exception as e:
        print("❌ Exception attrapée pendant la requête ou le parsing JSON !")
        traceback.print_exc()  # Affiche l'erreur complète avec stacktrace
        return f"### ❌ Erreur rencontrée\n```\n{e}\n```"

    results = data.get("results", [])
    if not results:
        print("⚠️ Aucun résultat retourné.")
        return "Aucun résultat trouvé."

    print(f"📝 Formatage de {len(results)} résultat(s)...")
    display = ""
    for r in results:
        display += f"### {r['title']}\n"
        display += f"**Score :** {r['score']:.2f}\n"
        display += f"**Résumé :** {r['summary']}\n\n"

    print("✅ Résultats formatés prêts à être affichés.")
    return display

# Interface Gradio
iface = gr.Interface(
    fn=search_enriched,
    inputs=gr.Textbox(label="Votre recherche juridique"),
    outputs=gr.Markdown(),
    title="Moteur de Recherche Juridique IA",
    description="Recherche Elastic enrichie par LLM (HuggingFace)"
)

# Lancer Gradio
print("🚀 Lancement de l'interface Gradio sur http://0.0.0.0:7860")
iface.launch(server_name="0.0.0.0", server_port=7860)
