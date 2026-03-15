"""
Database models for the AI Project Planner application.

This module defines the persistent storage schema for project plans using SQLModel.
"""

from sqlmodel import SQLModel, Field
import uuid


class PlanDB(SQLModel, table=True):
    """
    Represents the database schema for a generated project plan.

    Attributes:
        id (str): The primary key. Automatically generated as a unique UUID string.
        project_name (str): The name of the project.
        description (str): The user's original project description.
        tech_stack (str): A string representation of the technology stack.
        recommended_tech_stack (str): A JSON-encoded string of the AI's suggested tech stack.
        summary (str): The AI-generated architectural overview summary.
        phases (str): A JSON-encoded string containing the project phases and tasks.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    project_name: str
    description: str
    tech_stack: str
    recommended_tech_stack: str = "[]"
    summary: str
    phases: str
