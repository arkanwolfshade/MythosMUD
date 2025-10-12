/**
 * Refactored Game Connection Hook using XState FSM.
 *
 * Orchestrates SSE, WebSocket, and session management using explicit state machine.
 * Replaces 750+ lines of manual state tracking with ~200 lines of declarative logic.
 *
 * AI: This refactored version uses XState for robust connection management.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import { inputSanitizer } from '../utils/security';
import { logger } from '../utils/logger';
import { useConnectionState } from './useConnectionState';
import { useSSEConnection } from './useSSEConnection';
import { useWebSocketConnection } from './useWebSocketConnection';
import { useSessionManagement } from './useSessionManagement';

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

  // Session management
  const session = useSessionManagement({
    initialSessionId,
    onSessionChange,
  });

  // Connection state machine
  const connectionState = useConnectionState({
    maxReconnectAttempts: 5,
    onStateChange: state => {
      logger.debug('GameConnection', 'State changed', { state });

      // Update health when state changes
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
    sessionId: session.sessionId,
    onConnected: sseSessionId => {
      logger.info('GameConnection', 'SSE connected', { sessionId: sseSessionId });
      session.updateSessionId(sseSessionId);
      connectionState.onSSEConnected(sseSessionId);
    },
    onMessage: event => {
      try {
        const data = JSON.parse(event.data);
        setLastEvent(data);
        onEventRef.current?.(data);
      } catch (error) {
        logger.error('GameConnection', 'Error parsing SSE message', { error });
      }
    },
    onError: () => {
      connectionState.onSSEFailed('SSE connection error');
      onErrorRef.current?.('SSE connection failed');
    },
    onDisconnect: () => {
      logger.info('GameConnection', 'SSE disconnected');
    },
  });

  // WebSocket connection
  const wsConnection = useWebSocketConnection({
    authToken,
    sessionId: session.sessionId,
    onConnected: () => {
      logger.info('GameConnection', 'WebSocket connected');
      connectionState.onWSConnected();

      // Both connections are now ready
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
      connectionState.onWSFailed('WebSocket connection error');
      onErrorRef.current?.('WebSocket connection failed');
    },
    onDisconnect: () => {
      logger.info('GameConnection', 'WebSocket disconnected');
      onDisconnectRef.current?.();
    },
  });

  // State machine orchestration
  useEffect(() => {
    const state = connectionState.state;

    if (state === 'connecting_sse' && !sseConnection.isConnected) {
      sseConnection.connect();
    } else if (state === 'sse_connected' || state === 'connecting_ws') {
      // Trigger WebSocket connection after SSE
      if (session.sessionId && !wsConnection.isConnected) {
        connectionState.onWSConnected(); // Signal we're moving to WS phase
        wsConnection.connect();
      }
    }
  }, [connectionState, session.sessionId, sseConnection, wsConnection]);

  // Main connect function
  const connect = useCallback(() => {
    if (connectionState.isConnected) {
      logger.debug('GameConnection', 'Already connected, skipping');
      return;
    }

    logger.info('GameConnection', 'Starting connection sequence');
    connectionState.connect();
  }, [connectionState]);

  // Main disconnect function
  const disconnect = useCallback(() => {
    logger.info('GameConnection', 'Disconnecting all connections');

    sseConnection.disconnect();
    wsConnection.disconnect();
    connectionState.disconnect();
  }, [sseConnection, wsConnection, connectionState]);

  // Send command through WebSocket
  const sendCommand = useCallback(
    (command: string) => {
      if (!connectionState.isConnected) {
        logger.warn('GameConnection', 'Cannot send command: not connected');
        return;
      }

      // Sanitize command input
      const sanitizedCommand = inputSanitizer.sanitize(command);

      // Create command message
      const message = JSON.stringify({
        type: 'command',
        command: sanitizedCommand,
        timestamp: new Date().toISOString(),
      });

      wsConnection.sendMessage(message);
    },
    [connectionState.isConnected, wsConnection]
  );

  // Get connection info
  const getConnectionInfo = useCallback(() => {
    return {
      sessionId: session.sessionId,
      websocketConnected: wsConnection.isConnected,
      sseConnected: sseConnection.isConnected,
      connectionHealth: {
        websocket: wsConnection.isConnected ? 'healthy' : 'unhealthy',
        sse: sseConnection.isConnected ? 'healthy' : 'unhealthy',
        lastHealthCheck: Date.now(),
      },
      connectionState: connectionState.state,
      reconnectAttempts: connectionState.reconnectAttempts,
    };
  }, [session.sessionId, wsConnection.isConnected, sseConnection.isConnected, connectionState]);

  return {
    // State (mapped for backward compatibility)
    isConnected: connectionState.isConnected,
    isConnecting: connectionState.isConnecting,
    lastEvent,
    error: connectionState.lastError,
    reconnectAttempts: connectionState.reconnectAttempts,
    sseConnected: sseConnection.isConnected,
    websocketConnected: wsConnection.isConnected,
    sessionId: session.sessionId,
    connectionHealth: {
      websocket: wsConnection.isConnected ? ('healthy' as const) : ('unhealthy' as const),
      sse: sseConnection.isConnected ? ('healthy' as const) : ('unhealthy' as const),
      lastHealthCheck: Date.now(),
    },
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
    createNewSession: session.createNewSession,
    switchToSession: session.switchToSession,
    getConnectionInfo,
  };
}
