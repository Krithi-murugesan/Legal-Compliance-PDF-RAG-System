import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from .prompts import get_qa_prompt

def process_pdf_to_retriever(file_path):
    # 1. Load the PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # 2. Split into large chunks to keep legal context intact
    # 1500-2000 is the 'sweet spot' for legal RAG [16, 17]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 3. Create Vector Store (FAISS)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
    
    # Return as a retriever looking for the top 3 most relevant chunks [18]
    return vectorstore.as_retriever(search_kwargs={"k": 3})

def get_rag_chain(retriever):
    # Temperature 0 ensures deterministic, non-hallucinated legal answers [17, 19]
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create the 'Stuff' chain to inject context into the prompt [20, 21]
    combine_docs_chain = create_stuff_documents_chain(llm, get_qa_prompt())
    
    return create_retrieval_chain(retriever, combine_docs_chain)
