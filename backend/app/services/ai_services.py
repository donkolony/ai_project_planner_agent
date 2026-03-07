from app.core.config import get_settings
from openai import AzureOpenAI
import re

# Load settings
settings = get_settings()


class AIPlanner:
    def __init__(self):
        # Initialize Azure OpenAI client
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version
        )

        self.deployment_name = settings.azure_openai_deployment

    def generate_plan(self, project_name: str, description: str, tech_stack: list[str]):
        # Build the prompt
        prompt = f""" 
Your are a senior software architect. Generate a high-level software project plan. 
        
Project Name: {project_name} 
Description: {description} 
Tech Stack: {", ".join(tech_stack)} 

Please return in the following format:

Summary: <short project summary>
Phases:
1. <phase 1>
2. <phase 2>
3. <phase 3>
...
"""
        # Call Azure OpenAI
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": "You are a senior software architect."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
            temperature=0.7,
        )

        # Extracr AI output
        ai_output = response.choices[0].message.content

        # Extract summary using regex
        summary_match = re.search(r"Summary:\s*(.*)", ai_output)
        summary = (
            summary_match.group(1).strip() if summary_match else "No summary generated"
        )

        # Extract phases using regex
        phases_matches = re.findall(r"\d+\.\s*(.*)", ai_output)
        phases = [phase.strip() for phase in phases_matches] if phases_matches else []

        return {"summary": summary, "phases": phases}
