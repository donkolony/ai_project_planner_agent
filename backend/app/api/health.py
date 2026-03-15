"""
API router for system health and status checks.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    """
    Check the health status of the API.

    Returns:
        dict: A dictionary containing the current running status of the backend.
    """
    return {"status": "AI Project Planner Backend Running"}
