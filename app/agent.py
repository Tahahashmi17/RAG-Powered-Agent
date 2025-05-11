from .tools import calculate_expression, define_word
from .rag import run_rag_pipeline
def handle_query(query):
    query_lower = query.lower()
    decision = ""
    retrieved_docs = []
    # Route based on keywords
    if "calculate" in query_lower:
        # Extract expression after the word "calculate"
        expression = query_lower.split("calculate")[-1].strip()
        result = calculate_expression(expression)
        decision = "Calculator"  
    elif "define" in query_lower:
        # Extract word after the word "define"
        word = query_lower.split("define")[-1].strip()
        result = define_word(word)
        decision = "Dictionary"
    else:
        result, retrieved_docs = run_rag_pipeline(query)
        decision = "RAG (Retrieval-Augmented Generation)"
    return result, decision, retrieved_docs
