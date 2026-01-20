import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

export interface GameEvent {
  type: string;
  sequence_number: number;
  player_id?: string;
  room_id?: string;
  data: Record<string, unknown>;
  alias_chain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

export interface ConnectionHealth {
  websocket: 'healthy' | 'unhealthy' | 'unknown';
  lastHealthCheck: number | null;
}

export interface ConnectionMetadata {
  websocketConnectionId: string | null;
  totalConnections: number;
  connectionTypes: string[];
}

export interface ConnectionState {
  // Connection status
  isConnected: boolean;
  isConnecting: boolean;
  websocketConnected: boolean;
  error: string | null;
  reconnectAttempts: number;
  lastEvent: GameEvent | null;

  // Session management
  sessionId: string | null;

  // Connection health monitoring
  connectionHealth: ConnectionHealth;
  connectionMetadata: ConnectionMetadata;
}

export interface ConnectionActions {
  // Connection management
  setConnecting: (connecting: boolean) => void;
  setWebsocketConnected: (connected: boolean) => void;
  setError: (error: string | null) => void;
  setLastEvent: (event: GameEvent | null) => void;

  // Reconnection management
  incrementReconnectAttempts: () => void;
  resetReconnectAttempts: () => void;

  // Session management
  setSessionId: (sessionId: string | null) => void;
  createNewSession: () => string;
  switchToSession: (sessionId: string) => void;

  // Connection health
  updateConnectionHealth: (health: Partial<ConnectionHealth>) => void;
  completeHealthCheck: () => void;

  // Connection metadata
  updateConnectionMetadata: (metadata: Partial<ConnectionMetadata>) => void;

