# ðŸ§  NeuroSearch: Modular RAG Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Active-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

**NeuroSearch** is a production-ready, modular Retrieval-Augmented Generation (RAG) engine designed for local-first semantic search and question answering. It processes your private documents (PDF, Markdown, Text) and allows you to chat with them using local LLMs (via Ollama) or cloud providers.

## ðŸš€ Key Features

*   **Modular Architecture:** Clean separation of concerns (Ingestion, Embedding, Vector Store, LLM).
*   **Local-First:** Designed to run with Ollama (Llama 3, Mistral) for privacy-preserving AI.
*   **Pluggable Vector Stores:** Supports ChromaDB out-of-the-box, extensible to FAISS/Pinecone.
*   **Type-Safe:** Fully typed Python code with Pydantic validation.
*   **CLI Interface:** robust command-line tools for ingestion and querying.

## ðŸ— Architecture

```mermaid
graph TD
    A[Documents] -->|Ingest| B(Text Splitter)
    B -->|Chunks| C(Embedding Model)
    C -->|Vectors| D[(ChromaDB Vector Store)]
    E[User Query] -->|Embed| C
    D -->|Retrieve Context| F[RAG Orchestrator]
    E --> F
    F -->|Context + Query| G[LLM (Ollama)]
    G -->|Answer| H[User]
```

## ðŸ›  Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nft94/NeuroSearch.git
    cd NeuroSearch
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Ollama:**
    Ensure [Ollama](https://ollama.com/) is running locally:
    ```bash
    ollama serve
    ollama pull llama3
    ```

## ðŸ’» Usage

### 1. Ingest Documents
Process your local documents into the vector store:

```bash
python main.py ingest --dir ./data/docs
```

### 2. Chat with your Data
Start an interactive chat session:

```bash
python main.py chat
```

## ðŸ“‚ Project Structure

```
NeuroSearch/
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ ingest.py       # Document loading & splitting
â”‚   â”œâ”€â”€ vector_store.py # ChromaDB wrapper
â”‚   â”œâ”€â”€ llm.py          # Ollama interface
â”‚   â””â”€â”€ rag_engine.py   # Main RAG logic
â”œâ”€â”€ main.py             # CLI Entrypoint
â”œâ”€â”€ requirements.txt    # Dependencies
â””â”€â”€ README.md           # Documentation
```

## ðŸ¤ Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
