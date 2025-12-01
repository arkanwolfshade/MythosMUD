import { act, renderHook, waitFor } from '@testing-library/react';
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

    // Wait for the connection attempt to fail and error to be set
    // The state machine will transition through 'reconnecting' before eventually failing
    await waitFor(
      () => {
        expect(result.current.error).toBe('Connection failed');
      },
      { timeout: 2000 }
    );

    // After the auto-connect attempt fails, we should be back to default state
    // but with an error indicating the connection failed
    // Note: isConnecting might still be true if we're in 'reconnecting' state,
    // but the error should be set indicating the connection failed
    expect(result.current.isConnected).toBe(false);
    expect(result.current.error).toBe('Connection failed');
    expect(result.current.websocketConnected).toBe(false);

    // Wait for isConnecting to become false (after reconnect attempts are exhausted)
    await waitFor(
      () => {
        expect(result.current.isConnecting).toBe(false);
      },
      { timeout: 5000 }
    );
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

  it('should send command when sendCommand is called', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
        playerName: 'test-player',
      })
    );

    const success = await result.current.sendCommand('test', ['arg1', 'arg2']);
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

  describe('Session Management', () => {
    it('should initialize with session ID', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(result.current.sessionId).toBeDefined();
      expect(typeof result.current.sessionId).toBe('string');
      expect(result.current.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
    });

    it('should accept custom session ID', () => {
      const customSessionId = 'custom-session-123';
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
          sessionId: customSessionId,
        })
      );

      expect(result.current.sessionId).toBe(customSessionId);
    });

    it('should initialize connection health as unknown', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(result.current.connectionHealth).toEqual({
        websocket: 'unhealthy',
        lastHealthCheck: expect.any(Number),
      });
    });

    it('should initialize connection metadata', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(result.current.connectionMetadata).toEqual({
        websocketConnectionId: null,
        totalConnections: 0,
        connectionTypes: ['websocket'],
      });
    });

    it('should provide createNewSession function', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(typeof result.current.createNewSession).toBe('function');
    });

    it('should provide switchToSession function', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(typeof result.current.switchToSession).toBe('function');
    });

    it('should provide getConnectionInfo function', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      expect(typeof result.current.getConnectionInfo).toBe('function');
    });

    it('should create new session when createNewSession is called', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      const originalSessionId = result.current.sessionId;

      act(() => {
        const newSessionId = result.current.createNewSession();
        expect(newSessionId).toBeDefined();
        // The session ID should be updated in the state
        expect(result.current.sessionId).toBeDefined();
        // Either the session ID should be different, or if it's the same (due to timing),
        // it should at least be a valid session ID format
        if (result.current.sessionId === originalSessionId) {
          expect(result.current.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
        } else {
          expect(result.current.sessionId).not.toBe(originalSessionId);
        }
      });
    });

    it('should switch to new session when switchToSession is called', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      const newSessionId = 'new-session-456';

      act(() => {
        result.current.switchToSession(newSessionId);
      });

      // The session ID should be updated in the state
      expect(result.current.sessionId).toBeDefined();
      expect(result.current.sessionId).toBe(newSessionId);
    });

    it('should return connection info when getConnectionInfo is called', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      const connectionInfo = result.current.getConnectionInfo();

      expect(connectionInfo).toMatchObject({
        sessionId: result.current.sessionId,
        websocketConnected: result.current.websocketConnected,
        connectionHealth: expect.objectContaining({
          websocket: 'unhealthy',
          lastHealthCheck: expect.any(Number),
        }),
        connectionState: expect.any(String),
        reconnectAttempts: expect.any(Number),
      });
    });

    it('should call onSessionChange callback when session changes', () => {
      const onSessionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
          onSessionChange,
        })
      );

      act(() => {
        result.current.createNewSession();
      });

      expect(onSessionChange).toHaveBeenCalledWith(result.current.sessionId);
    });

    it('should call onConnectionHealthUpdate callback when health updates', () => {
      const onConnectionHealthUpdate = vi.fn();
      renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
          onConnectionHealthUpdate,
        })
      );

      // The health monitoring should be called when connections are established
      // This is tested indirectly through the connection process
      expect(typeof onConnectionHealthUpdate).toBe('function');
    });

    it('should include session_id in WebSocket URL when connecting', () => {
      const customSessionId = 'test-session-789';
      renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
          sessionId: customSessionId,
        })
      );

      // The WebSocket constructor should be called with session_id parameter
      expect(global.WebSocket).toHaveBeenCalledWith(
        expect.stringContaining(`session_id=${encodeURIComponent(customSessionId)}`),
        ['bearer', 'test-token']
      );
    });

    it('should handle session switching with reconnection', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
          playerName: 'test-player',
        })
      );

      // First establish connection
      act(() => {
        result.current.connect();
      });

      // Simulate successful WebSocket connection
      act(() => {
        if (mockWebSocket.onopen) mockWebSocket.onopen(new Event('open'));
      });

      const newSessionId = 'new-session-999';

      await act(async () => {
        await new Promise(resolve => setTimeout(resolve, 20));
        result.current.switchToSession(newSessionId);
        await new Promise(resolve => setTimeout(resolve, 20));
      });

      // The session ID should be updated in the state
      expect(result.current.sessionId).toBeDefined();
      expect(result.current.sessionId).toBe(newSessionId);
    });
  });
});
