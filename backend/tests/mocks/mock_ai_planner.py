"""
Mock implementation of the AI service for testing purposes.

Provides a predictable, deterministic response to avoid making actual
API calls to Azure OpenAI during the test suite execution.
"""


class MockAIPlanner:
    """
    A simulated version of the AIPlanner service.
    """

    def generate_plan(self, project_name: str, description: str, tech_stack: list[str]):
        """
        Simulate the generation of a project plan.

        Args:
            project_name (str): Name of the project.
            description (str): Description of the project.
            tech_stack (list[str]): List of technologies.

        Returns:
            dict: A static, mocked project plan structure containing
                  'summary' and 'phases'.
        """
        return {
            "summary": "Mock summary",
            "phases": [
                {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
                {"name": "Mock phase 2", "tasks": ["Task C"]},
            ],
        }
