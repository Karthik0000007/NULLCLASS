import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from embeddings.embedder import embed_chunks, model
from vector_store.fiass_db import FAISSVectorStore
import subprocess

def query_ollama(prompt, model_name="llama3"):
    result = subprocess.run(
        ["ollama", "run", model_name],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").strip()

def generate_rag_response(user_query, top_k=3):
    query_embedding = model.encode([user_query])[0]

    store = FAISSVectorStore()
    top_chunks = store.search(query_embedding, top_k=top_k)

    context = "\n\n".join(top_chunks)
    prompt = f"""You are a helpful assistant. Use the following context to answer the user's question. 
    {context}

    {user_query}

    Answer clearly:
"""
    return query_ollama(prompt)

# Testing 
if __name__ == "__main__":
    user_input = "How do chatbots use AI in customer support?"
    answer = generate_rag_response(user_input)
    print("\nAnswer:\n", answer)
