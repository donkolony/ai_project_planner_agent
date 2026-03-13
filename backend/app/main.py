from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.health import router as health_router
from app.api.planner import router as planner_router
import os


"""
This module should:
    - Create app
    - Register routes
    - Nothing else (all endpoints live in api/)
"""

settings = get_settings()

app = FastAPI(title=settings.app_name, version="0.1.0")

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
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "http://127.0.0.1:5176",
    ]
else:
    # Production: Allow from environment variable
    frontend_urls = os.getenv("FRONTEND_URL", "https://ai-project-planner.azurewebsites.net")
    # Support multiple URLs separated by comma
    allow_origins = [url.strip() for url in frontend_urls.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(planner_router)
