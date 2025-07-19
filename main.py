"""
Main entry point for the RAG PDF project.
"""

import os
from src.extract_text import extract_pdf_text
from src.preprocess import clean_text, chunk_text
from src.vector_store import create_vector_store
from src.rag_pipeline import create_rag_pipeline
from src.logger import get_logger

PDF_PATH = "data/250700077v1.pdf"
PERSIST_DIR = "chroma_db"
logger = get_logger(__name__)


def main() -> None:
    """
    Main function to extract text, create embeddings, and run a RAG query.
    """
    logger.info("Extracting text from PDF...")
    text = extract_pdf_text(PDF_PATH)
    cleaned_text = clean_text(text)

    logger.info("Chunking text...")
    chunks = chunk_text(cleaned_text)

    logger.info("Creating vector store...")
    create_vector_store(chunks, persist_dir=PERSIST_DIR)

    logger.info("Creating RAG pipeline...")
    qa = create_rag_pipeline(PERSIST_DIR)

    query = "What is the main result discussed in the paper?"
    response = qa.invoke(query)
    logger.info(f"Q: {query}")
    logger.info(f"A: {response['result']}")


if __name__ == "__main__":
    main()
