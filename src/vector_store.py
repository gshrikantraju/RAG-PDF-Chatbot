"""
Module for creating and querying a vector store.
"""

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vector_store(chunks: list[str], persist_dir: str = "chroma_db") -> Chroma:
    """
    Creates a Chroma vector store from text chunks.

    Args:
        chunks (list[str]): Text chunks.
        persist_dir (str): Directory to store the database.

    Returns:
        Chroma: Chroma vector store instance.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_texts(texts=chunks, embedding=embeddings, persist_directory=persist_dir)

    return db
