from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch, exceptions
from transformers import pipeline
import os

# Lecture de l'URL Elastic
elastic_url = os.getenv("ELASTIC_URL", "http://elasticsearch:9200")

app = FastAPI()

# Client ES
es = Elasticsearch(elastic_url)

# Pipeline summarization (HuggingFace)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.get("/")
def read_root():
    return {"message": "LLM Legal Search API"}

@app.get("/search")
def search(q: str):
    try:
        if not es.indices.exists(index="documents"):
            raise HTTPException(status_code=404, detail="Index 'documents' does not exist.")

        response = es.search(
            index="documents",
            query={
                "multi_match": {
                    "query": q,
                    "fields": ["title", "content"]
                }
            }
        )

        hits = response.get("hits", {}).get("hits", [])

        results = [
            {
                "title": hit.get("_source", {}).get("title", "N/A"),
                "content": hit.get("_source", {}).get("content", "N/A"),
                "score": hit.get("_score", 0)
            }
            for hit in hits
        ]

        return {"results": results}

    except exceptions.NotFoundError:
        raise HTTPException(status_code=404, detail="Index 'documents' not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during search: {e}")

@app.post("/enrich")
def enrich(text: str):
    try:
        summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during summarization: {e}")

@app.get("/search_enriched")
def search_enriched(q: str):
    try:
        if not es.indices.exists(index="documents"):
            raise HTTPException(status_code=404, detail="Index 'documents' does not exist.")

        response = es.search(
            index="documents",
            query={
                "multi_match": {
                    "query": q,
                    "fields": ["title", "content"]
                }
            }
        )

        hits = response.get("hits", {}).get("hits", [])

        results = []
        for hit in hits:
            source = hit.get("_source", {})
            title = source.get("title", "N/A")
            content = source.get("content", "N/A")
            score = hit.get("_score", 0)

            try:
                summary = summarizer(content, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
            except Exception as e:
                summary = f"Error generating summary: {e}"

            results.append({
                "title": title,
                "content": content,
                "summary": summary,
                "score": score
            })

        return {"results": results}

    except exceptions.NotFoundError:
        raise HTTPException(status_code=404, detail="Index 'documents' not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during enriched search: {e}")
