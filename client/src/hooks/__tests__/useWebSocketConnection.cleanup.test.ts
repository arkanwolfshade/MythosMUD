import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useWebSocketConnection } from '../useWebSocketConnection';
import './useWebSocketConnectionTestFixtures';
import {
  defaultOptions,
  latestWebSocketInstance,
  mockResourceManager,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from './useWebSocketConnectionTestFixtures';

describe('useWebSocketConnection - Cleanup', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('should cleanup on unmount', async () => {
    const { result, unmount } = renderHook(() => useWebSocketConnection(defaultOptions));

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

    // Unmount should trigger cleanup synchronously
    act(() => {
      unmount();
    });

    // Cleanup should happen immediately on unmount
    expect(wsTestState.mockWebSocketInstance?.getCloseCalls().length).toBeGreaterThan(0);
    expect(mockResourceManager.removeInterval).toHaveBeenCalled();
  });

  it('should cleanup ping interval on disconnect', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

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

    // Disconnect should trigger cleanup synchronously
    act(() => {
      result.current.disconnect();
    });

    // Cleanup should happen immediately on disconnect
    expect(mockResourceManager.removeInterval).toHaveBeenCalled();
  });

  it('should not call onDisconnect if WebSocket closed without ever connecting', async () => {
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

    // Close before opening (never connected)
    act(() => {
      wsTestState.mockWebSocketInstance?.simulateClose();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(false);
      },
      { timeout: 1000 }
    );

    // onDisconnect should not be called since we never connected
    expect(onDisconnect).not.toHaveBeenCalled();
  });
});
