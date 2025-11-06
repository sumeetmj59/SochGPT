from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path
import shutil, uuid, requests

# LangChain / Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma

# -----------------------------
# Config
# -----------------------------
DOCS_DIR = Path("docs")
DB_DIR = Path("chroma_db")       # on-disk Chroma
COLLECTION = "sil_embed_768"     # NEW name to avoid old 4096-dim collection
EMBED_MODEL = "nomic-embed-text" # embedding model from Ollama
GEN_MODEL = "mistral"            # LLM used for answering (generation)

# -----------------------------
# App & CORS
# -----------------------------
app = FastAPI(title="SIL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", "http://127.0.0.1:3000",
        "http://localhost:3001", "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure dirs exist
DOCS_DIR.mkdir(exist_ok=True)
DB_DIR.mkdir(exist_ok=True)

# Embeddings + VectorStore
emb = OllamaEmbeddings(model=EMBED_MODEL)  # returns 768-dim vectors
vs = Chroma(collection_name=COLLECTION, persist_directory=str(DB_DIR), embedding_function=emb)

# -----------------------------
# Utilities
# -----------------------------
def index_path(p: Path) -> None:
    """Load a file, split it, and add chunks to Chroma."""
    docs = []
    if p.suffix.lower() in {".txt", ".md", ".csv"}:
        docs.extend(TextLoader(str(p), autodetect_encoding=True).load())
    elif p.suffix.lower() == ".pdf":
        docs.extend(PyPDFLoader(str(p)).load())
    else:
        return  # unsupported; ignore

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    if chunks:
        vs.add_documents(chunks)
        vs.persist()

# -----------------------------
# Models
# -----------------------------
class ChatIn(BaseModel):
    query: str

# -----------------------------
# Routes
# -----------------------------
@app.post("/chat")
def chat(inp: ChatIn):
    # Retrieve top-k chunks from vector store
    retriever = vs.as_retriever(search_kwargs={"k": 4})
    ctx_docs = retriever.invoke(inp.query)  # LangChain 0.2+ API
    context = "\n\n".join(f"[{i+1}] {d.page_content[:1200]}" for i, d in enumerate(ctx_docs))

    prompt = f"""You are Sumeet's Intelligence Lab assistant.
Use the CONTEXT when helpful. If not found, answer naturally.
Keep answers friendly and concise.

CONTEXT:
{context}

Question: {inp.query}
Answer:"""

    try:
        r = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": GEN_MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        r.raise_for_status()
        out = r.json().get("response", "")
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Ollama error: {e}")

    sources = [d.metadata.get("source", "") for d in ctx_docs]
    return {"answer": out, "sources": sources}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    dst = DOCS_DIR / f"{uuid.uuid4().hex}{Path(file.filename).suffix}"
    with dst.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    index_path(dst)
    return {"ok": True, "stored_as": dst.name}

@app.get("/healthz")
def healthz():
    return {"ok": True}