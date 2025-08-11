import { useCallback, useEffect, useRef, useState } from 'react';
import { logger } from '../utils/logger';

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

interface GameConnectionState {
  isConnected: boolean;
  isConnecting: boolean;
  lastEvent: GameEvent | null;
  error: string | null;
  reconnectAttempts: number;
  sseConnected: boolean;
  websocketConnected: boolean;
}

interface UseGameConnectionOptions {
  playerId?: string; // Optional since not currently used
  playerName: string;
  authToken: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
}

export function useGameConnection({ authToken, onEvent, onConnect, onError, onDisconnect }: UseGameConnectionOptions) {
  const [state, setState] = useState<GameConnectionState>({
    isConnected: false,
    isConnecting: false,
    lastEvent: null,
    error: null,
    reconnectAttempts: 0,
    sseConnected: false,
    websocketConnected: false,
  });

  const eventSourceRef = useRef<EventSource | null>(null);
  const websocketRef = useRef<WebSocket | null>(null);
  const isConnectingRef = useRef(false);
  const wsPingIntervalRef = useRef<number | null>(null);
  const sseReconnectTimerRef = useRef<number | null>(null);
  const wsReconnectTimerRef = useRef<number | null>(null);
  const sseAttemptsRef = useRef(0);
  const wsAttemptsRef = useRef(0);
  const connectRef = useRef<(() => void) | null>(null);
  const connectWebSocketRef = useRef<(() => void) | null>(null);
  const scheduleSseReconnectRef = useRef<(() => void) | null>(null);
  const scheduleWsReconnectRef = useRef<(() => void) | null>(null);

  const clearTimers = useCallback(() => {
    if (wsPingIntervalRef.current !== null) {
      window.clearInterval(wsPingIntervalRef.current);
      wsPingIntervalRef.current = null;
    }
    if (sseReconnectTimerRef.current !== null) {
      window.clearTimeout(sseReconnectTimerRef.current);
      sseReconnectTimerRef.current = null;
    }
    if (wsReconnectTimerRef.current !== null) {
      window.clearTimeout(wsReconnectTimerRef.current);
      wsReconnectTimerRef.current = null;
    }
  }, []);

  const scheduleSseReconnect = useCallback(() => {
    if (sseReconnectTimerRef.current !== null) {
      return; // Already scheduled
    }

    const maxAttempts = 5;
    const baseDelay = 1000; // 1 second
    const maxDelay = 30000; // 30 seconds

    if (sseAttemptsRef.current >= maxAttempts) {
      logger.error('GameConnection', 'Max SSE reconnect attempts reached');
      setState(prev => ({ ...prev, error: 'Max reconnect attempts reached' }));
      return;
    }

    const delay = Math.min(baseDelay * Math.pow(2, sseAttemptsRef.current), maxDelay);
    sseAttemptsRef.current++;

    logger.info('GameConnection', 'Scheduling SSE reconnect', {
      attempt: sseAttemptsRef.current,
      delay,
    });

    sseReconnectTimerRef.current = window.setTimeout(() => {
      sseReconnectTimerRef.current = null;
      if (!state.isConnected && !isConnectingRef.current) {
        // Use a ref to avoid circular dependency
        if (connectRef.current) {
          connectRef.current();
        }
      }
    }, delay);
  }, [state.isConnected]);

  const scheduleWsReconnect = useCallback(() => {
    if (wsReconnectTimerRef.current !== null) {
      return; // Already scheduled
    }

    const maxAttempts = 5;
    const baseDelay = 1000; // 1 second
    const maxDelay = 30000; // 30 seconds

    if (wsAttemptsRef.current >= maxAttempts) {
      logger.error('GameConnection', 'Max WebSocket reconnect attempts reached');
      return;
    }

    const delay = Math.min(baseDelay * Math.pow(2, wsAttemptsRef.current), maxDelay);
    wsAttemptsRef.current++;

    logger.info('GameConnection', 'Scheduling WebSocket reconnect', {
      attempt: wsAttemptsRef.current,
      delay,
    });

    wsReconnectTimerRef.current = window.setTimeout(() => {
      wsReconnectTimerRef.current = null;
      if (state.sseConnected && !state.websocketConnected) {
        // Use a ref to avoid circular dependency
        if (connectWebSocketRef.current) {
          connectWebSocketRef.current();
        }
      }
    }, delay);
  }, [state.sseConnected, state.websocketConnected]);

  // Store schedule functions in refs to avoid circular dependencies
  scheduleSseReconnectRef.current = scheduleSseReconnect;
  scheduleWsReconnectRef.current = scheduleWsReconnect;

  const connectWebSocket = useCallback(() => {
    if (websocketRef.current) {
      logger.info('GameConnection', 'WebSocket already connected');
      return;
    }

    try {
      logger.info('GameConnection', 'Connecting WebSocket');
      const websocket = new WebSocket(`ws://localhost:54731/api/ws?token=${encodeURIComponent(authToken)}`);

      websocket.onopen = () => {
        logger.info('GameConnection', 'WebSocket connected');
        websocketRef.current = websocket;
        setState(prev => ({ ...prev, websocketConnected: true }));
        wsAttemptsRef.current = 0; // Reset attempts on successful connection

        // Start periodic ping to keep presence fresh
        if (wsPingIntervalRef.current === null) {
          wsPingIntervalRef.current = window.setInterval(() => {
            try {
              if (websocketRef.current && websocketRef.current.readyState === WebSocket.OPEN) {
                websocketRef.current.send(JSON.stringify({ type: 'ping' }));
              }
            } catch (err) {
              logger.error('GameConnection', 'Failed to send WS ping', { error: String(err) });
            }
          }, 25000);
        }
      };

      websocket.onmessage = event => {
        try {
          const gameEvent: GameEvent = JSON.parse(event.data);
          logger.info('GameConnection', 'WebSocket event received', { event_type: gameEvent.event_type });
          setState(prev => ({ ...prev, lastEvent: gameEvent }));
          onEvent?.(gameEvent);
        } catch (error) {
          logger.error('GameConnection', 'Failed to parse WebSocket event', { error: String(error) });
        }
      };

      websocket.onerror = error => {
        logger.error('GameConnection', 'WebSocket error', { error: String(error) });
        // Will attempt reconnect on close
      };

      websocket.onclose = () => {
        logger.info('GameConnection', 'WebSocket disconnected');
        websocketRef.current = null;
        setState(prev => ({ ...prev, websocketConnected: false }));
        if (wsPingIntervalRef.current !== null) {
          window.clearInterval(wsPingIntervalRef.current);
          wsPingIntervalRef.current = null;
        }
        // If SSE is still up, try to restore WS with backoff
        if (state.sseConnected) {
          if (scheduleWsReconnectRef.current) {
            scheduleWsReconnectRef.current();
          }
        }
      };
    } catch (error) {
      logger.error('GameConnection', 'Failed to connect WebSocket', { error: String(error) });
      if (scheduleWsReconnectRef.current) {
        scheduleWsReconnectRef.current();
      }
    }
  }, [authToken, onEvent, state.sseConnected]);

  // Store connectWebSocket function in ref to avoid circular dependency
  connectWebSocketRef.current = connectWebSocket;

  const connect = useCallback(async () => {
    if (isConnectingRef.current || state.isConnected) {
      logger.info('GameConnection', 'Already connecting or connected');
      return;
    }

    isConnectingRef.current = true;
    setState(prev => ({ ...prev, isConnecting: true, error: null }));

    try {
      logger.info('GameConnection', 'Connecting to game server');

      // Close any existing connection
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
        eventSourceRef.current = null;
      }

      // Prefer token-authenticated SSE endpoint; server resolves token -> user_id -> player_id
      const eventSource = new EventSource(`http://localhost:54731/api/events?token=${encodeURIComponent(authToken)}`);

      eventSourceRef.current = eventSource;

      eventSource.onopen = () => {
        logger.info('GameConnection', 'SSE connection established');
        isConnectingRef.current = false;
        setState(prev => ({
          ...prev,
          sseConnected: true,
          isConnecting: false,
          error: null,
        }));
        // Reset SSE backoff
        sseAttemptsRef.current = 0;
        if (sseReconnectTimerRef.current !== null) {
          window.clearTimeout(sseReconnectTimerRef.current);
          sseReconnectTimerRef.current = null;
        }
        onConnect?.();

        // Connect WebSocket for commands
        connectWebSocket();
      };

      eventSource.onmessage = event => {
        try {
          const gameEvent: GameEvent = JSON.parse(event.data);
          logger.info('GameConnection', 'Received event', { event_type: gameEvent.event_type });
          setState(prev => ({ ...prev, lastEvent: gameEvent }));
          onEvent?.(gameEvent);
        } catch (error) {
          logger.error('GameConnection', 'Failed to parse SSE event', { error: String(error) });
        }
      };

      eventSource.onerror = error => {
        logger.error('GameConnection', 'Connection error', { error: String(error) });
        isConnectingRef.current = false;
        setState(prev => ({
          ...prev,
          sseConnected: false,
          isConnecting: false,
          error: 'Connection failed',
        }));
        onError?.('Connection failed');
        // Proactively close and schedule reconnect
        try {
          eventSource.close();
        } catch {
          logger.info('GameConnection', 'SSE close after error');
        }
        eventSourceRef.current = null;
        if (scheduleSseReconnectRef.current) {
          scheduleSseReconnectRef.current();
        }
      };
    } catch (error) {
      logger.error('GameConnection', 'Failed to connect', { error: String(error) });
      isConnectingRef.current = false;
      setState(prev => ({
        ...prev,
        sseConnected: false,
        isConnecting: false,
        error: 'Failed to connect',
      }));
      onError?.('Failed to connect');
      if (scheduleSseReconnectRef.current) {
        scheduleSseReconnectRef.current();
      }
    }
  }, [authToken, onConnect, onEvent, onError, state.isConnected, connectWebSocket]);

  // Store connect function in ref to avoid circular dependency
  connectRef.current = connect;

  const disconnect = useCallback(() => {
    logger.info('GameConnection', 'Disconnecting');

    if (eventSourceRef.current) {
      eventSourceRef.current.close();
      eventSourceRef.current = null;
    }

    if (websocketRef.current) {
      websocketRef.current.close();
      websocketRef.current = null;
    }

    clearTimers();
    sseAttemptsRef.current = 0;
    wsAttemptsRef.current = 0;
    isConnectingRef.current = false;
    setState(prev => ({
      ...prev,
      sseConnected: false,
      websocketConnected: false,
      isConnecting: false,
    }));

    onDisconnect?.();
  }, [onDisconnect, clearTimers]);

  const sendCommand = useCallback((command: string, args: string[] = []) => {
    if (!websocketRef.current || websocketRef.current.readyState !== WebSocket.OPEN) {
      logger.error('GameConnection', 'WebSocket not connected');
      return false;
    }

    try {
      const commandData = {
        type: 'command',
        data: {
          command,
          args,
        },
      };
      websocketRef.current.send(JSON.stringify(commandData));
      logger.info('GameConnection', 'Command sent', { command, args });
      return true;
    } catch (error) {
      logger.error('GameConnection', 'Failed to send command', { error: String(error) });
      return false;
    }
  }, []);

  // Update isConnected when both SSE and WebSocket are ready
  useEffect(() => {
    const bothConnected = state.sseConnected && state.websocketConnected;
    setState(prev => ({ ...prev, isConnected: bothConnected }));

    if (bothConnected) {
      logger.info('GameConnection', 'Both SSE and WebSocket connected');
    }
  }, [state.sseConnected, state.websocketConnected]);

  return {
    ...state,
    connect,
    disconnect,
    sendCommand,
  };
}
