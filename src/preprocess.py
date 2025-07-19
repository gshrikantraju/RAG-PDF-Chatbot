"""
Module for text preprocessing and chunking.
"""

import re
from langchain.text_splitter import RecursiveCharacterTextSplitter


def clean_text(text: str) -> str:
    """
    Cleans and normalizes extracted text.

    Args:
        text (str): Raw text.

    Returns:
        str: Cleaned text.
    """
    text = re.sub(r"\n\s*\n", "\n\n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    """
    Splits text into chunks for RAG.

    Args:
        text (str): Input text.
        chunk_size (int): Maximum characters per chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        list[str]: List of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)
