from fastapi import APIRouter
from app.api.v1.endpoints import assessment, roadmaps, projects, chatbot

api_router = APIRouter()
api_router.include_router(assessment.router, prefix="/assessment", tags=["MOD_01: Skill Gap Engine"])
api_router.include_router(roadmaps.router, prefix="/roadmaps", tags=["MOD_02: Dynamic Roadmaps"])
api_router.include_router(projects.router, prefix="/projects", tags=["MOD_03: Project Builder"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["MOD_04: Resume & Mentor Chatbot"])