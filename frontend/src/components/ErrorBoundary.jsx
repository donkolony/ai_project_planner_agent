import React from 'react';

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null, errorInfo: null };
    }

    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
    }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.error("ErrorBoundary caught an error:", error, errorInfo);
        this.setState({
            error: error,
            errorInfo: errorInfo
        });
    }

    render() {
        if (this.state.hasError) {
            // You can render any custom fallback UI
            return (
                <div className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-4">
                    <div className="max-w-xl bg-white rounded-lg shadow-md p-8 border-t-4 border-red-500">
                        <h1 className="text-2xl font-bold text-red-600 mb-4">Oops! Something went wrong.</h1>
                        <p className="text-slate-600 mb-4">
                            The application encountered an unexpected error and could not be rendered.
                            This commonly happens if there is an issue with the local development environment or data fetching.
                        </p>
                        {this.state.error && (
                            <div className="bg-slate-100 p-4 rounded text-sm overflow-auto mb-4 border border-slate-300">
                                <p className="font-semibold font-mono text-red-500">{this.state.error.toString()}</p>
                                <pre className="mt-2 text-slate-500 text-xs">
                                    {this.state.errorInfo?.componentStack}
                                </pre>
                            </div>
                        )}
                        <button
                            onClick={() => window.location.reload()}
                            className="px-4 py-2 bg-primary-600 text-white rounded hover:bg-primary-700 transition"
                        >
                            Reload Page
                        </button>
                    </div>
                </div>
            );
        }

        return this.props.children;
    }
}

export default ErrorBoundary;
