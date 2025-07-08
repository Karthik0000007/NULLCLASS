import faiss
import os
import pickle
import numpy as np

class FAISSVectorStore:
    def __init__(self, dim=384, index_path="vector_store/faiss_index", metadata_path="vector_store/metadata.pkl"):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

        # Load existing if present
        if os.path.exists(index_path) and os.path.exists(metadata_path):
            self.load()

    def add_embeddings(self, embeddings, texts):
        if len(embeddings) == 0:
            return
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.text_chunks.extend(texts)
        self.save()

    def search(self, query_embedding, top_k=3):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)
        results = [self.text_chunks[i] for i in indices[0] if i < len(self.text_chunks)]
        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.metadata_path, "rb") as f:
            self.text_chunks = pickle.load(f)
