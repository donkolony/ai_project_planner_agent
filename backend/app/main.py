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

<<<<<<< HEAD
# Enable CORS to allow frontend requests from localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
=======
# Initialize database tables on startup (Not Needed here: to be removed)
@app.on_event("startup")
def on_startup():
    init_db()

>>>>>>> 5dcd6c24d9f57e1ce9825fa09ad4716bc230cd62

app.include_router(health_router)
app.include_router(planner_router)
