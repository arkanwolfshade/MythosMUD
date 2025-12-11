import { describe, expect, it } from 'vitest';
import { denormalizeGameData, normalizeGameData, type NormalizedGameData } from '../stateNormalization';

describe('State Normalization - Normalization Functions', () => {
  describe('normalizeGameData', () => {
    it('should normalize game data with entities', () => {
      const gameData = {
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: { north: 'room-2' },
          entities: [
            { id: 'npc-1', name: 'Test NPC', type: 'npc' },
            { id: 'item-1', name: 'Test Item', type: 'item' },
          ],
        },
        chatMessages: [
          {
            id: 'msg-1',
            text: 'Hello!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'TestPlayer',
            type: 'say',
          },
        ],
        gameLog: [],
      };

      const normalized = normalizeGameData(gameData);

      expect(normalized).toEqual({
        player: 'player-1',
        room: 'room-1',
        chatMessages: ['msg-1'],
        gameLog: [],
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_db: 100, lucidity: 80 },
            level: 5,
          },
          'room-1': {
            id: 'room-1',
            name: 'Test Room',
            description: 'A test room',
            exits: { north: 'room-2' },
            entities: ['npc-1', 'item-1'],
          },
          'npc-1': { id: 'npc-1', name: 'Test NPC', type: 'npc' },
          'item-1': { id: 'item-1', name: 'Test Item', type: 'item' },
          'msg-1': {
            id: 'msg-1',
            text: 'Hello!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'TestPlayer',
            type: 'say',
          },
        },
      });
    });

    it('should handle nested entities in room', () => {
      const gameData = {
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
          entities: [{ id: 'npc-1', name: 'Test NPC', type: 'npc' }],
        },
      };

      const normalized = normalizeGameData(gameData);

      expect(normalized.entities['room-1'].entities).toEqual(['npc-1']);
      expect(normalized.entities['npc-1']).toEqual({ id: 'npc-1', name: 'Test NPC', type: 'npc' });
    });

    it('should handle data without entities', () => {
      const gameData = {
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_db: 100 },
        },
      };

      const normalized = normalizeGameData(gameData);

      expect(normalized).toEqual({
        player: 'player-1',
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_db: 100 },
          },
        },
      });
    });
  });

  describe('denormalizeGameData', () => {
    it('should denormalize game data', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: 'room-1',
        chatMessages: ['msg-1'],
        gameLog: [],
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_db: 100, lucidity: 80 },
            level: 5,
          },
          'room-1': {
            id: 'room-1',
            name: 'Test Room',
            description: 'A test room',
            exits: { north: 'room-2' },
            entities: ['npc-1', 'item-1'],
          },
          'npc-1': { id: 'npc-1', name: 'Test NPC', type: 'npc' },
          'item-1': { id: 'item-1', name: 'Test Item', type: 'item' },
          'msg-1': {
            id: 'msg-1',
            text: 'Hello!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'TestPlayer',
            type: 'say',
          },
        },
      };

      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: { north: 'room-2' },
          entities: [
            { id: 'npc-1', name: 'Test NPC', type: 'npc' },
            { id: 'item-1', name: 'Test Item', type: 'item' },
          ],
        },
        chatMessages: [
          {
            id: 'msg-1',
            text: 'Hello!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'TestPlayer',
            type: 'say',
          },
        ],
        gameLog: [],
      });
    });

    it('should handle missing references gracefully', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: 'room-1',
        chatMessages: ['msg-1'],
        gameLog: [],
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_db: 100 },
          },
          // Missing room-1 and msg-1 entities
        },
      };

      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_db: 100 },
        },
        room: null, // Should be null when entity is missing
        chatMessages: [], // Should be empty array when entities are missing
        gameLog: [], // Should be empty array when entities are missing
      });
    });

    it('should handle null references', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {},
      };

      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
      });
    });
  });

  describe('Round-trip normalization', () => {
    it('should preserve data through normalize/denormalize cycle', () => {
      const originalData = {
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_db: 100, lucidity: 80 },
          level: 5,
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: { north: 'room-2' },
          entities: [
            { id: 'npc-1', name: 'Test NPC', type: 'npc' },
            { id: 'item-1', name: 'Test Item', type: 'item' },
          ],
        },
        chatMessages: [
          {
            id: 'msg-1',
            text: 'Hello!',
            timestamp: '2024-01-01T12:00:00Z',
            sender: 'TestPlayer',
            type: 'say',
          },
        ],
        gameLog: [],
      };

      const normalized = normalizeGameData(originalData);
      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual(originalData);
    });

    it('should handle complex nested structures', () => {
      const originalData = {
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          inventory: [
            { id: 'item-1', name: 'Sword', type: 'weapon' },
            { id: 'item-2', name: 'Potion', type: 'consumable' },
          ],
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: {},
          entities: [{ id: 'npc-1', name: 'Merchant', type: 'npc', inventory: ['item-3'] }],
        },
        chatMessages: [],
        gameLog: [],
      };

      const normalized = normalizeGameData(originalData);
      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual(originalData);
    });
  });
});
