/**
 * Server-Sent Events (SSE) connection hook.
 *
 * Manages SSE connection lifecycle with automatic cleanup and health tracking.
 *
 * AI: Extracted from useGameConnection to reduce complexity and improve testability.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import { logger } from '../utils/logger';
import { useResourceCleanup } from '../utils/resourceCleanup';

export interface SSEConnectionOptions {
  authToken: string;
  sessionId: string | null;
  onConnected?: (sessionId: string) => void;
  onMessage?: (event: MessageEvent) => void;
  onError?: (error: Event) => void;
  onDisconnect?: () => void;
}

export interface SSEConnectionResult {
  connect: () => void;
  disconnect: () => void;
  isConnected: boolean;
  lastError: string | null;
}

/**
 * Hook for managing SSE connection.
 *
 * Handles connection, reconnection, and message processing for Server-Sent Events.
 *
 * @param options - SSE connection configuration
 * @returns SSE connection state and control methods
 *
 * AI: SSE provides the initial session ID needed for WebSocket authentication.
 */
type EventSourceConstructor = {
  new (url: string | URL, eventSourceInitDict?: EventSourceInit): EventSource;
  (url: string | URL, eventSourceInitDict?: EventSourceInit): EventSource;
};

export function useSSEConnection(options: SSEConnectionOptions): SSEConnectionResult {
  const { authToken, sessionId, onConnected, onMessage, onError, onDisconnect } = options;

  const resourceManager = useResourceCleanup();
  const eventSourceRef = useRef<EventSource | null>(null);

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
    if (eventSourceRef.current) {
      logger.debug('SSEConnection', 'Disconnecting SSE');

      eventSourceRef.current.close();
      eventSourceRef.current = null;
      setIsConnected(false);

      onDisconnectRef.current?.();
    }
  }, []);

  const connect = useCallback(() => {
    if (!authToken) {
      logger.warn('SSEConnection', 'Cannot connect: missing auth token');
      return;
    }

    // Check if EventSource exists AND is actually connected (readyState 0 = CONNECTING, 1 = OPEN)
    if (eventSourceRef.current) {
      const readyState = eventSourceRef.current.readyState;
      if (readyState === EventSource.CONNECTING || readyState === EventSource.OPEN) {
        logger.debug('SSEConnection', 'SSE already connected, skipping', { readyState });
        return;
      }
      // EventSource exists but is closed - clean it up before reconnecting
      logger.debug('SSEConnection', 'SSE exists but is closed, cleaning up before reconnect', { readyState });
      disconnect();
    }

    try {
      const sseSessionId = sessionId || `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
      const params = new URLSearchParams();
      params.set('session_id', sseSessionId);
      if (authToken) {
        params.set('token', authToken);
      }
      const sseUrl = `/api/events?${params.toString()}`;

      logger.info('SSEConnection', 'Connecting to SSE', {
        sessionId: sseSessionId,
        hasToken: Boolean(authToken),
      });

      const eventSourceCtor = EventSource as unknown as EventSourceConstructor;
      const eventSourceOptions: EventSourceInit = { withCredentials: true };

      let eventSource: EventSource;
      try {
        eventSource = new eventSourceCtor(sseUrl, eventSourceOptions);
      } catch (error) {
        if (error instanceof TypeError && /not a constructor/i.test(String(error))) {
          eventSource = eventSourceCtor(sseUrl, eventSourceOptions);
        } else {
          throw error;
        }
      }

      eventSourceRef.current = eventSource;

      // Track as resource for cleanup
      resourceManager.registerEventSource(eventSource);

      eventSource.onopen = () => {
        logger.info('SSEConnection', 'SSE connected successfully');
        setIsConnected(true);
        setLastError(null);
        onConnectedRef.current?.(sseSessionId);
      };

      eventSource.onmessage = event => {
        onMessageRef.current?.(event);
      };

      eventSource.onerror = error => {
        logger.error('SSEConnection', 'SSE connection error', { error });
        setLastError('Connection failed');
        setIsConnected(false);
        onErrorRef.current?.(error);

        // Close and cleanup
        disconnect();
      };
    } catch (error) {
      logger.error('SSEConnection', 'Error creating SSE connection', { error });
      setLastError('Connection failed');
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
    isConnected,
    lastError,
  };
}
