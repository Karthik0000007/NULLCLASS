import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
task3_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Task-3'))
if task3_path not in sys.path:
    sys.path.append(task3_path)
from embeddings.embedder import model
from sentiment.analyzer import analyze_sentiment
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

    sentiment = analyze_sentiment(user_query)
    query_embedding = model.encode([user_query])[0]
    store = FAISSVectorStore()
    top_chunks = store.search(query_embedding, top_k=top_k)
    context = "\n\n".join(top_chunks)

    tone = {
        "positive": "Maintain a cheerful, thankful tone.",
        "neutral": "Be clear, professional, and helpful.",
        "negative": "Be empathetic, apologize briefly, and offer clear solutions."
    }[sentiment]

    prompt = f"""
You are a helpful customer service chatbot.

Use the following knowledge to answer the user question.
Tone guide: {tone}

 CONTEXT 
{context}

 USER QUERY 
{user_query}

Answer appropriately:
"""
    return query_ollama(prompt)

#Testing the RAG response generation
if __name__ == "__main__":
    user_input = "I'm very frustrated, nothing is working."
    response = generate_rag_response(user_input)
    print(f"\nFinal Answer:\n{response}")
