from app.schemas.roadmap import RoadmapRequest, RoadmapResponse, Milestone

class RoadmapService:
    async def generate_roadmap(self, payload: RoadmapRequest) -> RoadmapResponse:
        milestones = [
            Milestone(
                milestone_id=1,
                title="Foundation & Core Tooling",
                description=f"Master fundamental concepts required for {payload.target_job_role}.",
                estimated_hours=20,
                badge_name="Foundation Pathfinder"
            ),
            Milestone(
                milestone_id=2,
                title="Advanced Competency & Integration",
                description=f"Bridge skill gaps including: {', '.join(payload.missing_skills[:2])}.",
                estimated_hours=35,
                badge_name="SkillGap Closer Badge"
            ),
            Milestone(
                milestone_id=3,
                title="Capstone Portfolio Execution",
                description="Build and deploy a full-scale portfolio project to impress recruiters.",
                estimated_hours=45,
                badge_name="NEXORA Master Builder"
            )
        ]
        return RoadmapResponse(
            target_job_role=payload.target_job_role,
            total_estimated_weeks=6,
            milestones=milestones
        )

roadmap_service = RoadmapService()