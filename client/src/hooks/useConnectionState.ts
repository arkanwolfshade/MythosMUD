/**
 * React hook for using the connection state machine.
 *
 * Provides a clean API for components to interact with the connection FSM.
 *
 * AI: Separates state machine logic from React-specific concerns.
 */

import { useMachine } from '@xstate/react';
import { useCallback, useEffect } from 'react';
import { ConnectionContext, connectionMachine } from './useConnectionStateMachine';

/**
 * Connection state hook return type.
 *
 * AI: Type-safe interface for component usage.
 */
export interface UseConnectionStateResult {
  // Current state
  state: string;
  context: ConnectionContext;

  // State checks
  isDisconnected: boolean;
  isConnecting: boolean;
  isConnected: boolean;
  isReconnecting: boolean;
  isFailed: boolean;

  // Actions
  connect: () => void;
  disconnect: () => void;
  reconnect: () => void;
  reset: () => void;

  // Event handlers for connection callbacks
  onWSConnected: () => void;
  onWSFailed: (error: string) => void;

  // Metadata
  reconnectAttempts: number;
  lastError: string | null;
  sessionId: string | null;
}

/**
 * Custom hook for managing connection state with XState.
 *
 * Wraps the connection state machine and provides React-friendly API.
 *
 * Usage:
 * ```typescript
 * const { state, connect, disconnect, isConnected } = useConnectionState();
 *
 * // Start connection
 * connect();
 *
 * // Check state
 * if (isConnected) { ... }
 * ```
 *
 * @param options - Configuration options
 * @returns Connection state and control methods
 *
 * AI: This hook manages all connection state - no manual state management needed.
 */
export function useConnectionState(options?: {
  maxReconnectAttempts?: number;
  onStateChange?: (state: string) => void;
}): UseConnectionStateResult {
  const [state, send] = useMachine(connectionMachine, {
    context: {
      ...connectionMachine.context,
      maxReconnectAttempts: options?.maxReconnectAttempts ?? 5,
    },
  });

  // Notify parent of state changes
  useEffect(() => {
    if (options?.onStateChange) {
      options.onStateChange(state.value as string);
    }
  }, [state.value, options]);

  // Action callbacks
  const connect = useCallback(() => {
    send({ type: 'CONNECT' });
  }, [send]);

  const disconnect = useCallback(() => {
    send({ type: 'DISCONNECT' });
  }, [send]);

  const reconnect = useCallback(() => {
    send({ type: 'RECONNECT' });
  }, [send]);

  const reset = useCallback(() => {
    send({ type: 'RESET' });
  }, [send]);

  // Event handlers for connection lifecycle
  const onWSConnected = useCallback(() => {
    send({ type: 'WS_CONNECTED' });
  }, [send]);

  const onWSFailed = useCallback(
    (error: string) => {
      send({ type: 'WS_FAILED', error });
    },
    [send]
  );

  // Compute state flags
  const currentState = state.value as string;
  const isDisconnected = currentState === 'disconnected';
  const isConnecting = ['connecting_ws'].includes(currentState);
  const isConnected = currentState === 'fully_connected';
  const isReconnecting = currentState === 'reconnecting';
  const isFailed = currentState === 'failed';

  return {
    // Current state
    state: currentState,
    context: state.context,

    // State checks
    isDisconnected,
    isConnecting,
    isConnected,
    isReconnecting,
    isFailed,

    // Actions
    connect,
    disconnect,
    reconnect,
    reset,

    // Event handlers
    onWSConnected,
    onWSFailed,

    // Metadata
    reconnectAttempts: state.context.reconnectAttempts,
    lastError: state.context.lastError,
    sessionId: state.context.sessionId,
  };
}
