from pydantic import BaseModel
from typing import List

class ProjectBriefRequest(BaseModel):
    target_job_role: str
    skill_focus: str
    difficulty_level: str

class ProjectBriefResponse(BaseModel):
    project_title: str
    objective: str
    tech_stack: List[str]
    hands_on_tasks: List[str]
    recruiter_pitch: str