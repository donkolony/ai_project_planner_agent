import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createPlan } from "../api/plannerApi";

export default function ProjectForm() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    project_name: "",
    description: "",
    tech_stack: [],
  });
  const [techInput, setTechInput] = useState("");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleAddTech = (e) => {
    e.preventDefault();
    if (techInput.trim() && !formData.tech_stack.includes(techInput.trim())) {
      setFormData((prev) => ({
        ...prev,
        tech_stack: [...prev.tech_stack, techInput.trim()],
      }));
      setTechInput("");
    }
  };

  const handleRemoveTech = (tech) => {
    setFormData((prev) => ({
      ...prev,
      tech_stack: prev.tech_stack.filter((t) => t !== tech),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      if (!formData.project_name.trim() || !formData.description.trim()) {
        setError("Please fill in all required fields");
        return;
      }

      const response = await createPlan({
        project_name: formData.project_name,
        description: formData.description,
        tech_stack: formData.tech_stack,
      });

      setFormData({
        project_name: "",
        description: "",
        tech_stack: [],
      });

      navigate("/plan", { state: { plan: response } });
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          "Failed to generate plan. Please try again.",
      );
      console.error("Plan generation error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card max-w-2xl mx-auto">
      <h2 className="card-header">Create Your Project Plan</h2>

      {error && (
        <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-md">
          <p className="text-red-700 text-sm">{error}</p>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="project_name" className="label">
            Project Name <span className="text-red-500">*</span>
          </label>
          <input
            type="text"
            id="project_name"
            name="project_name"
            value={formData.project_name}
            onChange={handleInputChange}
            placeholder="e.g., AI Study Planner"
            className="input-field"
            required
          />
        </div>

        <div>
          <label htmlFor="description" className="label">
            Description <span className="text-red-500">*</span>
          </label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            placeholder="Describe your project idea in detail..."
            rows="5"
            className="input-field"
            required
          />
        </div>

        <div>
          <label htmlFor="tech_input" className="label">
            Technology Stack
          </label>
          <div className="flex gap-2 mb-3">
            <input
              type="text"
              id="tech_input"
              value={techInput}
              onChange={(e) => setTechInput(e.target.value)}
              placeholder="e.g., React, Node.js"
              className="input-field"
              onKeyPress={(e) => e.key === "Enter" && handleAddTech(e)}
            />
            <button
              type="button"
              onClick={handleAddTech}
              className="btn-secondary"
            >
              Add
            </button>
          </div>

          {formData.tech_stack.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {formData.tech_stack.map((tech) => (
                <div
                  key={tech}
                  className="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm flex items-center gap-2"
                >
                  <span>{tech}</span>
                  <button
                    type="button"
                    onClick={() => handleRemoveTech(tech)}
                    className="hover:text-primary-900 font-bold"
                  >
                    ×
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="flex gap-3 pt-4">
          <button
            type="submit"
            disabled={loading}
            className="btn-primary flex-1 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Generating Plan..." : "Generate Plan"}
          </button>
        </div>
      </form>
    </div>
  );
}
