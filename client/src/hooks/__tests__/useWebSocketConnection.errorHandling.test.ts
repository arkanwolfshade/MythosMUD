import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
// Fixtures import must load before the hook (@/ paths survive organizeImports on save).
import {
  defaultOptions,
  latestWebSocketInstance,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from '@/hooks/__tests__/useWebSocketConnectionTestFixtures';
import { useWebSocketConnection } from '@/hooks/useWebSocketConnection';

describe('useWebSocketConnection - Error Handling', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('should handle connection errors', async () => {
    const onError = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onError,
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
      wsTestState.mockWebSocketInstance?.simulateError();
    });

    await waitFor(
      () => {
        expect(result.current.lastError).toBe('WebSocket connection error');
        expect(result.current.isConnected).toBe(false);
      },
      { timeout: 1000 }
    );

    expect(onError).toHaveBeenCalled();
  });

  it('should handle WebSocket creation errors', async () => {
    const onError = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onError,
      })
    );

    // Mock WebSocket constructor to throw - use a class that throws in constructor
    const originalWebSocket = global.WebSocket;
    class ThrowingWebSocket {
      constructor() {
        throw new Error('WebSocket creation failed');
      }
    }
    global.WebSocket = ThrowingWebSocket as unknown as typeof WebSocket;

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        expect(result.current.lastError).toBe('WebSocket creation failed');
      },
      { timeout: 1000 }
    );

    expect(onError).toHaveBeenCalled();

    // Restore original WebSocket
    global.WebSocket = originalWebSocket;
  });

  it('should handle WebSocket creation errors with non-Error types', async () => {
    const onError = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onError,
      })
    );

    // Mock WebSocket constructor to throw a non-Error value
    const originalWebSocket = global.WebSocket;
    class ThrowingWebSocket {
      constructor() {
        throw 'String error'; // Non-Error type
      }
    }
    global.WebSocket = ThrowingWebSocket as unknown as typeof WebSocket;

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        expect(result.current.lastError).toBe('Unknown WebSocket error');
      },
      { timeout: 1000 }
    );

    expect(onError).toHaveBeenCalled();

    // Restore original WebSocket
    global.WebSocket = originalWebSocket;
  });
});
