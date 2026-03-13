from typing import Dict, Any
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from src.vector_store import VectorStoreManager
from src.llm import LLMInterface

class RAGOrchestrator:
    """
    Orchestrates the retrieval-augmented generation process.
    Connects the LLM, vector store, and prompt templates.
    """
    def __init__(self, vector_store: VectorStoreManager, llm_interface: LLMInterface):
        self.vector_store = vector_store
        self.llm = llm_interface.get_llm()
        self.retriever = self.vector_store.get_retriever()
        
        # Define a prompt template for context-aware Q&A
        self.prompt_template = """
        You are a helpful and knowledgeable AI assistant. Use the following pieces of context to answer the user's question.
        If the answer is not in the context, say that you don't know, but try to be helpful based on general knowledge.
        
        Context:
        {context}
        
        Question:
        {question}
        
        Answer:
        """
        self.prompt = PromptTemplate(
            template=self.prompt_template, input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def query(self, question: str) -> Dict[str, Any]:
        """
        Executes a RAG query and returns the answer with source documents.
        """
        result = self.qa_chain.invoke({"query": question})
        return result
