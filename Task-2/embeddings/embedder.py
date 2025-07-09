from sentence_transformers import SentenceTransformer
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, max_chunk_len=500):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_len:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def embed_chunks(text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return list(zip(chunks, embeddings))

# Testing
if __name__ == "__main__":
    text = """
    Artificial Intelligence is transforming every industry. 
    Customer service, education, and healthcare are seeing rapid innovations due to AI. 
    This chatbot is part of that change.
    """
    pairs = embed_chunks(text)
    print("Total Chunks:", len(pairs))
    print("Sample Chunk:", pairs[0][0])
    print("Sample Vector:", pairs[0][1][:5])
