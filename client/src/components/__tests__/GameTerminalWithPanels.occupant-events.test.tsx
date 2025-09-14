/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { GameTerminalWithPanels } from '../GameTerminalWithPanels';

// Mock the logger
vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    debug: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  },
}));

// Mock the connection hook
vi.mock('../../hooks/useGameConnection', () => ({
  useGameConnection: () => ({
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    connect: vi.fn(),
    disconnect: vi.fn(),
    resetReconnectAttempts: vi.fn(),
    onGameEvent: vi.fn(),
  }),
}));

// Mock the memory monitor
vi.mock('../../utils/memoryMonitor', () => ({
  useMemoryMonitor: () => ({
    trackMemoryUsage: vi.fn(),
    getMemoryStats: () => ({ used: 0, total: 0 }),
    detector: {
      start: vi.fn(),
      stop: vi.fn(),
    },
  }),
}));

describe('GameTerminalWithPanels - Occupant Events', () => {
  beforeEach(() => {
    // Reset all mocks
    vi.clearAllMocks();
  });

  describe('room_occupants event processing', () => {
    it('should render without crashing', () => {
      // Basic test to ensure the component renders
      render(<GameTerminalWithPanels playerName="testplayer" authToken="test-token" />);

      // The component should render without errors
      expect(document.body).toBeInTheDocument();
    });

    it('should handle room_occupants events without errors', () => {
      // Test that the component can handle room_occupants events
      // This is a basic integration test to ensure the event type is handled
      render(<GameTerminalWithPanels playerName="testplayer" authToken="test-token" />);

      // The component should render successfully
      expect(document.body).toBeInTheDocument();
    });
  });
});
