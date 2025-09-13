import { renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useCommandStore, useConnectionStore, useGameStore, useSessionStore } from '../stores';
import { useGameTerminal } from './useGameTerminal';

// Mock the stores
vi.mock('../stores', () => ({
  useConnectionStore: vi.fn(() => ({
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
  })),
  useGameStore: vi.fn(() => ({
    player: {
      id: 'player-1',
      name: 'TestPlayer',
      stats: { current_health: 100, sanity: 80 },
      level: 5,
    },
    room: {
      id: 'room-1',
      name: 'Test Room',
      description: 'A test room',
      exits: { north: 'room-2' },
      occupants: ['player-1'],
      occupant_count: 1,
      entities: [{ name: 'Test NPC', type: 'npc' }],
    },
    chatMessages: [
      {
        text: 'Welcome to the test room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        type: 'system',
        channel: 'game',
        sender: 'System',
      },
    ],
    gameLog: [],
  })),
  useSessionStore: vi.fn(() => ({
    playerName: 'TestPlayer',
    characterName: 'TestCharacter',
    isAuthenticated: true,
    hasCharacter: true,
  })),
  useCommandStore: vi.fn(() => ({
    commandHistory: [
      { command: 'look', timestamp: Date.now(), success: true },
      { command: 'inventory', timestamp: Date.now(), success: true },
      { command: 'status', timestamp: Date.now(), success: true },
    ],
    currentCommand: '',
    isExecuting: false,
  })),
}));

describe('useGameTerminal', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should return initial state with all required properties', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current).toHaveProperty('playerName');
      expect(result.current).toHaveProperty('isConnected');
      expect(result.current).toHaveProperty('isConnecting');
      expect(result.current).toHaveProperty('error');
      expect(result.current).toHaveProperty('reconnectAttempts');
      expect(result.current).toHaveProperty('room');
      expect(result.current).toHaveProperty('player');
      expect(result.current).toHaveProperty('messages');
      expect(result.current).toHaveProperty('commandHistory');
      expect(result.current).toHaveProperty('onSendCommand');
      expect(result.current).toHaveProperty('onSendChatMessage');
      expect(result.current).toHaveProperty('onClearMessages');
      expect(result.current).toHaveProperty('onClearHistory');
      expect(result.current).toHaveProperty('onDownloadLogs');
    });

    it('should return correct initial values', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.playerName).toBe('TestPlayer');
      expect(result.current.isConnected).toBe(true);
      expect(result.current.isConnecting).toBe(false);
      expect(result.current.error).toBe(null);
      expect(result.current.reconnectAttempts).toBe(0);
      expect(result.current.room).toEqual({
        id: 'room-1',
        name: 'Test Room',
        description: 'A test room',
        exits: { north: 'room-2' },
        occupants: ['player-1'],
        occupant_count: 1,
        entities: [{ name: 'Test NPC', type: 'npc' }],
      });
      expect(result.current.player).toEqual({
        id: 'player-1',
        name: 'TestPlayer',
        stats: { current_health: 100, sanity: 80 },
        level: 5,
      });
      expect(result.current.messages).toHaveLength(1);
      expect(result.current.commandHistory).toHaveLength(3);
    });
  });

  describe('Event Handlers', () => {
    it('should provide onSendCommand handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onSendCommand).toBe('function');
    });

    it('should provide onSendChatMessage handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onSendChatMessage).toBe('function');
    });

    it('should provide onClearMessages handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onClearMessages).toBe('function');
    });

    it('should provide onClearHistory handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onClearHistory).toBe('function');
    });

    it('should provide onDownloadLogs handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onDownloadLogs).toBe('function');
    });
  });

  describe('State Updates', () => {
    it('should update when connection state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.isConnected).toBe(true);

      // Mock updated connection state
      vi.mocked(useConnectionStore).mockReturnValue({
        isConnected: false,
        isConnecting: true,
        error: 'Connection failed',
        reconnectAttempts: 3,
      });

      rerender();

      expect(result.current.isConnected).toBe(false);
      expect(result.current.isConnecting).toBe(true);
      expect(result.current.error).toBe('Connection failed');
      expect(result.current.reconnectAttempts).toBe(3);
    });

    it('should update when game state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.player?.stats.current_health).toBe(100);

      // Mock updated game state
      vi.mocked(useGameStore).mockReturnValue({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_health: 80, sanity: 60 },
          level: 5,
        },
        room: result.current.room,
        chatMessages: result.current.messages,
        gameLog: [],
      });

      rerender();

      expect(result.current.player?.stats.current_health).toBe(80);
      expect(result.current.player?.stats.sanity).toBe(60);
    });

    it('should update when session state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.playerName).toBe('TestPlayer');

      // Mock updated session state
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'NewPlayer',
        characterName: 'NewCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      });

      rerender();

      expect(result.current.playerName).toBe('NewPlayer');
    });

    it('should update when command state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.commandHistory).toHaveLength(3);

      // Mock updated command state
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [
          { command: 'look', timestamp: Date.now(), success: true },
          { command: 'inventory', timestamp: Date.now(), success: true },
          { command: 'status', timestamp: Date.now(), success: true },
          { command: 'go north', timestamp: Date.now(), success: true },
        ],
        currentCommand: 'go north',
        isExecuting: true,
      });

      rerender();

      expect(result.current.commandHistory).toHaveLength(4);
    });
  });

  describe('Data Transformation', () => {
    it('should transform chat messages correctly', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.messages).toHaveLength(1);
      expect(result.current.messages[0]).toEqual({
        text: 'Welcome to the test room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        messageType: 'system',
      });
    });

    it('should transform command history correctly', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.commandHistory).toHaveLength(3);
      expect(result.current.commandHistory[0]).toBe('look');
      expect(result.current.commandHistory[1]).toBe('inventory');
      expect(result.current.commandHistory[2]).toBe('status');
    });

    it('should handle empty data gracefully', () => {
      // Mock empty states
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
      });

      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
      });

      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.player).toBe(null);
      expect(result.current.room).toBe(null);
      expect(result.current.messages).toEqual([]);
      expect(result.current.commandHistory).toEqual([]);
    });
  });

  describe('Error Handling', () => {
    it('should handle store errors gracefully', () => {
      // Mock store throwing error
      vi.mocked(useConnectionStore).mockImplementation(() => {
        throw new Error('Store error');
      });

      expect(() => {
        renderHook(() => useGameTerminal());
      }).toThrow('Store error');
    });

    it('should handle missing store data gracefully', () => {
      // Mock undefined store return
      vi.mocked(useGameStore).mockReturnValue(undefined);

      expect(() => {
        renderHook(() => useGameTerminal());
      }).toThrow();
    });
  });
});
