from langchain_community.embeddings.ollama import OllamaEmbeddings

# TODO: use Llama3 from Ollama


def get_embedding_function():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    return embeddings
