from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-Powered Student Skill & Career Navigator API by Team NEXORA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Health Check"])
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "tagline": "Know Your Skills. Build Your Future.",
        "status": "operational",
        "docs_url": "/docs"
    }