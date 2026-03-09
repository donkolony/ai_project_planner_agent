from sqlmodel import SQLModel, Field
from typing import List
import uuid


class PlanDB(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_name: str
    description: str
    tech_stack: str  # comma-separated
    summary: str
    phases: str  # JSON string
