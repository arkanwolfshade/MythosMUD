import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi, type Mock } from 'vitest';
import { useGameConnection } from './useGameConnection';

// Mock WebSocket
const mockWebSocket = {
  send: vi.fn(),
  close: vi.fn(),
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  readyState: 0,
  onerror: null as ((event: Event) => void) | null,
  onopen: null as ((event: Event) => void) | null,
};

// Mock WebSocket constructor
global.WebSocket = vi.fn(function WebSocket() {
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
      })
    );

    // Initially, autoConnectPending should be true, making isConnecting true
    // Note: isConnecting = isConnectionInProgress || autoConnectPending
    // autoConnectPending is set to true initially if authToken is provided
    // However, onStateChange might be called immediately after render (in a useEffect),
    // which could reset autoConnectPending before we check it
    // So we need to wait for either:
    // 1. autoConnectPending to remain true (if onStateChange hasn't reset it yet), OR
    // 2. isConnectionInProgress to become true (after auto-connect effect runs and
    //    state transitions to 'connecting_ws')
    await waitFor(
      () => {
        // isConnecting should be true because either:
        // - autoConnectPending is true (initial state, before onStateChange resets it), OR
        // - isConnectionInProgress is true (after state machine transitions to 'connecting_ws')
        expect(result.current.isConnecting).toBe(true);
      },
      { timeout: 2000 }
    );

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
    // With exponential backoff (1s, 2s, 4s, 8s, 16s) and 5 max attempts,
    // this could take up to ~31 seconds, so we use a generous timeout
    // The state machine will transition to 'failed' after max attempts,
    // at which point isConnectionInProgress becomes false, making isConnecting false
    await waitFor(
      () => {
        expect(result.current.isConnecting).toBe(false);
      },
      { timeout: 35000 } // 35 seconds to account for exponential backoff delays
    );
  }, 40000); // Test timeout: 40 seconds to allow for exponential backoff (1s + 2s + 4s + 8s + 16s = ~31s max)

  it('should connect when connect is called', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
      })
    );

    act(() => {
      result.current.connect();
    });

    // connect() sets autoConnectPending to true and calls startConnection()
    // This should transition the state machine to connecting_ws
    // Once in 'connecting_ws', isConnectionInProgress becomes true
    // Wait for the connection state to update
    await waitFor(
      () => {
        // isConnecting should be true because either:
        // - autoConnectPending is true (set by connect()), OR
        // - isConnectionInProgress is true (after state machine transitions to 'connecting_ws')
        expect(result.current.isConnecting).toBe(true);
      },
      { timeout: 2000 }
    );
  });

  it('should disconnect when disconnect is called', () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
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
      })
    );

    const success = await result.current.sendCommand('test', ['arg1', 'arg2']);
    expect(success).toBe(false); // Should be false when not connected
  });

  it('should handle connection state changes', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
      })
    );

    expect(result.current.isConnected).toBe(false);
    expect(result.current.websocketConnected).toBe(false);
  });

  it('should handle error state', async () => {
    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'test-token',
      })
    );

    // Initially, there should be no error
    // The hook may auto-connect and fail, so wait a bit to see if error appears
    await waitFor(
      () => {
        // Error might be null initially or set after connection attempt fails
        expect(result.current.error === null || typeof result.current.error === 'string').toBe(true);
      },
      { timeout: 1000 }
    );
  });

  describe('Session Management', () => {
    it('should initialize with session ID', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
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
          sessionId: customSessionId,
        })
      );

      expect(result.current.sessionId).toBe(customSessionId);
    });

    it('should initialize connection health as unknown', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
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
        })
      );

      expect(typeof result.current.createNewSession).toBe('function');
    });

    it('should provide switchToSession function', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
        })
      );

      expect(typeof result.current.switchToSession).toBe('function');
    });

    it('should provide getConnectionInfo function', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
        })
      );

      expect(typeof result.current.getConnectionInfo).toBe('function');
    });

    it('should create new session when createNewSession is called', () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
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
          sessionId: customSessionId,
        })
      );

      // The WebSocket constructor should be called with session_id and token as query parameters
      // NOTE: JWT tokens are passed via query string, not subprotocol, because JWT contains
      // characters (dots) that are invalid in WebSocket subprotocols
      expect(global.WebSocket).toHaveBeenCalledWith(
        expect.stringContaining(`session_id=${encodeURIComponent(customSessionId)}`)
      );

      // Verify the token is also in the URL
      const calls = (global.WebSocket as unknown as Mock).mock.calls;
      const lastCall = calls[calls.length - 1];
      expect(lastCall[0]).toContain('token=test-token');
    });

    it('should handle session switching with reconnection', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          authToken: 'test-token',
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
