import psycopg2
from pgvector.psycopg2 import register_vector
from embed_data import generate_embeddings

def store_embeddings():
    conn = psycopg2.connect(
        dbname="chatbot_db", user="postgres", password="password", host="localhost", port="5432"
    )
    cur = conn.cursor()
    
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            content TEXT,
            category TEXT,
            embedding VECTOR(384)
        )
    """)
    
    embeddings, metadata = generate_embeddings()
    for (content, category), embedding in zip(metadata, embeddings):
        cur.execute(
            "INSERT INTO documents (content, category, embedding) VALUES (%s, %s, %s)",
            (content, category, embedding.tolist())
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("Embeddings stored in PostgreSQL")

if __name__ == "__main__":
    store_embeddings()