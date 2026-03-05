from app.core.config import get_settings

settigs = get_settings()

class AIPlanner:
    def __init__(self):
        self.endpoint = settigs.azure_openai_endpoint
        self.api_key = settigs.azure_openai_api_key
        self.deployment_name = settigs.azure_openai_deployment
        self.api_version = settigs.azure_openai_api_version

        def generate_plan(self, project_name:str, description: str, tech_stack: list[str]):
            # TODO: Implement real Azure OpenAI call
            return {
                'summary': f'High-level plan for {project_name}',
                'phases': [
                    'Phase 1: Setup',
                    'Phase 2: Core Features',
                    'Phase 3: Deployment'
                ]
            }