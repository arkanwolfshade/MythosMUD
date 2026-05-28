import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useWebSocketConnection } from '../useWebSocketConnection';
import './useWebSocketConnectionTestFixtures';
import {
  defaultOptions,
  latestWebSocketInstance,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from './useWebSocketConnectionTestFixtures';

describe('useWebSocketConnection - Callback Updates', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('should use latest callbacks', async () => {
    const onConnected1 = vi.fn();
    const onConnected2 = vi.fn();

    const { result, rerender } = renderHook(
      ({ onConnected }) => useWebSocketConnection({ ...defaultOptions, onConnected }),
      {
        initialProps: { onConnected: onConnected1 },
      }
    );

    // Ensure hook is initialized
    expect(result.current).not.toBeNull();

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

    // Update callback before opening
    await act(async () => {
      rerender({ onConnected: onConnected2 });
    });
    // Yield so React can commit and refs (e.g. onConnected) are updated before simulateOpen
    await waitFor(
      () => {
        expect(wsTestState.mockWebSocketInstance).toBeDefined();
      },
      { timeout: 50 }
    );

    act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    // Wait for the callback to be called
    await waitFor(
      () => {
        expect(onConnected2).toHaveBeenCalled();
        expect(onConnected1).not.toHaveBeenCalled();
      },
      { timeout: 1000 }
    );
  });
});
