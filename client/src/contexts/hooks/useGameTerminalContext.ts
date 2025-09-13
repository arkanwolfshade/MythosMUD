import { useContext } from 'react';
import { GameTerminalContext, GameTerminalContextType } from '../GameTerminalContext';

// Hook to use the context
export const useGameTerminalContext = (): GameTerminalContextType => {
  const context = useContext(GameTerminalContext);
  if (!context) {
    throw new Error('useGameTerminalContext must be used within a GameTerminalProvider');
  }
  return context;
};

// Convenience hooks for specific parts of the context
export const useConnectionState = () => {
  const context = useGameTerminalContext();
  return {
    isConnected: context.isConnected,
    isConnecting: context.isConnecting,
    error: context.error,
    reconnectAttempts: context.reconnectAttempts,
  };
};

export const useSessionState = () => {
  const context = useGameTerminalContext();
  return {
    playerName: context.playerName,
    characterName: context.characterName,
    isAuthenticated: context.isAuthenticated,
    hasCharacter: context.hasCharacter,
  };
};

export const useGameState = () => {
  const context = useGameTerminalContext();
  return {
    room: context.room,
    player: context.player,
    messages: context.messages,
    commandHistory: context.commandHistory,
  };
};

export const useGameActions = () => {
  const context = useGameTerminalContext();
  return {
    onSendCommand: context.onSendCommand,
    onSendChatMessage: context.onSendChatMessage,
    onClearMessages: context.onClearMessages,
    onClearHistory: context.onClearHistory,
    onDownloadLogs: context.onDownloadLogs,
  };
};
