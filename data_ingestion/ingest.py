import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Ensure the directory exists
DATA_DIR = "data_ingestion"
os.makedirs(DATA_DIR, exist_ok=True)


MODEL = SentenceTransformer("all-MiniLM-L6-v2")


sample_docs = [
    "TSMC earnings beat expectations by 4%.",
    "Samsung earnings missed estimates by 2%.",
    "Asian tech sector exposure increased by 4% since yesterday.",
    "Market sentiment in Asia remains neutral due to rising bond yields.",
    "Investors are cautious about semiconductor stocks amid global demand shifts."
]


def create_vector_index(docs, index_file="faiss_index.pkl"):
    embeddings = MODEL.encode(docs)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save index and associated docs
    with open(os.path.join(DATA_DIR, index_file), "wb") as f:
        pickle.dump((index, docs), f)

    print(f"FAISS index created with {len(docs)} documents.")


if __name__ == "__main__":
    create_vector_index(sample_docs)
