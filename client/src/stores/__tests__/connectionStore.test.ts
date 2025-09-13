import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useConnectionStore } from '../connectionStore';

// Mock WebSocket
const mockWebSocket = {
  send: vi.fn(),
  close: vi.fn(),
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  readyState: 0,
};

// Mock EventSource
const mockEventSource = {
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  close: vi.fn(),
  readyState: 0,
};

// Mock global objects
global.WebSocket = vi.fn(() => mockWebSocket) as unknown as typeof WebSocket;
global.EventSource = vi.fn(() => mockEventSource) as unknown as typeof EventSource;

describe('Connection Store', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset store state
    useConnectionStore.getState().reset();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should have correct initial state', () => {
      const state = useConnectionStore.getState();

      expect(state.isConnected).toBe(false);
      expect(state.isConnecting).toBe(false);
      expect(state.sseConnected).toBe(false);
      expect(state.websocketConnected).toBe(false);
      expect(state.error).toBe(null);
      expect(state.reconnectAttempts).toBe(0);
      expect(state.sessionId).toBeDefined();
      expect(state.connectionHealth).toEqual({
        websocket: 'unknown',
        sse: 'unknown',
        lastHealthCheck: null,
      });
      expect(state.connectionMetadata).toEqual({
        websocketConnectionId: null,
        sseConnectionId: null,
        totalConnections: 0,
        connectionTypes: [],
      });
    });

    it('should generate valid session ID format', () => {
      const state = useConnectionStore.getState();
      expect(state.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
    });
  });

  describe('Connection Actions', () => {
    it('should set connecting state', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.setConnecting(true);
      });

      expect(result.current.isConnecting).toBe(true);
    });

    it('should set SSE connection state', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.setSseConnected(true);
      });

      expect(result.current.sseConnected).toBe(true);
    });

    it('should set WebSocket connection state', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.setWebsocketConnected(true);
      });

      expect(result.current.websocketConnected).toBe(true);
    });

    it('should set error state', () => {
      const { result } = renderHook(() => useConnectionStore());
      const errorMessage = 'Connection failed';

      act(() => {
        result.current.setError(errorMessage);
      });

      expect(result.current.error).toBe(errorMessage);
    });

    it('should clear error state', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.setError('Some error');
        result.current.setError(null);
      });

      expect(result.current.error).toBe(null);
    });
  });

  describe('Reconnection Management', () => {
    it('should increment reconnect attempts', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.incrementReconnectAttempts();
      });

      expect(result.current.reconnectAttempts).toBe(1);
    });

    it('should reset reconnect attempts', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.incrementReconnectAttempts();
        result.current.incrementReconnectAttempts();
        result.current.resetReconnectAttempts();
      });

      expect(result.current.reconnectAttempts).toBe(0);
    });
  });

  describe('Session Management', () => {
    it('should create new session', () => {
      const { result } = renderHook(() => useConnectionStore());
      const originalSessionId = result.current.sessionId;

      act(() => {
        const newSessionId = result.current.createNewSession();
        expect(newSessionId).toBeDefined();
        expect(newSessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
        expect(newSessionId).not.toBe(originalSessionId);
      });
    });

    it('should switch to existing session', () => {
      const { result } = renderHook(() => useConnectionStore());
      const newSessionId = 'custom-session-123';

      act(() => {
        result.current.switchToSession(newSessionId);
      });

      expect(result.current.sessionId).toBe(newSessionId);
    });

    it('should set session ID', () => {
      const { result } = renderHook(() => useConnectionStore());
      const sessionId = 'test-session-456';

      act(() => {
        result.current.setSessionId(sessionId);
      });

      expect(result.current.sessionId).toBe(sessionId);
    });
  });

  describe('Connection Health', () => {
    it('should update connection health', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.updateConnectionHealth({
          websocket: 'healthy',
          sse: 'unhealthy',
        });
      });

      expect(result.current.connectionHealth.websocket).toBe('healthy');
      expect(result.current.connectionHealth.sse).toBe('unhealthy');
      expect(result.current.connectionHealth.lastHealthCheck).toBeDefined();
    });

    it('should update partial connection health', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.updateConnectionHealth({
          websocket: 'healthy',
        });
      });

      expect(result.current.connectionHealth.websocket).toBe('healthy');
      expect(result.current.connectionHealth.sse).toBe('unknown'); // Should remain unchanged
    });

    it('should complete health check', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.completeHealthCheck();
      });

      expect(result.current.connectionHealth.lastHealthCheck).toBeDefined();
    });
  });

  describe('Connection Metadata', () => {
    it('should update connection metadata', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.updateConnectionMetadata({
          websocketConnectionId: 'ws-123',
          sseConnectionId: 'sse-456',
          totalConnections: 2,
          connectionTypes: ['websocket', 'sse'],
        });
      });

      expect(result.current.connectionMetadata.websocketConnectionId).toBe('ws-123');
      expect(result.current.connectionMetadata.sseConnectionId).toBe('sse-456');
      expect(result.current.connectionMetadata.totalConnections).toBe(2);
      expect(result.current.connectionMetadata.connectionTypes).toEqual(['websocket', 'sse']);
    });

    it('should update partial connection metadata', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.updateConnectionMetadata({
          websocketConnectionId: 'ws-789',
        });
      });

      expect(result.current.connectionMetadata.websocketConnectionId).toBe('ws-789');
      expect(result.current.connectionMetadata.sseConnectionId).toBe(null); // Should remain unchanged
    });
  });

  describe('Event Handling', () => {
    it('should set last event', () => {
      const { result } = renderHook(() => useConnectionStore());
      const testEvent = {
        type: 'test_event',
        sequence_number: 1,
        data: { message: 'test' },
      };

      act(() => {
        result.current.setLastEvent(testEvent);
      });

      expect(result.current.lastEvent).toEqual(testEvent);
    });

    it('should clear last event', () => {
      const { result } = renderHook(() => useConnectionStore());

      act(() => {
        result.current.setLastEvent({
          type: 'test_event',
          sequence_number: 1,
          data: {},
        });
        result.current.setLastEvent(null);
      });

      expect(result.current.lastEvent).toBe(null);
    });
  });

  describe('State Reset', () => {
    it('should reset all state to initial values', () => {
      const { result } = renderHook(() => useConnectionStore());

      // Modify state
      act(() => {
        result.current.setConnecting(true);
        result.current.setSseConnected(true);
        result.current.setWebsocketConnected(true);
        result.current.setError('test error');
        result.current.incrementReconnectAttempts();
        result.current.setSessionId('test-session');
      });

      // Reset state
      act(() => {
        result.current.reset();
      });

      expect(result.current.isConnecting).toBe(false);
      expect(result.current.sseConnected).toBe(false);
      expect(result.current.websocketConnected).toBe(false);
      expect(result.current.error).toBe(null);
      expect(result.current.reconnectAttempts).toBe(0);
      expect(result.current.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
    });
  });

  describe('Selectors', () => {
    it('should provide connection info selector', () => {
      const { result } = renderHook(() => useConnectionStore());

      const connectionInfo = result.current.getConnectionInfo();

      expect(connectionInfo).toEqual({
        sessionId: result.current.sessionId,
        websocketConnected: result.current.websocketConnected,
        sseConnected: result.current.sseConnected,
        connectionHealth: result.current.connectionHealth,
        connectionMetadata: result.current.connectionMetadata,
      });
    });

    it('should provide is fully connected selector', () => {
      const { result } = renderHook(() => useConnectionStore());

      expect(result.current.isFullyConnected()).toBe(false);

      act(() => {
        result.current.setSseConnected(true);
        result.current.setWebsocketConnected(true);
      });

      expect(result.current.isFullyConnected()).toBe(true);
    });

    it('should provide has any connection selector', () => {
      const { result } = renderHook(() => useConnectionStore());

      expect(result.current.hasAnyConnection()).toBe(false);

      act(() => {
        result.current.setSseConnected(true);
      });

      expect(result.current.hasAnyConnection()).toBe(true);
    });
  });
});
