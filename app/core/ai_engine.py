import json
import google.generativeai as genai
from app.config import settings

if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "mock-key-for-hackathon":
    genai.configure(api_key=settings.GEMINI_API_KEY)

class AIEngine:
    @staticmethod
    async def generate_recommendations(prompt: str) -> str:
        if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "mock-key-for-hackathon":
            return json.dumps({
                "status": "success",
                "mode": "fallback_simulation",
                "message": "AI Engine operating in high-speed simulation mode.",
                "insights": prompt[:100]
            })
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return json.dumps({"error": str(e)})

ai_engine = AIEngine()