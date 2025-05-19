
from utils.rag_toolkit import query_rag

def handle_chat(user_message):
    response = query_rag(user_message)
    return {"response": response}
