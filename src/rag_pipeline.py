"""
RAG pipeline module for querying.
"""

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI


def create_rag_pipeline(persist_dir: str = "chroma_db") -> RetrievalQA:
    """
    Creates a RAG pipeline using stored embeddings.

    Args:
        persist_dir (str): Directory of the Chroma DB.

    Returns:
        RetrievalQA: RAG pipeline.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
