from pathlib import Path
from typing import List, Tuple
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
import sys

DOCS_DIR = Path("docs")
DB_DIR = Path("chroma_db")

SMALLTALK = {
    "hi","hello","hey","yo","hola","namaste","sup",
    "bye","goodbye","see ya","cya","see you","thanks","thank you",
    "how are you","what's up","whats up","good night","good morning","good afternoon"
}

def is_smalltalk(q: str) -> bool:
    ql = q.lower().strip()
    return any(ql == s or ql.startswith(s) for s in SMALLTALK)

def load_docs():
    docs = []
    if not DOCS_DIR.exists():
        sys.exit("Docs folder not found. Expected ./docs")
    for p in DOCS_DIR.glob("*"):
        suff = p.suffix.lower()
        if suff == ".pdf":
            docs.extend(PyPDFLoader(str(p)).load())
        elif suff in (".txt", ".md", ".yaml", ".yml"):
            docs.extend(TextLoader(str(p), encoding="utf-8").load())
    if not docs:
        sys.exit("No documents found in ./docs. Add files and rerun.")
    return docs

def build_db():
    print("Building vector DB (one-time)…")
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=120)
    chunks = splitter.split_documents(load_docs())
    emb = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma.from_documents(chunks, emb, persist_directory=str(DB_DIR))
    db.persist()
    return db

def load_db():
    emb = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(persist_directory=str(DB_DIR), embedding_function=emb)

def format_context(docs_with_scores: List[Tuple[object,float]]) -> Tuple[str,List[str]]:
    cites, blocks = [], []
    for i, (d, score) in enumerate(docs_with_scores, 1):
        src = Path(d.metadata.get("source","unknown")).name
        page = d.metadata.get("page")
        s = f"{score:.2f}"
        cite = f"[{i}] {src}" + (f" (p.{page+1})" if isinstance(page, int) else "") + f" (rel {s})"
        cites.append(cite)
        blocks.append(f"--- {cite} ---\n{d.page_content[:1500]}")
    return ("\n\n".join(blocks) if blocks else ""), cites

def main():
    db = load_db() if DB_DIR.exists() else build_db()

    # Fast, small model by default (you can swap to mistral if you like)
    llm = Ollama(model="llama3.2:3b", temperature=0.2)

    print("\nSIL Copilot ready. Ask about your docs. Type 'q' to quit.\n")
    print("Tip: type '/sources on' or '/sources off' to toggle citations.\n")

    show_sources = False

    while True:
        q = input("Q: ").strip()
        if q.lower() in {"q","quit","exit"}:
            break

        # Commands
        if q.lower() in {"/sources on","/show sources on"}:
            show_sources = True
            print("Citations ON.\n")
            continue
        if q.lower() in {"/sources off","/show sources off"}:
            show_sources = False
            print("Citations OFF.\n")
            continue

        # Smalltalk → natural reply, no citations
        if is_smalltalk(q):
            prompt = (
                "You are a friendly, concise assistant. Respond naturally to the user’s smalltalk. "
                "Keep it short and warm; don’t mention documents or citations.\n"
                f"User: {q}\nAssistant:"
            )
            print("\n--- Answer ---\n")
            print(llm.invoke(prompt), "\n")
            continue

        # Retrieval with scores; only use context if relevant enough
        # We’ll keep items with score >= 0.40 (0 is identical, 1 is far for Chroma cosine distance)
        raw = db.similarity_search_with_relevance_scores(q, k=3)
        filtered = [(d,s) for d,s in raw if s <= 0.40]  # smaller = more similar

        if filtered:
            context, cites = format_context(filtered)
            prompt = (
                "You are SIL Copilot. Use ONLY the context to answer. "
                "Be concise and action-oriented. If something is not covered, say you don’t know.\n\n"
                f"{context}\n\nQuestion: {q}\n\n"
                "Answer clearly. If you rely on specific facts from context, you MAY include bracketed numbers [1], [2] inline."
            )
            answer = llm.invoke(prompt)
            print("\n--- Answer ---\n")
            print(answer, "\n")
            if show_sources:
                print("Sources:\n" + "\n".join(cites) + "\n")
        else:
            # No useful context: answer generally (no citations)
            prompt = (
                "You are a helpful assistant. The user asked a general question not covered by the internal documents. "
                "Answer naturally in plain English without mentioning documents or citations.\n"
                f"User question: {q}\nAssistant:"
            )
            print("\n--- Answer ---\n")
            print(llm.invoke(prompt), "\n")

if __name__ == "__main__":
    main()
