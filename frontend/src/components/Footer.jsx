export default function Footer() {
  return (
    <footer className="bg-slate-900 text-slate-400 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-white font-semibold mb-4">About</h3>
            <p className="text-sm">
              AI Project Planner Agent helps you convert project ideas into
              structured development plans using artificial intelligence.
            </p>
          </div>
        </div>
        <div className="border-t border-slate-800 mt-8 pt-8 text-center text-sm">
          <p>&copy; 2026 AI Project Planner Agent. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}
