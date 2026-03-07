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
    def __init__(self):
        # Initialize Azure OpenAI client
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
        )

        self.deployment_name = settings.azure_openai_deployment

    def _parse_ai_response(self, ai_output: str):
        """
        Safely parse AI JSON output.
        """

        try:
            data = json.loads(ai_output)

            summary = data.get("summary", "")
            phases = data.get("phases", [])

            return {"summary": summary, "phases": phases}

        except json.JSONDecodeError as e:
            logging.error(f"JSON parsing failed: {e}")

            return {"summary": "AI returned an invalid response", "phases": []}

    def generate_plan(self, project_name: str, description: str, tech_stack: list[str]):

        try:
            # Build the prompt
            prompt = f""" 
            You are an expert software architect.

            Generate a high-level software project plan. 
                    
            Project Name: {project_name} 
            Description: {description} 
            Tech Stack: {", ".join(tech_stack)} 

            Return the result strictly as JSON in the following format:

            {{
                "summary": "2 sentence summary of the project",
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
                # max_tokens=1000,
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            ai_output = response.choices[0].message.content

            # Parse the JSON response
            return self._parse_ai_response(ai_output)

        except Exception as e:
            # Log error for developers
            logging.error(f"AIPlanner Error: {e}")

            # Safe fallback response for user
            return {
                "Summary: Could not generate plan due to an internal error.\n"
                "Phases:\n1. Setup\n2. Development\n3. Deployment"
            }
