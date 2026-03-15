export default function WeeklyPlanView({ phases }) {
  if (!phases || phases.length === 0) {
    return (
      <div className="card">
        <h2 className="card-header">Weekly Sprint Roadmap</h2>
        <p className="text-slate-600">No phases available</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2 className="card-header">📅 Weekly Sprint Roadmap</h2>

      <div className="space-y-4">
        {phases.map((phase, index) => (
          <div
            key={index}
            className="relative pl-8 pb-8 border-l-2 border-primary-300"
          >
            {/* Timeline dot */}
            <div className="absolute -left-3 top-1 w-4 h-4 bg-primary-600 rounded-full border-4 border-white shadow"></div>

            {/* Phase content */}
            <div className="bg-slate-50 rounded-lg p-4">
              <h3 className="font-semibold text-slate-900 text-lg mb-3">
                {phase.name}
              </h3>

              {phase.tasks && phase.tasks.length > 0 && (
                <div>
                  <h4 className="text-sm font-medium text-slate-700 mb-2">
                    Tasks:
                  </h4>
                  <ul className="space-y-2">
                    {phase.tasks.map((task, taskIndex) => (
                      <li
                        key={taskIndex}
                        className="flex items-start gap-2 text-sm text-slate-600"
                      >
                        <span className="text-primary-600 font-bold mt-0.5">
                          ✓
                        </span>
                        <span>{task}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Timeline bottom cap */}
      <div className="ml-4 mt-4 w-0.5 h-4 bg-gradient-to-b from-primary-300 to-transparent"></div>
    </div>
  );
}
