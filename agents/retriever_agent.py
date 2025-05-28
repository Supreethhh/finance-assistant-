import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

DATA_DIR = "data_ingestion"
MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_relevant_docs(query, index_file="faiss_index.pkl", top_k=2):
    with open(os.path.join(DATA_DIR, index_file), "rb") as f:
        index, docs = pickle.load(f)

    query_embedding = MODEL.encode([query])
    _, indices = index.search(query_embedding, top_k)
    return [docs[i] for i in indices[0]]
# Index and retrieve documents using FAISS
