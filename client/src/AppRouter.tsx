/**
 * App Router component.
 *
 * Handles routing between the main app and the standalone map page.
 * The map page route doesn't clear tokens, allowing it to read from localStorage.
 */

import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { App } from './App';

// Lazy load MapPage for code splitting
const MapPage = lazy(() => import('./pages/MapPage').then(m => ({ default: m.MapPage })));

function LoadingFallback() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-mythos-terminal-primary mx-auto mb-4"></div>
        <p>Loading...</p>
      </div>
    </div>
  );
}

/**
 * Main router component that handles routing.
 */
export function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/map"
          element={
            <Suspense fallback={<LoadingFallback />}>
              <MapPage />
            </Suspense>
          }
        />
        <Route path="/*" element={<App />} />
      </Routes>
    </BrowserRouter>
  );
}
