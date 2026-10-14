from app.schemas.project import ProjectBriefRequest, ProjectBriefResponse

class ProjectService:
    async def build_project(self, payload: ProjectBriefRequest) -> ProjectBriefResponse:
        return ProjectBriefResponse(
            project_title=f"Enterprise {payload.target_job_role} Production System",
            objective=f"Build a level-matched {payload.difficulty_level.lower()} application focusing on {payload.skill_focus}.",
            tech_stack=["Python FastAPI", "Docker", "PostgreSQL", "Redis"],
            hands_on_tasks=[
                "Step 1: Initialize architecture with modular clean separation.",
                "Step 2: Implement core business logic and REST endpoints.",
                "Step 3: Containerize application services using Docker Compose.",
                "Step 4: Write comprehensive unit and integration test suites."
            ],
            recruiter_pitch="Demonstrates hands-on production readiness, container orchestration mastery, and robust backend engineering."
        )

project_service = ProjectService()