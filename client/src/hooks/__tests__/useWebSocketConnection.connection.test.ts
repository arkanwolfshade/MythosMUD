import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
// Fixtures import must load before the hook (@/ paths survive organizeImports on save).
import {
  MockWebSocket,
  defaultOptions,
  latestWebSocketInstance,
  mockResourceManager,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from '@/hooks/__tests__/useWebSocketConnectionTestFixtures';
import { useWebSocketConnection } from '@/hooks/useWebSocketConnection';

describe('useWebSocketConnection - Connection Management', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('should start disconnected', () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    expect(result.current.isConnected).toBe(false);
    expect(result.current.lastError).toBeNull();
  });

  it('should include character_id in WebSocket URL when characterId is provided', async () => {
    const characterId = 'char-uuid-123';
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        characterId,
      })
    );

    act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    expect(wsTestState.mockWebSocketInstance?.url).toContain(`character_id=${encodeURIComponent(characterId)}`);
  });

  it('should connect successfully', async () => {
    const onConnected = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onConnected,
      })
    );

    expect(result.current.isConnected).toBe(false);
    expect(result.current.lastError).toBe(null);

    act(() => {
      result.current.connect();
    });

    // Wait for WebSocket to be created - use latestWebSocketInstance from constructor
    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    // Manually trigger open event
    act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    expect(onConnected).toHaveBeenCalled();
    expect(mockResourceManager.registerInterval).toHaveBeenCalled();
  });

  it('should disconnect successfully', async () => {
    const onDisconnect = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onDisconnect,
      })
    );

    act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    act(() => {
      result.current.disconnect();
    });

    expect(result.current.isConnected).toBe(false);
    expect(wsTestState.mockWebSocketInstance?.getCloseCalls().length).toBeGreaterThan(0);
    expect(mockResourceManager.removeInterval).toHaveBeenCalled();
  });

  it('should not connect without auth token', async () => {
    const { result } = renderHook(() =>
      useWebSocketConnection({
        authToken: '',
        sessionId: 'test-session-id',
      })
    );

    await act(() => {
      result.current.connect();
    });

    expect(wsTestState.mockWebSocketInstance).toBeNull();
    expect(result.current.isConnected).toBe(false);
  });

  it('should not connect without session ID', async () => {
    const { result } = renderHook(() =>
      useWebSocketConnection({
        authToken: 'test-token',
        sessionId: null,
      })
    );

    await act(() => {
      result.current.connect();
    });

    expect(wsTestState.mockWebSocketInstance).toBeNull();
    expect(result.current.isConnected).toBe(false);
  });

  it('should not reconnect if already connected', async () => {
    const onConnected = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onConnected,
      })
    );

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    const firstInstance = wsTestState.mockWebSocketInstance;
    const onConnectedCallCount = onConnected.mock.calls.length;

    await act(() => {
      result.current.connect();
    });

    // Should not create a new WebSocket, but should call onConnected again
    expect(wsTestState.mockWebSocketInstance).toBe(firstInstance);
    expect(onConnected.mock.calls.length).toBeGreaterThan(onConnectedCallCount);
  });

  it('should handle WebSocket already OPEN when connecting', async () => {
    const onConnected = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onConnected,
      })
    );

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    // Set WebSocket to OPEN state
    if (wsTestState.mockWebSocketInstance) {
      wsTestState.mockWebSocketInstance.readyState = MockWebSocket.OPEN;
    }

    await act(() => {
      result.current.connect();
    });

    // Should call onConnected since WebSocket is already OPEN
    expect(onConnected).toHaveBeenCalled();
    expect(result.current.isConnected).toBe(true);
  });

  it('should handle connect when WebSocket is in CONNECTING state', async () => {
    // Test line 160: readyState === WebSocket.CONNECTING branch
    // Test line 165: false branch when readyState is CONNECTING (not OPEN)
    const onConnected = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onConnected,
      })
    );

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    // Set WebSocket to CONNECTING state (not yet OPEN) without disconnecting
    // This simulates a WebSocket that is currently connecting
    if (wsTestState.mockWebSocketInstance) {
      wsTestState.mockWebSocketInstance.readyState = MockWebSocket.CONNECTING;
      // Ensure isConnected is false (it should be by default until OPEN)
      await act(() => {
        // Don't disconnect, just verify the state
      });
    }

    // Clear any previous onConnected calls
    onConnected.mockClear();

    // Try to connect again while in CONNECTING state
    await act(() => {
      result.current.connect();
    });

    // Should return early without calling onConnected (since not OPEN yet)
    // Line 160-170: should log debug and return without calling onConnected
    // Line 165: false branch - CONNECTING !== OPEN, so setIsConnected and onConnected not called
    expect(onConnected).not.toHaveBeenCalled(); // Not OPEN yet, so won't call
    // isConnected should remain false since CONNECTING !== OPEN
    expect(result.current.isConnected).toBe(false);
  });

  it('should cleanup closed WebSocket before reconnecting', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    // Close the WebSocket by simulating close event
    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateClose();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(false);
      },
      { timeout: 1000 }
    );

    // Now connect again - should create a new WebSocket instance
    await act(() => {
      result.current.connect();
    });

    // Should create a new WebSocket instance after cleanup
    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        // Should have a new instance or the old one should be cleaned up
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );
  });

  it('should cleanup closed connection before reconnecting', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    // Close the connection
    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateClose();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(false);
      },
      { timeout: 1000 }
    );

    const firstInstance = wsTestState.mockWebSocketInstance;

    // Reconnect
    await act(() => {
      result.current.connect();
    });

    // Should create a new WebSocket after cleanup
    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
        expect(wsTestState.mockWebSocketInstance).not.toBe(firstInstance);
      },
      { timeout: 1000 }
    );
  });
});
