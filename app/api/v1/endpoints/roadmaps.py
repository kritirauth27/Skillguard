from fastapi import APIRouter
from app.schemas.roadmap import RoadmapRequest, RoadmapResponse
from app.services.roadmap_service import roadmap_service

router = APIRouter()

@router.post("/generate", response_model=RoadmapResponse)
async def create_roadmap(payload: RoadmapRequest):
    return await roadmap_service.generate_roadmap