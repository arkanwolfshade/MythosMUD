/**
 * XState connection state machine for robust connection management.
 *
 * Implements explicit finite state machine for managing WebSocket
 * connection lifecycle with automatic recovery and health tracking.
 *
 * AI: State machines eliminate implicit state bugs common in connection handling.
 */

import { assign, setup } from 'xstate';

/**
 * Connection state definitions.
 *
 * AI: Explicit states prevent impossible states like "connected but also connecting"
 */
export type ConnectionState = 'disconnected' | 'connecting_ws' | 'fully_connected' | 'reconnecting' | 'failed';

/**
 * Events that trigger state transitions.
 *
 * AI: Type-safe events ensure all transitions are explicit and testable.
 */
export type ConnectionEvent =
  | { type: 'CONNECT' }
  | { type: 'WS_CONNECTED' }
  | { type: 'WS_FAILED'; error: string }
  | { type: 'ERROR'; error: string }
  | { type: 'DISCONNECT' }
  | { type: 'RETRY' }
  | { type: 'RECONNECT' }
  | { type: 'CONNECTION_TIMEOUT' }
  | { type: 'RESET' };

/**
 * Context data stored with the state machine.
 *
 * Replaces multiple refs with single source of truth.
 *
 * AI: XState context provides typed, immutable state updates.
 */
export interface ConnectionContext {
  sessionId: string | null;
  reconnectAttempts: number;
  maxReconnectAttempts: number;
  lastError: string | null;
  connectionStartTime: number | null;
  lastConnectedTime: number | null;
  wsUrl: string | null;
}

/**
 * Connection state machine definition using XState v5.
 *
 * Implements robust connection lifecycle with:
 * - WebSocket connection establishment
 * - Automatic reconnection with backoff
 * - Timeout guards (30s connection, 5s reconnect)
 * - Error tracking and recovery
 *
 * States:
 * - disconnected: Initial state, no connections
 * - connecting_ws: Establishing WebSocket connection
 * - fully_connected: WebSocket connection established
 * - reconnecting: Attempting to restore connection
 * - failed: All connection attempts exhausted
 *
 * AI: FSM ensures deterministic behavior and testable transitions.
 */
export const connectionMachine = setup({
  types: {
    context: {} as ConnectionContext,
    events: {} as ConnectionEvent,
  },
  actions: {
    /**
     * Reset connection metadata.
     * AI: Clean slate for fresh connection attempts.
     */
    resetConnection: assign({
      sessionId: () => null,
      lastError: () => null,
      connectionStartTime: () => null,
      reconnectAttempts: () => 0,
    }),

    /**
     * Store connection start time when connection begins.
     * AI: Used to track connection duration and timeout.
     */
    storeConnectionStartTime: assign({
      connectionStartTime: () => Date.now(),
    }),

    /**
     * Mark connection as fully established.
     * AI: WebSocket connected - system is operational.
     */
    markFullyConnected: assign({
      lastConnectedTime: () => Date.now(),
      reconnectAttempts: 0,
      lastError: null,
    }),

    /**
     * Store connection error.
     * AI: Error tracking for debugging and monitoring.
     */
    storeError: assign({
      lastError: ({ event }) => {
        if ('error' in event) {
          return event.error;
        }
        return 'Unknown error';
      },
    }),

    /**
     * Increment reconnect attempt counter.
     * AI: Track retry attempts for exponential backoff.
     */
    incrementReconnectAttempts: assign({
      reconnectAttempts: ({ context }) => context.reconnectAttempts + 1,
    }),

    /**
     * Clear all connection state.
     * AI: For clean shutdown or reset.
     */
    clearAllState: assign({
      sessionId: null,
      reconnectAttempts: 0,
      lastError: null,
      connectionStartTime: null,
      wsUrl: null,
    }),
  },

  guards: {
    /**
     * Check if more reconnect attempts are allowed.
     * AI: Prevents infinite reconnection loops.
     */
    canReconnect: ({ context }) => {
      return context.reconnectAttempts < context.maxReconnectAttempts;
    },

    /**
     * Check if max reconnect attempts exhausted.
     * AI: Triggers failure state after all retries.
     */
    maxAttemptsReached: ({ context }) => {
      return context.reconnectAttempts >= context.maxReconnectAttempts;
    },
  },

  delays: {
    /**
     * Connection timeout (30 seconds).
     * AI: Prevents hanging on unresponsive servers.
     */
    CONNECTION_TIMEOUT: 30000,

    /**
     * Reconnection delay with exponential backoff.
     * AI: Calculated as: min(1000 * 2^attempts, 30000)
     */
    RECONNECT_DELAY: ({ context }) => {
      const delay = Math.min(1000 * Math.pow(2, context.reconnectAttempts), 30000);
      return delay;
    },
  },
}).createMachine({
  id: 'connection',
  initial: 'disconnected',
  context: {
    sessionId: null,
    reconnectAttempts: 0,
    maxReconnectAttempts: 5,
    lastError: null,
    connectionStartTime: null,
    lastConnectedTime: null,
    wsUrl: null,
  },
  states: {
    disconnected: {
      entry: 'resetConnection',
      on: {
        CONNECT: {
          target: 'connecting_ws',
          actions: ['resetConnection', 'storeConnectionStartTime'],
        },
      },
    },

    connecting_ws: {
      on: {
        WS_CONNECTED: {
          target: 'fully_connected',
          actions: 'markFullyConnected',
        },
        WS_FAILED: {
          target: 'reconnecting',
          actions: ['storeError', 'incrementReconnectAttempts'],
        },
        ERROR: {
          target: 'reconnecting',
          actions: ['storeError', 'incrementReconnectAttempts'],
        },
        CONNECTION_TIMEOUT: {
          target: 'reconnecting',
          actions: ['storeError', 'incrementReconnectAttempts'],
        },
        DISCONNECT: {
          target: 'disconnected',
        },
      },
      after: {
        CONNECTION_TIMEOUT: {
          target: 'reconnecting',
          actions: assign({
            lastError: 'WebSocket connection timeout',
            reconnectAttempts: ({ context }) => context.reconnectAttempts + 1,
          }),
        },
      },
    },

    fully_connected: {
      on: {
        DISCONNECT: {
          target: 'disconnected',
        },
        WS_FAILED: {
          target: 'reconnecting',
          actions: ['storeError', 'incrementReconnectAttempts'],
        },
        RETRY: {
          target: 'reconnecting',
          actions: 'incrementReconnectAttempts',
        },
        ERROR: {
          target: 'reconnecting',
          actions: ['storeError', 'incrementReconnectAttempts'],
        },
      },
    },

    reconnecting: {
      always: [
        {
          guard: 'maxAttemptsReached',
          target: 'failed',
        },
      ],
      after: {
        RECONNECT_DELAY: [
          {
            guard: 'canReconnect',
            target: 'connecting_ws',
          },
          {
            target: 'failed',
          },
        ],
      },
      on: {
        DISCONNECT: {
          target: 'disconnected',
        },
        RESET: {
          target: 'disconnected',
          actions: 'clearAllState',
        },
        RECONNECT: {
          target: 'connecting_ws',
          actions: ['resetConnection', 'storeConnectionStartTime'],
        },
      },
    },

    failed: {
      on: {
        RESET: {
          target: 'disconnected',
          actions: 'clearAllState',
        },
        RECONNECT: {
          target: 'connecting_ws',
          actions: ['resetConnection', 'storeConnectionStartTime'],
        },
        RETRY: {
          target: 'reconnecting',
        },
        DISCONNECT: {
          target: 'disconnected',
        },
      },
    },
  },
});
