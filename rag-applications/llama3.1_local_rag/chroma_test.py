from chromadb.config import Settings
from langchain_chroma import Chroma

settings = Settings(
    chroma_host="localhost",
    chroma_port=8000,
)

vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=embeddings,
    client_settings=settings
)
