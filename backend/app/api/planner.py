from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_services import AIPlanner  # import AI service
from app.models.plan import PlanResponse  # import response model

router = APIRouter(prefix="/plan", tags=["Planner"])

ai_planner = AIPlanner()


class PlanRequest(BaseModel):
    project_name: str
    description: str
    tech_stack: list[str]


@router.post("/", response_model=PlanResponse)
async def generate_plan(payload: PlanRequest):

    result = ai_planner.generate_plan(
        project_name=payload.project_name,
        description=payload.description,
        tech_stack=payload.tech_stack,
    )

    return result
