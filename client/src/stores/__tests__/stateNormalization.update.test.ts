import { describe, expect, it } from 'vitest';
import { removeEntitiesFromNormalizedData, updateNormalizedData, type NormalizedGameData } from '../stateNormalization';

describe('State Normalization - Update Operations', () => {
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
});
