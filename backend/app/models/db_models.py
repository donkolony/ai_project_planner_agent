from sqlmodel import SQLModel, Field
from typing import List
import uuid


class PlanDB(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    project_name: str
    description: str
    tech_stack: str  # comma-separated
    summary: str
    phases: str  # JSON string
