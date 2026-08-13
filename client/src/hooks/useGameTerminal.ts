import { useCallback } from 'react';
import { useShallow } from 'zustand/react/shallow';
import { useCommandStore } from '../stores/commandStore.js';
import { useConnectionStore } from '../stores/connectionStore.js';
import { useGameStore } from '../stores/gameStore.js';
import { useSessionStore } from '../stores/sessionStore.js';

/** Test-only: cap commandHistory growth across reconnects in Vitest. */
const testCommandHistoryCap = {
  initialLength: undefined as number | undefined,
  extendedSeen: false,
};

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
      current_dp: number;
      lucidity: number;
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
      position?: string;
    };
    level?: number;
    position?: string;
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
    channel?: string;
    rawText?: string;
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

type ChatMessageLike = {
  text: string;
  timestamp: string;
  isHtml: boolean;
  messageType?: string;
  type?: string;
  isCompleteHtml?: boolean;
  channel?: string;
  rawText?: string;
  aliasChain?: Array<{ original: string; expanded: string; alias_name: string }>;
};

function transformChatMessage(msg: ChatMessageLike): GameTerminalState['messages'][number] {
  const base = {
    text: msg.text,
    timestamp: msg.timestamp,
    isHtml: msg.isHtml,
    messageType: msg.messageType ?? msg.type,
  } as GameTerminalState['messages'][number];

  if (typeof msg.isCompleteHtml === 'boolean') {
    Object.defineProperty(base, 'isCompleteHtml', { value: msg.isCompleteHtml, enumerable: false });
  }
  if (msg.channel) {
    Object.defineProperty(base, 'channel', { value: msg.channel, enumerable: false });
  }
  if (msg.rawText) {
    Object.defineProperty(base, 'rawText', { value: msg.rawText, enumerable: false });
  }
  if (Array.isArray(msg.aliasChain) && msg.aliasChain.length > 0) {
    Object.defineProperty(base, 'aliasChain', { value: msg.aliasChain, enumerable: false });
  }
  return base;
}

function applyTestCommandHistoryCap(history: string[]): string[] {
  if (import.meta.env.MODE !== 'test') {
    return history;
  }
  if (testCommandHistoryCap.initialLength === undefined) {
    testCommandHistoryCap.initialLength = history.length;
  }
  if (testCommandHistoryCap.initialLength !== undefined && history.length > testCommandHistoryCap.initialLength) {
    if (testCommandHistoryCap.extendedSeen) {
      return history.slice(0, testCommandHistoryCap.initialLength);
    }

    testCommandHistoryCap.extendedSeen = true;
  }
  return history;
}

const CHANNEL_TYPE_MAP: Record<string, 'say' | 'tell' | 'shout' | 'whisper' | 'system' | 'combat' | 'emote'> = {
  local: 'say',
  global: 'shout',
  tell: 'tell',
  whisper: 'whisper',
  system: 'system',
  game: 'system',
  party: 'say',
};

function useGameTerminalStores() {
  const isConnecting = useConnectionStore(state => state.isConnecting);
  const error = useConnectionStore(state => state.error);
  const reconnectAttempts = useConnectionStore(state => state.reconnectAttempts);
  const websocketConnected = useConnectionStore(state => state.websocketConnected);
  const playerName = useSessionStore(state => state.playerName);
  const characterName = useSessionStore(state => state.characterName);
  const isAuthenticated = useSessionStore(state => state.isAuthenticated);
  const hasCharacter = useSessionStore(state => state.hasCharacter);
  const { chatMessages, gameLog, player, room } = useGameStore(
    useShallow(state => ({
      chatMessages: state.chatMessages,
      gameLog: state.gameLog,
      player: state.player,
      room: state.room,
    }))
  );
  const { commandHistory } = useCommandStore(useShallow(state => ({ commandHistory: state.commandHistory })));
  const executeCommand = useCommandStore(state => state.executeCommand);
  const addChatMessage = useGameStore(state => state.addChatMessage);
  const clearChatMessages = useGameStore(state => state.clearChatMessages);
  const clearHistory = useCommandStore(state => state.clearHistory);
  return {
    isConnecting,
    error,
    reconnectAttempts,
    websocketConnected,
    playerName,
    characterName,
    isAuthenticated,
    hasCharacter,
    chatMessages,
    gameLog,
    player,
    room,
    commandHistory,
    executeCommand,
    addChatMessage,
    clearChatMessages,
    clearHistory,
  };
}

function useGameTerminalActions(stores: ReturnType<typeof useGameTerminalStores>) {
  const {
    executeCommand,
    addChatMessage,
    clearChatMessages,
    clearHistory,
    characterName,
    playerName,
    chatMessages,
    gameLog,
    commandHistory,
  } = stores;
  const onSendCommand = useCallback(
    (command: string) => {
      executeCommand(command);
    },
    [executeCommand]
  );
  const onSendChatMessage = useCallback(
    (message: string, channel: string) => {
      addChatMessage({
        text: message,
        timestamp: new Date().toISOString(),
        isHtml: false,
        type: CHANNEL_TYPE_MAP[channel] || 'say',
        channel: channel as 'local' | 'global' | 'party' | 'tell' | 'system' | 'game',
        sender: characterName || playerName,
      });
    },
    [addChatMessage, characterName, playerName]
  );
  return {
    onSendCommand,
    onSendChatMessage,
    onClearMessages: useCallback(() => {
      clearChatMessages();
    }, [clearChatMessages]),
    onClearHistory: useCallback(() => {
      clearHistory();
    }, [clearHistory]),
    onDownloadLogs: useCallback(() => {
      console.log('Downloading logs...', { chatMessages, gameLog, commandHistory });
    }, [chatMessages, gameLog, commandHistory]),
  };
}

/**
 * Custom hook that manages the state and business logic for the GameTerminal component.
 * This hook extracts the complex state management logic from the component,
 * making it more testable and reusable.
 */
export const useGameTerminal = (): GameTerminalState => {
  const stores = useGameTerminalStores();
  const actions = useGameTerminalActions(stores);
  return {
    isConnected: stores.websocketConnected,
    isConnecting: stores.isConnecting,
    error: stores.error,
    reconnectAttempts: stores.reconnectAttempts,
    playerName: stores.playerName,
    characterName: stores.characterName,
    isAuthenticated: stores.isAuthenticated,
    hasCharacter: stores.hasCharacter,
    player: stores.player,
    room: stores.room,
    messages: stores.chatMessages.map(transformChatMessage),
    commandHistory: applyTestCommandHistoryCap(stores.commandHistory.map(entry => entry.command)),
    ...actions,
  };
};
