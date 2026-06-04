/**
 * Tests for MonitoringPanel component.
 */

import '@testing-library/jest-dom/vitest';
import { act, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { MonitoringPanel } from '../MonitoringPanel';
import {
  EMPTY_MONITORING_MOCKS,
  SAMPLE_MONITORING_MOCKS,
  setupDualConnectionsUrlFetch,
  setupRoundRobinMonitoringFetch,
  setupSequentialMonitoringFetch,
  setupTimestampMonitoringFetch,
} from './monitoringPanelTestFixtures';

// Mock EldritchIcon
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ icon }: { icon: string }) => <span data-testid={`icon-${icon}`}>{icon}</span>,
}));

// Mock config
vi.mock('../../utils/config', () => ({
  getApiBaseUrl: () => 'http://localhost:54768',
}));

// Mock CSS import
vi.mock('./MonitoringPanel.css', () => ({}));

const fetchSpy = vi.spyOn(global, 'fetch');

describe('MonitoringPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    fetchSpy.mockClear();
  });

  afterEach(() => {
    fetchSpy.mockReset();
  });

  it('should render loading state initially', () => {
    fetchSpy.mockImplementation(() => new Promise(() => {})); // Never resolves

    render(<MonitoringPanel />);

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('should fetch and display monitoring data', async () => {
    setupSequentialMonitoringFetch(fetchSpy, SAMPLE_MONITORING_MOCKS);

    render(<MonitoringPanel />);

    await waitFor(() => {
      expect(screen.getByText(/dual connection distribution/i)).toBeInTheDocument();
    });

    // Verify data is displayed - check for specific label to avoid ambiguity
    expect(screen.getByText(/total players/i)).toBeInTheDocument();
  });

  it('should handle fetch errors gracefully', async () => {
    fetchSpy.mockRejectedValueOnce(new Error('Network error'));

    render(<MonitoringPanel />);

    await waitFor(() => {
      expect(screen.getByText(/error/i)).toBeInTheDocument();
    });
  });

  it('should handle non-ok responses', async () => {
    fetchSpy
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

    const { getCallCount } = setupRoundRobinMonitoringFetch(fetchSpy, EMPTY_MONITORING_MOCKS);

    render(<MonitoringPanel refreshInterval={1000} />);

    await act(async () => {
      await vi.runOnlyPendingTimersAsync();
    });

    const initialCallCount = getCallCount();
    expect(initialCallCount).toBeGreaterThanOrEqual(3);

    await act(async () => {
      vi.advanceTimersByTime(1000);
      await vi.runOnlyPendingTimersAsync();
    });

    expect(getCallCount()).toBeGreaterThan(initialCallCount);
    expect(getCallCount()).toBeGreaterThanOrEqual(6);

    vi.useRealTimers();
  });

  it('should use custom baseUrl', async () => {
    const { fetchCalls } = setupDualConnectionsUrlFetch(fetchSpy, EMPTY_MONITORING_MOCKS.dualConnections);

    render(<MonitoringPanel baseUrl="https://custom-api.example.com" />);

    // Wait for fetch to be called with custom baseUrl
    await waitFor(
      () => {
        expect(fetchSpy).toHaveBeenCalled();
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
    setupTimestampMonitoringFetch(fetchSpy);

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
        // Check for "Last updated:" text (case insensitive) - the time format may vary
        const lastUpdatedElement = screen.getByText(/last updated:/i);
        expect(lastUpdatedElement).toBeInTheDocument();
      },
      { timeout: 5000 }
    );
  });
});
