from fastapi import APIRouter
from app.schemas.assessment import SkillAssessmentRequest, SkillAssessmentResponse
from app.services.gap_service import gap_service

router = APIRouter()

@router.post("/evaluate", response_model=SkillAssessmentResponse)
async def evaluate_skills(payload: SkillAssessmentRequest):
    return await gap_service.analyze_gap