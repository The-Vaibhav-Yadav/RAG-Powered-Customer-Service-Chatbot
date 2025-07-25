from sentence_transformers import SentenceTransformer
import os

def generate_embeddings():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    data_folder = 'data'
    embeddings = []
    metadata = []
    
    for file_name in os.listdir(data_folder):
        with open(os.path.join(data_folder, file_name), 'r') as f:
            content = f.read().splitlines()
            for line in content:
                if line.strip():
                    embedding = model.encode(line)
                    category = file_name.split('.')[0]
                    embeddings.append(embedding)
                    metadata.append((line, category))
    
    return embeddings, metadata

if __name__ == "__main__":
    embeddings, metadata = generate_embeddings()
    print(f"Generated {len(embeddings)} embeddings")