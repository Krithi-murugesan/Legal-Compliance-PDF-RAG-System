# Legal-Compliance-PDF-RAG-System
# A high-precision RAG assistant for legal and compliance auditing, featuring zero-hallucination guardrails and page-level source citations.
A professional-grade Retrieval-Augmented Generation (RAG) application designed to analyze complex legal documents (like GDPR, ISO standards, or contracts) and provide cited, fact-based answers.

# 🌟 Key Features
Legal-Grade Accuracy: Configured with temperature=0 and a specialized system prompt to prevent hallucinations and legal liability.

Source Citations: Automatically extracts and displays the specific Page Numbers used to generate the answer.

Intelligent Chunking: Uses a recursive 1500-character window to ensure legal clauses remain intact and contextually coherent.

Real-Time UI: Built with Streamlit, featuring loading spinners and a clean chat interface.

# 🛠️ Technical Stack
Framework:  (0.3.x)

LLM: OpenAI GPT-4o

Vector Store: FAISS (Facebook AI Similarity Search)

Frontend: Streamlit

Embeddings: OpenAI text-embedding-3-small

# 📁 Project Structure
## 🚀 Getting Started
1. Installation
Clone the repository and install the dependencies:

2. Configuration
Create a .env file in the root directory and add OpenAI API Key

3. Running the App
## 📈 Real-Time Scenarios Captured
Compliance Auditing: Identifying mandatory requirements (e.g., "When is a DPIA required?").

Regulatory Research: Quick verification of legal deadlines and article definitions.

Risk Management: Identifying exceptions to rights or liability clauses in commercial contracts.

# ⚠️ Disclaimer
This tool is for informational purposes only. It is designed to assist with document retrieval and should not be used as a substitute for professional legal advice.
