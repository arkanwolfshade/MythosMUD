import { describe, expect, it } from 'vitest';
import { denormalizeGameData, normalizeGameData, type NormalizedGameData } from '../stateNormalization';

describe('State Normalization - Edge Cases', () => {
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
        const entities = (denormalized.room as unknown as { entities: unknown[] }).entities;
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
