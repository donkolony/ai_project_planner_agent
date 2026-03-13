import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.health import router as health_router
from app.api.planner import router as planner_router
from app.core.database import init_db # not needed to be removed


"""
This module should:
    - Create app
    - Register routes
    - Nothing else (all endpoints live in api/)
"""

settings = get_settings()

app = FastAPI(title=settings.app_name, version="0.1.0")


# Enable CORS to allow frontend requests from localhost:5173

# Configure CORS based on environment
if settings.environment == "development":
    allow_origins = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
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
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables on startup (Not Needed here: to be removed)
@app.on_event("startup")
def on_startup():
    init_db()



app.include_router(health_router)
app.include_router(planner_router)
