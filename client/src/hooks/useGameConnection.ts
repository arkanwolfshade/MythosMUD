import { useCallback, useEffect, useReducer, useRef } from 'react';
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

type GameConnectionAction =
  | { type: 'SET_CONNECTING'; payload: boolean }
  | { type: 'SET_SSE_CONNECTED'; payload: boolean }
  | { type: 'SET_WEBSOCKET_CONNECTED'; payload: boolean }
  | { type: 'SET_ERROR'; payload: string | null }
  | { type: 'SET_LAST_EVENT'; payload: GameEvent }
  | { type: 'INCREMENT_RECONNECT_ATTEMPTS' }
  | { type: 'RESET_RECONNECT_ATTEMPTS' }
  | { type: 'RESET_STATE' };

const initialState: GameConnectionState = {
  isConnected: false,
  isConnecting: false,
  lastEvent: null,
  error: null,
  reconnectAttempts: 0,
  sseConnected: false,
  websocketConnected: false,
};

function gameConnectionReducer(state: GameConnectionState, action: GameConnectionAction): GameConnectionState {
  switch (action.type) {
    case 'SET_CONNECTING':
      return { ...state, isConnecting: action.payload };
    case 'SET_SSE_CONNECTED': {
      const newSseState = {
        ...state,
        sseConnected: action.payload,
        // CRITICAL FIX: Connection is established if either SSE OR WebSocket is connected
        isConnected: action.payload || state.websocketConnected,
        error: action.payload ? null : state.error,
      };
      console.error('🚨 CRITICAL DEBUG: SSE_CONNECTED reducer', {
        action: action.type,
        payload: action.payload,
        oldSseConnected: state.sseConnected,
        oldWebsocketConnected: state.websocketConnected,
        oldIsConnected: state.isConnected,
        newSseConnected: newSseState.sseConnected,
        newWebsocketConnected: newSseState.websocketConnected,
        newIsConnected: newSseState.isConnected,
      });
      return newSseState;
    }
    case 'SET_WEBSOCKET_CONNECTED': {
      const newWsState = {
        ...state,
        websocketConnected: action.payload,
        // CRITICAL FIX: Connection is established if either SSE OR WebSocket is connected
        isConnected: action.payload || state.sseConnected,
        error: action.payload ? null : state.error,
      };
      console.error('🚨 CRITICAL DEBUG: WEBSOCKET_CONNECTED reducer', {
        action: action.type,
        payload: action.payload,
        oldSseConnected: state.sseConnected,
        oldWebsocketConnected: state.websocketConnected,
        oldIsConnected: state.isConnected,
        newSseConnected: newWsState.sseConnected,
        newWebsocketConnected: newWsState.websocketConnected,
        newIsConnected: newWsState.isConnected,
        willUpdateIsConnected: action.payload || state.sseConnected,
      });
      return newWsState;
    }
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    case 'SET_LAST_EVENT':
      return { ...state, lastEvent: action.payload };
    case 'INCREMENT_RECONNECT_ATTEMPTS':
      return { ...state, reconnectAttempts: state.reconnectAttempts + 1 };
    case 'RESET_RECONNECT_ATTEMPTS':
      return { ...state, reconnectAttempts: 0 };
    case 'RESET_STATE':
      return { ...initialState };
    default:
      return state;
  }
}

interface UseGameConnectionOptions {
  playerId?: string;
  playerName: string;
  authToken: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
}

