/**
 * Integration tests for dual connection system on the client side.
 *
 * This module tests the complete dual connection system integration from the client perspective,
 * including simultaneous WebSocket and SSE connections, message handling, session management,
 * and error recovery.
 */

import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameConnection } from '../src/hooks/useGameConnection';

// Mock WebSocket and EventSource
class MockWebSocket {
  public readyState = WebSocket.CONNECTING;
  public url: string;
  public onopen: ((event: Event) => void) | null = null;
  public onclose: ((event: CloseEvent) => void) | null = null;
  public onerror: ((event: Event) => void) | null = null;
  public onmessage: ((event: MessageEvent) => void) | null = null;
  public send = vi.fn();
  public close = vi.fn();

  constructor(url: string) {
    this.url = url;
    // Simulate connection after a short delay
    setTimeout(() => {
      this.readyState = WebSocket.OPEN;
      this.onopen?.(new Event('open'));
    }, 10);
  }
}

class MockEventSource {
  public readyState = EventSource.CONNECTING;
  public url: string;
  public onopen: ((event: Event) => void) | null = null;
  public onerror: ((event: Event) => void) | null = null;
  public onmessage: ((event: MessageEvent) => void) | null = null;
  public close = vi.fn();

  constructor(url: string) {
    this.url = url;
    // Simulate connection after a short delay
    setTimeout(() => {
      this.readyState = EventSource.OPEN;
      this.onopen?.(new Event('open'));
    }, 10);
  }
}

// Mock global objects
global.WebSocket = MockWebSocket as any;
global.EventSource = MockEventSource as any;

