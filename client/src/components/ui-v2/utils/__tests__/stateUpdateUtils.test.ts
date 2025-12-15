/**
 * Tests for stateUpdateUtils.
 */

import { describe, expect, it } from 'vitest';
import type { GameStateUpdates } from '../../eventHandlers/types';
import type { Player, Room } from '../../types';
import { applyPlayerUpdate, applyRoomUpdate, mergeOccupantData, mergeRoomUpdate } from '../stateUpdateUtils';

describe('stateUpdateUtils', () => {
  describe('mergeOccupantData', () => {
    it('should merge occupant data from new room', () => {
      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: ['player1'],
        npcs: ['npc1'],
        occupant_count: 2,
      };

      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: [],
        npcs: [],
      };

      const result = mergeOccupantData(newRoom, existingRoom);
      expect(result.players).toEqual(['player1']);
      expect(result.npcs).toEqual(['npc1']);
      expect(result.occupant_count).toBe(2);
    });

    it('should use existing room data when new room data is missing', () => {
      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
      };

      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: ['player1'],
        npcs: ['npc1'],
        occupant_count: 2,
      };

      const result = mergeOccupantData(newRoom, existingRoom);
      expect(result.players).toEqual(['player1']);
      expect(result.npcs).toEqual(['npc1']);
      expect(result.occupant_count).toBe(2);
    });
  });

  describe('mergeRoomUpdate', () => {
    it('should return new room when existing room is null', () => {
      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
      };

      const result = mergeRoomUpdate(null, newRoom);
      expect(result).toEqual(newRoom);
    });

    it('should return new room when room IDs differ', () => {
      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
      };

      const newRoom: Room = {
        id: 'room2',
        name: 'Room 2',
        description: 'A test room',
        exits: {},
      };

      const result = mergeRoomUpdate(existingRoom, newRoom);
      expect(result).toEqual(newRoom);
    });

    it('should merge room updates for same room ID', () => {
      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: ['player1'],
      };

      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1 Updated',
        description: 'A test room',
        exits: {},
        npcs: ['npc1'],
      };

      const result = mergeRoomUpdate(existingRoom, newRoom);
      expect(result.id).toBe('room1');
      expect(result.name).toBe('Room 1 Updated');
      expect(result.players).toEqual(['player1']);
      expect(result.npcs).toEqual(['npc1']);
    });
  });

  describe('applyPlayerUpdate', () => {
    it('should apply player update when present', () => {
      const eventUpdates: GameStateUpdates = {
        player: {
          id: 'player1',
          name: 'Player 1',
        } as Player,
      };

      const updates: Partial<{ player: Player | null }> = {};

      applyPlayerUpdate(eventUpdates, updates);

      expect(updates.player).toEqual(eventUpdates.player);
    });

    it('should not modify updates when player is undefined', () => {
      const eventUpdates: GameStateUpdates = {};
      const updates: Partial<{ player: Player | null }> = { player: null };

      applyPlayerUpdate(eventUpdates, updates);

      expect(updates.player).toBeNull();
    });
  });

  describe('applyRoomUpdate', () => {
    it('should apply room update when present', () => {
      const eventUpdates: GameStateUpdates = {
        room: {
          id: 'room1',
          name: 'Room 1',
          description: 'A test room',
          exits: {},
        },
      };

      const updates: Partial<{ room: Room | null }> = {};

      applyRoomUpdate(eventUpdates, updates, mergeRoomUpdate);

      expect(updates.room).toEqual(eventUpdates.room);
    });

    it('should merge room update when existing room exists', () => {
      const eventUpdates: GameStateUpdates = {
        room: {
          id: 'room1',
          name: 'Room 1 Updated',
          description: 'A test room',
          exits: {},
        },
      };

      const updates: Partial<{ room: Room | null }> = {
        room: {
          id: 'room1',
          name: 'Room 1',
          description: 'A test room',
          exits: {},
          players: ['player1'],
        },
      };

      applyRoomUpdate(eventUpdates, updates, mergeRoomUpdate);

      expect(updates.room?.id).toBe('room1');
      expect(updates.room?.name).toBe('Room 1 Updated');
    });

    it('should not modify updates when room is undefined', () => {
      const eventUpdates: GameStateUpdates = {};
      const updates: Partial<{ room: Room | null }> = { room: null };

      applyRoomUpdate(eventUpdates, updates, mergeRoomUpdate);

      expect(updates.room).toBeNull();
    });
  });
});
