export default function ArchitectureView({ summary }) {
  if (!summary) {
    return (
      <div className="card">
        <h2 className="card-header">Architecture Overview</h2>
        <p className="text-slate-600">No architecture data available</p>
      </div>
    )
  }

  return (
    <div className="card">
      <h2 className="card-header">🏗️ Architecture Overview</h2>
      <div className="prose prose-sm max-w-none text-slate-700">
        <p className="whitespace-pre-wrap">{summary}</p>
      </div>
      
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
          <h3 className="font-semibold text-blue-900 mb-2">Frontend</h3>
          <p className="text-sm text-blue-700">React + Vite with Tailwind CSS</p>
        </div>
        <div className="bg-green-50 border border-green-200 rounded-lg p-4">
          <h3 className="font-semibold text-green-900 mb-2">Backend</h3>
          <p className="text-sm text-green-700">FastAPI with SQLModel</p>
        </div>
        <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
          <h3 className="font-semibold text-purple-900 mb-2">Database</h3>
          <p className="text-sm text-purple-700">SQLite with SQLModel ORM</p>
        </div>
        <div className="bg-orange-50 border border-orange-200 rounded-lg p-4">
          <h3 className="font-semibold text-orange-900 mb-2">AI Services</h3>
          <p className="text-sm text-orange-700">Azure OpenAI API Integration</p>
        </div>
      </div>
    </div>
  )
}
