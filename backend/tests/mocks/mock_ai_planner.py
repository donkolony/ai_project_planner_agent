"""
A mock generate_plan() function to replace the real AI service during tests
"""


class MockAIPlanner:
    def generate_plan(self, project_name, description, tech_stack):
        return {
            "summary": "Mock summary",
            "phases": [
                {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
                {"name": "Mock phase 2", "tasks": ["Task C"]},
            ],
        }
