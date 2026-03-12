export default function Header() {
  return (
    <header className="bg-gradient-to-r from-primary-900 to-primary-900 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <img src="/logo.svg" alt="Project Planner Logo" className="w-20 h-20" />
            <h1 className="text-2xl font-bold">Project Planner</h1>
          </div>
          {/* <p className="text-primary-100 text-sm">Transform ideas into structured plans</p> */}
        </div>
      </div>
    </header>
  )
}
