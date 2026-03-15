from pydantic import BaseModel
from typing import List


class Phase(BaseModel):
    name: str
    tasks: List[str]


class PlanResponse(BaseModel):
    summary: str
    phases: List[Phase]
