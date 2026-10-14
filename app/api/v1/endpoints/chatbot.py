from fastapi import APIRouter
from app.schemas.chatbot import MentorQueryRequest, MentorQueryResponse
from app.services.chatbot_service import chatbot_service

router = APIRouter()

@router.post("/mentor", response_model=MentorQueryResponse)
async def mentor_chat(payload: MentorQueryRequest):
    return await chatbot_service.consult_mentor