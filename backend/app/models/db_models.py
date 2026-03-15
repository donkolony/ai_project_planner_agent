# from typing import List # not used (to be removed)
from sqlmodel import SQLModel, Field
import uuid


class PlanDB(SQLModel, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True
    )  # generates a unique ID Tag
    project_name: str
    description: str
    tech_stack: str
    summary: str
    phases: str
