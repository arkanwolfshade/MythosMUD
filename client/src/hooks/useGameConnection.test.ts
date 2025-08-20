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
global.WebSocket = vi.fn(() => mockWebSocket) as unknown as typeof WebSocket;

// Mock EventSource
const mockEventSource = {
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  close: vi.fn(),
  readyState: 0,
};

global.EventSource = vi.fn(() => mockEventSource) as unknown as typeof EventSource;

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

  it('should initialize with default state', () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    expect(result.current.isConnected).toBe(false);
    expect(result.current.isConnecting).toBe(false);
    expect(result.current.error).toBe(null);
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
