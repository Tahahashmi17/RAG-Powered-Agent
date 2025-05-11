import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings()
index_path = "index_store"
def load_documents(folder_path="data/docs/"):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = f.read()
                docs.append(Document(page_content=content))
    return docs
def build_or_load_faiss_index():
    if os.path.exists(os.path.join(index_path, "index.faiss")):
        return FAISS.load_local(index_path, embedding)
    else:
        docs = load_documents()
        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        chunks = text_splitter.split_documents(docs)
        vectorstore = FAISS.from_documents(chunks, embedding)
        vectorstore.save_local(index_path)
        return vectorstore
def run_rag_pipeline(query):
    vectorstore = build_or_load_faiss_index()
    docs = vectorstore.similarity_search(query, k=3)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=docs, question=query)
    return answer, [doc.page_content for doc in docs]
