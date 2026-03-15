export default function LoadingSpinner({ message = "Loading..." }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl p-8 text-center">
        <div className="relative w-16 h-16 mx-auto mb-4">
          <div className="absolute inset-0 bg-gradient-to-r from-primary-600 to-primary-400 rounded-full opacity-20 animate-pulse"></div>
          <div className="absolute inset-2 bg-white rounded-full flex items-center justify-center">
            <div className="w-8 h-8 border-3 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
          </div>
        </div>
        <p className="text-slate-700 font-medium">{message}</p>
      </div>
    </div>
  );
}
