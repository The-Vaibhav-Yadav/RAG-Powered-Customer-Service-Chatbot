from fastapi import FastAPI
from pydantic import BaseModel
from query_classifier import train_classifier, classify_query
from rag_retrieval import retrieve_and_generate

app = FastAPI()
vectorizer, classifier = train_classifier()

class Query(BaseModel):
    text: str

@app.post("/chat")
async def chat(query: Query):
    category = classify_query(query.text, vectorizer, classifier)
    response = retrieve_and_generate(query.text, category)
    return {"response": response}