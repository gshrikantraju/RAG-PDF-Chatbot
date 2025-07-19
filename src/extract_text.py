"""
Module for extracting text from PDF files using unstructured.
"""

import os
from unstructured.partition.pdf import partition_pdf


def extract_pdf_text(file_path: str) -> str:
    """
    Extracts text content from a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    elements = partition_pdf(filename=file_path)
    text_content = "\n".join(
        [el.text for el in elements if hasattr(el, "text")]
    )
    return text_content
