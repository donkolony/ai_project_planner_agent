from fastapi import FastAPI
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

# Initialize database tables on startup (Not Needed here: to be removed)
@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(health_router)
app.include_router(planner_router)
