import { describe, expect, it } from 'vitest';
import {
  createEntityMap,
  denormalizeGameData,
  getEntityById,
  mergeEntityMaps,
  normalizeGameData,
  removeEntityFromMap,
  updateEntityInMap,
  type NormalizedGameData,
} from '../stateNormalization';

describe('State Normalization', () => {
  describe('createEntityMap', () => {
    it('should create entity map from array', () => {
      const entities = [
        { id: '1', name: 'Entity 1', type: 'player' },
        { id: '2', name: 'Entity 2', type: 'npc' },
        { id: '3', name: 'Entity 3', type: 'item' },
      ];

      const entityMap = createEntityMap(entities);

      expect(entityMap).toEqual({
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
        '3': { id: '3', name: 'Entity 3', type: 'item' },
      });
    });

    it('should handle empty array', () => {
      const entityMap = createEntityMap([]);
      expect(entityMap).toEqual({});
    });

    it('should handle entities without id', () => {
      const entities = [
        { name: 'Entity 1', type: 'player' },
        { id: '2', name: 'Entity 2', type: 'npc' },
      ];

      const entityMap = createEntityMap(entities);

      expect(entityMap).toEqual({
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      });
    });
  });

  describe('mergeEntityMaps', () => {
    it('should merge two entity maps', () => {
      const map1 = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      };

      const map2 = {
        '3': { id: '3', name: 'Entity 3', type: 'item' },
        '4': { id: '4', name: 'Entity 4', type: 'monster' },
      };

      const merged = mergeEntityMaps(map1, map2);

      expect(merged).toEqual({
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
        '3': { id: '3', name: 'Entity 3', type: 'item' },
        '4': { id: '4', name: 'Entity 4', type: 'monster' },
      });
    });

    it('should handle overlapping entities (second map wins)', () => {
      const map1 = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      };

      const map2 = {
        '2': { id: '2', name: 'Updated Entity 2', type: 'npc' },
        '3': { id: '3', name: 'Entity 3', type: 'item' },
      };

      const merged = mergeEntityMaps(map1, map2);

      expect(merged).toEqual({
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Updated Entity 2', type: 'npc' },
        '3': { id: '3', name: 'Entity 3', type: 'item' },
      });
    });

    it('should handle empty maps', () => {
      const merged = mergeEntityMaps({}, {});
      expect(merged).toEqual({});
    });
  });

  describe('getEntityById', () => {
    it('should get entity by id', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      };

      const entity = getEntityById(entityMap, '1');
      expect(entity).toEqual({ id: '1', name: 'Entity 1', type: 'player' });
    });

    it('should return null for non-existent id', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
      };

      const entity = getEntityById(entityMap, '999');
      expect(entity).toBeNull();
    });
  });

  describe('updateEntityInMap', () => {
    it('should update existing entity', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      };

      const updated = updateEntityInMap(entityMap, '1', { name: 'Updated Entity 1' });

      expect(updated).toEqual({
        '1': { id: '1', name: 'Updated Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      });
    });

    it('should add new entity if id does not exist', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
      };

      const updated = updateEntityInMap(entityMap, '2', { id: '2', name: 'New Entity', type: 'npc' });

      expect(updated).toEqual({
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'New Entity', type: 'npc' },
      });
    });
  });

  describe('removeEntityFromMap', () => {
    it('should remove entity by id', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      };

      const updated = removeEntityFromMap(entityMap, '1');

      expect(updated).toEqual({
        '2': { id: '2', name: 'Entity 2', type: 'npc' },
      });
    });

    it('should return same map if id does not exist', () => {
      const entityMap = {
        '1': { id: '1', name: 'Entity 1', type: 'player' },
      };

      const updated = removeEntityFromMap(entityMap, '999');

      expect(updated).toBe(entityMap); // Should return same reference
    });
  });

  describe('normalizeGameData', () => {
    it('should normalize game data with entities', () => {
      const gameData = {
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
            stats: { current_health: 100, sanity: 80 },
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
          stats: { current_health: 100 },
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
            stats: { current_health: 100 },
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
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_health: 100, sanity: 80 },
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
          stats: { current_health: 100, sanity: 80 },
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
        entities: {
          'player-1': {
            id: 'player-1',
            name: 'TestPlayer',
            stats: { current_health: 100 },
          },
          // Missing room-1 and msg-1 entities
        },
      };

      const denormalized = denormalizeGameData(normalized);

      expect(denormalized).toEqual({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_health: 100 },
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
          stats: { current_health: 100, sanity: 80 },
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