describe('Dual Connection Integration Tests', () => {
  let mockWebSocket: MockWebSocket;
  let mockEventSource: MockEventSource;

  beforeEach(() => {
    vi.clearAllMocks();
    // Reset global mocks
    mockWebSocket = new MockWebSocket('ws://localhost:8000/ws');
    mockEventSource = new MockEventSource('http://localhost:8000/events');
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Connection Establishment', () => {
    it('should establish both WebSocket and SSE connections', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      // Connect both WebSocket and SSE
      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
        expect(result.current.hasWebSocket).toBe(true);
        expect(result.current.hasSSE).toBe(true);
        expect(result.current.connectionCount).toBe(2);
      });

      // Verify session ID is generated
      expect(result.current.sessionId).toBeDefined();
      expect(typeof result.current.sessionId).toBe('string');
    });

    it('should handle connection establishment with custom session ID', async () => {
      const customSessionId = 'custom-session-123';
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
          initialSessionId: customSessionId,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
        expect(result.current.sessionId).toBe(customSessionId);
      });
    });

    it('should establish connections with session ID in URLs', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Verify that the session ID is included in the connection URLs
      expect(result.current.sessionId).toBeDefined();
      const sessionId = result.current.sessionId!;

      // The URLs should contain the session_id parameter
      expect(mockWebSocket.url).toContain(`session_id=${sessionId}`);
      expect(mockEventSource.url).toContain(`session_id=${sessionId}`);
    });
  });

  describe('Message Handling', () => {
    it('should handle messages from both WebSocket and SSE', async () => {
      const onMessage = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage,
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate WebSocket message
      const wsMessage = { type: 'websocket_message', content: 'Hello from WebSocket' };
      act(() => {
        mockWebSocket.onmessage?.(
          new MessageEvent('message', {
            data: JSON.stringify(wsMessage),
          })
        );
      });

      // Simulate SSE message
      const sseMessage = { type: 'sse_message', content: 'Hello from SSE' };
      act(() => {
        mockEventSource.onmessage?.(
          new MessageEvent('message', {
            data: JSON.stringify(sseMessage),
          })
        );
      });

      // Verify both messages were received
      expect(onMessage).toHaveBeenCalledTimes(2);
      expect(onMessage).toHaveBeenCalledWith(wsMessage);
      expect(onMessage).toHaveBeenCalledWith(sseMessage);
    });

    it('should handle malformed messages gracefully', async () => {
      const onMessage = vi.fn();
      const onError = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage,
          onError,
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate malformed WebSocket message
      act(() => {
        mockWebSocket.onmessage?.(
          new MessageEvent('message', {
            data: 'invalid json',
          })
        );
      });

      // Simulate malformed SSE message
      act(() => {
        mockEventSource.onmessage?.(
          new MessageEvent('message', {
            data: 'also invalid json',
          })
        );
      });

      // Verify error handling
      expect(onError).toHaveBeenCalledTimes(2);
      expect(onMessage).not.toHaveBeenCalled();
    });
  });

  describe('Session Management', () => {
    it('should create new session and switch connections', async () => {
      const onSessionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
          onSessionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      const originalSessionId = result.current.sessionId;

      // Create new session
      await act(async () => {
        const newSessionId = await result.current.createNewSession();
        expect(newSessionId).toBeDefined();
        expect(newSessionId).not.toBe(originalSessionId);
      });

      // Verify session change callback was called
      expect(onSessionChange).toHaveBeenCalledWith(expect.any(String), originalSessionId);

      // Verify new session ID
      expect(result.current.sessionId).not.toBe(originalSessionId);
    });

    it('should switch to existing session', async () => {
      const onSessionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
          onSessionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      const originalSessionId = result.current.sessionId;
      const targetSessionId = 'target-session-456';

      // Switch to existing session
      await act(async () => {
        await result.current.switchToSession(targetSessionId);
      });

      // Verify session change callback was called
      expect(onSessionChange).toHaveBeenCalledWith(targetSessionId, originalSessionId);

      // Verify session ID was updated
      expect(result.current.sessionId).toBe(targetSessionId);
    });

    it('should provide connection information', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      const connectionInfo = result.current.getConnectionInfo();

      expect(connectionInfo).toEqual({
        isConnected: true,
        hasWebSocket: true,
        hasSSE: true,
        connectionCount: 2,
        sessionId: result.current.sessionId,
        lastConnected: expect.any(Date),
        connectionHealth: expect.any(Object),
      });
    });
  });

  describe('Error Handling and Recovery', () => {
    it('should handle WebSocket connection errors', async () => {
      const onError = vi.fn();
      const onConnectionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError,
          onConnectionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate WebSocket error
      act(() => {
        mockWebSocket.onerror?.(new Event('error'));
      });

      // Verify error handling
      expect(onError).toHaveBeenCalledWith(
        expect.objectContaining({
          type: 'websocket_error',
          message: expect.any(String),
        })
      );

      // SSE should still be connected
      expect(result.current.hasSSE).toBe(true);
    });

    it('should handle SSE connection errors', async () => {
      const onError = vi.fn();
      const onConnectionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError,
          onConnectionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate SSE error
      act(() => {
        mockEventSource.onerror?.(new Event('error'));
      });

      // Verify error handling
      expect(onError).toHaveBeenCalledWith(
        expect.objectContaining({
          type: 'sse_error',
          message: expect.any(String),
        })
      );

      // WebSocket should still be connected
      expect(result.current.hasWebSocket).toBe(true);
    });

    it('should handle complete connection loss', async () => {
      const onError = vi.fn();
      const onConnectionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError,
          onConnectionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate both connections closing
      act(() => {
        mockWebSocket.onclose?.(new CloseEvent('close'));
        mockEventSource.onerror?.(new Event('error'));
      });

      // Verify connection state updated
      expect(result.current.isConnected).toBe(false);
      expect(result.current.connectionCount).toBe(0);
    });

    it('should attempt reconnection on connection loss', async () => {
      const onConnectionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange,
          autoReconnect: true,
          reconnectInterval: 100,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate connection loss
      act(() => {
        mockWebSocket.onclose?.(new CloseEvent('close'));
        mockEventSource.onerror?.(new Event('error'));
      });

      // Wait for reconnection attempt
      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Verify reconnection occurred
      expect(onConnectionChange).toHaveBeenCalledWith(true);
    });
  });

  describe('Connection Health Monitoring', () => {
    it('should monitor connection health', async () => {
      const onConnectionHealthUpdate = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
          onConnectionHealthUpdate,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Wait for health check
      await waitFor(
        () => {
          expect(onConnectionHealthUpdate).toHaveBeenCalled();
        },
        { timeout: 2000 }
      );

      // Verify health update was called with correct data
      const healthUpdate = onConnectionHealthUpdate.mock.calls[0][0];
      expect(healthUpdate).toEqual({
        isHealthy: true,
        websocketHealth: expect.any(Object),
        sseHealth: expect.any(Object),
        lastHealthCheck: expect.any(Date),
      });
    });

    it('should detect unhealthy connections', async () => {
      const onConnectionHealthUpdate = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
          onConnectionHealthUpdate,
          healthCheckInterval: 100,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Simulate WebSocket becoming unhealthy
      mockWebSocket.readyState = WebSocket.CLOSED;

      // Wait for health check to detect the issue
      await waitFor(
        () => {
          expect(onConnectionHealthUpdate).toHaveBeenCalledWith(
            expect.objectContaining({
              isHealthy: false,
              websocketHealth: expect.objectContaining({
                isHealthy: false,
              }),
            })
          );
        },
        { timeout: 1000 }
      );
    });
  });

  describe('Disconnection', () => {
    it('should disconnect all connections cleanly', async () => {
      const onConnectionChange = vi.fn();
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange,
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Disconnect
      await act(async () => {
        await result.current.disconnect();
      });

      // Verify disconnection
      expect(result.current.isConnected).toBe(false);
      expect(result.current.connectionCount).toBe(0);
      expect(mockWebSocket.close).toHaveBeenCalled();
      expect(mockEventSource.close).toHaveBeenCalled();
      expect(onConnectionChange).toHaveBeenCalledWith(false);
    });

    it('should preserve session ID after disconnection', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      const sessionId = result.current.sessionId;

      // Disconnect
      await act(async () => {
        await result.current.disconnect();
      });

      // Verify session ID is preserved
      expect(result.current.sessionId).toBe(sessionId);
    });
  });

  describe('Performance and Load Testing', () => {
    it('should handle rapid connection/disconnection cycles', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      // Perform multiple connect/disconnect cycles
      for (let i = 0; i < 5; i++) {
        await act(async () => {
          await result.current.connect();
        });

        await waitFor(() => {
          expect(result.current.isConnected).toBe(true);
        });

        await act(async () => {
          await result.current.disconnect();
        });

        expect(result.current.isConnected).toBe(false);
      }

      // Final state should be disconnected
      expect(result.current.isConnected).toBe(false);
      expect(result.current.connectionCount).toBe(0);
    });

    it('should handle multiple session switches efficiently', async () => {
      const { result } = renderHook(() =>
        useGameConnection({
          onMessage: vi.fn(),
          onError: vi.fn(),
          onConnectionChange: vi.fn(),
        })
      );

      await act(async () => {
        await result.current.connect();
      });

      await waitFor(() => {
        expect(result.current.isConnected).toBe(true);
      });

      // Perform multiple session switches
      const sessionIds = ['session-1', 'session-2', 'session-3', 'session-4', 'session-5'];

      for (const sessionId of sessionIds) {
        await act(async () => {
          await result.current.switchToSession(sessionId);
        });

        expect(result.current.sessionId).toBe(sessionId);
      }

      // Final session should be the last one
      expect(result.current.sessionId).toBe('session-5');
    });
  });
});
