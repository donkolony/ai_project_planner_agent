# test_ai_planner.py

from app.services.ai_services import AIPlanner

# Create an instance of AIPlanner
planner = AIPlanner()

# Sample project data
project_name = "AI Project Planner Agent"
description = "An AI agent that generates project plans"
tech_stack = ["Python", "FastAPI", "React", "Tailwind"]

# Generate plan
result = planner.generate_plan(project_name, description, tech_stack)

# Print results
print("Summary:", result["summary"])
print("Phases:")
for phase in result["phases"]:
    print("-", phase)
    