from app.schemas.assessment import SkillAssessmentRequest, SkillAssessmentResponse
from app.core.ai_engine import ai_engine
import json

class GapService:
    async def analyze_gap(self, payload: SkillAssessmentRequest) -> SkillAssessmentResponse:
        prompt = f"Analyze skills for {payload.student_name} aiming for {payload.target_job_role}."
        raw_ai_res = await ai_engine.generate_recommendations(prompt)

        try:
            cleaned = raw_ai_res.replace("json", "").replace("", "").strip()
            data = json.loads(cleaned)
        except Exception:
            data = {
                "market_readiness_score": 68,
                "missing_skills": ["Docker", "Kubernetes", "Advanced CI/CD Pipelines", "System Design"],
                "industry_demand_analysis": f"High market demand for {payload.target_job_role} with emphasis on cloud-native practices.",
                "recommendation_summary": "Bridge missing technical competencies through targeted hands-on project execution."
            }

        return SkillAssessmentResponse(
            student_name=payload.student_name,
            target_job_role=payload.target_job_role,
            market_readiness_score=data.get("market_readiness_score", 70),
            missing_skills=data.get("missing_skills", ["Containerization", "Cloud Deployments"]),
            industry_demand_analysis=data.get("industry_demand_analysis", "Strong industry alignment required."),
            recommendation_summary=data.get("recommendation_summary", "Focus on practical project execution.")
        )

gap_service = GapService()