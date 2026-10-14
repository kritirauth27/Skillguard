from typing import List
from pydantic import BaseModel

class SkillAssessmentRequest(BaseModel):
    student_name: str
    degree: str
    current_skills: List[str]
    interests: List[str]
    target_job_role: str

class SkillAssessmentResponse(BaseModel):
    student_name: str
    target_job_role: str
    market_readiness_score: int
    missing_skills: List[str]
    industry_demand_analysis: str
    recommendation_summary: str