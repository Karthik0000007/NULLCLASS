import os
from embeddings.embedder import embed_chunks
from vector_store.fiass_db import FAISSVectorStore
from apscheduler.schedulers.background import BackgroundScheduler
import time

def get_all_texts(source_folder="sources"):
    texts = []
    for fname in os.listdir(source_folder):
        if fname.endswith(".txt"):
            path = os.path.join(source_folder, fname)
            with open(path, "rb") as f:  # Read in binary mode
                try:
                    raw = f.read()
                    decoded = raw.decode("utf-8")
                except UnicodeDecodeError:
                    decoded = raw.decode("utf-16", errors="ignore")  # fallback
            texts.append(decoded)
    return texts


def refresh_vector_store():
    print("Updating vector store...")
    texts = get_all_texts()
    all_chunks = []
    all_vectors = []

    for text in texts:
        chunks_and_vecs = embed_chunks(text)
        chunks, vecs = zip(*chunks_and_vecs)
        all_chunks.extend(chunks)
        all_vectors.extend(vecs)
    store = FAISSVectorStore()
    store.index.reset()  
    store.text_chunks = [] 
    store.add_embeddings(all_vectors, all_chunks)

    print(f"Vector store updated with {len(all_chunks)} chunks.")

def start_scheduler(interval_minutes=30):
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_vector_store, 'interval', minutes=interval_minutes)
    scheduler.start()
    print(f"Auto-update scheduled every {interval_minutes} minutes.")
    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler stopped.")


