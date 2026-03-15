import ProjectForm from "../components/ProjectForm";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-slate-900 mb-4">
            Transform Your Project Ideas
          </h2>
          <p className="text-xl text-slate-600 max-w-2xl mx-auto">
            Submit your project concept and let AI create a detailed development
            plan with architecture, phases, tasks, and ready-to-use GitHub
            issues.
          </p>
        </div>

        <ProjectForm />

        <div className="mt-16 grid grid-cols-1 md:grid-cols-2 gap-8"></div>
      </div>
    </div>
  );
}
