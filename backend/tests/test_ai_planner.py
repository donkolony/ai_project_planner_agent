from tests.mocks.mock_ai_planner import MockAIPlanner


def test_mock_ai_planner_returns_expected_structure():
    planner = MockAIPlanner()

    result = planner.generate_plan(
        project_name="AI Project Planner Agent",
        description="An AI agent that generates project plans",
        tech_stack=["Python", "FastAPI", "React"],
    )

    assert isinstance(result, dict)
    assert "summary" in result
    assert "phases" in result
    assert isinstance(result["phases"], list)
    # spot-check the mock content
    assert result["summary"] == "Mock summary"
    assert result["phases"][0]["name"] == "Mock phase 1"
