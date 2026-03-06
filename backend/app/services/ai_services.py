from app.core.config import get_settings
from openai import AzureOpenAI

settings = get_settings()


class AIPlanner:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            api_version=settings.azure_openai_api_version,
            endpoint=settings.azure_openai_endpoint,
        )

        self.deployment_name = settings.azure_openai_deployment

    def generate_plan(self, project_name: str, description: str, tech_stack: list[str]):
        prompt = f""" 
        Create a high-level software project plan. 
        
        Project Name: {project_name} 
        Description: {description} 
        Tech Stack: {", ".join(tech_stack)} 
        
        Provide: 
        1. A short project summary 
        2. A list of development phases 
        
        """

        response = self.client.chat.completion.create(
            model=self.deployment_name,
            message=[
                {"role": "system", "content": "You are a senior software architect."},
                {"role": "user", "content": prompt},
            ],
        )

        ai_output = response.choices[0].message.content

        return {
            "summary": ai_output,
            "phases": [
                "Phase 1: Setup",
                "Phase 2: Development",
                "Phase 3: Deployment",
            ],
        }
