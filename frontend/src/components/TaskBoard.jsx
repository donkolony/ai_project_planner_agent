/**
 * Renders a visual board of all tasks flattened from the project phases.
 * Displays tasks in a grid layout with interactive (visual-only) checkboxes.
 *
 * @param {Object} props - The component props.
 * @param {Array<{name: string, tasks: string[]}>} props.phases - An array of phase objects containing the phase name and its associated tasks.
 * @returns {JSX.Element} The rendered task board component.
 */
export default function TaskBoard({ phases }) {
  if (!phases || phases.length === 0) {
    return (
      <div className="card">
        <h2 className="card-header">Task Breakdown</h2>
        <p className="text-slate-600">No tasks available</p>
      </div>
    );
  }

  const allTasks = [];
  phases.forEach((phase, phaseIndex) => {
    if (phase.tasks && Array.isArray(phase.tasks)) {
      phase.tasks.forEach((task, taskIndex) => {
        allTasks.push({
          id: `${phaseIndex}-${taskIndex}`,
          task,
          phase: phase.name,
        });
      });
    }
  });

  return (
    <div className="card">
      <h2 className="card-header">📋 Task Breakdown</h2>

      {allTasks.length === 0 ? (
        <p className="text-slate-600">No tasks found</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {allTasks.map((item) => (
            <div
              key={item.id}
              className="bg-gradient-to-br from-slate-50 to-slate-100 rounded-lg p-4 border border-slate-200 hover:shadow-md transition"
            >
              <div className="flex items-start gap-3">
                <div className="mt-1">
                  <input
                    type="checkbox"
                    className="w-4 h-4 rounded border-slate-300 text-primary-600 cursor-pointer"
                  />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-slate-900 line-clamp-3">
                    {item.task}
                  </p>
                  <p className="text-xs text-slate-500 mt-2">
                    <span className="inline-block bg-primary-100 text-primary-700 px-2 py-1 rounded">
                      {item.phase}
                    </span>
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      <div className="mt-6 pt-4 border-t border-slate-200">
        <div className="flex justify-between text-sm text-slate-600">
          <span>
            Total Tasks:{" "}
            <span className="font-semibold">{allTasks.length}</span>
          </span>
          <span>
            Phases: <span className="font-semibold">{phases.length}</span>
          </span>
        </div>
      </div>
    </div>
  );
}
