from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/plan", tags=["Planner"])


class PlanRequest(BaseModel):
    project_name: str
    description: str
    tech_stack: list[str]


class PlanResponse(BaseModel):
    summary: str
    phases: list[str]


@router.post("/", response_model=PlanResponse)
def generate_plan(payload: PlanRequest):
    return PlanResponse(
        summary=f"High-level plan for {payload.project_name}",
        phases=["Phase 1: Setup", "Phase 2: Core Features", "Phase 3: Deployment"],
    )
