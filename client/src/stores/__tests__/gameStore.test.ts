import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameStore } from '../gameStore';

describe('Game Store', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset store state
    useGameStore.getState().reset();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should have correct initial state', () => {
      const state = useGameStore.getState();

      expect(state.player).toBe(null);
      expect(state.room).toBe(null);
      expect(state.chatMessages).toEqual([]);
      expect(state.gameLog).toEqual([]);
      expect(state.isLoading).toBe(false);
      expect(state.lastUpdate).toBe(null);
    });
  });

  describe('Player Management', () => {
    it('should set player data', () => {
      const { result } = renderHook(() => useGameStore());
      const playerData = {
        id: 'player-123',
        name: 'TestPlayer',
        stats: {
          current_db: 100,
          lucidity: 80,
          strength: 15,
          dexterity: 12,
          constitution: 14,
          intelligence: 16,
          wisdom: 13,
          charisma: 10,
        },
        level: 5,
      };

      act(() => {
        result.current.setPlayer(playerData);
      });

      expect(result.current.player).toEqual(playerData);
    });

    it('should update player stats', () => {
      const { result } = renderHook(() => useGameStore());
      const initialPlayer = {
        id: 'player-123',
        name: 'TestPlayer',
        stats: {
          current_db: 100,
          lucidity: 80,
          strength: 15,
        },
        level: 5,
      };

      act(() => {
        result.current.setPlayer(initialPlayer);
        result.current.updatePlayerStats({
          current_db: 80,
          lucidity: 70,
        });
      });

      expect(result.current.player?.stats.current_db).toBe(80);
      expect(result.current.player?.stats.lucidity).toBe(70);
      expect(result.current.player?.stats.strength).toBe(15); // Should remain unchanged
    });

    it('should clear player data', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.setPlayer({
          id: 'player-123',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        });
        result.current.clearPlayer();
      });

      expect(result.current.player).toBe(null);
    });
  });

  describe('Room Management', () => {
    it('should set room data', () => {
      const { result } = renderHook(() => useGameStore());
      const roomData = {
        id: 'room-123',
        name: 'Test Room',
        description: 'A test room description',
        exits: { north: 'room-124', south: 'room-122' },
        occupants: ['player-123', 'player-456'],
        occupant_count: 2,
        entities: [{ id: 'entity-123', name: 'Test Entity', type: 'npc' }],
      };

      act(() => {
        result.current.setRoom(roomData);
      });

      expect(result.current.room).toEqual(roomData);
    });

    it('should update room occupants', () => {
      const { result } = renderHook(() => useGameStore());
      const initialRoom = {
        id: 'room-123',
        name: 'Test Room',
        description: 'A test room',
        exits: {},
        occupants: ['player-123'],
        occupant_count: 1,
      };

      act(() => {
        result.current.setRoom(initialRoom);
        result.current.updateRoomOccupants(['player-123', 'player-456', 'player-789']);
      });

      expect(result.current.room?.occupants).toEqual(['player-123', 'player-456', 'player-789']);
      expect(result.current.room?.occupant_count).toBe(3);
    });

    it('should clear room data', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.setRoom({
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
        });
        result.current.clearRoom();
      });

      expect(result.current.room).toBe(null);
    });
  });

  describe('Chat Messages', () => {
    it('should add chat message', () => {
      const { result } = renderHook(() => useGameStore());
      const message = {
        text: 'Hello world!',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        type: 'say' as const,
        channel: 'local' as const,
        sender: 'TestPlayer',
      };

      act(() => {
        result.current.addChatMessage(message);
      });

      expect(result.current.chatMessages).toHaveLength(1);
      expect(result.current.chatMessages[0]).toEqual(message);
    });

    it('should add multiple chat messages', () => {
      const { result } = renderHook(() => useGameStore());
      const messages = [
        {
          text: 'First message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'say' as const,
          channel: 'local' as const,
          sender: 'Player1',
        },
        {
          text: 'Second message',
          timestamp: '2024-01-01T12:01:00Z',
          isHtml: false,
          type: 'say' as const,
          channel: 'local' as const,
          sender: 'Player2',
        },
      ];

      act(() => {
        result.current.addChatMessage(messages[0]);
        result.current.addChatMessage(messages[1]);
      });

      expect(result.current.chatMessages).toHaveLength(2);
      expect(result.current.chatMessages).toEqual(messages);
    });

    it('should clear chat messages', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.addChatMessage({
          text: 'Test message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'say' as const,
          channel: 'local' as const,
          sender: 'TestPlayer',
        });
        result.current.clearChatMessages();
      });

      expect(result.current.chatMessages).toEqual([]);
    });

    it('should limit chat message history', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        // Add more messages than the limit (assuming limit is 100)
        for (let i = 0; i < 150; i++) {
          result.current.addChatMessage({
            text: `Message ${i}`,
            timestamp: `2024-01-01T12:${i.toString().padStart(2, '0')}:00Z`,
            isHtml: false,
            type: 'say' as const,
            channel: 'local' as const,
            sender: 'TestPlayer',
          });
        }
      });

      // Should not exceed the maximum number of messages
      expect(result.current.chatMessages.length).toBeLessThanOrEqual(100);
    });
  });

  describe('Game Log', () => {
    it('should add game log entry', () => {
      const { result } = renderHook(() => useGameStore());
      const logEntry = {
        text: 'You enter the room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        type: 'system' as const,
      };

      act(() => {
        result.current.addGameLogEntry(logEntry);
      });

      expect(result.current.gameLog).toHaveLength(1);
      expect(result.current.gameLog[0]).toEqual(logEntry);
    });

    it('should clear game log', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.addGameLogEntry({
          text: 'Test log entry',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'system' as const,
        });
        result.current.clearGameLog();
      });

      expect(result.current.gameLog).toEqual([]);
    });

    it('should limit game log history', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        // Add more entries than the limit (assuming limit is 100)
        for (let i = 0; i < 150; i++) {
          result.current.addGameLogEntry({
            text: `Log entry ${i}`,
            timestamp: `2024-01-01T12:${i.toString().padStart(2, '0')}:00Z`,
            isHtml: false,
            type: 'system' as const,
          });
        }
      });

      // Should not exceed the maximum number of entries
      expect(result.current.gameLog.length).toBeLessThanOrEqual(100);
    });
  });

  describe('Loading State', () => {
    it('should set loading state', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.setLoading(true);
      });

      expect(result.current.isLoading).toBe(true);
    });

    it('should clear loading state', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.setLoading(true);
        result.current.setLoading(false);
      });

      expect(result.current.isLoading).toBe(false);
    });
  });

  describe('Last Update Tracking', () => {
    it('should update last update timestamp', () => {
      const { result } = renderHook(() => useGameStore());
      const timestamp = Date.now();

      act(() => {
        result.current.updateLastUpdate(timestamp);
      });

      expect(result.current.lastUpdate).toBe(timestamp);
    });

    it('should update last update timestamp automatically on data changes', () => {
      const { result } = renderHook(() => useGameStore());
      const beforeUpdate = result.current.lastUpdate;

      act(() => {
        result.current.setPlayer({
          id: 'player-123',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        });
      });

      expect(result.current.lastUpdate).toBeGreaterThan(beforeUpdate || 0);
    });
  });

  describe('State Reset', () => {
    it('should reset all state to initial values', () => {
      const { result } = renderHook(() => useGameStore());

      // Modify state
      act(() => {
        result.current.setPlayer({
          id: 'player-123',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        });
        result.current.setRoom({
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
        });
        result.current.addChatMessage({
          text: 'Test message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'say' as const,
          channel: 'local' as const,
          sender: 'TestPlayer',
        });
        result.current.setLoading(true);
      });

      // Reset state
      act(() => {
        result.current.reset();
      });

      expect(result.current.player).toBe(null);
      expect(result.current.room).toBe(null);
      expect(result.current.chatMessages).toEqual([]);
      expect(result.current.gameLog).toEqual([]);
      expect(result.current.isLoading).toBe(false);
      expect(result.current.lastUpdate).toBe(null);
    });
  });

  describe('Selectors', () => {
    it('should provide player stats selector', () => {
      const { result } = renderHook(() => useGameStore());

      expect(result.current.getPlayerStats()).toBe(null);

      act(() => {
        result.current.setPlayer({
          id: 'player-123',
          name: 'TestPlayer',
          stats: {
            current_db: 100,
            lucidity: 80,
            strength: 15,
          },
          level: 5,
        });
      });

      expect(result.current.getPlayerStats()).toEqual({
        current_db: 100,
        lucidity: 80,
        strength: 15,
      });
    });

    it('should provide room occupants count selector', () => {
      const { result } = renderHook(() => useGameStore());

      expect(result.current.getRoomOccupantsCount()).toBe(0);

      act(() => {
        result.current.setRoom({
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
          occupants: ['player-1', 'player-2', 'player-3'],
          occupant_count: 3,
        });
      });

      expect(result.current.getRoomOccupantsCount()).toBe(3);
    });

    it('should provide recent chat messages selector', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        for (let i = 0; i < 5; i++) {
          result.current.addChatMessage({
            text: `Message ${i}`,
            timestamp: `2024-01-01T12:${i.toString().padStart(2, '0')}:00Z`,
            isHtml: false,
            type: 'say' as const,
            channel: 'local' as const,
            sender: 'TestPlayer',
          });
        }
      });

      const recentMessages = result.current.getRecentChatMessages(3);
      expect(recentMessages).toHaveLength(3);
      expect(recentMessages[0].text).toBe('Message 2'); // Most recent
      expect(recentMessages[2].text).toBe('Message 4'); // Oldest of the 3
    });

    it('should provide recent game log entries selector', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        for (let i = 0; i < 5; i++) {
          result.current.addGameLogEntry({
            text: `Log entry ${i}`,
            timestamp: `2024-01-01T12:${i.toString().padStart(2, '0')}:00Z`,
            isHtml: false,
            type: 'system' as const,
          });
        }
      });

      const recentEntries = result.current.getRecentGameLogEntries(3);
      expect(recentEntries).toHaveLength(3);
      expect(recentEntries[0].text).toBe('Log entry 2'); // Most recent
      expect(recentEntries[2].text).toBe('Log entry 4'); // Oldest of the 3
    });

    it('should update player stats when player is null', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        // Don't set player first
        result.current.updatePlayerStats({
          current_db: 80,
          lucidity: 70,
        });
      });

      // Should not crash, player should remain null
      expect(result.current.player).toBe(null);
    });

    it('should update room occupants when room is null', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        // Don't set room first
        result.current.updateRoomOccupants(['player-1', 'player-2']);
      });

      // Should not crash, room should remain null
      expect(result.current.room).toBe(null);
    });

    it('should get room occupants count when room is null', () => {
      const { result } = renderHook(() => useGameStore());

      expect(result.current.getRoomOccupantsCount()).toBe(0);
    });

    it('should get room occupants count when occupant_count is undefined', () => {
      const { result } = renderHook(() => useGameStore());

      act(() => {
        result.current.setRoom({
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
          // No occupant_count
        });
      });

      expect(result.current.getRoomOccupantsCount()).toBe(0);
    });
  });
});
