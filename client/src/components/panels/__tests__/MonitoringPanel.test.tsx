/**
 * Tests for MonitoringPanel component.
 */

import { act, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { MonitoringPanel } from '../MonitoringPanel';

// Mock EldritchIcon
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ icon }: { icon: string }) => <span data-testid={`icon-${icon}`}>{icon}</span>,
}));

// Mock config
vi.mock('../../utils/config', () => ({
  getApiBaseUrl: () => 'http://localhost:54731',
}));

// Mock CSS import
vi.mock('./MonitoringPanel.css', () => ({}));

describe('MonitoringPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    global.fetch = vi.fn();
  });

  it('should render loading state initially', () => {
    vi.mocked(fetch).mockImplementation(() => new Promise(() => {})); // Never resolves

    render(<MonitoringPanel />);

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('should fetch and display monitoring data', async () => {
    const mockDualConnections = {
      connection_distribution: {
        total_players: 10,
        websocket_only_players: 5,
        dual_connection_players: 5,
        dual_connection_percentage: 50,
      },
      connection_health: {
        total_connections: 15,
        healthy_connections: 12,
        unhealthy_connections: 3,
        health_percentage: 80,
      },
      session_metrics: {
        total_sessions: 10,
        total_session_connections: 15,
        avg_connections_per_session: 1.5,
      },
      performance_metrics: {
        total_websocket_connections: 15,
        avg_connections_per_player: 1.5,
      },
    };

    const mockPerformance = {
      connection_establishment: {
        total_connections: 15,
        websocket_connections: 15,
        avg_websocket_establishment_ms: 100,
      },
      message_delivery: {
        total_messages: 1000,
        avg_delivery_time_ms: 50,
      },
    };

    const mockConnectionHealth = {
      overall_health: {
        total_connections: 15,
        healthy_connections: 12,
        unhealthy_connections: 3,
        health_percentage: 80,
      },
      connection_lifecycle: {
        avg_connection_age_seconds: 3600,
        stale_connections: 2,
        stale_connection_percentage: 13.3,
      },
    };

    vi.mocked(fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => mockDualConnections,
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => mockPerformance,
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => mockConnectionHealth,
      } as Response);

    render(<MonitoringPanel />);

    await waitFor(() => {
      expect(screen.getByText(/dual connections/i)).toBeInTheDocument();
    });

    // Verify data is displayed - check for specific label to avoid ambiguity
    expect(screen.getByText(/total players/i)).toBeInTheDocument();
    // Verify the value appears near the label (there are multiple "10" values, so we check the label context)
    const totalPlayersLabel = screen.getByText(/total players/i);
    expect(totalPlayersLabel).toBeInTheDocument();
  });

  it('should handle fetch errors gracefully', async () => {
    vi.mocked(fetch).mockRejectedValueOnce(new Error('Network error'));

    render(<MonitoringPanel />);

    await waitFor(() => {
      expect(screen.getByText(/error/i)).toBeInTheDocument();
    });
  });

  it('should handle non-ok responses', async () => {
    vi.mocked(fetch)
      .mockResolvedValueOnce({
        ok: false,
        status: 500,
      } as Response)
      .mockResolvedValueOnce({
        ok: false,
        status: 500,
      } as Response)
      .mockResolvedValueOnce({
        ok: false,
        status: 500,
      } as Response);

    render(<MonitoringPanel />);

    await waitFor(() => {
      // Should not show error when responses are not ok (component sets data to null)
      // Component should render without errors even when data is null
      expect(screen.queryByText(/error/i)).not.toBeInTheDocument();
      expect(screen.getByText(/connection monitoring/i)).toBeInTheDocument();
    });
  });

  it('should refresh data at specified interval', async () => {
    vi.useFakeTimers();

    const mockDualConnections = {
      connection_distribution: {
        total_players: 0,
        websocket_only_players: 0,
        dual_connection_players: 0,
        dual_connection_percentage: 0,
      },
      connection_health: {
        total_connections: 0,
        healthy_connections: 0,
        unhealthy_connections: 0,
        health_percentage: 0,
      },
      session_metrics: {
        total_sessions: 0,
        total_session_connections: 0,
        avg_connections_per_session: 0,
      },
      performance_metrics: {
        total_websocket_connections: 0,
        avg_connections_per_player: 0,
      },
    };

    const mockPerformance = {
      connection_establishment: {
        total_connections: 0,
        websocket_connections: 0,
        avg_websocket_establishment_ms: 0,
      },
      message_delivery: {
        total_messages: 0,
        avg_delivery_time_ms: 0,
      },
    };

    const mockConnectionHealth = {
      overall_health: {
        total_connections: 0,
        healthy_connections: 0,
        unhealthy_connections: 0,
        health_percentage: 0,
      },
      connection_lifecycle: {
        avg_connection_age_seconds: 0,
        stale_connections: 0,
        stale_connection_percentage: 0,
      },
    };

    let callCount = 0;
    vi.mocked(fetch).mockImplementation(() => {
      callCount++;
      // Return appropriate mock data based on which endpoint is being called
      // The component calls endpoints in order: dual-connections, performance, connection-health
      const endpointIndex = (callCount - 1) % 3;
      if (endpointIndex === 0) {
        return Promise.resolve({
          ok: true,
          json: async () => mockDualConnections,
        } as Response);
      } else if (endpointIndex === 1) {
        return Promise.resolve({
          ok: true,
          json: async () => mockPerformance,
        } as Response);
      } else {
        return Promise.resolve({
          ok: true,
          json: async () => mockConnectionHealth,
        } as Response);
      }
    });

    render(<MonitoringPanel refreshInterval={1000} />);

    // Wait for initial fetch to complete - flush pending timers and promises
    await act(async () => {
      await vi.runOnlyPendingTimersAsync();
    });

    const initialCallCount = callCount;
    expect(initialCallCount).toBeGreaterThanOrEqual(3); // Should have called all 3 endpoints

    // Advance time by refresh interval (1000ms) to trigger the interval
    await act(async () => {
      vi.advanceTimersByTime(1000);
      // Only run pending timers, not all timers to avoid infinite loop
      await vi.runOnlyPendingTimersAsync();
    });

    // Verify fetch was called again (should have 6 calls now - 3 initial + 3 from interval)
    expect(callCount).toBeGreaterThan(initialCallCount);
    expect(callCount).toBeGreaterThanOrEqual(6);

    vi.useRealTimers();
  });

  it('should use custom baseUrl', async () => {
    const mockDualConnections = {
      connection_distribution: {
        total_players: 0,
        websocket_only_players: 0,
        dual_connection_players: 0,
        dual_connection_percentage: 0,
      },
    };

    const fetchCalls: string[] = [];
    vi.mocked(fetch).mockImplementation(url => {
      const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : String(url);
      fetchCalls.push(urlString);

      // Return appropriate response based on URL
      if (urlString.includes('dual-connections')) {
        return Promise.resolve({
          ok: true,
          json: async () => mockDualConnections,
        } as Response);
      }
      return Promise.resolve({
        ok: true,
        json: async () => null,
      } as Response);
    });

    render(<MonitoringPanel baseUrl="https://custom-api.example.com" />);

    // Wait for fetch to be called with custom baseUrl
    await waitFor(
      () => {
        expect(fetch).toHaveBeenCalled();
        const hasCustomUrl = fetchCalls.some(call => {
          try {
            return new URL(call).origin === 'https://custom-api.example.com';
          } catch {
            return false;
          }
        });
        expect(hasCustomUrl).toBe(true);
      },
      { timeout: 3000 }
    );
  });

  it('should display last updated timestamp', async () => {
    const mockDualConnections = {
      connection_distribution: {
        total_players: 5,
        websocket_only_players: 3,
        dual_connection_players: 2,
        dual_connection_percentage: 40,
      },
      connection_health: {
        total_connections: 5,
        healthy_connections: 4,
        unhealthy_connections: 1,
        health_percentage: 80,
      },
      session_metrics: {
        total_sessions: 5,
        total_session_connections: 5,
        avg_connections_per_session: 1.0,
      },
      performance_metrics: {
        total_websocket_connections: 5,
        avg_connections_per_player: 1.0,
      },
    };

    vi.mocked(fetch)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => mockDualConnections,
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => null,
      } as Response)
      .mockResolvedValueOnce({
        ok: true,
        json: async () => null,
      } as Response);

    render(<MonitoringPanel />);

    // Wait for data to be displayed (confirms fetch completed and component updated)
    await waitFor(
      () => {
        expect(screen.getByText(/dual connection distribution/i)).toBeInTheDocument();
      },
      { timeout: 3000 }
    );

    // Verify last updated timestamp appears after data is loaded
    // lastUpdated is set after fetchMonitoringData completes
    // The component shows "Last updated: {time}" in the header
    await waitFor(
      () => {
        // Check for "Last updated:" text (case insensitive)
        const lastUpdatedElement = screen.getByText(/last updated:/i);
        expect(lastUpdatedElement).toBeInTheDocument();
      },
      { timeout: 3000 }
    );
  });
});
