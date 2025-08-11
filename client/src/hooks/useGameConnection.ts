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
  playerId: string;
  playerName: string;
  authToken: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
}

export function useGameConnection({
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  playerId,
  playerName,
  authToken,
  onEvent,
  onConnect,
  onError,
  onDisconnect,
}: UseGameConnectionOptions) {
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
    const attempt = sseAttemptsRef.current;
    const delay = Math.min(1000 * Math.pow(2, attempt), 30000);
    logger.info('GameConnection', `Scheduling SSE reconnect in ${delay}ms (attempt ${attempt + 1})`);
    sseReconnectTimerRef.current = window.setTimeout(() => {
      sseAttemptsRef.current += 1;
      connect();
    }, delay);
  }, [connect]);

  const scheduleWsReconnect = useCallback(() => {
    const attempt = wsAttemptsRef.current;
    const delay = Math.min(1000 * Math.pow(2, attempt), 30000);
    logger.info('GameConnection', `Scheduling WS reconnect in ${delay}ms (attempt ${attempt + 1})`);
    wsReconnectTimerRef.current = window.setTimeout(() => {
      wsAttemptsRef.current += 1;
      connectWebSocket();
    }, delay);
  }, [connectWebSocket]);

  // Connect WebSocket for commands after SSE connection is established
  const connectWebSocket = useCallback(() => {
    if (!authToken || !playerName) {
      logger.error('GameConnection', 'Missing auth token or player name for WebSocket');
      return;
    }

    try {
      // WebSocket endpoint uses JWT token; server resolves user_id -> player_id
      const wsUrl = `ws://localhost:54731/api/ws?token=${encodeURIComponent(authToken)}`;
      const websocket = new WebSocket(wsUrl);

      websocketRef.current = websocket;

      websocket.onopen = () => {
        logger.info('GameConnection', 'WebSocket connected');
        setState(prev => ({ ...prev, websocketConnected: true }));
        // Reset WS backoff attempts
        wsAttemptsRef.current = 0;
        if (wsReconnectTimerRef.current !== null) {
          window.clearTimeout(wsReconnectTimerRef.current);
          wsReconnectTimerRef.current = null;
        }
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
          scheduleWsReconnect();
        }
      };
    } catch (error) {
      logger.error('GameConnection', 'Failed to connect WebSocket', { error: String(error) });
      scheduleWsReconnect();
    }
  }, [authToken, playerName, onEvent, scheduleWsReconnect, state.sseConnected]);

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
          logger.error('GameConnection', 'Failed to parse event', { error: String(error) });
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
        scheduleSseReconnect();
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
      scheduleSseReconnect();
    }
  }, [authToken, onConnect, onEvent, onError, state.isConnected, connectWebSocket, scheduleSseReconnect]);

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
