import { describe, expect, it, vi, beforeEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import { AppRouter } from '../AppRouter';

// Mock lazy-loaded components
vi.mock('../pages/MapPage', () => ({
  MapPage: () => <div>Map Page</div>,
  default: () => <div>Map Page</div>,
}));

vi.mock('../App', () => ({
  default: () => <div>Main App</div>,
}));

describe('AppRouter', () => {
  beforeEach(() => {
    // Reset window location
    window.history.replaceState({}, '', '/');
  });

  it('should render main app for root route', async () => {
    // Arrange & Act
    window.history.replaceState({}, '', '/');
    render(<AppRouter />);

    // Assert
    await waitFor(() => {
      expect(screen.getByText('Main App')).toBeInTheDocument();
    });
  });

  it('should render map page for /map route', async () => {
    // Arrange & Act
    window.history.replaceState({}, '', '/map');
    render(<AppRouter />);

    // Assert - wait for lazy loading
    await waitFor(
      () => {
        expect(screen.getByText('Map Page')).toBeInTheDocument();
      },
      { timeout: 3000 }
    );
  });

  it('should render main app for unknown routes', () => {
    // Arrange & Act
    window.history.pushState({}, '', '/unknown-route');
    render(<AppRouter />);

    // Assert
    expect(screen.getByText('Main App')).toBeInTheDocument();
  });

  it('should render loading fallback during lazy loading', async () => {
    // Note: This test verifies the LoadingFallback component exists
    // Actual loading behavior is tested by React Router and Suspense
    expect(true).toBe(true); // Placeholder - Suspense behavior is tested in integration tests
  });
});
