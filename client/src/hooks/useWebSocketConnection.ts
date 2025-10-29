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
import { csrfProtection, inputSanitizer } from '../utils/security';

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
 * AI: WebSocket requires session ID from SSE for authentication.
 */
export function useWebSocketConnection(options: WebSocketConnectionOptions): WebSocketConnectionResult {
  const { authToken, sessionId, onConnected, onMessage, onError, onDisconnect } = options;

  const resourceManager = useResourceCleanup();
  const websocketRef = useRef<WebSocket | null>(null);
  const pingIntervalRef = useRef<number | null>(null);
  const reconnectTimerRef = useRef<number | null>(null);
  const manualDisconnectRef = useRef<boolean>(false);
  const reconnectAttemptsRef = useRef<number>(0);
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

    // Close WebSocket
    if (websocketRef.current) {
      logger.debug('WebSocketConnection', 'Disconnecting WebSocket');

      websocketRef.current.close();
      websocketRef.current = null;
      setIsConnected(false);

      onDisconnectRef.current?.();
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

        // Generate CSRF token and include it in the message
        const csrfToken = csrfProtection.generateToken();

        // Send the sanitized message with CSRF protection
        const messageWithCSRF = JSON.stringify({
          message: sanitizedMessage,
          csrfToken: csrfToken,
          timestamp: Date.now(),
        });

        websocketRef.current.send(messageWithCSRF);
        logger.debug('WebSocketConnection', 'Message sent', {
          messageLength: sanitizedMessage.length,
          csrfToken: csrfToken.substring(0, 8) + '...', // Log partial token
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

    if (websocketRef.current) {
      logger.debug('WebSocketConnection', 'WebSocket already connected, skipping');
      return;
    }

    try {
      manualDisconnectRef.current = false;
      // Use relative URL with Vite proxy and pass JWT via subprotocols (bearer, <token>)
      const wsUrl = `/api/ws?session_id=${encodeURIComponent(sessionId)}`;
      const protocols: string[] = ['bearer', authToken];

      logger.info('WebSocketConnection', 'Connecting to WebSocket', { url: wsUrl });

      const ws = new WebSocket(wsUrl, protocols);
      websocketRef.current = ws;

      ws.onopen = () => {
        logger.info('WebSocketConnection', 'WebSocket connected successfully');
        setIsConnected(true);
        setLastError(null);

        // reset reconnect attempts on successful open
        reconnectAttemptsRef.current = 0;

        // Enhanced ping with NATS health check
        pingIntervalRef.current = window.setInterval(async () => {
          if (ws.readyState === WebSocket.OPEN) {
            // Send ping to WebSocket
            ws.send(JSON.stringify({ type: 'ping' }));

            // Also check NATS health via server
            try {
              const healthResponse = await fetch('/api/health/nats', {
                method: 'GET',
                headers: { Authorization: `Bearer ${authToken}` },
              });

              if (!healthResponse.ok) {
                logger.warn('WebSocketConnection', 'NATS health check failed');
                // Trigger reconnection or degradation
              }
            } catch (error) {
              logger.warn('WebSocketConnection', 'NATS health check error', { error });
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

        onDisconnectRef.current?.();

        // Schedule reconnect unless disconnect was manual
        if (!manualDisconnectRef.current) {
          const attempt = reconnectAttemptsRef.current + 1;
          reconnectAttemptsRef.current = attempt;
          // Exponential backoff with jitter
          const base = Math.min(30000, 1000 * Math.pow(2, attempt - 1));
          const jitter = Math.floor(Math.random() * 250);
          const delay = base + jitter;
          logger.info('WebSocketConnection', 'Scheduling reconnect', { attempt, delay });
          reconnectTimerRef.current = window.setTimeout(() => {
            reconnectTimerRef.current = null;
            // Only reconnect if still not connected and not manually disconnected
            if (!manualDisconnectRef.current && !websocketRef.current) {
              if (connectRef.current) {
                connectRef.current();
              }
            }
          }, delay);
          resourceManager.registerTimer(reconnectTimerRef.current);
        }
      };
    } catch (error) {
      logger.error('WebSocketConnection', 'Error creating WebSocket connection', { error });
      setLastError(error instanceof Error ? error.message : 'Unknown WebSocket error');
      onErrorRef.current?.(error as Event);
    }
  }, [authToken, sessionId, resourceManager]);

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
