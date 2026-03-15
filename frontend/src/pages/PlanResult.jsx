import { useLocation, useNavigate } from "react-router-dom";
import ArchitectureView from "../components/ArchitectureView";
import WeeklyPlanView from "../components/WeeklyPlanView";
import TaskBoard from "../components/TaskBoard";
import IssueList from "../components/IssueList";

/**
 * Renders the comprehensive results dashboard for a generated project plan.
 * Expects to receive the generated `plan` object and `projectName` via
 * React Router's `location.state` from the previous navigation event.
 * Assembles and displays the Architecture, Roadmap, Tasks, and Issues sub-components.
 *
 * @returns {JSX.Element} The rendered project plan dashboard, or a fallback UI if no state data is found.
 */
export default function PlanResult() {
  const location = useLocation();
  const navigate = useNavigate();
  const plan = location.state?.plan;

  if (!plan) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="card max-w-md text-center">
          <h2 className="card-header">No Plan Found</h2>
          <p className="text-slate-600 mb-4">
            Please generate a plan first by submitting a project idea.
          </p>
          <button onClick={() => navigate("/")} className="btn-primary">
            Back to Home
          </button>
        </div>
      </div>
    );
  }

  const projectName = location.state?.projectName || "Project";

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <button
            onClick={() => navigate("/")}
            className="text-primary-600 hover:text-primary-700 text-sm font-medium mb-4"
          >
            ← Back to Home
          </button>
          <h1 className="text-3xl font-bold text-slate-900">
            {projectName} - Development Plan
          </h1>
          <p className="text-slate-600 mt-2">
            Your AI-generated project plan with architecture, phases, tasks, and
            issues
          </p>
        </div>

        {/* Navigation Tabs */}
        <div className="bg-white rounded-lg shadow-md mb-8 p-2 flex flex-wrap gap-2">
          <a
            href="#architecture"
            className="px-4 py-2 rounded bg-primary-600 text-white text-sm font-medium"
          >
            Architecture
          </a>
          <a
            href="#roadmap"
            className="px-4 py-2 rounded hover:bg-slate-100 text-slate-700 text-sm font-medium"
          >
            Roadmap
          </a>
          <a
            href="#tasks"
            className="px-4 py-2 rounded hover:bg-slate-100 text-slate-700 text-sm font-medium"
          >
            Tasks
          </a>
          <a
            href="#issues"
            className="px-4 py-2 rounded hover:bg-slate-100 text-slate-700 text-sm font-medium"
          >
            Issues
          </a>
        </div>

        {/* Main Content */}
        <div className="space-y-8">
          {/* Architecture Section */}
          <section id="architecture">
            <ArchitectureView summary={plan.summary} />
          </section>

          {/* Weekly Plan Section */}
          <section id="roadmap">
            <WeeklyPlanView phases={plan.phases} />
          </section>

          {/* Task Board Section */}
          <section id="tasks">
            <TaskBoard phases={plan.phases} />
          </section>

          {/* Issues Section */}
          <section id="issues">
            <IssueList phases={plan.phases} projectName={projectName} />
          </section>
        </div>

        {/* Export Section */}
        <div className="mt-12 card bg-blue-50 border-blue-200">
          <h2 className="card-header text-blue-900">💾 Export & Continue</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button className="btn-secondary hover:bg-blue-100 text-blue-900">
              📥 Download as JSON
            </button>
            <button className="btn-secondary hover:bg-blue-100 text-blue-900">
              📄 Export as PDF
            </button>
            <button onClick={() => navigate("/")} className="btn-primary">
              ➕ Create New Plan
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
