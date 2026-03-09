# RAG-Powered Customer Service Chatbot

A Retrieval-Augmented Generation (RAG) system serving as a customer service assistant for "TechTrend Innovations."

## Architecture & Features
This solution combines local embedders, a vector database, and local LLMs to safely query proprietary data:
- **Embeddings**: Uses `sentence-transformers` (`all-MiniLM-L6-v2`) to compute semantic vectors of the documentation contexts (`embed_data.py`).
- **Database Storage**: Integrates with PostgreSQL utilizing the `pgvector` extension to safely persist vectors (`store_embeddings.py`) for similarity lookups indexed by category.
- **Generation Engine**: Pulls nearest-neighbor documents using a categorization match (`rag_retrieval.py`) inside Postgres, injects the matched contexts into an LLM prompt, and offloads answer generation to a locally hosted `Ollama` endpoint utilizing the `gemma:2b` model.
- **Classification Routing**: Classifies the query intent to fetch relative categorizations beforehand (`query_classifier.py`).

### Prerequisites
- Python 3.x
- [uv](https://github.com/astral-sh/uv) (for managing dependencies specified in `pyproject.toml`)
- PostgreSQL database configured with the `pgvector` extension.
- [Ollama](https://ollama.com/) running locally with the `gemma:2b` model pulled.

### Launching the Application
Launch the graphical interface directly:
```bash
uv run frontend.py
```
