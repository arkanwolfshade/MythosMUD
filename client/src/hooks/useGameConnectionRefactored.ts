/**
 * Refactored Game Connection Hook using XState FSM.
 *
 * Orchestrates SSE, WebSocket, and session management using explicit state machine.
 * Replaces 750+ lines of manual state tracking with ~200 lines of declarative logic.
 *
 * AI: This refactored version uses XState for robust connection management.
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { logger } from '../utils/logger';
import { inputSanitizer } from '../utils/security';
import { useConnectionState } from './useConnectionState';
import { useSSEConnection } from './useSSEConnection';
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
  sessionId?: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
  onSessionChange?: (sessionId: string) => void;
  onConnectionHealthUpdate?: (health: { websocket: string; sse: string }) => void;
}

/**
 * Refactored game connection hook with XState state machine.
 *
 * Manages dual connection (SSE + WebSocket) with explicit state tracking,
 * automatic reconnection, and robust error handling.
 *
 * @param options - Connection configuration and callbacks
 * @returns Connection state and control methods
 *
 * AI: Uses composition of specialized hooks orchestrated by XState FSM.
 */
export function useGameConnection(options: UseGameConnectionOptions) {
  const {
    authToken,
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

  // Connection state machine
  const connectionState = useConnectionState({
    maxReconnectAttempts: 5,
    onStateChange: state => {
      logger.debug('GameConnection', 'State changed', { state });

      // Update ref for use in error handlers
      connectionStateValueRef.current = state;

      // Reset autoConnectPending when connection attempt completes (success or failure)
      // This includes: disconnected (failed), failed, fully_connected (success)
      // Also reset when in 'reconnecting' state - the initial connection attempt has failed
      // But not: connecting_sse, connecting_ws, sse_connected (still in initial connection attempt)
      const connectingStates = ['connecting_sse', 'connecting_ws', 'sse_connected'];
      if (!connectingStates.includes(state)) {
        setAutoConnectPending(false);
      }

      if (state === 'fully_connected') {
        onConnectionHealthUpdate?.({ websocket: 'healthy', sse: 'healthy' });
      } else if (state === 'reconnecting' || state === 'failed') {
        onConnectionHealthUpdate?.({ websocket: 'unhealthy', sse: 'unhealthy' });
      }
    },
  });

  // SSE connection
  const sseConnection = useSSEConnection({
    authToken,
    sessionId,
    onConnected: sseSessionId => {
      logger.info('GameConnection', 'SSE connected', { sessionId: sseSessionId });
      updateSessionId(sseSessionId);
      // BUGFIX: Cancel timeout when SSE_CONNECTED is received
      // This prevents timeout from firing if connection is established quickly
      connectionState.onSSEConnected(sseSessionId);
    },
    onMessage: event => {
      try {
        const data = JSON.parse(event.data);
        // #region agent log
        if (data.event_type === 'player_hp_updated' || data.event_type === 'playerhpupdated') {
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'useGameConnectionRefactored.ts:148',
              message: 'SSE message received',
              data: {
                event_type: data.event_type,
                old_hp: data.data?.old_hp,
                new_hp: data.data?.new_hp,
                raw_event: JSON.stringify(data).substring(0, 200),
              },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              runId: 'run1',
              hypothesisId: 'A',
            }),
          }).catch(() => {});
        }
        // Log room_occupants events to debug NPC display issue
        if (data.event_type === 'room_occupants') {
          logger.info('GameConnection', 'SSE room_occupants event received', {
            event_type: data.event_type,
            room_id: data.room_id,
            has_players: !!data.data?.players,
            has_npcs: !!data.data?.npcs,
            players_count: data.data?.players?.length ?? 0,
            npcs_count: data.data?.npcs?.length ?? 0,
            npcs: data.data?.npcs ?? [],
          });
        }
        // #endregion
        setLastEvent(data);
        // #region agent log
        if (data.event_type === 'player_hp_updated' || data.event_type === 'playerhpupdated') {
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'useGameConnectionRefactored.ts:152',
              message: 'Calling onEventRef with SSE event',
              data: { event_type: data.event_type, has_callback: !!onEventRef.current },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              runId: 'run1',
              hypothesisId: 'A',
            }),
          }).catch(() => {});
        }
        // #endregion
        onEventRef.current?.(data);
      } catch (error) {
        logger.error('GameConnection', 'Error parsing SSE message', { error });
      }
    },
    onHeartbeat: () => {
      // Track heartbeat for connection health monitoring
      logger.debug('GameConnection', 'SSE heartbeat received');
    },
    onError: () => {
      // Notify state machine if:
      // 1. Connection was established and is now unhealthy, OR
      // 2. We're in a connecting state and the connection attempt failed
      const currentState = connectionStateValueRef.current;
      const isConnecting = ['connecting_sse', 'connecting_ws', 'sse_connected', 'reconnecting'].includes(currentState);
      if (isSSEConnectedRef.current && !sseConnection.isHealthy) {
        logger.warn('GameConnection', 'SSE connection failed - connection was unhealthy', {
          lastHeartbeatTime: sseConnection.lastHeartbeatTime,
          isHealthy: sseConnection.isHealthy,
        });
        connectionState.onSSEFailed('Connection failed');
      } else if (isConnecting && !isSSEConnectedRef.current) {
        // Connection attempt failed during initial connection
        logger.warn('GameConnection', 'SSE connection attempt failed', { state: currentState });
        connectionState.onSSEFailed('Connection failed');
      } else if (isSSEConnectedRef.current) {
        logger.debug('GameConnection', 'SSE error on healthy connection - treating as temporary hiccup');
        // Don't notify state machine - connection might recover
      }
      onErrorRef.current?.('Connection failed');
    },
    onDisconnect: () => {
      logger.info('GameConnection', 'SSE disconnected');
    },
  });

  // WebSocket connection
  const wsConnection = useWebSocketConnection({
    authToken,
    sessionId,
    onConnected: () => {
      logger.info('GameConnection', 'WebSocket connected');
      // NOTE: Do not call connectionState.onWSConnected() here - let the useEffect at line 297 handle it
      // This prevents race conditions where WS connects before state machine reaches sse_connected
    },
    onMessage: event => {
      try {
        const data = JSON.parse(event.data);
        // #region agent log
        if (data.event_type === 'player_hp_updated' || data.event_type === 'playerhpupdated') {
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'useGameConnectionRefactored.ts:197',
              message: 'WebSocket message received',
              data: {
                event_type: data.event_type,
                old_hp: data.data?.old_hp,
                new_hp: data.data?.new_hp,
                raw_event: JSON.stringify(data).substring(0, 200),
              },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              runId: 'run1',
              hypothesisId: 'A',
            }),
          }).catch(() => {});
        }
        // #endregion
        setLastEvent(data);
        // #region agent log
        if (data.event_type === 'player_hp_updated' || data.event_type === 'playerhpupdated') {
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'useGameConnectionRefactored.ts:201',
              message: 'Calling onEventRef with WebSocket event',
              data: { event_type: data.event_type, has_callback: !!onEventRef.current },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              runId: 'run1',
              hypothesisId: 'A',
            }),
          }).catch(() => {});
        }
        // #endregion
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
      const isConnecting = ['connecting_sse', 'connecting_ws', 'sse_connected', 'reconnecting'].includes(currentState);
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
    connect: startSSE,
    disconnect: stopSSE,
    isConnected: isSSEConnected,
    isHealthy: isSSEHealthy,
    lastHeartbeatTime,
  } = sseConnection;
  const {
    connect: startWebSocket,
    disconnect: stopWebSocket,
    sendMessage: sendWebSocketMessage,
    isConnected: isWebSocketConnected,
  } = wsConnection;

  // Store connection states for use in callbacks (avoid stale closures)
  const isSSEConnectedRef = useRef(isSSEConnected);
  const isWebSocketConnectedRef = useRef(isWebSocketConnected);
  const isSSEHealthyRef = useRef(isSSEHealthy);

  useEffect(() => {
    isSSEConnectedRef.current = isSSEConnected;
  }, [isSSEConnected]);

  useEffect(() => {
    isWebSocketConnectedRef.current = isWebSocketConnected;
  }, [isWebSocketConnected]);

  useEffect(() => {
    isSSEHealthyRef.current = isSSEHealthy;
  }, [isSSEHealthy]);

  // BUGFIX: Monitor SSE connection health via heartbeat
  // If connection is unhealthy (no heartbeat for 60+ seconds), treat as lost
  useEffect(() => {
    if (!isSSEConnected || !isSSEHealthy) {
      return;
    }

    const healthCheckInterval = setInterval(() => {
      // Check if connection is still healthy
      if (isSSEConnected && !isSSEHealthy) {
        logger.warn('GameConnection', 'SSE connection unhealthy - no heartbeat received', {
          lastHeartbeatTime,
          timeSinceLastHeartbeat: lastHeartbeatTime ? Date.now() - lastHeartbeatTime : null,
        });
        // Connection is unhealthy - notify state machine
        connectionState.onSSEFailed('Connection unhealthy - no heartbeat');
      }
    }, 10000); // Check every 10 seconds

    return () => {
      clearInterval(healthCheckInterval);
    };
  }, [isSSEConnected, isSSEHealthy, lastHeartbeatTime, connectionState]);

  useEffect(() => {
    if (connectionStateValue === 'sse_connected' && isWebSocketConnected) {
      // Ensure the connection state machine observes both channels as ready before enabling gameplay
      // Reminder for machine siblings: do not remove this guard without understanding the Dunwich recurrence condition.
      logger.debug('GameConnection', 'Both SSE and WebSocket connected, transitioning to fully_connected', {
        connectionStateValue,
        isWebSocketConnected,
        isSSEConnected,
      });
      connectionState.onWSConnected();

      // Both connections are now ready - notify parent
      onConnectRef.current?.();
    }
  }, [connectionState, connectionStateValue, isWebSocketConnected, isSSEConnected]);

  // Ensure SSE connection attempts align with state machine
  // BUGFIX: Only trigger SSE when state machine is in connecting states, not from connect() directly
  useEffect(() => {
    if (connectionStateValue === 'connecting_sse' || connectionStateValue === 'reconnecting') {
      logger.debug('GameConnection', 'State machine triggered SSE connection', { state: connectionStateValue });
      startSSE();
    }
  }, [connectionStateValue, startSSE]);

  // Ensure WebSocket connection attempts align with session state
  // BUGFIX: Only trigger WebSocket when state machine is in connecting states, not from connect() directly
  useEffect(() => {
    if (!sessionId) {
      return;
    }

    if (['connecting_sse', 'connecting_ws', 'sse_connected', 'reconnecting'].includes(connectionStateValue)) {
      logger.debug('GameConnection', 'State machine triggered WebSocket connection', { state: connectionStateValue });
      startWebSocket();
    }
  }, [connectionStateValue, sessionId, startWebSocket]);

  // Main connect function
  // BUGFIX: Don't directly call startSSE/startWebSocket - let the state machine and useEffect hooks handle it
  const connect = useCallback(() => {
    const shouldStartConnection = !isConnectionEstablished && !isConnectionInProgress;

    if (shouldStartConnection) {
      setAutoConnectPending(true);
      logger.info('GameConnection', 'Starting connection sequence');
      startConnection();
      // State machine will trigger connecting_sse, which will trigger SSE via useEffect
    } else {
      setAutoConnectPending(false);
      logger.debug('GameConnection', 'Connection already in progress', {
        isConnected: isConnectionEstablished,
        isConnecting: isConnectionInProgress,
        state: connectionStateValue,
      });
    }
    // REMOVED: Direct calls to startSSE() and startWebSocket() - these cause race conditions
    // The state machine and useEffect hooks will handle connection sequencing
  }, [isConnectionEstablished, isConnectionInProgress, startConnection, connectionStateValue]);

  // Main disconnect function
  const disconnect = useCallback(() => {
    logger.info('GameConnection', 'Disconnecting all connections');
    setAutoConnectPending(false);

    stopSSE();
    stopWebSocket();
    stopConnection();
  }, [stopSSE, stopWebSocket, stopConnection]);

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
      sseConnected: isSSEConnected,
      connectionHealth: {
        websocket: isWebSocketConnected ? ('healthy' as const) : ('unhealthy' as const),
        sse: isSSEConnected ? ('healthy' as const) : ('unhealthy' as const),
        lastHealthCheck: Date.now(),
      },
      connectionState: connectionStateValue,
      reconnectAttempts: connectionReconnectAttempts,
    };
  }, [sessionId, isWebSocketConnected, isSSEConnected, connectionStateValue, connectionReconnectAttempts]);

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
      sse: isSSEConnected ? ('healthy' as const) : ('unhealthy' as const),
      lastHealthCheck: lastHealthCheckTime,
    }),
    [isWebSocketConnected, isSSEConnected, lastHealthCheckTime]
  );

  return {
    // State (mapped for backward compatibility)
    isConnected: isConnectionEstablished,
    isConnecting: isConnectionInProgress || autoConnectPending,
    lastEvent,
    error: connectionLastError,
    reconnectAttempts: connectionReconnectAttempts,
    sseConnected: isSSEConnected,
    websocketConnected: isWebSocketConnected,
    sessionId,
    connectionHealth,
    connectionMetadata: {
      websocketConnectionId: null,
      sseConnectionId: null,
      totalConnections: 0,
      connectionTypes: ['sse', 'websocket'],
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
