# RAG-Powered Multi-Agent Q&A Assistant:
This project is a simple Flask-based assistant that can answer questions by intelligently choosing how to respond. It uses a Retrieval-Augmented Generation (RAG) approach for document-based queries, and it can also handle very basic calculations and definitions.

---

#Features
- **RAG Pipeline with OpenAI**  
It retrieves relevant information from local `.txt` documents and generates an answer using GPT-3.5.(If Open AI Quota is full, This will not work)
- **Agent Routing Logic**  
  - If the query includes "calculate", it performs a calculation.  
  - If the query includes "define", it provides a word definition using a free dictionary API.  
  - All other queries go through the RAG pipeline.
- **Web Interface**  
  Built using Flask. Users can input queries and see the selected tool, retrieved content, and final answer.
---
# Folder Structure

├── app/
│ ├── init.py
│ ├── routes.py
│ ├── agent.py
│ ├── rag.py
│ ├── tools.py
│ └── templates/
│ └── index.html
├── data/
│ └── docs/ # .txt files 
├── index_store/
├── run.py
├── requirements.txt
└── .env  #OpenAI API key

---

# 1. Install Dependencies:
pip install -r requirements.txt

# 2. Add API key
OPENAI_API_KEY=your-api-key-here

# 3. Run the file (run.py)

# Queries to be searched:
1. What is your return policy? → To Test RAG
2. calculate 250 / 5 + 30 → use calculator
3. define momentum → use dictionary API

Notes
-- If OpenAI quota is exceeded, RAG will not work but calculator and Definition searching (Dictonary) will still function.
-- The assistant will log which tool was used for each query.
-- Embeddings and indexes are saved locally after first use.

