import { describe, expect, it } from 'vitest';
import { getEntitiesByIds, getEntitiesByType, type NormalizedGameData } from '../stateNormalization';

describe('State Normalization - Query Operations', () => {
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
});
