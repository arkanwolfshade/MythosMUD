import { useCallback, useEffect, useRef, useState } from 'react';

interface GameEvent {
  event_type: string;
  timestamp: string;
  sequence_number: number;
  player_id?: string;
  room_id?: string;
  data: Record<string, any>;
}

interface GameConnectionState {
  isConnected: boolean;
  isConnecting: boolean;
  lastEvent: GameEvent | null;
  error: string | null;
  reconnectAttempts: number;
}

interface UseGameConnectionOptions {
  playerId: string;
  authToken: string;
  onEvent?: (event: GameEvent) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
  onError?: (error: string) => void;
  autoReconnect?: boolean;
  maxReconnectAttempts?: number;
}

export function useGameConnection({
  playerId,
  authToken,
  onEvent,
  onConnect,
  onDisconnect,
  onError,
  autoReconnect = true,
  maxReconnectAttempts = 5,
}: UseGameConnectionOptions) {
  const [state, setState] = useState<GameConnectionState>({
    isConnected: false,
    isConnecting: false,
    lastEvent: null,
    error: null,
    reconnectAttempts: 0,
  });

  const eventSourceRef = useRef<EventSource | null>(null);
  const websocketRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const reconnectAttemptsRef = useRef(0);

  const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  // Connect to SSE stream for game state updates
  const connectSSE = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
    }

    setState(prev => ({ ...prev, isConnecting: true, error: null }));

    const eventSource = new EventSource(
      `${baseUrl}/events/${playerId}`,
      {
        headers: {
          'Authorization': `Bearer ${authToken}`,
        },
      }
    );

    eventSource.onopen = () => {
      setState(prev => ({ 
        ...prev, 
        isConnected: true, 
        isConnecting: false,
        reconnectAttempts: 0 
      }));
      reconnectAttemptsRef.current = 0;
      onConnect?.();
    };

    eventSource.onmessage = (event) => {
      try {
        const gameEvent: GameEvent = JSON.parse(event.data);
        setState(prev => ({ ...prev, lastEvent: gameEvent }));
        onEvent?.(gameEvent);
      } catch (error) {
        console.error('Failed to parse SSE event:', error);
        setState(prev => ({ 
          ...prev, 
          error: 'Failed to parse game event' 
        }));
        onError?.('Failed to parse game event');
      }
    };

    eventSource.onerror = (error) => {
      console.error('SSE connection error:', error);
      setState(prev => ({ 
        ...prev, 
        isConnected: false, 
        isConnecting: false,
        error: 'SSE connection failed'
      }));
      onError?.('SSE connection failed');
      
      if (autoReconnect && reconnectAttemptsRef.current < maxReconnectAttempts) {
        reconnectAttemptsRef.current++;
        setState(prev => ({ 
          ...prev, 
          reconnectAttempts: reconnectAttemptsRef.current 
        }));
        
        reconnectTimeoutRef.current = setTimeout(() => {
          connectSSE();
        }, Math.min(1000 * Math.pow(2, reconnectAttemptsRef.current), 30000));
      }
    };

    eventSourceRef.current = eventSource;
  }, [playerId, authToken, baseUrl, onEvent, onConnect, onError, autoReconnect, maxReconnectAttempts]);

  // Connect to WebSocket for interactive commands
  const connectWebSocket = useCallback(() => {
    if (websocketRef.current) {
      websocketRef.current.close();
    }

    const wsUrl = `${baseUrl.replace('http', 'ws')}/ws/${playerId}`;
    const websocket = new WebSocket(wsUrl);

    websocket.onopen = () => {
      console.log('WebSocket connected');
    };

    websocket.onmessage = (event) => {
      try {
        const gameEvent: GameEvent = JSON.parse(event.data);
        setState(prev => ({ ...prev, lastEvent: gameEvent }));
        onEvent?.(gameEvent);
      } catch (error) {
        console.error('Failed to parse WebSocket message:', error);
      }
    };

    websocket.onerror = (error) => {
      console.error('WebSocket error:', error);
      setState(prev => ({ 
        ...prev, 
        error: 'WebSocket connection failed' 
      }));
    };

    websocket.onclose = () => {
      console.log('WebSocket disconnected');
    };

    websocketRef.current = websocket;
  }, [playerId, baseUrl, onEvent]);

  // Send command via WebSocket
  const sendCommand = useCallback((command: string, args: string[] = []) => {
    if (websocketRef.current?.readyState === WebSocket.OPEN) {
      const message = {
        command,
        args,
        timestamp: new Date().toISOString(),
      };
      websocketRef.current.send(JSON.stringify(message));
      return true;
    } else {
      setState(prev => ({ 
        ...prev, 
        error: 'WebSocket not connected' 
      }));
      return false;
    }
  }, []);

  // Connect to both SSE and WebSocket
  const connect = useCallback(() => {
    connectSSE();
    connectWebSocket();
  }, [connectSSE, connectWebSocket]);

  // Disconnect from both connections
  const disconnect = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
      eventSourceRef.current = null;
    }
    
    if (websocketRef.current) {
      websocketRef.current.close();
      websocketRef.current = null;
    }
    
    if (reconnectTimeoutRef.current) {
      clearTimeout(reconnectTimeoutRef.current);
      reconnectTimeoutRef.current = null;
    }
    
    setState(prev => ({ 
      ...prev, 
      isConnected: false, 
      isConnecting: false,
      reconnectAttempts: 0 
    }));
    reconnectAttemptsRef.current = 0;
    onDisconnect?.();
  }, [onDisconnect]);

  // Auto-connect on mount
  useEffect(() => {
    if (playerId && authToken) {
      connect();
    }
    
    return () => {
      disconnect();
    };
  }, [playerId, authToken, connect, disconnect]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      disconnect();
    };
  }, [disconnect]);

  return {
    ...state,
    connect,
    disconnect,
    sendCommand,
  };
} 