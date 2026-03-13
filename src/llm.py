from langchain_community.llms import Ollama
from langchain_core.language_models.llms import LLM

class LLMInterface:
    """
    Interface for interacting with Local LLMs (via Ollama).
    """
    def __init__(self, model_name: str = "llama3", temperature: float = 0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = Ollama(model=self.model_name, temperature=self.temperature)

    def get_llm(self) -> LLM:
        """
        Returns the LangChain LLM instance.
        """
        return self.llm
