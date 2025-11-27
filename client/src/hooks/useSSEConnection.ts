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


// Helper to generate a secure random string of given length
function generateSecureRandomString(length: number): string {
  const array = new Uint8Array(length);
  window.crypto.getRandomValues(array);
  // Convert bytes to hex string
  return Array.from(array, b => b.toString(16).padStart(2, '0')).join('').substr(0, length);
}
export interface SSEConnectionOptions {
  authToken: string;
  sessionId: string | null;
  onConnected?: (sessionId: string) => void;
  onMessage?: (event: MessageEvent) => void;
  onError?: (error: Event) => void;
  onDisconnect?: () => void;
  onHeartbeat?: () => void;
}

export interface SSEConnectionResult {
  connect: () => void;
  disconnect: () => void;
  isConnected: boolean;
  lastError: string | null;
  lastHeartbeatTime: number | null;
  isHealthy: boolean;
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
  const [lastHeartbeatTime, setLastHeartbeatTime] = useState<number | null>(null);

  // Ref to track last heartbeat time for use in error handler (avoid stale closure)
  const lastHeartbeatTimeRef = useRef<number | null>(null);

  // Stable callback refs
  const onConnectedRef = useRef(onConnected);
  const onMessageRef = useRef(onMessage);
  const onErrorRef = useRef(onError);
  const onDisconnectRef = useRef(onDisconnect);
  const onHeartbeatRef = useRef(options.onHeartbeat);

  // Update callback refs
  useEffect(() => {
    onConnectedRef.current = onConnected;
    onMessageRef.current = onMessage;
    onErrorRef.current = onError;
    onDisconnectRef.current = onDisconnect;
    onHeartbeatRef.current = options.onHeartbeat;
  }, [onConnected, onMessage, onError, onDisconnect, options.onHeartbeat]);

  // Update heartbeat ref when state changes
  useEffect(() => {
    lastHeartbeatTimeRef.current = lastHeartbeatTime;
  }, [lastHeartbeatTime]);

  // Heartbeat health monitoring - connection is healthy if we received a heartbeat within last 60 seconds
  // Server sends heartbeats every 30 seconds, so 60 seconds gives us 2 missed heartbeats before marking unhealthy
  const isHealthy = lastHeartbeatTime !== null && Date.now() - lastHeartbeatTime < 60000;

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
        logger.debug('SSEConnection', 'SSE already connected, notifying state machine', { readyState });
        // BUGFIX: Still call onConnected even if SSE is already connected
        // This allows the state machine to transition from connecting_sse to sse_connected
        // when the connection is restored after a page reload or reconnect
        if (readyState === EventSource.OPEN) {
          // SSE is fully connected - use provided sessionId or generate one
          const sseSessionId = sessionId || `session_${Date.now()}_${generateSecureRandomString(16)}`;
          logger.debug('SSEConnection', 'SSE already connected, calling onConnected with sessionId', {
            sessionId: sseSessionId,
            readyState,
          });
          setIsConnected(true);
          onConnectedRef.current?.(sseSessionId);
        }
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
        const now = Date.now();
        logger.info('SSEConnection', 'SSE connected successfully');
        setIsConnected(true);
        setLastError(null);
        setLastHeartbeatTime(now);
        lastHeartbeatTimeRef.current = now;
        onConnectedRef.current?.(sseSessionId);
      };

      eventSource.onmessage = event => {
        try {
          const data = JSON.parse(event.data);
          // Track heartbeat events for connection health monitoring
          if (data.event_type === 'heartbeat') {
            const now = Date.now();
            setLastHeartbeatTime(now);
            lastHeartbeatTimeRef.current = now;
            logger.debug('SSEConnection', 'Heartbeat received', { timestamp: now });
            onHeartbeatRef.current?.();
          }
        } catch {
          // Not JSON, might be plain text - still process it
        }
        onMessageRef.current?.(event);
      };

      eventSource.onerror = error => {
        // Compute health at error time using ref to avoid stale closure
        const heartbeatTime = lastHeartbeatTimeRef.current;
        const currentHealth = heartbeatTime !== null && Date.now() - heartbeatTime < 60000;
        const timeSinceLastHeartbeat = heartbeatTime ? Date.now() - heartbeatTime : null;

        logger.error('SSEConnection', 'SSE connection error', {
          error,
          isHealthy: currentHealth,
          lastHeartbeatTime: heartbeatTime,
          timeSinceLastHeartbeat,
        });
        setLastError('Connection failed');
        setIsConnected(false);

        // BUGFIX: Only trigger error callback if connection was actually unhealthy
        // This distinguishes actual connection loss from temporary network hiccups
        // If we received a heartbeat recently, this might be a temporary issue
        if (!currentHealth || heartbeatTime === null) {
          logger.warn('SSEConnection', 'SSE error on unhealthy connection - treating as real failure', {
            isHealthy: currentHealth,
            lastHeartbeatTime: heartbeatTime,
            timeSinceLastHeartbeat,
          });
          onErrorRef.current?.(error);
          // Close and cleanup only if connection is actually unhealthy
          disconnect();
        } else {
          logger.debug('SSEConnection', 'SSE error on healthy connection - treating as temporary hiccup', {
            isHealthy: currentHealth,
            lastHeartbeatTime: heartbeatTime,
            timeSinceLastHeartbeat,
          });
          // Don't disconnect - connection might recover
          // The heartbeat monitoring will detect if connection is actually lost
        }
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
    lastHeartbeatTime,
    isHealthy,
  };
}
