from fastapi import APIRouter
from app.schemas.project import ProjectBriefRequest, ProjectBriefResponse
from app.services.project_service import project_service

router = APIRouter()

@router.post("/build-brief", response_model=ProjectBriefResponse)
async def generate_project_brief(payload: ProjectBriefRequest):
    return await project_service.build_project(payload)