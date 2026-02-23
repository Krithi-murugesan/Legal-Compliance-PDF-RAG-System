from langchain_core.prompts import ChatPromptTemplate

# Legal System Prompt: Enforces strict context-based answering and liability disclaimers
LEGAL_SYSTEM_PROMPT = (
    "You are an assistant for professional legal and compliance question-answering tasks. "
    "Use ONLY the following pieces of retrieved context to answer the question. "
    "If you don't know the answer based on the context, state that you do not know. "
    "IMPORTANT: You are an information retrieval assistant, not a licensed attorney. "
    "Do not provide official legal advice. Always reference specific pages."
    "\n\n"
    "{context}"
)

def get_qa_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", LEGAL_SYSTEM_PROMPT),
        ("human", "{input}"),
    ])
