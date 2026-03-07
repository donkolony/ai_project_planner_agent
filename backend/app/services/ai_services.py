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

Return in this exact format:

Summary: <short project summary, 1-2 sentences>
Phases:
1. <phase 1>
2. <phase 2>
3. <phase 3>
...

Do not include any markdown symbols like ** or _.
"""
        # Call AzureOpenAI chat endpoint
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": "You are a senior software architect."},
                {"role": "user", "content": prompt},
            ],
            # max_tokens=1000,
            temperature=0.7,
        )

        
        ai_output = response.choices[0].message.content

        """
        .+? -> stops at the first line break
        (?:\n|$) -> stops at a newline or end of string
        re.IGNORECASE -> matches summary regardless of capitilzation
        .strip() -> removes extra spaces and symbols at the edges
        """

        # Extract summary
        summary_match = re.search(r"Summary:\s*(.+?)(?:\n|$)", ai_output, re.IGNORECASE)
        if summary_match:
            summary = summary_match.group(1).strip()
        else:
            # fallback to firsts line if no excplicit Summary
            summary = ai_output.split("\n")[0].strip()
        summary = re.sub(r"[*_`]", "", summary)

        # Extract phases
        phases_matches = re.findall(r"\d+\.\s*(.*)", ai_output)
        phases = [phase.strip() for phase in phases_matches] if phases_matches else []

        return {"summary": summary, "phases": phases}
