import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useCommandStore } from '../commandStore';
import { useConnectionStore } from '../connectionStore';
import { useGameStore } from '../gameStore';
import { useSessionStore } from '../sessionStore';
import { denormalizeGameData, normalizeGameData } from '../stateNormalization';

describe('State Management Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset all store states
    useConnectionStore.getState().reset();
    useGameStore.getState().reset();
    useSessionStore.getState().reset();
    useCommandStore.getState().reset();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Cross-Store Communication', () => {
    it('should handle complete game session flow', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());
      const { result: gameResult } = renderHook(() => useGameStore());
      const { result: sessionResult } = renderHook(() => useSessionStore());
      const { result: commandResult } = renderHook(() => useCommandStore());

      // 1. User logs in
      act(() => {
        sessionResult.current.setPlayerName('TestPlayer');
        sessionResult.current.setInviteCode('INVITE123');
        sessionResult.current.setAuthToken('auth-token-123');
        sessionResult.current.setAuthenticated(true);
        sessionResult.current.setHasCharacter(true);
        sessionResult.current.setCharacterName('TestCharacter');
      });

      expect(sessionResult.current.isAuthenticated).toBe(true);
      expect(sessionResult.current.hasCharacter).toBe(true);

      // 2. Connection is established
      act(() => {
        connectionResult.current.setSseConnected(true);
        connectionResult.current.setWebsocketConnected(true);
      });

      expect(connectionResult.current.isFullyConnected()).toBe(true);

      // 3. Game data is received and normalized
      const gameData = {
        player: {
          id: 'player-123',
          name: 'TestCharacter',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        },
        room: {
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: { north: 'room-124' },
          entities: [{ id: 'npc-1', name: 'Test NPC', type: 'npc' }],
        },
        chatMessages: [],
      };

      const normalizedData = normalizeGameData(gameData);
      const denormalizedData = denormalizeGameData(normalizedData);

      act(() => {
        gameResult.current.setPlayer(denormalizedData.player);
        gameResult.current.setRoom(denormalizedData.room);
      });

      expect(gameResult.current.player?.name).toBe('TestCharacter');
      expect(gameResult.current.room?.name).toBe('Test Room');

      // 4. User executes commands
      act(() => {
        commandResult.current.executeCommand('look around');
      });

      expect(commandResult.current.lastExecutedCommand).toBe('look around');
      expect(commandResult.current.commandHistory).toHaveLength(1);

      // 5. Chat messages are received
      act(() => {
        gameResult.current.addChatMessage({
          text: 'You see a test room with an NPC.',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'system',
          channel: 'game',
          sender: 'System',
        });
      });

      expect(gameResult.current.chatMessages).toHaveLength(1);
    });

    it('should handle connection state affecting game state', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());
      const { result: gameResult } = renderHook(() => useGameStore());

      // Set up game state
      act(() => {
        gameResult.current.setPlayer({
          id: 'player-123',
          name: 'TestPlayer',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        });
      });

      // Connection is lost
      act(() => {
        connectionResult.current.setSseConnected(false);
        connectionResult.current.setWebsocketConnected(false);
        connectionResult.current.setError('Connection lost');
      });

      expect(connectionResult.current.isFullyConnected()).toBe(false);
      expect(connectionResult.current.error).toBe('Connection lost');

      // Game state should remain intact
      expect(gameResult.current.player?.name).toBe('TestPlayer');

      // Connection is restored
      act(() => {
        connectionResult.current.setSseConnected(true);
        connectionResult.current.setWebsocketConnected(true);
        connectionResult.current.setError(null);
      });

      expect(connectionResult.current.isFullyConnected()).toBe(true);
      expect(connectionResult.current.error).toBe(null);
    });

    it('should handle session timeout affecting all stores', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());
      const { result: gameResult } = renderHook(() => useGameStore());
      const { result: sessionResult } = renderHook(() => useSessionStore());
      const { result: commandResult } = renderHook(() => useCommandStore());

      // Set up authenticated session
      act(() => {
        sessionResult.current.setAuthenticated(true);
        sessionResult.current.setHasCharacter(true);
        sessionResult.current.setCharacterName('TestCharacter');
        sessionResult.current.setAuthToken('auth-token-123');
        connectionResult.current.setSseConnected(true);
        connectionResult.current.setWebsocketConnected(true);
        gameResult.current.setPlayer({
          id: 'player-123',
          name: 'TestCharacter',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        });
        commandResult.current.addToHistory('look around');
      });

      // Simulate session timeout
      act(() => {
        sessionResult.current.updateLastActivity(Date.now() - 31 * 60 * 1000); // 31 minutes ago
      });

      expect(sessionResult.current.isSessionExpired()).toBe(true);

      // Logout should reset all stores
      act(() => {
        sessionResult.current.logout();
        connectionResult.current.reset();
        gameResult.current.reset();
        commandResult.current.reset();
      });

      expect(sessionResult.current.isAuthenticated).toBe(false);
      expect(connectionResult.current.isConnected).toBe(false);
      expect(gameResult.current.player).toBe(null);
      expect(commandResult.current.commandHistory).toEqual([]);
    });
  });

  describe('State Normalization Integration', () => {
    it('should handle complex game data normalization across stores', () => {
      const { result: gameResult } = renderHook(() => useGameStore());

      const complexGameData = {
        player: {
          id: 'player-123',
          name: 'TestCharacter',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
          inventory: [
            { id: 'item-1', name: 'Sword', type: 'weapon' },
            { id: 'item-2', name: 'Potion', type: 'consumable' },
          ],
        },
        room: {
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room with many entities',
          exits: { north: 'room-124', south: 'room-122' },
          entities: [
            { id: 'npc-1', name: 'Merchant', type: 'npc' },
            { id: 'npc-2', name: 'Guard', type: 'npc' },
            { id: 'item-3', name: 'Treasure Chest', type: 'container' },
          ],
        },
        chatMessages: [
          {
            id: 'msg-1',
            text: 'Welcome to the test room!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'System',
            type: 'system',
            channel: 'game',
          },
          {
            id: 'msg-2',
            text: 'Hello there!',
            timestamp: '2024-01-01T12:01:00Z',
            sender: 'TestCharacter',
            type: 'say',
            channel: 'local',
          },
        ],
      };

      // Normalize the data
      const normalizedData = normalizeGameData(complexGameData);

      // Verify normalization worked correctly
      expect(normalizedData.player).toBe('player-123');
      expect(normalizedData.room).toBe('room-123');
      expect(normalizedData.chatMessages).toEqual(['msg-1', 'msg-2']);
      expect(normalizedData.entities['player-123']).toBeDefined();
      expect(normalizedData.entities['room-123']).toBeDefined();
      expect(normalizedData.entities['npc-1']).toBeDefined();
      expect(normalizedData.entities['item-1']).toBeDefined();

      // Denormalize and set in store
      const denormalizedData = denormalizeGameData(normalizedData);

      act(() => {
        gameResult.current.setPlayer(denormalizedData.player);
        gameResult.current.setRoom(denormalizedData.room);
        denormalizedData.chatMessages.forEach(msg => {
          gameResult.current.addChatMessage(msg);
        });
      });

      // Verify data integrity
      expect(gameResult.current.player?.name).toBe('TestCharacter');
      expect(gameResult.current.room?.name).toBe('Test Room');
      expect(gameResult.current.room?.entities).toHaveLength(3);
      expect(gameResult.current.chatMessages).toHaveLength(2);
    });

    it('should handle incremental updates to normalized data', () => {
      const { result: gameResult } = renderHook(() => useGameStore());

      // Initial game data
      const initialData = {
        player: {
          id: 'player-123',
          name: 'TestCharacter',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        },
        room: {
          id: 'room-123',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
          entities: [],
        },
        chatMessages: [],
      };

      const normalizedInitial = normalizeGameData(initialData);
      const denormalizedInitial = denormalizeGameData(normalizedInitial);

      act(() => {
        gameResult.current.setPlayer(denormalizedInitial.player);
        gameResult.current.setRoom(denormalizedInitial.room);
      });

      // Update with new entities
      const updatedData = {
        ...initialData,
        room: {
          ...initialData.room,
          entities: [{ id: 'npc-1', name: 'New NPC', type: 'npc' }],
        },
      };

      const normalizedUpdated = normalizeGameData(updatedData);
      const denormalizedUpdated = denormalizeGameData(normalizedUpdated);

      act(() => {
        gameResult.current.setRoom(denormalizedUpdated.room);
      });

      expect(gameResult.current.room?.entities).toHaveLength(1);
      expect(gameResult.current.room?.entities[0].name).toBe('New NPC');
    });
  });

  describe('Performance and Memory Management', () => {
    it('should handle large amounts of chat messages efficiently', () => {
      const { result: gameResult } = renderHook(() => useGameStore());

      act(() => {
        // Add many chat messages
        for (let i = 0; i < 1000; i++) {
          gameResult.current.addChatMessage({
            text: `Message ${i}`,
            timestamp: `2024-01-01T12:${(i % 60).toString().padStart(2, '0')}:00Z`,
            isHtml: false,
            type: 'say',
            channel: 'local',
            sender: 'TestPlayer',
          });
        }
      });

      // Should not exceed the maximum number of messages
      expect(gameResult.current.chatMessages.length).toBeLessThanOrEqual(100);
    });

    it('should handle large command history efficiently', () => {
      const { result: commandResult } = renderHook(() => useCommandStore());

      act(() => {
        // Add many commands
        for (let i = 0; i < 1000; i++) {
          commandResult.current.addToHistory(`command ${i}`);
        }
      });

      // Should not exceed the maximum number of commands
      expect(commandResult.current.commandHistory.length).toBeLessThanOrEqual(100);
    });

    it('should handle rapid state updates without memory leaks', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());
      const { result: gameResult } = renderHook(() => useGameStore());

      // Simulate rapid state updates
      act(() => {
        for (let i = 0; i < 100; i++) {
          connectionResult.current.updateConnectionHealth({
            websocket: i % 2 === 0 ? 'healthy' : 'unhealthy',
          });
          gameResult.current.updateLastUpdate(Date.now());
        }
      });

      // State should be consistent
      expect(connectionResult.current.connectionHealth.websocket).toBe('unhealthy');
      expect(gameResult.current.lastUpdate).toBeGreaterThan(0);
    });
  });

  describe('Error Handling and Recovery', () => {
    it('should handle malformed game data gracefully', () => {
      const { result: gameResult } = renderHook(() => useGameStore());

      // Try to set malformed data
      act(() => {
        try {
          gameResult.current.setPlayer(null as unknown as Player);
          gameResult.current.setRoom(null as unknown as Room);
        } catch {
          // Should handle gracefully
        }
      });

      // State should remain consistent
      expect(gameResult.current.player).toBe(null);
      expect(gameResult.current.room).toBe(null);
    });

    it('should recover from connection errors', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());

      // Simulate connection error
      act(() => {
        connectionResult.current.setError('Connection failed');
        connectionResult.current.setSseConnected(false);
        connectionResult.current.setWebsocketConnected(false);
      });

      expect(connectionResult.current.error).toBe('Connection failed');
      expect(connectionResult.current.isFullyConnected()).toBe(false);

      // Recover from error
      act(() => {
        connectionResult.current.setError(null);
        connectionResult.current.setSseConnected(true);
        connectionResult.current.setWebsocketConnected(true);
      });

      expect(connectionResult.current.error).toBe(null);
      expect(connectionResult.current.isFullyConnected()).toBe(true);
    });

    it('should handle session expiration gracefully', () => {
      const { result: sessionResult } = renderHook(() => useSessionStore());

      // Set up authenticated session
      act(() => {
        sessionResult.current.setAuthenticated(true);
        sessionResult.current.setHasCharacter(true);
        sessionResult.current.setCharacterName('TestCharacter');
        sessionResult.current.setAuthToken('auth-token-123');
      });

      // Simulate session expiration
      act(() => {
        sessionResult.current.updateLastActivity(Date.now() - 31 * 60 * 1000);
      });

      expect(sessionResult.current.isSessionExpired()).toBe(true);

      // Handle session expiration
      act(() => {
        sessionResult.current.logout();
      });

      expect(sessionResult.current.isAuthenticated).toBe(false);
      expect(sessionResult.current.hasCharacter).toBe(false);
      expect(sessionResult.current.characterName).toBe('');
      expect(sessionResult.current.authToken).toBe('');
    });
  });

  describe('State Synchronization', () => {
    it('should maintain consistency across stores during updates', () => {
      const { result: connectionResult } = renderHook(() => useConnectionStore());
      const { result: gameResult } = renderHook(() => useGameStore());
      const { result: sessionResult } = renderHook(() => useSessionStore());

      // Set up initial state
      act(() => {
        sessionResult.current.setAuthenticated(true);
        sessionResult.current.setCharacterName('TestCharacter');
        connectionResult.current.setSseConnected(true);
        connectionResult.current.setWebsocketConnected(true);
        gameResult.current.setPlayer({
          id: 'player-123',
          name: 'TestCharacter',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        });
      });

      // Verify consistency
      expect(sessionResult.current.isAuthenticated).toBe(true);
      expect(sessionResult.current.characterName).toBe('TestCharacter');
      expect(connectionResult.current.isFullyConnected()).toBe(true);
      expect(gameResult.current.player?.name).toBe('TestCharacter');

      // Update character name across stores
      act(() => {
        sessionResult.current.setCharacterName('UpdatedCharacter');
        gameResult.current.setPlayer({
          ...gameResult.current.player!,
          name: 'UpdatedCharacter',
        });
      });

      // Verify consistency maintained
      expect(sessionResult.current.characterName).toBe('UpdatedCharacter');
      expect(gameResult.current.player?.name).toBe('UpdatedCharacter');
    });
  });
});
