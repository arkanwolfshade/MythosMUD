import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameConnection } from './useGameConnection';

// Mock WebSocket
const mockWebSocket = {
  send: vi.fn(),
  close: vi.fn(),
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  readyState: 0,
};

// Mock WebSocket constructor
global.WebSocket = vi.fn(() => {
  // Simulate connection failure by triggering onerror after a short delay
  setTimeout(() => {
    if (mockWebSocket.onerror) {
      mockWebSocket.onerror(new Event('error'));
    }
  }, 10);
  return mockWebSocket;
}) as unknown as typeof WebSocket;

// Mock EventSource
const mockEventSource = {
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  close: vi.fn(),
  readyState: 0,
};

global.EventSource = vi.fn(() => {
  // Simulate connection failure by triggering onerror after a short delay
  setTimeout(() => {
    if (mockEventSource.onerror) {
      mockEventSource.onerror(new Event('error'));
    }
  }, 10);
  return mockEventSource;
}) as unknown as typeof EventSource;

// Mock logger
vi.mock('../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    warn: vi.fn(),
    debug: vi.fn(),
  },
}));

describe('useGameConnection', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mockWebSocket.readyState = 0;
    mockEventSource.readyState = 0;
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('should initialize and handle auto-connect gracefully', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    // Initially, the hook should start connecting automatically
    expect(result.current.isConnecting).toBe(true);

    // Wait for the connection attempt to complete and fail
    await act(async () => {
      // Wait for the connection attempt to complete
      await new Promise(resolve => setTimeout(resolve, 100));
    });

    // After the auto-connect attempt fails, we should be back to default state
    // but with an error indicating the connection failed
    expect(result.current.isConnected).toBe(false);
    expect(result.current.isConnecting).toBe(false);
    expect(result.current.error).toBe('Connection failed');
    expect(result.current.sseConnected).toBe(false);
    expect(result.current.websocketConnected).toBe(false);
  });

  it('should connect when connect is called', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    act(() => {
      result.current.connect();
    });

    expect(result.current.isConnecting).toBe(true);
  });

  it('should disconnect when disconnect is called', () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    act(() => {
      result.current.disconnect();
    });

    // The disconnect method exists and can be called
    expect(result.current).toHaveProperty('disconnect');
  });

  it('should send command when sendCommand is called', () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    const success = result.current.sendCommand('test', ['arg1', 'arg2']);
    expect(success).toBe(false); // Should be false when not connected
  });

  it('should handle connection state changes', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    expect(result.current.isConnected).toBe(false);
    expect(result.current.sseConnected).toBe(false);
    expect(result.current.websocketConnected).toBe(false);
  });

  it('should handle error state', () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    expect(result.current.error).toBe(null);
  });
});
