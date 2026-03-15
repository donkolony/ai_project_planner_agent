"""
Core service for interacting with AI models to generate project plans.

This module encapsulates the logic for prompt construction, Azure OpenAI
API communication, and robust parsing of AI-generated content.
"""

import re
import logging
import json
from app.core.config import get_settings
from openai import AzureOpenAI

# Setup logging
logging.basicConfig(level=logging.ERROR)

# Load settings
settings = get_settings()


class AIPlanner:
    """
    A service class to handle project plan generation using Azure OpenAI.

    Attributes:
        client (AzureOpenAI): The initialized Azure OpenAI client.
        deployment_name (str): The specific model deployment name to target.
    """

    def __init__(self):
        """
        Initialize the AIPlanner with configuration settings from the environment.
        """
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
        )

        self.deployment_name = settings.azure_openai_deployment

    def _parse_ai_response(self, ai_output: str):
        """
        Safely parse the raw string output from the AI into a structured dictionary.

        Args:
            ai_output (str): The raw JSON string returned by the AI model.

        Returns:
            dict: A dictionary containing 'summary' and 'phases'.
                  Returns a fallback structure if parsing fails.
        """
        try:
            data = json.loads(ai_output)

            summary = data.get("summary", "")
            phases = data.get("phases", [])

            return {"summary": summary, "phases": phases}

        except json.JSONDecodeError as e:
            logging.error(f"JSON parsing failed: {e}")

            return {"summary": "AI returned an invalid response", "phases": []}


def generate_plan(
    self, project_name: str, description: str, tech_stack: list[str] = None
):
    """
    Construct a prompt and call the AI model to generate a project roadmap.

    This method handles the high-level orchestration of the AI request,
    including prompt engineering and error handling for the API call.

    Args:
        project_name (str): Name of the project.
        description (str): Detailed user description of the project goal.
        tech_stack (list[str], optional): List of technologies to be integrated. Defaults to None.

    Returns:
        dict: The parsed project plan or a hardcoded fallback if the service fails.
    """
    if tech_stack is None:
        tech_stack = []

    try:
        # Dynamically handle the tech stack input
        if len(tech_stack) > 0:
            stack_context = (
                f"Strictly use the following technologies: {', '.join(tech_stack)}"
            )
        else:
            stack_context = "None provided. You must infer the most appropriate, minimal, and lightweight technologies based solely on the project description."

        # Build the prompt
        prompt = f""" 
            You are an expert software architect.

            Generate a high-level software project plan based on the user's requirements. 
                    
            Project Name: {project_name} 
            Description: {description} 
            Tech Stack: {stack_context} 

            Instructions:
            1. If specific technologies are provided, build the architecture and phases around them.
            2. If no tech stack is provided, deduce the most sensible stack. Do NOT overcomplicate. For example, do not add a backend or database if the description implies a simple static site, CLI tool, or local script.
            
            Return the result strictly as JSON in the exact following format:
            {{
                "summary": "2 sentence summary of the project",
                "recommended_tech_stack": ["tech 1", "tech 2"],
                "phases": [
                    {{
                        "name": "Phase name",
                        "tasks": ["task 1", "task 2"]
                    }}
                ]
            }}

            Do not include any markdown formatting.
            Do not include explanations.
            Return valid JSON only.
            """

        # ... (your existing code to call Azure OpenAI and parse the JSON)

        # Call AzureOpenAI chat endpoint
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior software architect.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            response_format={"type": "json_object"},
        )

        ai_output = response.choices[0].message.content

        # Parse the JSON response
        return self._parse_ai_response(ai_output)

    except Exception as e:
        # Log error for developers
        logging.error(f"AIPlanner Error: {e}")

        # Safe fallback response for user
        return {
            "summary": "Could not generate plan due to an internal error.",
            "phases": [
                {"name": "Setup", "tasks": ["Investigate connection error"]},
                {"name": "Development", "tasks": ["Try again later"]},
            ],
        }
