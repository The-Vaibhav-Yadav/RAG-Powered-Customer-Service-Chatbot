# RAG TechTrend Chatbot System

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-blue)
![Ollama](https://img.shields.io/badge/Ollama-gemma%3A2b-orange)

A completely localized, privacy-first Retrieval-Augmented Generation (RAG) system acting as an intelligent customer service AI for "TechTrend Innovations". The project dynamically contextualizes user queries and synthesizes factual answers seamlessly utilizing LLM vectors.

## Table of Contents
- [Tech Stack & Architecture](#tech-stack--architecture)
- [Prerequisites](#prerequisites)
- [Installation & Local Setup](#installation--local-setup)
- [Usage & Running the App](#usage--running-the-app)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing Guidelines](#contributing-guidelines)
- [License and Contact](#license-and-contact)

## Tech Stack & Architecture

- **Embeddings**: `sentence-transformers` (`all-MiniLM-L6-v2`) computes rapid semantic vectors of incoming requests.
- **Database**: `PostgreSQL` actively leveraged with the `pgvector` extension utilizing optimized cosine similarity nearest-neighbor lookup.
- **LLM Engine**: Localized language generation managed strictly through `Ollama` hosting the Google `gemma:2b` lightweight model.

```mermaid
graph TD;
    User-->Frontend;
    Frontend-->classifier[Query Classifier];
    classifier-->postgres[(PostgreSQL pgvector)];
    postgres-->ollama[Ollama LLM (gemma:2b)];
    ollama-->User;
```

## Prerequisites

- Python 3.10+ and the `uv` package manager natively installed.
- **PostgreSQL Server**: Must be visibly running on port `5432` with the `pgvector` extension fully installed.
- **Ollama Engine**: Must be active on the system with the targeted LLM model downloaded: `ollama run gemma:2b`.

## Installation & Local Setup

```bash
git clone https://github.com/The-Vaibhav-Yadav/RAG-Powered-Customer-Service-Chatbot.git
cd RAG-Powered-Customer-Service-Chatbot
uv sync
```

Ensure you instantiate your database properly targeting the credentials embedded within `rag_retrieval.py` (`dbname="chatbot_db"`).

## Usage & Running the App

Initially embed baseline TechTrend corporate documents into the vector instance:
```bash
uv run python store_embeddings.py
```

Launch the overarching interactive graphical/terminal frontend:
```bash
uv run python frontend.py
```

## Testing

For vector stability, confirm manual outputs dynamically testing categorization lookups:
```bash
uv run python query_classifier.py
```

## Deployment

Presently orchestrated for local execution due to the Ollama dependency. For robust production deployment, containerize the stack utilizing Docker/Docker-Compose wrapping Postgres, Ollama, and the FastApi wrapper into contiguous bridged networks.

## Contributing Guidelines
Use standard gitflow protocols. Create a feature branch, append unit tests evaluating vector lookups against mocked database responses, and enforce static typing parameters throughout newly created pipeline extensions.

## License and Contact
- **License**: MIT
- **Author**: Vaibhav Yadav (https://github.com/The-Vaibhav-Yadav)
