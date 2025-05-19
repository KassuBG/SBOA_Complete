
from fastapi import APIRouter
from agents import lead_agent, chat_agent

router = APIRouter()

@router.post("/lead")
def score_lead(data: dict):
    return lead_agent.capture_leads(data)

@router.post("/chat")
def chat_response(data: dict):
    return chat_agent.handle_chat(data["message"])
