/**
 * WebSocket connection hook.
 *
 * Manages WebSocket connection lifecycle with ping/pong heartbeat and automatic cleanup.
 *
 * AI: Extracted from useGameConnection to reduce complexity and improve testability.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import { logger } from '../utils/logger';
import { useResourceCleanup } from '../utils/resourceCleanup';
import { inputSanitizer } from '../utils/security';

export interface WebSocketConnectionOptions {
  authToken: string;
  sessionId: string | null;
  onConnected?: () => void;
  onMessage?: (event: MessageEvent) => void;
  onError?: (error: Event) => void;
  onDisconnect?: () => void;
}

export interface WebSocketConnectionResult {
  connect: () => void;
  disconnect: () => void;
  sendMessage: (message: string) => void;
  isConnected: boolean;
  lastError: string | null;
}

/**
 * Hook for managing WebSocket connection.
 *
 * Handles connection, ping/pong heartbeat, and message sending for WebSocket.
 *
 * @param options - WebSocket connection configuration
 * @returns WebSocket connection state and control methods
 *
 * AI: WebSocket requires session ID for authentication and connection tracking.
 */
export function useWebSocketConnection(options: WebSocketConnectionOptions): WebSocketConnectionResult {
  const { authToken, sessionId, onConnected, onMessage, onError, onDisconnect } = options;

  const resourceManager = useResourceCleanup();
  const websocketRef = useRef<WebSocket | null>(null);
  const lastWebSocketRef = useRef<WebSocket | null>(null);
  const pingIntervalRef = useRef<number | null>(null);
  const reconnectTimerRef = useRef<number | null>(null);
  const manualDisconnectRef = useRef<boolean>(false);
  const reconnectAttemptsRef = useRef<number>(0);
  const hasEverConnectedRef = useRef<boolean>(false);
  const connectRef = useRef<() => void>();

  // Use state instead of refs for values that need to trigger re-renders
  const [isConnected, setIsConnected] = useState(false);
  const [lastError, setLastError] = useState<string | null>(null);

  // Stable callback refs
  const onConnectedRef = useRef(onConnected);
  const onMessageRef = useRef(onMessage);
  const onErrorRef = useRef(onError);
  const onDisconnectRef = useRef(onDisconnect);

  // Update callback refs
  useEffect(() => {
    onConnectedRef.current = onConnected;
    onMessageRef.current = onMessage;
    onErrorRef.current = onError;
    onDisconnectRef.current = onDisconnect;
  }, [onConnected, onMessage, onError, onDisconnect]);

  const disconnect = useCallback(() => {
    manualDisconnectRef.current = true;
    // Clear ping interval
    if (pingIntervalRef.current !== null) {
      window.clearInterval(pingIntervalRef.current);
      resourceManager.removeInterval(pingIntervalRef.current);
      pingIntervalRef.current = null;
    }

    // Clear reconnect timer
    if (reconnectTimerRef.current !== null) {
      window.clearTimeout(reconnectTimerRef.current);
      resourceManager.removeTimer(reconnectTimerRef.current);
      reconnectTimerRef.current = null;
    }

    const socketToClose = websocketRef.current ?? lastWebSocketRef.current;
    if (socketToClose) {
      logger.debug('WebSocketConnection', 'Disconnecting WebSocket');

      socketToClose.close();
      if (socketToClose === websocketRef.current) {
        websocketRef.current = null;
      }
      lastWebSocketRef.current = null;
      setIsConnected(false);

      if (hasEverConnectedRef.current) {
        onDisconnectRef.current?.();
      }
    }
  }, [resourceManager]);

  const sendMessage = useCallback(
    (message: string) => {
      if (!websocketRef.current || !isConnected) {
        logger.warn('WebSocketConnection', 'Cannot send message: WebSocket not connected');
        return;
      }

      try {
        // Enhanced input validation
        if (!message || typeof message !== 'string') {
          logger.warn('WebSocketConnection', 'Invalid message type');
          return;
        }

        if (message.length > 1000) {
          // Message length limit
          logger.warn('WebSocketConnection', 'Message too long');
          return;
        }

        // Sanitize the message first
        const sanitizedMessage = inputSanitizer.sanitizeCommand(message);

        // Validate sanitization didn't remove too much
        if (sanitizedMessage.length < message.length * 0.5) {
          logger.warn('WebSocketConnection', 'Message heavily sanitized, rejecting');
          return;
        }

        // Send the sanitized message without embedding sensitive tokens
        const outbound = JSON.stringify({
          message: sanitizedMessage,
          timestamp: Date.now(),
        });

        websocketRef.current.send(outbound);
        logger.debug('WebSocketConnection', 'Message sent', {
          messageLength: sanitizedMessage.length,
        });
      } catch (error) {
        logger.error('WebSocketConnection', 'Error sending message', { error });
      }
    },
    [isConnected]
  );

  const connect = useCallback(() => {
    if (!authToken || !sessionId) {
      logger.warn('WebSocketConnection', 'Cannot connect: missing auth token or session ID');
      return;
    }

    // Check if WebSocket exists AND is actually connected (readyState 0 = CONNECTING, 1 = OPEN)
    if (websocketRef.current) {
      const readyState = websocketRef.current.readyState;
      if (readyState === WebSocket.CONNECTING || readyState === WebSocket.OPEN) {
        logger.debug('WebSocketConnection', 'WebSocket already connected, notifying state machine', { readyState });
        // BUGFIX: Still call onConnected even if WebSocket is already connected
        // This allows the state machine to transition to fully_connected
        // when the connection is restored after a page reload or reconnect
        if (readyState === WebSocket.OPEN) {
          logger.debug('WebSocketConnection', 'WebSocket already connected, calling onConnected', { readyState });
          setIsConnected(true);
          onConnectedRef.current?.();
        }
        return;
      }
      // WebSocket exists but is closed/closing - clean it up before reconnecting
      logger.debug('WebSocketConnection', 'WebSocket exists but is closed, cleaning up before reconnect', {
        readyState,
      });
      disconnect();
    }

    try {
      manualDisconnectRef.current = false;
      // Use relative URL with Vite proxy and pass JWT via subprotocols (bearer, <token>)
      const wsUrl = `/api/ws?session_id=${encodeURIComponent(sessionId)}`;
      const protocols: string[] = ['bearer', authToken];

      logger.info('WebSocketConnection', 'Connecting to WebSocket', { url: wsUrl });

      const ws = new WebSocket(wsUrl, protocols);
      websocketRef.current = ws;
      lastWebSocketRef.current = ws;

      ws.onopen = () => {
        logger.info('WebSocketConnection', 'WebSocket connected successfully');
        setIsConnected(true);
        setLastError(null);
        hasEverConnectedRef.current = true;

        // reset reconnect attempts on successful open
        reconnectAttemptsRef.current = 0;

        // Enhanced ping with NATS health check
        pingIntervalRef.current = window.setInterval(async () => {
          if (ws.readyState === WebSocket.OPEN) {
            // Send ping to WebSocket
            ws.send(JSON.stringify({ type: 'ping' }));

            // DEV-only: check NATS health via server
            if (import.meta.env.DEV) {
              try {
                const healthResponse = await fetch('/api/monitoring/health', {
                  method: 'GET',
                  headers: { Authorization: `Bearer ${authToken}` },
                });
                if (!healthResponse.ok) {
                  logger.warn('WebSocketConnection', 'NATS health check failed');
                }
              } catch (error) {
                logger.warn('WebSocketConnection', 'NATS health check error', { error });
              }
            }
          }
        }, 30000);

        resourceManager.registerInterval(pingIntervalRef.current);

        onConnectedRef.current?.();
      };

      ws.onmessage = event => {
        onMessageRef.current?.(event);
      };

      ws.onerror = error => {
        logger.error('WebSocketConnection', 'WebSocket error', { error });
        setLastError('WebSocket connection error');
        setIsConnected(false);
        onErrorRef.current?.(error);
      };

      ws.onclose = () => {
        logger.info('WebSocketConnection', 'WebSocket closed');
        setIsConnected(false);

        // Clear ping interval
        if (pingIntervalRef.current !== null) {
          window.clearInterval(pingIntervalRef.current);
          resourceManager.removeInterval(pingIntervalRef.current);
          pingIntervalRef.current = null;
        }
        if (hasEverConnectedRef.current) {
          onDisconnectRef.current?.();
        }

        // BUGFIX: Don't schedule reconnection here - let the state machine handle it
        // The state machine's reconnection logic is more robust and prevents conflicts
        // The onDisconnect callback will notify the state machine, which will handle reconnection
        logger.debug('WebSocketConnection', 'WebSocket closed, state machine will handle reconnection');
      };
    } catch (error) {
      logger.error('WebSocketConnection', 'Error creating WebSocket connection', { error });
      setLastError(error instanceof Error ? error.message : 'Unknown WebSocket error');
      onErrorRef.current?.(error as Event);
    }
  }, [authToken, sessionId, resourceManager, disconnect]);

  useEffect(() => {
    connectRef.current = connect;
  }, [connect]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      disconnect();
    };
  }, [disconnect]);

  return {
    connect,
    disconnect,
    sendMessage,
    isConnected,
    lastError,
  };
}
