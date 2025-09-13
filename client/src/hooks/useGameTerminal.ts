import { useCallback } from 'react';
import { useCommandStore, useConnectionStore, useGameStore, useSessionStore } from '../stores';

export interface GameTerminalState {
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

/**
 * Custom hook that manages the state and business logic for the GameTerminal component.
 * This hook extracts the complex state management logic from the component,
 * making it more testable and reusable.
 */
export const useGameTerminal = (): GameTerminalState => {
  // Get state from stores
  const connectionState = useConnectionStore();
  const gameState = useGameStore();
  const sessionState = useSessionStore();
  const commandState = useCommandStore();

  // Transform chat messages to match component interface
  const transformedMessages = gameState.chatMessages.map(msg => ({
    text: msg.text,
    timestamp: msg.timestamp,
    isHtml: msg.isHtml,
    isCompleteHtml: msg.isCompleteHtml,
    messageType: msg.type,
    aliasChain: msg.aliasChain,
  }));

  // Transform command history to simple string array
  const transformedCommandHistory = commandState.commandHistory.map(entry => entry.command);

  // Event handlers
  const onSendCommand = useCallback(
    (command: string) => {
      commandState.executeCommand(command);
    },
    [commandState]
  );

  const onSendChatMessage = useCallback(
    (message: string, channel: string) => {
      // This would typically send a chat message through the game connection
      // For now, we'll add it to the game log
      gameState.addGameLogEntry({
        text: message,
        timestamp: new Date().toISOString(),
        type: 'chat',
        channel,
        sender: sessionState.characterName || sessionState.playerName,
      });
    },
    [gameState, sessionState]
  );

  const onClearMessages = useCallback(() => {
    gameState.clearChatMessages();
  }, [gameState]);

  const onClearHistory = useCallback(() => {
    commandState.clearHistory();
  }, [commandState]);

  const onDownloadLogs = useCallback(() => {
    // This would typically trigger a download of the game logs
    // For now, we'll just log to console
    console.log('Downloading logs...', {
      chatMessages: gameState.chatMessages,
      gameLog: gameState.gameLog,
      commandHistory: commandState.commandHistory,
    });
  }, [gameState, commandState]);

  return {
    // Connection state
    isConnected: connectionState.isFullyConnected(),
    isConnecting: connectionState.isConnecting,
    error: connectionState.error,
    reconnectAttempts: connectionState.reconnectAttempts,

    // Session state
    playerName: sessionState.playerName,
    characterName: sessionState.characterName,
    isAuthenticated: sessionState.isAuthenticated,
    hasCharacter: sessionState.hasCharacter,

    // Game state
    player: gameState.player,
    room: gameState.room,
    messages: transformedMessages,
    commandHistory: transformedCommandHistory,

    // Event handlers
    onSendCommand,
    onSendChatMessage,
    onClearMessages,
    onClearHistory,
    onDownloadLogs,
  };
};