export function useGameConnection({ authToken, onEvent, onConnect, onError, onDisconnect }: UseGameConnectionOptions) {
  // CRITICAL DEBUG: Log when hook is called
  console.error('🚨 CRITICAL DEBUG: useGameConnection hook CALLED', {
    hasAuthToken: !!authToken,
    authTokenLength: authToken?.length || 0,
    playerName: 'unknown',
    timestamp: new Date().toISOString(),
  });

  const [state, dispatch] = useReducer(gameConnectionReducer, initialState);

  // Refs for stable references
  const eventSourceRef = useRef<EventSource | null>(null);
  const websocketRef = useRef<WebSocket | null>(null);
  const wsPingIntervalRef = useRef<number | null>(null);
  const sseReconnectTimerRef = useRef<number | null>(null);
  const wsReconnectTimerRef = useRef<number | null>(null);
  const sseAttemptsRef = useRef(0);
  const wsAttemptsRef = useRef(0);
  const isConnectingRef = useRef(false);
  const hasConnectedRef = useRef(false);

  // Stable callback references
  const onEventRef = useRef(onEvent);
  const onConnectRef = useRef(onConnect);
  const onDisconnectRef = useRef(onDisconnect);
  const onErrorRef = useRef(onError);

  // Update refs when callbacks change
  useEffect(() => {
    onEventRef.current = onEvent;
    onConnectRef.current = onConnect;
    onDisconnectRef.current = onDisconnect;
    onErrorRef.current = onError;
  }, [onEvent, onConnect, onDisconnect, onError]);

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
    const baseDelay = 1000;
    const maxDelay = 30000;

    if (sseAttemptsRef.current >= maxAttempts) {
      logger.error('GameConnection', 'Max SSE reconnect attempts reached');
      dispatch({ type: 'SET_ERROR', payload: 'Max reconnect attempts reached' });
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
        // Trigger reconnect through the main connect function
        hasConnectedRef.current = false;
      }
    }, delay);
  }, [state.isConnected]);

  const scheduleWsReconnect = useCallback(() => {
    if (wsReconnectTimerRef.current !== null) {
      return; // Already scheduled
    }

    const maxAttempts = 5;
    const baseDelay = 1000;
    const maxDelay = 30000;

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
        // Trigger WebSocket reconnect
        connectWebSocket();
      }
    }, delay);
  }, [state.sseConnected, state.websocketConnected]); // eslint-disable-line react-hooks/exhaustive-deps

  const connectWebSocket = useCallback(() => {
    if (websocketRef.current) {
      logger.info('GameConnection', 'WebSocket already connected');
      return;
    }

    try {
      logger.info('GameConnection', 'Connecting WebSocket');
      // Fix: Connect directly to game server for WebSocket (Vite proxy cannot handle WebSocket)
      // The game server runs on port 54731, not through the Vite dev server proxy
      const wsUrl = `ws://localhost:54731/api/ws?token=${encodeURIComponent(authToken)}`;
      logger.info('GameConnection', 'Creating WebSocket connection', { url: wsUrl });
      const websocket = new WebSocket(wsUrl);

      websocket.onopen = () => {
        logger.info('GameConnection', 'WebSocket connected');
        websocketRef.current = websocket;
        dispatch({ type: 'SET_WEBSOCKET_CONNECTED', payload: true });
        wsAttemptsRef.current = 0;

        // Start periodic ping
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
          dispatch({ type: 'SET_LAST_EVENT', payload: gameEvent });

          // Add simple debugging for ALL events to see what we're receiving
          console.log('🚨 DEBUG: useGameConnection received event', {
            eventType: gameEvent.event_type,
            hasOnEventRef: !!onEventRef.current,
          });

          // Add simple debugging to verify onEvent callback is called
          console.log('🚨 DEBUG: About to call onEvent callback', {
            eventType: gameEvent.event_type,
            hasCallback: !!onEventRef.current,
          });

          onEventRef.current?.(gameEvent);

          // Add debugging after callback to verify it was called
          console.log('🚨 DEBUG: onEvent callback completed', {
            eventType: gameEvent.event_type,
          });
        } catch (error) {
          logger.error('GameConnection', 'Failed to parse WebSocket event', { error: String(error) });
        }
      };

      websocket.onerror = error => {
        logger.error('GameConnection', 'WebSocket error', { error: String(error) });
      };

      websocket.onclose = event => {
        logger.info('GameConnection', 'WebSocket disconnected', {
          code: event.code,
          reason: event.reason,
          wasClean: event.wasClean,
        });
        websocketRef.current = null;
        dispatch({ type: 'SET_WEBSOCKET_CONNECTED', payload: false });
        if (wsPingIntervalRef.current !== null) {
          window.clearInterval(wsPingIntervalRef.current);
          wsPingIntervalRef.current = null;
        }
        // CRITICAL FIX: Only attempt reconnection if SSE is still connected
        // This prevents infinite reconnection loops
        if (state.sseConnected) {
          logger.info('GameConnection', 'SSE still connected, scheduling WebSocket reconnection');
          scheduleWsReconnect();
        } else {
          logger.warning('GameConnection', 'Both SSE and WebSocket disconnected, not attempting reconnection');
        }
      };
    } catch (error) {
      logger.error('GameConnection', 'Failed to connect WebSocket', { error: String(error) });
      scheduleWsReconnect();
    }
  }, [authToken, scheduleWsReconnect, state.sseConnected]);

  const connect = useCallback(async () => {
    // CRITICAL DEBUG: Log when connect function is called
    console.error('🚨 CRITICAL DEBUG: connect function CALLED', {
      hasAuthToken: !!authToken,
      authTokenLength: authToken?.length || 0,
      isConnecting: isConnectingRef.current,
      isConnected: state.isConnected,
      timestamp: new Date().toISOString(),
    });

    if (isConnectingRef.current || state.isConnected) {
      logger.info('GameConnection', 'Already connecting or connected');
      return;
    }

    isConnectingRef.current = true;
    dispatch({ type: 'SET_CONNECTING', payload: true });

    try {
      logger.info('GameConnection', 'Connecting to game server', { authToken: authToken ? 'present' : 'missing' });

      // Close any existing connection
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
        eventSourceRef.current = null;
      }

      const sseUrl = `/api/events?token=${encodeURIComponent(authToken)}`;
      logger.info('GameConnection', 'Creating SSE connection', { url: sseUrl });
      const eventSource = new EventSource(sseUrl);

      eventSourceRef.current = eventSource;

      eventSource.onopen = () => {
        logger.info('GameConnection', 'SSE connection established');
        isConnectingRef.current = false;
        dispatch({ type: 'SET_SSE_CONNECTED', payload: true });
        dispatch({ type: 'SET_CONNECTING', payload: false });
        sseAttemptsRef.current = 0;
        if (sseReconnectTimerRef.current !== null) {
          window.clearTimeout(sseReconnectTimerRef.current);
          sseReconnectTimerRef.current = null;
        }
        onConnectRef.current?.();
        connectWebSocket();
      };

      eventSource.onmessage = event => {
        try {
          const gameEvent: GameEvent = JSON.parse(event.data);
          logger.info('GameConnection', 'Received event', { event_type: gameEvent.event_type });
          dispatch({ type: 'SET_LAST_EVENT', payload: gameEvent });
          onEventRef.current?.(gameEvent);
        } catch (error) {
          logger.error('GameConnection', 'Failed to parse SSE event', { error: String(error) });
        }
      };

      eventSource.onerror = error => {
        logger.error('GameConnection', 'SSE connection error', { error: String(error) });
        isConnectingRef.current = false;
        dispatch({ type: 'SET_SSE_CONNECTED', payload: false });
        dispatch({ type: 'SET_CONNECTING', payload: false });
        dispatch({ type: 'SET_ERROR', payload: 'Connection failed' });
        onErrorRef.current?.('Connection failed');
        try {
          eventSource.close();
        } catch {
          logger.info('GameConnection', 'SSE close after error');
        }
        eventSourceRef.current = null;
        scheduleSseReconnect();
      };

      // CRITICAL FIX: Connect WebSocket immediately after SSE attempt
      // Don't wait for SSE to succeed - this restores multiplayer functionality
      logger.info('GameConnection', 'Connecting WebSocket immediately after SSE attempt');
      connectWebSocket();
    } catch (error) {
      logger.error('GameConnection', 'Failed to connect', { error: String(error) });
      isConnectingRef.current = false;
      dispatch({ type: 'SET_SSE_CONNECTED', payload: false });
      dispatch({ type: 'SET_CONNECTING', payload: false });
      dispatch({ type: 'SET_ERROR', payload: 'Failed to connect' });
      onErrorRef.current?.('Failed to connect');
      scheduleSseReconnect();
    }
  }, [authToken, connectWebSocket, scheduleSseReconnect, state.isConnected]); // Include all dependencies

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
    hasConnectedRef.current = false;
    dispatch({ type: 'RESET_STATE' });
    onDisconnectRef.current?.();
  }, [clearTimers]);

  const sendCommand = useCallback((command: string, args: string[] = []) => {
    // CRITICAL FIX: Enhanced connection validation
    if (!websocketRef.current) {
      logger.error('GameConnection', 'WebSocket reference not available');
      return false;
    }

    if (websocketRef.current.readyState !== WebSocket.OPEN) {
      logger.error('GameConnection', 'WebSocket not in OPEN state', {
        readyState: websocketRef.current.readyState,
        readyStateText: ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'][websocketRef.current.readyState],
      });
      return false;
    }

    try {
      const commandData = {
        type: 'game_command', // CRITICAL FIX: Use correct message type
        command,
        args,
      };
      websocketRef.current.send(JSON.stringify(commandData));
      logger.info('GameConnection', 'Command sent', { command, args });
      return true;
    } catch (error) {
      logger.error('GameConnection', 'Failed to send command', { error: String(error) });
      // CRITICAL FIX: Mark WebSocket as disconnected if send fails
      dispatch({ type: 'SET_WEBSOCKET_CONNECTED', payload: false });
      return false;
    }
  }, []);

  // Auto-reconnect logic
  useEffect(() => {
    if (!hasConnectedRef.current && !state.isConnected && !state.isConnecting && !isConnectingRef.current) {
      hasConnectedRef.current = true;
      connect();
    }
  }, [connect, state.isConnected, state.isConnecting]); // Include all dependencies

  return {
    ...state,
    connect,
    disconnect,
    sendCommand,
  };
}
