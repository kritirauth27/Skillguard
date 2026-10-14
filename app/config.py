import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SkillGuard by NEXORA"
    API_V1_STR: str = "/api/v1"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "mock-key-for-hackathon")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()