  // State management
  reset: () => void;
}

export interface ConnectionSelectors {
  // Computed properties
  isFullyConnected: () => boolean;
  hasAnyConnection: () => boolean;
  getConnectionInfo: () => {
    sessionId: string | null;
    websocketConnected: boolean;
    connectionHealth: ConnectionHealth;
    connectionMetadata: ConnectionMetadata;
  };
}

type ConnectionStore = ConnectionState & ConnectionActions & ConnectionSelectors;

/**
 * **Zustand Store Usage Patterns:**
 *
 * Zustand stores automatically handle subscription lifecycle - components do not need to
 * manually unsubscribe. However, components should follow these patterns:
 *
 * 1. **Use store actions, not direct state manipulation:**
 *    - Use setConnecting(), setWebsocketConnected(), etc. instead of directly modifying state
 *    - This ensures proper state updates and prevents memory leaks from stale references
 *
 * 2. **Reset store state when appropriate:**
 *    - Call reset() on logout, session expiration, or component unmount
 *    - This clears all state and prevents memory leaks from accumulated data
 *
 * 3. **Use selectors for performance:**
 *    - Always use selectors to subscribe only to needed state fields
 *    - This prevents unnecessary re-renders when unrelated state changes
 *
 * 4. **No manual subscription cleanup needed:**
 *    - Zustand's useStore hook automatically handles subscription/unsubscription
 *    - Components using useConnectionStore() don't need useEffect cleanup for store subscriptions
 *    - Only cleanup needed is for external resources (WebSocket connections, timers, etc.)
 *
 * **CORRECT Usage Examples:**
 *
 * ```tsx
 * // ✅ GOOD: Using selectors to subscribe only to needed fields
 * function MyComponent() {
 *   const isConnecting = useConnectionStore(state => state.isConnecting);
 *   const error = useConnectionStore(state => state.error);
 *   const reset = useConnectionStore(state => state.reset);
 *
 *   return <div>{isConnecting ? 'Connecting...' : 'Connected'}</div>;
 * }
 *
 * // ✅ GOOD: Using selector functions for computed values (but prefer direct state access)
 * function StatusComponent() {
 *   const websocketConnected = useConnectionStore(state => state.websocketConnected);
 *   // Prefer: const isConnected = websocketConnected;
 *   // Over: const isConnected = useConnectionStore(state => state.isFullyConnected());
 * }
 * ```
 *
 * **INCORRECT Usage Examples (Anti-patterns):**
 *
 * ```tsx
 * // ❌ BAD: Subscribing to entire store causes re-renders on any state change
 * function MyComponent() {
 *   const connectionState = useConnectionStore(); // Don't do this!
 *   return <div>{connectionState.isConnecting ? 'Connecting...' : 'Connected'}</div>;
 * }
 *
 * // ❌ BAD: Calling selector functions inside selectors still subscribes to entire store
 * function MyComponent() {
 *   const isConnected = useConnectionStore(state => state.isFullyConnected()); // Don't do this!
 *   // Instead, use: const isConnected = useConnectionStore(state => state.websocketConnected);
 * }
 * ```
 *
 * **Note on Selector Functions:**
 * - Selector functions like `isFullyConnected()`, `hasAnyConnection()`, and `getConnectionInfo()`
 *   are kept for backward compatibility but should NOT be called inside component selectors.
 * - Instead, access the underlying state directly (e.g., use `websocketConnected` instead of `isFullyConnected()`).
 * - These functions can still be useful for non-React code or when you need to access state outside of components.
 */

/**
 * Generate a cryptographically secure session ID.
 * Human reader: uses Web Crypto API instead of Math.random() for security.
 * AI reader: session IDs must be unpredictable to prevent session hijacking.
 */
const generateSessionId = (): string => {
  // Use crypto.getRandomValues for cryptographically secure randomness
  const array = new Uint8Array(9);
  crypto.getRandomValues(array);
  // Convert to base36 string (similar to Math.random().toString(36))
  const randomPart = Array.from(array)
    .map(byte => byte.toString(36))
    .join('')
    .substring(0, 9);
  const timestamp = Date.now();
  return `session_${timestamp}_${randomPart}`;
};

const createInitialState = (sessionId?: string): ConnectionState => ({
  isConnected: false,
  isConnecting: false,
  websocketConnected: false,
  error: null,
  reconnectAttempts: 0,
  lastEvent: null,
  sessionId: sessionId || generateSessionId(),
  connectionHealth: {
    websocket: 'unknown',
    lastHealthCheck: null,
  },
  connectionMetadata: {
    websocketConnectionId: null,
    totalConnections: 0,
    connectionTypes: [],
  },
});

export const useConnectionStore = create<ConnectionStore>()(
  devtools(
    (set, get) => ({
      ...createInitialState(),

      // Connection management actions
      setConnecting: (connecting: boolean) =>
        set(
          state => ({
            isConnecting: connecting,
            isConnected: connecting ? state.isConnected : false,
          }),
          false,
          'setConnecting'
        ),

      setWebsocketConnected: (connected: boolean) =>
        set(
          state => ({
            websocketConnected: connected,
            isConnected: connected,
            error: connected ? null : state.error,
          }),
          false,
          'setWebsocketConnected'
        ),

      setError: (error: string | null) => set({ error }, false, 'setError'),

      setLastEvent: (event: GameEvent | null) => set({ lastEvent: event }, false, 'setLastEvent'),

      // Reconnection management actions
      incrementReconnectAttempts: () =>
        set(state => ({ reconnectAttempts: state.reconnectAttempts + 1 }), false, 'incrementReconnectAttempts'),

      resetReconnectAttempts: () => set({ reconnectAttempts: 0 }, false, 'resetReconnectAttempts'),

      // Session management actions
      setSessionId: (sessionId: string | null) => set({ sessionId }, false, 'setSessionId'),

      createNewSession: () => {
        const newSessionId = generateSessionId();
        set({ sessionId: newSessionId }, false, 'createNewSession');
        return newSessionId;
      },

      switchToSession: (sessionId: string) => set({ sessionId }, false, 'switchToSession'),

      // Connection health actions
      updateConnectionHealth: (health: Partial<ConnectionHealth>) =>
        set(
          state => ({
            connectionHealth: {
              ...state.connectionHealth,
              ...health,
              lastHealthCheck: Date.now(),
            },
          }),
          false,
          'updateConnectionHealth'
        ),

      completeHealthCheck: () =>
        set(
          state => ({
            connectionHealth: {
              ...state.connectionHealth,
              lastHealthCheck: Date.now(),
            },
          }),
          false,
          'completeHealthCheck'
        ),

      // Connection metadata actions
      updateConnectionMetadata: (metadata: Partial<ConnectionMetadata>) =>
        set(
          state => ({
            connectionMetadata: {
              ...state.connectionMetadata,
              ...metadata,
            },
          }),
          false,
          'updateConnectionMetadata'
        ),

      // State management actions
      reset: () => set(createInitialState(), false, 'reset'),

      // Selectors
      isFullyConnected: () => {
        const state = get();
        return state.websocketConnected;
      },

      hasAnyConnection: () => {
        const state = get();
        return state.websocketConnected;
      },

      getConnectionInfo: () => {
        const state = get();
        return {
          sessionId: state.sessionId,
          websocketConnected: state.websocketConnected,
          connectionHealth: state.connectionHealth,
          connectionMetadata: state.connectionMetadata,
        };
      },
    }),
    {
      name: 'connection-store',
      enabled: import.meta.env.MODE === 'development',
      partialize: (state: ConnectionStore) => ({
        sessionId: state.sessionId,
        connectionHealth: state.connectionHealth,
        connectionMetadata: state.connectionMetadata,
      }),
    }
  )
);
