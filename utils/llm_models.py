from langchain_groq import ChatGroq

def load_llm():
    # Using ChatGroq with Gemma
    return ChatGroq(model="gemma2-9b-it")