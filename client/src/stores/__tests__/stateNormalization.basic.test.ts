import { describe, expect, it } from 'vitest';
import {
  createEntityMap,
  getEntityById,
  mergeEntityMaps,
  removeEntityFromMap,
  updateEntityInMap,
  type Entity,
} from '../stateNormalization';

describe('State Normalization - Basic Operations', () => {
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
      ] as Entity[];

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
});
