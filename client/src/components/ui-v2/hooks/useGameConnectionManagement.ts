// Game connection management hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback, useEffect, useRef } from 'react';
import { logger } from '../../../utils/logger';
import { useGameConnection } from '../../../hooks/useGameConnectionRefactored';
import type { GameEvent } from '../eventHandlers/types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import type { ChatMessage } from '../types';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseGameConnectionManagementParams {
  authToken: string;
  playerName: string;
  onLogout?: () => void;
  onGameEvent: (event: GameEvent) => void;
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
}

export const useGameConnectionManagement = ({
  authToken,
  playerName,
  onLogout,
  onGameEvent,
  setGameState,
}: UseGameConnectionManagementParams) => {
  const hasAttemptedConnection = useRef(false);

  const handleConnectionLoss = useCallback(() => {
    logger.info('GameClientV2Container', 'Connection lost, triggering logout flow');
    const connectionLostMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'Connection to server lost. Returning to login screen...',
      timestamp: new Date().toISOString(),
      messageType: 'system',
      isHtml: false,
    });

    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, connectionLostMessage],
    }));

    setTimeout(() => {
      if (onLogout) {
        onLogout();
      }
    }, 1000);
  }, [onLogout, setGameState]);

  const handleConnect = useCallback(() => {
    logger.info('GameClientV2Container', 'Connected to game server');
  }, []);

  const handleDisconnect = useCallback(() => {
    logger.info('GameClientV2Container', 'Disconnected from game server');
  }, []);

  const handleError = useCallback((error: string) => {
    logger.error('GameClientV2Container', 'Game connection error', { error });
  }, []);

  const {
    isConnected,
    isConnecting,
    error,
    reconnectAttempts,
    connect,
    disconnect: disconnectFn,
    sendCommand,
  } = useGameConnection({
    authToken,
    onEvent: onGameEvent,
    onConnect: handleConnect,
    onDisconnect: handleDisconnect,
    onError: handleError,
  });

  useEffect(() => {
    if (!isConnected && !isConnecting && reconnectAttempts >= 5) {
      logger.warn('GameClientV2Container', 'All reconnection attempts failed, triggering logout');
      handleConnectionLoss();
    }
  }, [isConnected, isConnecting, reconnectAttempts, handleConnectionLoss]);

  useEffect(() => {
    if (!hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameClientV2Container', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
      });
      connect();
    }

    return () => {
      logger.info('GameClientV2Container', 'Cleaning up connection on unmount');
      disconnectFn();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return {
    isConnected,
    isConnecting,
    error,
    reconnectAttempts,
    sendCommand,
    disconnect: disconnectFn,
  };
};
