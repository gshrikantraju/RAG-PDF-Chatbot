# **RAG PDF Project**

A **Retrieval-Augmented Generation (RAG) pipeline** that:

1. Extracts text from PDF documents.
2. Cleans and chunks the text for embedding.
3. Stores embeddings in **ChromaDB**.
4. Uses **LangChain + OpenAI** to answer queries based on document context.

---

## **Features**

- PDF text extraction using `unstructured`.
- Text preprocessing (cleaning & chunking).
- Embedding creation using **OpenAI Embeddings**.
- Vector store powered by **Chroma**.
- Query interface using **LangChain RetrievalQA**.
- Structured logging (via `logging` module).
- Follows **PEP8** coding standards.

---

## **Project Structure**

```
rag_pdf_project/
│
├── data/                       # Folder for PDFs
│   └── sample.pdf
│
├── src/                        # Source modules
│   ├── __init__.py
│   ├── extract_text.py         # PDF text extraction
│   ├── preprocess.py           # Cleaning & chunking
│   ├── vector_store.py         # Chroma vector store creation
│   ├── rag_pipeline.py         # RAG query pipeline
│   └── logger.py               # Logger setup
│
├── main.py                     # Entry point for the pipeline
├── pyproject.toml              # Project dependencies & metadata
└── README.md                   # Project documentation
```

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone <your_repo_url>
cd rag_pdf_project
```

### **2. Create a Virtual Environment**

Using **uv**:

```bash
uv venv rag_env
source rag_env/bin/activate
```

### **3. Install Dependencies**

Install all dependencies from `pyproject.toml`:

```bash
uv pip install .
```

(Or use `uv sync` if you have `tool.uv` configured.)

---

## **Setting OpenAI API Key**

```bash
export OPENAI_API_KEY="your_api_key_here"     # macOS/Linux
setx OPENAI_API_KEY "your_api_key_here"       # Windows
```

---

## **Usage**

### **Run the Pipeline**

```bash
python main.py
```

The script will:

- Extract and chunk text from `data/sample.pdf`.
- Build a vector store.
- Answer a sample query:

```
Q: What is the main result discussed in the paper?
A: <answer>
```

---

## **Logging**

Logs are displayed in the console.
The `logger.py` module is used for structured logging, replacing print statements.

---

## **Dependencies**

All dependencies are defined in `pyproject.toml`.
Example `dependencies` section:

```toml
[project]
dependencies = [
    "unstructured",
    "langchain",
    "langchain-openai",
    "langchain-chroma",
    "chromadb",
    "openai",
    "tiktoken"
]
```

---

## **Future Enhancements**

- Add support for multiple PDFs.
- Enable file-based logging (`logs/app.log`).
- Deploy as a REST API with **FastAPI**.
- Interactive chatbot UI.
