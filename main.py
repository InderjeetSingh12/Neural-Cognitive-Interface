import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from src.ingest import IngestionEngine
from src.vector_store import HybridVectorStore
from src.llm import LLMInterface
from src.rag_engine import ResearchRAGEngine

console = Console()

@click.group()
def cli():
    """
    ðŸ§  NeuroSearch Research: Advanced 2-Stage RAG CLI.
    """
    pass

@cli.command()
@click.option("--dir", default="./data/docs", help="Directory containing documents.")
def ingest(dir):
    """
    Ingest docs and fit BM25 sparse retriever.
    """
    console.print(Panel(f"ðŸš€ [bold cyan]Research Ingestion Phase[/bold cyan]\nDirectory: {dir}", title="NeuroSearch ML Research"))
    
    ingestion_engine = IngestionEngine()
    vector_store_manager = HybridVectorStore()
    
    try:
        docs = ingestion_engine.load_documents(dir)
        if not docs:
            console.print("[yellow]No documents found.[/yellow]")
            return

        chunks = ingestion_engine.split_documents(docs)
        vector_store_manager.add_documents(chunks)
        
        console.print(f"[green]Successfully indexed {len(chunks)} chunks with Hybrid (Dense + BM25) support![/green]")
        
    except Exception as e:
        console.print(f"[red]Ingestion Error: {e}[/red]")

@cli.command()
@click.option("--model", default="llama3", help="Ollama model.")
@click.option("--alpha", default=0.5, type=float, help="Hybrid alpha (1.0=Dense, 0.0=Sparse).")
def chat(model, alpha):
    """
    Start a session with 2-Stage Hybrid Retrieval & Re-ranking.
    """
    console.print(Panel(f"ðŸ’¬ [bold green]Research Chat Session[/bold green]\nModel: {model} | Hybrid Alpha: {alpha}", title="NeuroSearch RAG"))
    
    vector_store = HybridVectorStore()
    llm_interface = LLMInterface(model_name=model)
    rag_engine = ResearchRAGEngine(vector_store, llm_interface)
    
    console.print("[italic dim]Status: Cross-Encoder (MS-MARCO) Ready for Re-ranking.[/italic dim]\n")
    
    while True:
        user_query = Prompt.ask("[bold blue]Query[/bold blue]")
        
        if user_query.lower() in ["exit", "quit"]:
            break
            
        with console.status("[bold green]Stage 1: Hybrid Retrieval | Stage 2: Cross-Encoder Re-ranking...[/bold green]"):
            try:
                response = rag_engine.query(user_query, alpha=alpha)
                answer = response.get("result", "No answer found.")
                sources = response.get("source_documents", [])
                
                console.print(f"\n[bold green]NeuroSearch Research AI:[/bold green]\n{answer}\n")
                
                if sources:
                    console.print("[bold italic]Verified Sources (Re-ranked):[/bold italic]")
                    for i, doc in enumerate(sources):
                        source_name = doc.metadata.get('source', 'Unknown')
                        console.print(f"{i+1}. [dim]{source_name}[/dim]")
                console.print("\n" + "="*60 + "\n")
                
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    cli()
