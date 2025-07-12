# Task 1: Customer Support Chatbot Analytics Dashboard

## 📌 Overview
This project implements an analytics dashboard for a **Customer Service Chatbot**. It logs and visualizes:
- Total number of user queries
- Most commonly discussed topics
- Average satisfaction ratings (1–5 scale)

## 🧰 Features
- 📊 Flask-based dashboard
- 📁 Real-time log support via CSV
- 🧠 Metrics calculated: total queries, top 5 topics, satisfaction

## 🛠️ How to Run

### 1. Clone this project and navigate to the folder
```bash
git clone <https://github.com/Karthik0000007/NULLCLASS>
cd Task-1
```
### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Start the dashboard
```bash
python app.py
```
## File Structure
```bash
Task-1/
├── app.py
├── chatbot_logger.py
├── analytics_utils.py
├── customer_service_interactions.csv
├── requirements.txt
└── templates/
    └── dashboard.html
```
# Task-2 Dynamic Knowledge Base Chatbot

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** powered Customer Service Chatbot that dynamically updates its knowledge base. It uses local embeddings, FAISS vector store, and a local Ollama LLM to answer queries using up-to-date, embedded documents.

## 🧰 Features
- 🧠 RAG-powered chatbot using sentence-transformers + FAISS
- 💬 LLM backend via Ollama (local)
- 🔁 Auto-update system for ingesting new documents from /sources
- 📁 CLI Admin Tool for manual DB refresh and source monitoring
- 🧠 Chunk-based embedding using nltk + MiniLM

## 🛠️ How to Run

### 1. Clone this project and navigate to the folder
```bash
git clone <https://github.com/Karthik0000007/NULLCLASS>
cd Task-2
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3 Make sure Ollama is running
```bash
ollama run llama3
```
### 4. Start the chatbot
```bash
python -m chatbot.chatbot
```
## File Structure
```bash
Task-2/
├── chatbot/
│   ├── chatbot.py
├── embeddings/
│   ├── embedder.py
├── vector_store/
│   ├── faiss_db.py
│   ├── last_update.txt
├── utils/
│   ├── auto_updater.py
│   ├── admin_cli.py
├── sources/
│   └── support_ai.txt
├── requirements.txt


