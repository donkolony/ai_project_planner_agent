from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from app.services.ai_services import AIPlanner
from app.models.plan import PlanResponse
from app.models.db_models import PlanDB
# from app.core.database import get_session
import json
from uuid import UUID
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/plan", tags=["Planner"])


class PlanRequest(BaseModel):
    project_name: str
    description: str
    tech_stack: list[str]


def get_ai_planner():
    return AIPlanner()


@router.post("/", response_model=PlanResponse)
async def generate_plan(
    payload: PlanRequest,
    # session: Session = Depends(get_session),
    ai_planner: AIPlanner = Depends(get_ai_planner),
):
    logger.info(f"📋 Generating plan for project: {payload.project_name}")
    
    try:
        result = ai_planner.generate_plan(
            project_name=payload.project_name,
            description=payload.description,
            tech_stack=payload.tech_stack,
        )
        logger.info(f"✅ Plan generated successfully for: {payload.project_name}")
    except Exception as e:
        logger.error(f"❌ Error generating plan: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to generate plan: {str(e)}")

    # try:
    #     # Save plan to DB
    #     db_plan = PlanDB(
    #         project_name=payload.project_name,
    #         description=payload.description,
    #         tech_stack=json.dumps(payload.tech_stack),
    #         summary=result["summary"],
    #         phases=json.dumps(result["phases"]),
    #     )
    #     session.add(db_plan)
    #     session.commit()
    #     session.refresh(db_plan)
    #     logger.info(f"💾 Plan saved to database with ID: {db_plan.id}")
    # except Exception as e:
    #     logger.error(f"❌ Error saving plan to database: {str(e)}", exc_info=True)
    #     session.rollback()
    #     raise HTTPException(status_code=500, detail=f"Failed to save plan: {str(e)}")

    return {"summary": result["summary"], "phases": result["phases"]}


@router.get("/{plan_id}", response_model=PlanResponse)
async def get_plan(plan_id: UUID): # session: Session = Depends(get_session)):
    # plan = session.get(PlanDB, plan_id)
    # if not plan:
    #     raise HTTPException(status_code=404, detail="Plan not found")
    # return {"summary": plan.summary, "phases": json.loads(plan.phases)}
    raise HTTPException(status_code=501, detail="Persistence disabled")


@router.get("/", response_model=list[PlanResponse])
async def get_all_plans(): # session: Session = Depends(get_session)):
    # plans = session.exec(select(PlanDB)).all()
    # return [
    #     {"summary": p.summary, "phases": json.loads(p.phases)}
    #     for p in plans
    # ]
    return []