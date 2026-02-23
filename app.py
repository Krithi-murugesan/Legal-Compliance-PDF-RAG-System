import streamlit as st
import os
from dotenv import load_dotenv
from src.engine import process_pdf_to_retriever, get_rag_chain

load_dotenv()

# UI Configuration [26, 27]
st.set_page_config(page_title="Legal & Compliance RAG", layout="wide")
st.title("📄 Legal Expert PDF Auditor")

# Chat Memory Setup [28, 29]
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for PDF Ingestion [18, 30]
with st.sidebar:
    st.header("Document Upload")
    uploaded_file = st.file_uploader("Upload Legal PDF", type="pdf")
    
    if uploaded_file:
        with st.spinner("Analyzing PDF and building knowledge base..."):
            # Save temporary file for the loader [31, 32]
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.session_state.retriever = process_pdf_to_retriever("temp.pdf")
            st.success("PDF Ready for Auditing!")

# Chat Interface [33, 34]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a compliance question..."):
    if "retriever" not in st.session_state:
        st.error("Please upload a PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Searching document..."):
                chain = get_rag_chain(st.session_state.retriever)
                response = chain.invoke({"input": prompt})
                
                answer = response["answer"]
                
                # Citation and Source Preview Logic [25, 35]
                sources = set()
                for doc in response["context"]:
                    page = doc.metadata.get("page", 0) + 1
                    sources.add(f"Page {page}")
                
                full_res = f"{answer}\n\n**Sources:** {', '.join(sorted(sources))}"
                st.markdown(full_res)
                
                with st.expander("Trust but Verify: View Source Snippets"):
                    for doc in response["context"]:
                        st.info(f"**Snippet from Page {doc.metadata.get('page',0)+1}:**\n\n{doc.page_content}")

                st.session_state.messages.append({"role": "assistant", "content": full_res})
