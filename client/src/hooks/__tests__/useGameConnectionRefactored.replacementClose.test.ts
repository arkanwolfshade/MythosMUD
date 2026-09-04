/**
 * Regression test for the ADR-018 session-replacement reconnect storm (#297/#610).
 *
 * onDisconnect correctly classifies a replacement close (code 1000, "New game session
 * established") and calls connectionState.disconnect() -- terminal, no retry. But a separate
 * effect, `useEffect(() => { ... connect(); }, [authToken, connect, disconnect])`, depended on
 * `connect`'s own identity, which changes on every state transition (connect's useCallback deps
 * include connectionStateValue). That churn re-ran the effect on every transition and called
 * connect() again unconditionally, undoing the terminal decision within milliseconds -- a storm
 * where each tab's revival re-kicked the other, observed as new-game-session.spec.ts /
 * rest-command.spec.ts / chat-messages.spec.ts never reaching a stable Connected state. Fixed by
 * depending only on authToken and calling connect/disconnect through stable refs.
 */
import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import {
  defaultOptions,
  latestWebSocketInstance,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from './useWebSocketConnectionTestFixtures';
import { useGameConnection } from '../useGameConnectionRefactored';

describe('useGameConnection - replacement close does not reconnect (#297/#610)', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('does not open a new WebSocket after an ADR-018 replacement close', async () => {
    const { result } = renderHook(() => useGameConnection(defaultOptions));

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
      connectedInstance?.simulateClose(1000, 'New game session established');
    });

    await waitFor(() => {
      expect(result.current.isConnected).toBe(false);
    });

    // Give any spurious reconnect a chance to happen -- a real drop reconnects near-instantly, so
    // absence after a macrotask flush is a meaningful negative, not just "hasn't happened yet".
    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 50));
    });

    // The mock WebSocket constructor updates latestWebSocketInstance on every `new WebSocket(...)`.
    // A stray reconnect would have replaced it with a different instance.
    expect(latestWebSocketInstance).toBe(connectedInstance);
    expect(result.current.isConnected).toBe(false);
  });
});
