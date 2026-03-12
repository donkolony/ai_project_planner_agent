import ProjectForm from '../components/ProjectForm'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-slate-900 mb-4">
            Transform Your Project Ideas
          </h2>
          <p className="text-xl text-slate-600 max-w-2xl mx-auto">
            Submit your project concept and let AI create a detailed development plan
            with architecture, phases, tasks, and ready-to-use GitHub issues.
          </p>
        </div>

        {/* <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div className="bg-white rounded-lg p-6 shadow-md border-l-4 border-blue-500">
            <div className="text-3xl mb-3">💡</div>
            <h3 className="font-semibold text-slate-900 mb-2">Smart Planning</h3>
            <p className="text-slate-600 text-sm">
              AI-powered analysis to break down your project into actionable phases
            </p>
          </div>

          <div className="bg-white rounded-lg p-6 shadow-md border-l-4 border-green-500">
            <div className="text-3xl mb-3">📋</div>
            <h3 className="font-semibold text-slate-900 mb-2">Task Breakdown</h3>
            <p className="text-slate-600 text-sm">
              Detailed task lists organized by phase with clear deliverables
            </p>
          </div>

          <div className="bg-white rounded-lg p-6 shadow-md border-l-4 border-purple-500">
            <div className="text-3xl mb-3">🐙</div>
            <h3 className="font-semibold text-slate-900 mb-2">GitHub Ready</h3>
            <p className="text-slate-600 text-sm">
              Auto-generated issues ready to import into your GitHub repository
            </p>
          </div>
        </div> */}

        <ProjectForm />

        <div className="mt-16 grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* <div>
            <h3 className="text-lg font-semibold text-slate-900 mb-4">How It Works</h3>
            <ol className="space-y-3 text-slate-600">
              <li className="flex gap-3">
                <span className="text-primary-600 font-bold">1.</span>
                <span>Describe your project idea and tech stack</span>
              </li>
              <li className="flex gap-3">
                <span className="text-primary-600 font-bold">2.</span>
                <span>AI analyzes and creates a comprehensive development plan</span>
              </li>
              <li className="flex gap-3">
                <span className="text-primary-600 font-bold">3.</span>
                <span>Review architecture, phases, tasks, and issues</span>
              </li>
              <li className="flex gap-3">
                <span className="text-primary-600 font-bold">4.</span>
                <span>Copy issues to your GitHub repository and start building</span>
              </li>
            </ol>
          </div> */}

          {/* <div>
            <h3 className="text-lg font-semibold text-slate-900 mb-4">Features</h3>
            <ul className="space-y-2 text-slate-600">
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Architecture visualization
              </li>
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Weekly sprint roadmap
              </li>
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Task board with phase grouping
              </li>
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Git-ready issues
              </li>
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Copy to clipboard functionality
              </li>
              <li className="flex items-center gap-2">
                <span className="text-green-600">✓</span> Responsive design
              </li>
            </ul>
          </div> */}
        </div>
      </div>
    </div>
  )
}
