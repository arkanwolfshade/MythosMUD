import React, { createContext, ReactNode, useContext } from 'react';
import { useGameTerminal } from '../hooks/useGameTerminal';

// Context type definition
interface GameTerminalContextType {
  // Connection state
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;

  // Session state
  playerName: string;
  characterName: string;
  isAuthenticated: boolean;
  hasCharacter: boolean;

  // Game state
  player: {
    id: string;
    name: string;
    stats: {
      current_health: number;
      sanity: number;
      strength?: number;
      dexterity?: number;
      constitution?: number;
      intelligence?: number;
      wisdom?: number;
      charisma?: number;
      occult_knowledge?: number;
      fear?: number;
      corruption?: number;
      cult_affiliation?: number;
    };
    level?: number;
  } | null;
  room: {
    id: string;
    name: string;
    description: string;
    plane?: string;
    zone?: string;
    sub_zone?: string;
    environment?: string;
    exits: Record<string, string>;
    occupants?: string[];
    occupant_count?: number;
    entities?: Array<{
      name: string;
      type: string;
    }>;
  } | null;
  messages: Array<{
    text: string;
    timestamp: string;
    isHtml: boolean;
    isCompleteHtml?: boolean;
    messageType?: string;
    aliasChain?: Array<{
      original: string;
      expanded: string;
      alias_name: string;
    }>;
  }>;
  commandHistory: string[];

  // Event handlers
  onSendCommand: (command: string) => void;
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages: () => void;
  onClearHistory: () => void;
  onDownloadLogs: () => void;
}

// Create the context
const GameTerminalContext = createContext<GameTerminalContextType | null>(null);

// Context provider component
interface GameTerminalProviderProps {
  children: ReactNode;
}

export const GameTerminalProvider: React.FC<GameTerminalProviderProps> = ({ children }) => {
  const gameTerminalState = useGameTerminal();

  return <GameTerminalContext.Provider value={gameTerminalState}>{children}</GameTerminalContext.Provider>;
};

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
    player: context.player,
    room: context.room,
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
