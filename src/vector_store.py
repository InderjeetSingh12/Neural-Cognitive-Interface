from typing import List, Optional
import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import os

class VectorStoreManager:
    """
    Manages interactions with the ChromaDB vector store.
    Designed for modularity and scalability.
    """
    def __init__(self, collection_name: str = "neuro_search", persist_directory: str = "./data/chroma"):
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Ensure directory exists
        os.makedirs(persist_directory, exist_ok=True)
        
        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
            collection_name=self.collection_name
        )

    def add_documents(self, documents: List[Document]):
        """
        Adds a list of documents to the vector store.
        """
        print(f"Adding {len(documents)} documents to vector store...")
        self.db.add_documents(documents)
        print("Documents added successfully.")

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Performs a similarity search for the given query.
        """
        return self.db.similarity_search(query, k=k)

    def get_retriever(self, k: int = 4):
        """
        Returns a retriever object for use in LangChain chains.
        """
        return self.db.as_retriever(search_kwargs={"k": k})
