/// <reference lib="ES2015" />

import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
// Fixtures import must load before the hook: it calls vi.mock('../../utils/resourceCleanup', ...),
// and vi.mock() only intercepts a module that hasn't already been imported and cached. Importing
// the hook first (as this previously did, despite this very comment saying not to -- @/ paths
// survive organizeImports on save, but this plain relative pair doesn't sort back on its own)
// evaluates the hook's real `useResourceCleanup` import before the mock registers, so every
// assertion against mockResourceManager silently watches the wrong object (#297/#778 CI failure).
import {
  defaultOptions,
  latestWebSocketInstance,
  mockResourceManager,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from './useWebSocketConnectionTestFixtures';
import { useWebSocketConnection } from '../useWebSocketConnection';

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

  it('should call onDisconnect exactly once for an explicit disconnect() (#297)', async () => {
    // disconnect() notifies onDisconnect synchronously, then calls ws.close() -- which itself
    // fires onclose (also notifying onDisconnect). Without the manualDisconnectRef guard, both
    // paths fire for a single logical disconnect: it double-counts reconnect attempts and, in
    // production, can leave the reconnect state machine forcing a second WebSocket for what was
    // only ever one intentional close (observed as a runaway reconnect/backoff loop in e2e).
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

    expect(onDisconnect).toHaveBeenCalledTimes(1);
  });

  it('should pass the close code and reason through to onDisconnect (#297/#610)', async () => {
    // The reconnect-vs-give-up decision (useGameConnectionRefactored's onDisconnect wiring) needs
    // the WebSocket close code to distinguish a normal closure (1000 -- e.g. the server replacing
    // this connection with a newer session) from an actual failure. Before this, onDisconnect took
    // no arguments at all, so every close looked identical and a graceful session replacement
    // retried indefinitely against whichever session currently held the connection.
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
      wsTestState.mockWebSocketInstance?.simulateClose(1000, 'New game session established');
    });

    expect(onDisconnect).toHaveBeenCalledWith({ code: 1000, reason: 'New game session established' });
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
