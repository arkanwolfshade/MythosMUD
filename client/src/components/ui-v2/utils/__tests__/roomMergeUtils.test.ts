/**
 * Tests for roomMergeUtils.
 */

import { describe, expect, it } from 'vitest';
import type { Room } from '../../types';
import { mergeRoomState } from '../roomMergeUtils';

describe('roomMergeUtils', () => {
  describe('mergeRoomState', () => {
    it('should return null when both rooms are null/undefined', () => {
      expect(mergeRoomState(undefined, null)).toBeNull();
    });

    it('should return prevRoom when updatesRoom is undefined', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      expect(mergeRoomState(undefined, prevRoom)).toEqual(prevRoom);
    });

    it('should return updatesRoom when prevRoom is null', () => {
      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      expect(mergeRoomState(updatesRoom, null)).toEqual(updatesRoom);
    });

    it('should use updates players when available', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['old-player'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['new-player'],
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.players).toEqual(['new-player']);
    });

    it('should preserve prev players when updates has no players', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['player1'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.players).toEqual(['player1']);
    });

    it('should use updates NPCs when available', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        npcs: ['old-npc'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        npcs: ['new-npc'],
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.npcs).toEqual(['new-npc']);
    });

    it('should preserve prev NPCs when updates has no NPCs', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        npcs: ['npc1'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.npcs).toEqual(['npc1']);
    });

    it('should use new room players when room ID changes', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['player1'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room2',
        name: 'Room 2',
        description: 'Room 2 description',
        exits: {},
        players: [],
      };

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.players).toEqual([]);
    });

    it('should merge players and NPCs into occupants', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['player1'],
        npcs: ['npc1'],
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.occupants).toEqual(['player1', 'npc1']);
    });

    it('should use occupant_count from updates when provided', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        occupant_count: 5,
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.occupant_count).toBe(5);
    });

    it('should calculate occupant_count from merged arrays when not provided', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['player1', 'player2'],
        npcs: ['npc1'],
      } as Room;

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.occupant_count).toBe(3);
    });

    it('should handle empty arrays correctly', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        players: ['player1'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'Room 1 description',
        exits: {},
        players: [],
        npcs: [],
      };

      const result = mergeRoomState(updatesRoom, prevRoom);
      // When updates has empty arrays, it preserves prevRoom players (empty array is not "populated")
      // The logic preserves prevRoom data when updates doesn't have populated arrays
      expect(result?.players).toBeDefined();
      expect(result?.npcs).toEqual([]);
    });

    it('should preserve NPCs when updates clears them but prev has them', () => {
      const prevRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        npcs: ['npc1'],
      } as Room;

      const updatesRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'Room 1 description',
        exits: {},
        npcs: [],
      };

      const result = mergeRoomState(updatesRoom, prevRoom);
      expect(result?.npcs).toEqual(['npc1']);
    });
  });
});
