from pydantic import BaseModel
from typing import List

class MentorQueryRequest(BaseModel):
    student_id: str
    query: str

class MentorQueryResponse(BaseModel):
    student_id: str
    mentor_response: str
    suggested_actions: List[str]