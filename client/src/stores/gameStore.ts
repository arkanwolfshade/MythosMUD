import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

export interface Player {
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
  inventory?: Array<{
    id: string;
    name: string;
    type: string;
    [key: string]: unknown;
  }>;
}

export interface Room {
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
    id: string;
    name: string;
    type: string;
    [key: string]: unknown;
  }>;
}

export interface ChatMessage {
  id?: string;
  text: string;
  timestamp: string;
  isHtml: boolean;
  type: 'say' | 'tell' | 'shout' | 'whisper' | 'system' | 'combat' | 'emote';
  channel: 'local' | 'global' | 'party' | 'tell' | 'system' | 'game';
  sender?: string;
  target?: string;
  [key: string]: unknown;
}

export interface GameLogEntry {
  id?: string;
  text: string;
  timestamp: string;
  isHtml: boolean;
  type: 'system' | 'combat' | 'action' | 'error' | 'info';
  [key: string]: unknown;
}

export interface GameState {
  // Core game data
  player: Player | null;
  room: Room | null;
  chatMessages: ChatMessage[];
  gameLog: GameLogEntry[];

  // UI state
  isLoading: boolean;
  lastUpdate: number | null;
}

export interface GameActions {
  // Player management
  setPlayer: (player: Player | null) => void;
  updatePlayerStats: (stats: Partial<Player['stats']>) => void;
  clearPlayer: () => void;

  // Room management
  setRoom: (room: Room | null) => void;
  updateRoomOccupants: (occupants: string[]) => void;
  clearRoom: () => void;

  // Chat messages
  addChatMessage: (message: ChatMessage) => void;
  clearChatMessages: () => void;

  // Game log
  addGameLogEntry: (entry: GameLogEntry) => void;
  clearGameLog: () => void;

  // UI state
  setLoading: (loading: boolean) => void;
  updateLastUpdate: (timestamp: number) => void;

  // State management
  reset: () => void;
}

export interface GameSelectors {
  // Computed properties
  getPlayerStats: () => Player['stats'] | null;
  getRoomOccupantsCount: () => number;
  getRecentChatMessages: (count: number) => ChatMessage[];
  getRecentGameLogEntries: (count: number) => GameLogEntry[];
}

type GameStore = GameState & GameActions & GameSelectors;

const MAX_CHAT_MESSAGES = 100;
const MAX_GAME_LOG_ENTRIES = 100;

const createInitialState = (): GameState => ({
  player: null,
  room: null,
  chatMessages: [],
  gameLog: [],
  isLoading: false,
  lastUpdate: null,
});

export const useGameStore = create<GameStore>()(
  devtools(
    (set, get) => ({
      ...createInitialState(),

      // Player management actions
      setPlayer: (player: Player | null) => set({ player, lastUpdate: Date.now() }, false, 'setPlayer'),

      updatePlayerStats: (stats: Partial<Player['stats']>) =>
        set(
          state => ({
            player: state.player ? { ...state.player, stats: { ...state.player.stats, ...stats } } : null,
            lastUpdate: Date.now(),
          }),
          false,
          'updatePlayerStats'
        ),

      clearPlayer: () => set({ player: null, lastUpdate: Date.now() }, false, 'clearPlayer'),

      // Room management actions
      setRoom: (room: Room | null) => set({ room, lastUpdate: Date.now() }, false, 'setRoom'),

      updateRoomOccupants: (occupants: string[]) =>
        set(
          state => ({
            room: state.room ? { ...state.room, occupants, occupant_count: occupants.length } : null,
            lastUpdate: Date.now(),
          }),
          false,
          'updateRoomOccupants'
        ),

      clearRoom: () => set({ room: null, lastUpdate: Date.now() }, false, 'clearRoom'),

      // Chat messages actions
      addChatMessage: (message: ChatMessage) =>
        set(
          state => {
            const newMessages = [...state.chatMessages, message];
            // Limit the number of messages to prevent memory issues
            const limitedMessages = newMessages.slice(-MAX_CHAT_MESSAGES);
            return {
              chatMessages: limitedMessages,
              lastUpdate: Date.now(),
            };
          },
          false,
          'addChatMessage'
        ),

      clearChatMessages: () => set({ chatMessages: [], lastUpdate: Date.now() }, false, 'clearChatMessages'),

      // Game log actions
      addGameLogEntry: (entry: GameLogEntry) =>
        set(
          state => {
            const newEntries = [...state.gameLog, entry];
            // Limit the number of entries to prevent memory issues
            const limitedEntries = newEntries.slice(-MAX_GAME_LOG_ENTRIES);
            return {
              gameLog: limitedEntries,
              lastUpdate: Date.now(),
            };
          },
          false,
          'addGameLogEntry'
        ),

      clearGameLog: () => set({ gameLog: [], lastUpdate: Date.now() }, false, 'clearGameLog'),

      // UI state actions
      setLoading: (loading: boolean) => set({ isLoading: loading }, false, 'setLoading'),

      updateLastUpdate: (timestamp: number) => set({ lastUpdate: timestamp }, false, 'updateLastUpdate'),

      // State management actions
      reset: () => set(createInitialState(), false, 'reset'),

      // Selectors
      getPlayerStats: () => {
        const state = get();
        return state.player?.stats || null;
      },

      getRoomOccupantsCount: () => {
        const state = get();
        return state.room?.occupant_count || 0;
      },

      getRecentChatMessages: (count: number) => {
        const state = get();
        return state.chatMessages.slice(-count);
      },

      getRecentGameLogEntries: (count: number) => {
        const state = get();
        return state.gameLog.slice(-count);
      },
    }),
    {
      name: 'game-store',
      partialize: state => ({
        player: state.player,
        room: state.room,
        lastUpdate: state.lastUpdate,
      }),
    }
  )
);
