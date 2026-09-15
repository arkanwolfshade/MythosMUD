/**
 * Regression for #822: typed `/rest` (or any server intentional_disconnect) must not
 * auto-reconnect. Logout button sets intentionalExitInProgressRef before sending rest;
 * typed `/rest` only gets the server event -- onMessage must arm the same flag before
 * the socket closes, so onDisconnect skips reconnect and calls onIntentionalDisconnect.
 */
import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameConnection } from '../useGameConnectionRefactored';
import {
  defaultOptions,
  latestWebSocketInstance,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from './useWebSocketConnectionTestFixtures';

describe('useGameConnection - intentional_disconnect (#822)', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('arms intentional exit from intentional_disconnect and does not reconnect', async () => {
    const intentionalExitInProgressRef = { current: false };
    const onIntentionalDisconnect = vi.fn();

    const { result } = renderHook(() =>
      useGameConnection({
        ...defaultOptions,
        intentionalExitInProgressRef,
        onIntentionalDisconnect,
      })
    );

    await waitFor(() => {
      wsTestState.mockWebSocketInstance = latestWebSocketInstance;
      expect(wsTestState.mockWebSocketInstance).not.toBeNull();
    });

    act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(() => {
      expect(result.current.isConnected).toBe(true);
    });

    const connectedInstance = wsTestState.mockWebSocketInstance;

    act(() => {
      connectedInstance?.simulateMessage(
        JSON.stringify({
          event_type: 'intentional_disconnect',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: { message: 'You have rested and disconnected from the game.' },
        })
      );
    });

    expect(intentionalExitInProgressRef.current).toBe(true);

    act(() => {
      connectedInstance?.simulateClose(1000, 'Normal Closure');
    });

    await waitFor(() => {
      expect(result.current.isConnected).toBe(false);
    });

    expect(onIntentionalDisconnect).toHaveBeenCalledTimes(1);

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 50));
    });

    expect(latestWebSocketInstance).toBe(connectedInstance);
    expect(result.current.isConnected).toBe(false);
  });
});
