import { describe, expect, it } from 'vitest';
import {
  createEntityMap,
  denormalizeGameData,
  getEntitiesByIds,
  getEntitiesByType,
  getEntityById,
  mergeEntityMaps,
  normalizeGameData,
  removeEntitiesFromNormalizedData,
  removeEntityFromMap,
  updateEntityInMap,
  updateNormalizedData,
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

  describe('updateNormalizedData', () => {
    it('should update normalized data with new entities', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: 'room-1',
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
          'room-1': { id: 'room-1', name: 'Room 1', type: 'room' },
        },
      };

      const newEntities = {
        'npc-1': { id: 'npc-1', name: 'NPC 1', type: 'npc' },
        'item-1': { id: 'item-1', name: 'Item 1', type: 'item' },
      };

      const updated = updateNormalizedData(normalized, newEntities);

      expect(updated.entities).toEqual({
        'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
        'room-1': { id: 'room-1', name: 'Room 1', type: 'room' },
        'npc-1': { id: 'npc-1', name: 'NPC 1', type: 'npc' },
        'item-1': { id: 'item-1', name: 'Item 1', type: 'item' },
      });
    });

    it('should overwrite existing entities with new ones', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Old Name', type: 'player' },
        },
      };

      const newEntities = {
        'player-1': { id: 'player-1', name: 'New Name', type: 'player' },
      };

      const updated = updateNormalizedData(normalized, newEntities);

      expect(updated.entities['player-1']).toEqual({ id: 'player-1', name: 'New Name', type: 'player' });
    });
  });

  describe('getEntitiesByType', () => {
    it('should get entities by type', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
          'player-2': { id: 'player-2', name: 'Player 2', type: 'player' },
          'npc-1': { id: 'npc-1', name: 'NPC 1', type: 'npc' },
          'item-1': { id: 'item-1', name: 'Item 1', type: 'item' },
        },
      };

      const players = getEntitiesByType(normalized, 'player');
      expect(players).toHaveLength(2);
      expect(players.map(p => p.id)).toEqual(['player-1', 'player-2']);

      const npcs = getEntitiesByType(normalized, 'npc');
      expect(npcs).toHaveLength(1);
      expect(npcs[0].id).toBe('npc-1');
    });

    it('should return empty array when no entities match type', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
        },
      };

      const monsters = getEntitiesByType(normalized, 'monster');
      expect(monsters).toEqual([]);
    });

    it('should handle entities without type field', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'entity-1': { id: 'entity-1', name: 'Entity 1' }, // No type field
          'entity-2': { id: 'entity-2', name: 'Entity 2', type: 'player' },
        },
      };

      const players = getEntitiesByType(normalized, 'player');
      expect(players).toHaveLength(1);
      expect(players[0].id).toBe('entity-2');
    });
  });

  describe('getEntitiesByIds', () => {
    it('should get entities by IDs', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
          'player-2': { id: 'player-2', name: 'Player 2', type: 'player' },
          'npc-1': { id: 'npc-1', name: 'NPC 1', type: 'npc' },
        },
      };

      const entities = getEntitiesByIds(normalized, ['player-1', 'npc-1']);

      expect(entities).toHaveLength(2);
      expect(entities.map(e => e.id)).toEqual(['player-1', 'npc-1']);
    });

    it('should filter out non-existent IDs', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
        },
      };

      const entities = getEntitiesByIds(normalized, ['player-1', 'non-existent', 'player-2']);

      expect(entities).toHaveLength(1);
      expect(entities[0].id).toBe('player-1');
    });

    it('should return empty array for empty IDs array', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
        },
      };

      const entities = getEntitiesByIds(normalized, []);
      expect(entities).toEqual([]);
    });
  });

  describe('removeEntitiesFromNormalizedData', () => {
    it('should remove entities by IDs', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
          'npc-1': { id: 'npc-1', name: 'NPC 1', type: 'npc' },
          'item-1': { id: 'item-1', name: 'Item 1', type: 'item' },
        },
      };

      const updated = removeEntitiesFromNormalizedData(normalized, ['npc-1', 'item-1']);

      expect(updated.entities).toEqual({
        'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
      });
    });

    it('should handle removing non-existent IDs gracefully', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
        },
      };

      const updated = removeEntitiesFromNormalizedData(normalized, ['non-existent', 'player-1']);

      expect(updated.entities).toEqual({});
    });

    it('should preserve other normalized data fields', () => {
      const normalized: NormalizedGameData = {
        player: 'player-1',
        room: 'room-1',
        chatMessages: ['msg-1'],
        gameLog: ['log-1'],
        entities: {
          'player-1': { id: 'player-1', name: 'Player 1', type: 'player' },
          'room-1': { id: 'room-1', name: 'Room 1', type: 'room' },
        },
      };

      const updated = removeEntitiesFromNormalizedData(normalized, ['player-1']);

      expect(updated.player).toBe('player-1'); // Still references removed entity
      expect(updated.room).toBe('room-1');
      expect(updated.chatMessages).toEqual(['msg-1']);
      expect(updated.gameLog).toEqual(['log-1']);
      expect(updated.entities).toEqual({
        'room-1': { id: 'room-1', name: 'Room 1', type: 'room' },
      });
    });
  });

  describe('Edge Cases - Helper Functions', () => {
    it('should handle entities with non-string id in extractEntities', () => {
      const gameData = {
        player: {
          id: 123 as unknown as string, // Non-string id
          name: 'TestPlayer',
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
        },
      };

      const normalized = normalizeGameData(gameData);

      // Entity with non-string id should not be extracted
      expect(normalized.entities['room-1']).toBeDefined();
      expect(normalized.entities['123']).toBeUndefined();
    });

    it('should handle null and undefined values in arrays during extraction', () => {
      const gameData = {
        room: {
          id: 'room-1',
          entities: [{ id: 'npc-1', name: 'NPC 1' }, null, undefined, { id: 'item-1', name: 'Item 1' }],
        },
      };

      const normalized = normalizeGameData(gameData);

      // Should extract entities even with null/undefined in array
      expect(normalized.entities['room-1']).toBeDefined();
      expect(normalized.entities['npc-1']).toBeDefined();
      expect(normalized.entities['item-1']).toBeDefined();
    });

    it('should handle nested object structures in extractEntities', () => {
      const gameData = {
        player: {
          id: 'player-1',
          inventory: {
            weapons: [
              { id: 'sword-1', name: 'Sword', type: 'weapon' },
              { id: 'staff-1', name: 'Staff', type: 'weapon' },
            ],
          },
          stats: {
            health: {
              current: 100,
              max: 100,
            },
          },
        },
      };

      const normalized = normalizeGameData(gameData);

      // Should extract all nested entities
      expect(normalized.entities['player-1']).toBeDefined();
      expect(normalized.entities['sword-1']).toBeDefined();
      expect(normalized.entities['staff-1']).toBeDefined();
    });

    it('should handle entities array that is not all strings in restoreEntityReferences', () => {
      const normalized: NormalizedGameData = {
        player: null,
        room: 'room-1',
        chatMessages: [],
        gameLog: [],
        entities: {
          'room-1': {
            id: 'room-1',
            name: 'Test Room',
            // entities array with mixed types (not all strings)
            entities: ['npc-1', { id: 'npc-2' }, 'item-1'],
          },
          'npc-1': { id: 'npc-1', name: 'NPC 1' },
          'item-1': { id: 'item-1', name: 'Item 1' },
        },
      };

      const denormalized = denormalizeGameData(normalized);

      // Should handle mixed array correctly
      expect(denormalized.room).toBeDefined();
      if (denormalized.room) {
        const entities = (denormalized.room as { entities: unknown[] }).entities;
        // Should process array items that aren't all strings
        expect(Array.isArray(entities)).toBe(true);
      }
    });

    it('should handle non-entities arrays in replaceEntitiesWithIds', () => {
      const gameData = {
        room: {
          id: 'room-1',
          name: 'Test Room',
          // Array that is not named 'entities' and doesn't have all items with id
          items: [{ id: 'item-1', name: 'Item 1' }, { name: 'Item without id' }, 'string item'],
        },
      };

      const normalized = normalizeGameData(gameData);

      // Should normalize correctly even with mixed array types
      expect(normalized.entities['room-1']).toBeDefined();
      expect(normalized.entities['item-1']).toBeDefined();
    });

    it('should handle identity check in replaceEntitiesWithIds', () => {
      const entity = { id: 'entity-1', name: 'Entity 1' };
      const gameData = {
        room: {
          id: 'room-1',
          name: 'Test Room',
          // Use the same object reference
          nestedEntity: entity,
          reference: entity, // Same reference
        },
      };

      const normalized = normalizeGameData(gameData);

      // Both references should be processed correctly
      expect(normalized.entities['room-1']).toBeDefined();
      expect(normalized.entities['entity-1']).toBeDefined();
    });

    it('should handle empty arrays and empty objects in extractEntities', () => {
      const gameData = {
        room: {
          id: 'room-1',
          emptyArray: [],
          emptyObject: {},
          nested: {
            id: 'nested-1',
            name: 'Nested',
          },
        },
      };

      const normalized = normalizeGameData(gameData);

      // Should extract entities even with empty structures
      expect(normalized.entities['room-1']).toBeDefined();
      expect(normalized.entities['nested-1']).toBeDefined();
    });
  });
});
