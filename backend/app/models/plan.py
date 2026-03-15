"""
Pydantic schemas for API response modeling.

This module defines the data structures used for serializing and
validating the project plans returned to the frontend.
"""

from pydantic import BaseModel
from typing import List, Optional


class Phase(BaseModel):
    """
    Represents a specific development phase within a project plan.

    Attributes:
        name (str): The name of the phase (e.g., 'Setup', 'Frontend Development').
        tasks (List[str]): A list of specific actionable tasks belonging to this phase.
    """

    name: str
    tasks: List[str]


class PlanResponse(BaseModel):
    """
    The main response schema for a completed AI project plan.

    Attributes:
        summary (str): A high-level architectural and technical overview of the project.
        recommended_tech_stack (Optional[List[str]]): A list of technologies suggested by the AI. Defaults to an empty list.
        phases (List[Phase]): A structured roadmap consisting of multiple development phases.
    """

    summary: str
    recommended_tech_stack: Optional[List[str]] = []
    phases: List[Phase]