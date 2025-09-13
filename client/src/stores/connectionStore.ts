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
  sse: 'healthy' | 'unhealthy' | 'unknown';
  lastHealthCheck: number | null;
}

export interface ConnectionMetadata {
  websocketConnectionId: string | null;
  sseConnectionId: string | null;
  totalConnections: number;
  connectionTypes: string[];
}

export interface ConnectionState {
  // Connection status
  isConnected: boolean;
  isConnecting: boolean;
  sseConnected: boolean;
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
  setSseConnected: (connected: boolean) => void;
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
  isFullyConnected: boolean;
  hasAnyConnection: boolean;
  getConnectionInfo: () => {
    sessionId: string | null;
    websocketConnected: boolean;
    sseConnected: boolean;
    connectionHealth: ConnectionHealth;
    connectionMetadata: ConnectionMetadata;
  };
}

type ConnectionStore = ConnectionState & ConnectionActions & ConnectionSelectors;

const generateSessionId = (): string => {
  const timestamp = Date.now();
  const random = Math.random().toString(36).substring(2, 8);
  return `session_${timestamp}_${random}`;
};

const createInitialState = (sessionId?: string): ConnectionState => ({
  isConnected: false,
  isConnecting: false,
  sseConnected: false,
  websocketConnected: false,
  error: null,
  reconnectAttempts: 0,
  lastEvent: null,
  sessionId: sessionId || generateSessionId(),
  connectionHealth: {
    websocket: 'unknown',
    sse: 'unknown',
    lastHealthCheck: null,
  },
  connectionMetadata: {
    websocketConnectionId: null,
    sseConnectionId: null,
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

      setSseConnected: (connected: boolean) =>
        set(
          state => ({
            sseConnected: connected,
            isConnected: connected && state.websocketConnected,
            error: connected ? null : state.error,
          }),
          false,
          'setSseConnected'
        ),

      setWebsocketConnected: (connected: boolean) =>
        set(
          state => ({
            websocketConnected: connected,
            isConnected: connected && state.sseConnected,
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
        return state.sseConnected && state.websocketConnected;
      },

      hasAnyConnection: () => {
        const state = get();
        return state.sseConnected || state.websocketConnected;
      },

      getConnectionInfo: () => {
        const state = get();
        return {
          sessionId: state.sessionId,
          websocketConnected: state.websocketConnected,
          sseConnected: state.sseConnected,
          connectionHealth: state.connectionHealth,
          connectionMetadata: state.connectionMetadata,
        };
      },
    }),
    {
      name: 'connection-store',
      partialize: state => ({
        sessionId: state.sessionId,
        connectionHealth: state.connectionHealth,
        connectionMetadata: state.connectionMetadata,
      }),
    }
  )
);
