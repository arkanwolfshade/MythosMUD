/**
 * WebSocket connection hook.
 *
 * Manages WebSocket connection lifecycle with ping/pong heartbeat and automatic cleanup.
 *
 * AI: Extracted from useGameConnection to reduce complexity and improve testability.
 */

import { useCallback, useEffect, useRef } from 'react';
import { csrfProtection, inputSanitizer } from '../utils/security';
import { logger } from '../utils/logger';
import { useResourceCleanup } from '../utils/resourceCleanup';

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
  const isConnectedRef = useRef(false);
  const lastErrorRef = useRef<string | null>(null);

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
    // Clear ping interval
    if (pingIntervalRef.current !== null) {
      window.clearInterval(pingIntervalRef.current);
      resourceManager.removeInterval(pingIntervalRef.current);
      pingIntervalRef.current = null;
    }

    // Close WebSocket
    if (websocketRef.current) {
      logger.debug('WebSocketConnection', 'Disconnecting WebSocket');

      websocketRef.current.close();
      websocketRef.current = null;
      isConnectedRef.current = false;

      onDisconnectRef.current?.();
    }
  }, [resourceManager]);

  const sendMessage = useCallback((message: string) => {
    if (!websocketRef.current || !isConnectedRef.current) {
      logger.warn('WebSocketConnection', 'Cannot send message: WebSocket not connected');
      return;
    }

    try {
      // Apply CSRF protection and input sanitization
      const protectedMessage = csrfProtection.addToken(message);
      const sanitizedMessage = inputSanitizer.sanitize(protectedMessage);

      websocketRef.current.send(sanitizedMessage);
      logger.debug('WebSocketConnection', 'Message sent', { message: sanitizedMessage });
    } catch (error) {
      logger.error('WebSocketConnection', 'Error sending message', { error });
    }
  }, []);

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
      const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsHost = window.location.host;
      const encodedToken = encodeURIComponent(authToken);
      const encodedSession = encodeURIComponent(sessionId);
      const wsUrl = `${wsProtocol}//${wsHost}/ws?token=${encodedToken}&session_id=${encodedSession}`;

      logger.info('WebSocketConnection', 'Connecting to WebSocket', { url: wsUrl });

      const ws = new WebSocket(wsUrl);
      websocketRef.current = ws;

      ws.onopen = () => {
        logger.info('WebSocketConnection', 'WebSocket connected successfully');
        isConnectedRef.current = true;
        lastErrorRef.current = null;

        // Start ping interval (30s)
        pingIntervalRef.current = window.setInterval(() => {
          if (ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify({ type: 'ping' }));
          }
        }, 30000);

        resourceManager.addInterval(pingIntervalRef.current);

        onConnectedRef.current?.();
      };

      ws.onmessage = event => {
        onMessageRef.current?.(event);
      };

      ws.onerror = error => {
        logger.error('WebSocketConnection', 'WebSocket error', { error });
        lastErrorRef.current = 'WebSocket connection error';
        isConnectedRef.current = false;
        onErrorRef.current?.(error);
      };

      ws.onclose = () => {
        logger.info('WebSocketConnection', 'WebSocket closed');
        isConnectedRef.current = false;

        // Clear ping interval
        if (pingIntervalRef.current !== null) {
          window.clearInterval(pingIntervalRef.current);
          resourceManager.removeInterval(pingIntervalRef.current);
          pingIntervalRef.current = null;
        }

        onDisconnectRef.current?.();
      };
    } catch (error) {
      logger.error('WebSocketConnection', 'Error creating WebSocket connection', { error });
      lastErrorRef.current = error instanceof Error ? error.message : 'Unknown WebSocket error';
      onErrorRef.current?.(error as Event);
    }
  }, [authToken, sessionId, disconnect, resourceManager]);

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
    isConnected: isConnectedRef.current,
    lastError: lastErrorRef.current,
  };
}
