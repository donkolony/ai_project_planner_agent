"""
API router for project plan generation and retrieval.

Handles endpoints related to creating AI-generated project plans
and fetching stored plans from the database.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Session
from app.services.ai_services import AIPlanner
from app.models.plan import PlanResponse
from app.models.db_models import PlanDB
from app.core.database import get_session
import json

router = APIRouter(prefix="/plan", tags=["Planner"])

ai_planner = AIPlanner()


class PlanRequest(BaseModel):
    """
    Schema for an incoming project plan generation request.

    Attributes:
        project_name (str): The name of the proposed project.
        description (str): A detailed description of the project idea.
        tech_stack (list[str]): A list of technologies to be used.
    """

    project_name: str
    description: str
    tech_stack: Optional[List[str]] = []


@router.post("/", response_model=PlanResponse)
async def generate_plan(payload: PlanRequest, session: Session = Depends(get_session)):
    """
    Generate a new AI-driven project plan based on user requirements.

    Args:
        payload (PlanRequest): The project details submitted by the user.
        session (Session): The database session dependency.

    Returns:
        PlanResponse: The newly generated project plan containing the architecture summary and phases.
    """
    result = ai_planner.generate_plan(
        project_name=payload.project_name,
        description=payload.description,
        tech_stack=payload.tech_stack,
    )

    return result


@router.get("/{plan_id}", response_model=PlanResponse)
async def get_plan(plan_id: str, session: Session = Depends(get_session)):
    """
    Retrieve a specific project plan by its ID.

    Args:
        plan_id (str): The unique identifier of the plan to retrieve.
        session (Session): The database session dependency.

    Returns:
        PlanResponse: The requested project plan.

    Raises:
        HTTPException: If no plan with the given ID is found in the database.
    """
    plan = session.get(PlanDB, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    return {
        "summary": plan.summary,
        "recommended_tech_stack": json.loads(plan.recommended_tech_stack),
        "phases": json.loads(plan.phases),
    }


@router.get("/", response_model=list[PlanResponse])
async def get_all_plans(session: Session = Depends(get_session)):
    """
    Retrieve all previously generated project plans.

    Args:
        session (Session): The database session dependency.

    Returns:
        list[PlanResponse]: A list of all stored project plans.
    """
    plans = session.query(PlanDB).all()
    return [
        {
            "summary": p.summary,
            "recommended_tech_stack": json.loads(p.recommended_tech_stack),
            "phases": json.loads(p.phases),
        }
        for p in plans
    ]
