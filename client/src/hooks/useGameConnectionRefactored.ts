/**
 * Refactored Game Connection Hook using XState FSM.
 *
 * Orchestrates WebSocket connection and session management using explicit state machine.
 * Replaces 750+ lines of manual state tracking with ~200 lines of declarative logic.
 *
 * AI: This refactored version uses XState for robust connection management.
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { logger } from '../utils/logger';
import { inputSanitizer } from '../utils/security';
import { useConnectionState } from './useConnectionState';
import { useSessionManagement } from './useSessionManagement';
import { useWebSocketConnection } from './useWebSocketConnection';

interface GameEvent {
  event_type: string;
  timestamp: string;
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

export interface UseGameConnectionOptions {
  authToken: string;
  characterId?: string; // MULTI-CHARACTER: Selected character ID for WebSocket connection
  sessionId?: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
  onSessionChange?: (sessionId: string) => void;
  onConnectionHealthUpdate?: (health: { websocket: string }) => void;
}

/**
 * Refactored game connection hook with XState state machine.
 *
 * Manages WebSocket connection with explicit state tracking,
 * automatic reconnection, and robust error handling.
 *
 * @param options - Connection configuration and callbacks
 * @returns Connection state and control methods
 *
 * AI: Uses composition of specialized hooks orchestrated by XState FSM.
 */
/**
 * Generate a cryptographically secure session ID.
 * Human reader: uses Web Crypto API instead of Math.random() for security.
 * AI reader: session IDs must be unpredictable to prevent session hijacking.
 */
