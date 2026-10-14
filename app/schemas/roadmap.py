from typing import List
from pydantic import BaseModel

class Milestone(BaseModel):
    milestone_id: int
    title: str
    description: str
    estimated_hours: int
    badge_name: str

class RoadmapRequest(BaseModel):
    target_job_role: str
    missing_skills: List[str]

class RoadmapResponse(BaseModel):
    target_job_role: str
    total_estimated_weeks: int
    milestones: List[Milestone]