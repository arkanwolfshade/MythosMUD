export function MapPageLoadingView() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-mythos-terminal-primary mx-auto mb-4"></div>
        <p>Loading map...</p>
      </div>
    </div>
  );
}

export function MapPageErrorView({ error }: { error: string }) {
  return (
    <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="text-center max-w-md p-6">
        <h1 className="text-2xl font-bold mb-4 text-mythos-terminal-error">Error</h1>
        <p className="mb-4">{error}</p>
        <button
          onClick={() => {
            window.close();
          }}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          Close
        </button>
      </div>
    </div>
  );
}

export function MapPageAuthRequiredView() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="text-center max-w-md p-6">
        <h1 className="text-2xl font-bold mb-4">Authentication Required</h1>
        <p className="mb-4">Please log in to view the map.</p>
        <button
          onClick={() => (window.location.href = '/')}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          Go to Login
        </button>
      </div>
    </div>
  );
}
