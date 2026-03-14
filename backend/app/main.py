from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
# from app.core.database import init_db
from app.api.health import router as health_router
from app.api.planner import router as planner_router
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
This module should:
    - Create app
    - Register routes
    - Nothing else (all endpoints live in api/)
"""

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables (Commented out)
    # init_db()
    # logger.info("✅ Database initialized")
    yield

app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)

# Configure CORS based on environment
if settings.environment == "development":
    allow_origins = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "https://ai-project-planner-agent.vercel.app"
    ]
    
    logger.info("🔒 CORS Configuration - Environment: development")
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"], # Use "*" to allow all methods to prevent headaches
        allow_headers=["*"],
    )
else:
    # Production: Allow from environment variable
    fallback_urls = "https://ai-project-planner.azurewebsites.net,https://ai-project-planner-frontend-git-main-donkolonys-projects.vercel.app,https://ai-project-planner-frontend.vercel.app,http://localhost:5173"
    
    frontend_urls = os.getenv("FRONTEND_URL", fallback_urls)
    allow_origins = [url.strip() for url in frontend_urls.split(",")]

    logger.info(f"🔒 CORS Configuration - Environment: {settings.environment}")
    logger.info(f"🔒 Allowed Origins: {allow_origins}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_origin_regex=r"https://.*\.vercel\.app", # This is how FastAPI handles sub-domain wildcards safely
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(health_router)
app.include_router(planner_router)

# Root endpoint to verify API is running
@app.get("/")
async def root():
    return {
        "message": "AI Project Planner API",
        "version": "0.1.0",
        "status": "running",
        "environment": settings.environment,
    }

logger.info("✅ FastAPI application initialized successfully")