const generateSecureSessionId = (): string => {
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

export function useGameConnection(options: UseGameConnectionOptions) {
  const {
    authToken,
    characterId,
    sessionId: initialSessionId,
    onEvent,
    onConnect,
    onDisconnect,
    onError,
    onSessionChange,
    onConnectionHealthUpdate,
  } = options;

  const [lastEvent, setLastEvent] = useState<GameEvent | null>(null);
  const [autoConnectPending, setAutoConnectPending] = useState<boolean>(() => Boolean(authToken));

  const pendingSessionSwitchRef = useRef<string | null>(null);
  const userOnSessionChangeRef = useRef(onSessionChange);
  const connectRef = useRef<() => void>(() => {});
  const connectionStateValueRef = useRef<string>('disconnected');

  // Stable callback refs
  const onEventRef = useRef(onEvent);
  const onConnectRef = useRef(onConnect);
  const onDisconnectRef = useRef(onDisconnect);
  const onErrorRef = useRef(onError);

  useEffect(() => {
    onEventRef.current = onEvent;
    onConnectRef.current = onConnect;
    onDisconnectRef.current = onDisconnect;
    onErrorRef.current = onError;
  }, [onEvent, onConnect, onDisconnect, onError]);

  useEffect(() => {
    userOnSessionChangeRef.current = onSessionChange;
  }, [onSessionChange]);

  // Session management
  const session = useSessionManagement({
    initialSessionId,
    onSessionChange: newSessionId => {
      userOnSessionChangeRef.current?.(newSessionId);

      if (pendingSessionSwitchRef.current === newSessionId) {
        pendingSessionSwitchRef.current = null;
        connectRef.current();
      }
    },
  });

  const {
    sessionId,
    createNewSession: sessionCreateNewSession,
    switchToSession: sessionSwitchToSession,
    updateSessionId,
  } = session;

  // Track if we've received the first state change callback
  // This prevents resetting autoConnectPending on the initial 'disconnected' state notification
  const hasReceivedFirstStateChangeRef = useRef(false);

  // Memoize the onStateChange callback to prevent the useEffect in useConnectionState from running multiple times
  // The options object is recreated on each render, which would cause the useEffect to run repeatedly
  const handleStateChange = useCallback(
    (state: string) => {
      logger.debug('GameConnection', 'State changed', { state });

      // Update ref for use in error handlers
      connectionStateValueRef.current = state;

      // Reset autoConnectPending when connection attempt completes (success or failure)
      // This includes: disconnected (failed), failed, fully_connected (success)
      // But NOT: connecting_ws or reconnecting (still attempting to connect)
      // IMPORTANT: Don't reset on the very first state change callback (initial 'disconnected' state)
      // This allows the auto-connect effect to run and start the connection before autoConnectPending is reset
      const connectingStates = ['connecting_ws', 'reconnecting'];
      const isFirstCallback = !hasReceivedFirstStateChangeRef.current && state === 'disconnected';

      if (isFirstCallback) {
        hasReceivedFirstStateChangeRef.current = true;
      }

      // Only reset if:
      // 1. State is not in connecting states (not 'connecting_ws' or 'reconnecting')
      // 2. This is not the first callback (initial state notification)
      if (!connectingStates.includes(state) && !isFirstCallback) {
        setAutoConnectPending(false);
      }

      if (state === 'fully_connected') {
        onConnectionHealthUpdate?.({ websocket: 'healthy' });
      } else if (state === 'reconnecting' || state === 'failed') {
        onConnectionHealthUpdate?.({ websocket: 'unhealthy' });
      }
    },
    [onConnectionHealthUpdate]
  );

  // Connection state machine
  const connectionState = useConnectionState({
    maxReconnectAttempts: 5,
    onStateChange: handleStateChange,
  });

  // WebSocket connection
  const wsConnection = useWebSocketConnection({
    authToken,
    characterId,
    sessionId,
    onConnected: () => {
      logger.info('GameConnection', 'WebSocket connected');
      // Generate session ID if not already set (WebSocket now handles session ID generation)
      if (!sessionId) {
        const newSessionId = generateSecureSessionId();
        updateSessionId(newSessionId);
      }
      connectionState.onWSConnected();
      onConnectRef.current?.();
    },
    onMessage: event => {
      try {
        const data = JSON.parse(event.data);
        setLastEvent(data);
        onEventRef.current?.(data);
      } catch (error) {
        logger.error('GameConnection', 'Error parsing WebSocket message', { error });
      }
    },
    onError: () => {
      // Notify state machine if:
      // 1. Connection was established and failed, OR
      // 2. We're in a connecting state and the connection attempt failed
      const currentState = connectionStateValueRef.current;
      const isConnecting = ['connecting_ws', 'reconnecting'].includes(currentState);
      if (isWebSocketConnectedRef.current) {
        connectionState.onWSFailed('Connection failed');
      } else if (isConnecting && !isWebSocketConnectedRef.current) {
        // Connection attempt failed during initial connection
        logger.warn('GameConnection', 'WebSocket connection attempt failed', { state: currentState });
        connectionState.onWSFailed('Connection failed');
      }
      onErrorRef.current?.('Connection failed');
    },
    onDisconnect: () => {
      logger.info('GameConnection', 'WebSocket disconnected');
      // Notify the connection state machine that WebSocket failed
      connectionState.onWSFailed('Connection failed');
      onDisconnectRef.current?.();
    },
  });

  const {
    state: connectionStateValue,
    connect: startConnection,
    disconnect: stopConnection,
    reset: resetConnection,
    isConnected: isConnectionEstablished,
    isConnecting: isConnectionInProgress,
    reconnectAttempts: connectionReconnectAttempts,
    lastError: connectionLastError,
  } = connectionState;

  const {
    connect: startWebSocket,
    disconnect: stopWebSocket,
    sendMessage: sendWebSocketMessage,
    isConnected: isWebSocketConnected,
  } = wsConnection;

  // Store connection state for use in callbacks (avoid stale closures)
  const isWebSocketConnectedRef = useRef(isWebSocketConnected);

  useEffect(() => {
    isWebSocketConnectedRef.current = isWebSocketConnected;
  }, [isWebSocketConnected]);

  // Ensure WebSocket connection attempts align with state machine
  // BUGFIX: Only trigger WebSocket when state machine is in connecting states, not from connect() directly
  useEffect(() => {
    if (!sessionId) {
      // Generate session ID if not set
      const newSessionId = generateSecureSessionId();
      updateSessionId(newSessionId);
      return;
    }

    if (['connecting_ws', 'reconnecting'].includes(connectionStateValue)) {
      logger.debug('GameConnection', 'State machine triggered WebSocket connection', { state: connectionStateValue });
      startWebSocket();
    }
  }, [connectionStateValue, sessionId, startWebSocket, updateSessionId]);

  // Auto-connect effect: trigger connection when autoConnectPending is true
  // Note: sessionId is generated synchronously by useSessionManagement, so it should be available immediately
  useEffect(() => {
    if (autoConnectPending && sessionId && !isConnectionEstablished && !isConnectionInProgress) {
      logger.debug('GameConnection', 'Auto-connecting', { sessionId });
      startConnection();
    }
  }, [autoConnectPending, sessionId, isConnectionEstablished, isConnectionInProgress, startConnection, authToken]);

  // Main connect function
  // BUGFIX: Don't directly call startWebSocket - let the state machine and useEffect hooks handle it
  const connect = useCallback(() => {
    const shouldStartConnection = !isConnectionEstablished && !isConnectionInProgress;

    if (shouldStartConnection) {
      setAutoConnectPending(true);
      logger.info('GameConnection', 'Starting connection sequence');
      startConnection();
      // State machine will trigger connecting_ws, which will trigger WebSocket via useEffect
    } else {
      setAutoConnectPending(false);
      logger.debug('GameConnection', 'Connection already in progress', {
        isConnected: isConnectionEstablished,
        isConnecting: isConnectionInProgress,
        state: connectionStateValue,
      });
    }
    // REMOVED: Direct calls to startWebSocket() - these cause race conditions
    // The state machine and useEffect hooks will handle connection sequencing
  }, [isConnectionEstablished, isConnectionInProgress, startConnection, connectionStateValue]);

  // Main disconnect function
  const disconnect = useCallback(() => {
    logger.info('GameConnection', 'Disconnecting all connections');
    setAutoConnectPending(false);

    stopWebSocket();
    stopConnection();
  }, [stopWebSocket, stopConnection]);

  useEffect(() => {
    connectRef.current = connect;
  }, [connect]);

  useEffect(() => {
    if (!authToken) {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- disconnect updates local state when auth changes
      disconnect();
      return;
    }

    connect();
  }, [authToken, connect, disconnect]);

  useEffect(() => {
    return () => {
      disconnect();
    };
  }, [disconnect]);

  // Send command through WebSocket
  const sendCommand = useCallback(
    async (command: string, args: string[] = []): Promise<boolean> => {
      if (!isConnectionEstablished) {
        logger.warn('GameConnection', 'Cannot send command: not connected');
        return false;
      }

      try {
        // Sanitize command and arguments
        const sanitizedCommand = inputSanitizer.sanitizeCommand(command);
        const sanitizedArgs = args.map(arg => inputSanitizer.sanitizeCommand(arg));

        // Create command message matching the server's expected format
        const message = JSON.stringify({
          type: 'game_command',
          data: {
            command: sanitizedCommand,
            args: sanitizedArgs,
          },
          timestamp: new Date().toISOString(),
        });

        sendWebSocketMessage(message);
        logger.info('GameConnection', 'Command sent', { command: sanitizedCommand, args: sanitizedArgs });
        return true;
      } catch (error) {
        logger.error('GameConnection', 'Failed to send command', { error: String(error) });
        return false;
      }
    },
    [isConnectionEstablished, sendWebSocketMessage]
  );

  // Get connection info
  const getConnectionInfo = useCallback(() => {
    return {
      sessionId,
      websocketConnected: isWebSocketConnected,
      connectionHealth: {
        websocket: isWebSocketConnected ? ('healthy' as const) : ('unhealthy' as const),
        lastHealthCheck: Date.now(),
      },
      connectionState: connectionStateValue,
      reconnectAttempts: connectionReconnectAttempts,
    };
  }, [sessionId, isWebSocketConnected, connectionStateValue, connectionReconnectAttempts]);

  const switchToSession = useCallback(
    (newSessionId: string) => {
      if (!newSessionId || sessionId === newSessionId) {
        return;
      }

      pendingSessionSwitchRef.current = newSessionId;
      disconnect();
      resetConnection();
      sessionSwitchToSession(newSessionId);
      setAutoConnectPending(true);
    },
    [sessionId, sessionSwitchToSession, disconnect, resetConnection]
  );

  // Connection state monitoring - detect when all connections are lost
  const wasConnectedRef = useRef(false);
  useEffect(() => {
    const wasConnected = wasConnectedRef.current;
    const isCurrentlyConnected = isConnectionEstablished;

    // If we were connected but are no longer connected, trigger onDisconnect
    if (wasConnected && !isCurrentlyConnected) {
      logger.info('GameConnection', 'All connections lost, triggering onDisconnect callback');
      options.onDisconnect?.();
    }

    // Update the ref for next comparison
    wasConnectedRef.current = isCurrentlyConnected;
  }, [isConnectionEstablished, options.onDisconnect, options]);

  // Memoize connection health - use function initializer to avoid impure calls during render
  const [lastHealthCheckTime] = useState(() => Date.now());
  const connectionHealth = useMemo(
    () => ({
      websocket: isWebSocketConnected ? ('healthy' as const) : ('unhealthy' as const),
      lastHealthCheck: lastHealthCheckTime,
    }),
    [isWebSocketConnected, lastHealthCheckTime]
  );

  return {
    // State (mapped for backward compatibility)
    isConnected: isConnectionEstablished,
    isConnecting: isConnectionInProgress || autoConnectPending,
    lastEvent,
    error: connectionLastError,
    reconnectAttempts: connectionReconnectAttempts,
    websocketConnected: isWebSocketConnected,
    sessionId,
    connectionHealth,
    connectionMetadata: {
      websocketConnectionId: null,
      totalConnections: isWebSocketConnected ? 1 : 0,
      connectionTypes: ['websocket'],
    },

    // Actions
    connect,
    disconnect,
    sendCommand,

    // Session management (backward compatibility)
    createNewSession: sessionCreateNewSession,
    switchToSession,
    getConnectionInfo,
  };
}
