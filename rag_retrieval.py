import psycopg2
from pgvector.psycopg2 import register_vector
from sentence_transformers import SentenceTransformer
import ollama

def retrieve_and_generate(query, category):
    # Convert query to embedding
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query)
    
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="chatbot_db", user="postgres", password="password", host="localhost", port="5432"
    )
    cur = conn.cursor()
    register_vector(conn)
    
    # Retrieve relevant documents
    cur.execute(
        """
        SELECT content
        FROM documents
        WHERE category = %s
        ORDER BY embedding <=> %s::vector
        LIMIT 2
        """,
        (category, query_embedding.tolist())
    )
    docs = [row[0] for row in cur.fetchall()]
    
    cur.close()
    conn.close()
    
    # Generate response
    prompt = f"""You are a customer service assistant for TechTrend Innovations. 
    Use the following information to answer the question naturally and concisely:
    {' '.join(docs)}\nQuestion: {query}\nAnswer:"""

    response = ollama.generate(model="gemma:2b", prompt=prompt)['response']
    
    return response