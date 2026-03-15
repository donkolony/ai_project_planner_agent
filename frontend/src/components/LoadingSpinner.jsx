import { useState } from "react";

/**
 * Renders a list of GitHub-ready issues generated from project phases.
 * Provides functionality to copy formatted Markdown issues to the clipboard.
 *
 * @param {Object} props - The component props.
 * @param {Array<{name: string, tasks: string[]}>} props.phases - An array of project phase objects, each containing a name and a list of tasks.
 * @param {string} props.projectName - The name of the overall project, used to contextualize issue descriptions.
 * @returns {JSX.Element} The rendered issue list component.
 */
export default function IssueList({ phases, projectName }) {
  const [copiedIndex, setCopiedIndex] = useState(null);

  // Generate GitHub-ready issues from phases and tasks
  const generateIssues = () => {
    const issues = [];

    phases.forEach((phase, phaseIndex) => {
      // Create phase setup issue
      issues.push({
        id: `phase-${phaseIndex}`,
        title: `[${phase.name}] Setup and Planning`,
        description: `Initialize ${phase.name} phase for ${projectName}`,
        labels: [
          "phase",
          "setup",
          phase.name.toLowerCase().replace(/\s+/g, "-"),
        ],
        acceptance_criteria: [
          `Define ${phase.name} scope and objectives`,
          "Create detailed task list",
          "Assign resources",
          "Set milestones and deadlines",
        ],
      });

      // Create task issues
      if (phase.tasks && Array.isArray(phase.tasks)) {
        phase.tasks.forEach((task, taskIndex) => {
          issues.push({
            id: `task-${phaseIndex}-${taskIndex}`,
            title: task,
            description: `Task from ${phase.name} phase\n\nProject: ${projectName}`,
            labels: [phase.name.toLowerCase().replace(/\s+/g, "-"), "task"],
            acceptance_criteria: [
              "Task is completed",
              "Code is reviewed",
              "Tests are passing",
              "Documentation is updated",
            ],
          });
        });
      }
    });

    return issues;
  };

  const issues = generateIssues();

  const copyToClipboard = (issue, index) => {
    const issueMarkdown = `# ${issue.title}

## Description
${issue.description}

## Acceptance Criteria
${issue.acceptance_criteria.map((criterion) => `- [ ] ${criterion}`).join("\n")}

## Labels
${issue.labels.map((label) => `\`${label}\``).join(", ")}`;

    navigator.clipboard.writeText(issueMarkdown).then(() => {
      setCopiedIndex(index);
      setTimeout(() => setCopiedIndex(null), 2000);
    });
  };

  if (issues.length === 0) {
    return (
      <div className="card">
        <h2 className="card-header">Git Issues</h2>
        <p className="text-slate-600">No issues available</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2 className="card-header">🐙 Git-Ready Issues</h2>
      <p className="text-sm text-slate-600 mb-4">
        Copy any issue to clipboard and paste into your GitHub repository
      </p>

      <div className="space-y-3 max-h-96 overflow-y-auto">
        {issues.map((issue, index) => (
          <div
            key={issue.id}
            className="border border-slate-200 rounded-lg p-4 hover:shadow-md transition"
          >
            <div className="flex items-start justify-between gap-4">
              <div className="flex-1 min-w-0">
                <h3 className="font-semibold text-slate-900 text-sm mb-1 line-clamp-2">
                  {issue.title}
                </h3>
                <p className="text-xs text-slate-600 mb-2">
                  {issue.description}
                </p>

                <div className="flex flex-wrap gap-1 mb-2">
                  {issue.labels.map((label) => (
                    <span
                      key={label}
                      className="inline-block bg-slate-100 text-slate-700 px-2 py-0.5 rounded text-xs"
                    >
                      {label}
                    </span>
                  ))}
                </div>

                <details className="text-xs">
                  <summary className="cursor-pointer text-primary-600 hover:text-primary-700">
                    View acceptance criteria
                  </summary>
                  <ul className="mt-2 space-y-1 text-slate-600">
                    {issue.acceptance_criteria.map((criterion, idx) => (
                      <li key={idx} className="ml-4">
                        • {criterion}
                      </li>
                    ))}
                  </ul>
                </details>
              </div>

              <button
                onClick={() => copyToClipboard(issue, index)}
                className="flex-shrink-0 px-3 py-1.5 bg-slate-100 hover:bg-primary-600 hover:text-white text-slate-700 rounded text-xs font-medium transition"
              >
                {copiedIndex === index ? "✓ Copied" : "Copy"}
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 pt-4 border-t border-slate-200">
        <p className="text-sm text-slate-600">
          Total Issues: <span className="font-semibold">{issues.length}</span>
        </p>
      </div>
    </div>
  );
}
