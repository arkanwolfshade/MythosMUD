/**
 * Tests for stateUpdateUtils.
 */

import { describe, expect, it, vi } from 'vitest';
import type { GameStateUpdates } from '../../eventHandlers/types';
import type { ChatMessage, Player, Room } from '../../types';
import type { GameState } from '../stateUpdateUtils';
import {
  applyEventUpdates,
  applyPlayerUpdate,
  applyRoomUpdate,
  mergeOccupantData,
  mergeRoomUpdate,
  sanitizeAndApplyUpdates,
} from '../stateUpdateUtils';

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

    it('should treat non-array players as empty array (Array.isArray branch)', () => {
      const newRoom = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {} as Record<string, string>,
        players: 'malformed' as unknown as string[],
        npcs: [],
      };

      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {},
        players: ['p1'],
        npcs: [],
      };

      const result = mergeOccupantData(newRoom as Room, existingRoom);
      expect(result.players).toEqual([]);
      expect(result.npcs).toEqual([]);
    });

    it('should treat non-array npcs as empty array when new room has occupant data (Array.isArray branch)', () => {
      const newRoom = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {} as Record<string, string>,
        players: ['p1'], // hasOccupantData true -> use newRoom values
        npcs: { foo: 1 } as unknown as string[], // non-array -> fallback to []
      };

      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {},
        players: [],
        npcs: ['n1'],
      };

      const result = mergeOccupantData(newRoom as Room, existingRoom);
      expect(result.players).toEqual(['p1']);
      expect(result.npcs).toEqual([]);
    });

    it('should use occupants.length when existingRoom.occupant_count is undefined (useNewOccupants false)', () => {
      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {},
        players: [],
        npcs: [],
      };

      const existingRoom = {
        id: 'room1',
        name: 'Room 1',
        description: '',
        exits: {} as Record<string, string>,
        players: ['p1', 'p2'],
        npcs: ['n1'],
        occupant_count: undefined,
      };

      const result = mergeOccupantData(newRoom, existingRoom as Room);
      expect(result.occupant_count).toBe(3);
    });

    it('should preserve existing occupants when new room has empty arrays (room_update after room_occupants)', () => {
      const newRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      };

      const existingRoom: Room = {
        id: 'room1',
        name: 'Room 1',
        description: 'A test room',
        exits: {},
        players: ['player1', 'player2'],
        npcs: ['npc1'],
        occupants: ['player1', 'player2', 'npc1'],
        occupant_count: 3,
      };

      const result = mergeOccupantData(newRoom, existingRoom);
      expect(result.players).toEqual(['player1', 'player2']);
      expect(result.npcs).toEqual(['npc1']);
      expect(result.occupants).toEqual(['player1', 'player2', 'npc1']);
      expect(result.occupant_count).toBe(3);
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

  // applyMessageUpdates is tested through applyEventUpdates

  describe('applyEventUpdates', () => {
    it('should apply all update types when present', () => {
      const eventUpdates: GameStateUpdates = {
        player: { id: 'player1', name: 'Player' } as Player,
        room: { id: 'room1', name: 'Room', description: 'Desc', exits: {} },
        messages: [
          { text: 'Message 1', timestamp: new Date().toISOString(), isHtml: false },
          { text: 'Message 2', timestamp: new Date().toISOString(), isHtml: false },
        ],
      };

      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [{ text: 'Existing', timestamp: new Date().toISOString(), isHtml: false }];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.player).toBeDefined();
      expect(updates.room).toBeDefined();
      expect(updates.messages).toBeDefined();
      expect(updates.messages).toHaveLength(3);
    });

    it('should append messages to existing updates.messages', () => {
      const eventUpdates: GameStateUpdates = {
        messages: [{ text: 'New', timestamp: new Date().toISOString(), isHtml: false }],
      };

      const updates: Partial<GameState> = {
        messages: [{ text: 'Existing in updates', timestamp: new Date().toISOString(), isHtml: false }],
      };
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.messages).toHaveLength(2);
      expect(updates.messages?.[0].text).toBe('Existing in updates');
    });

    it('should not modify updates when messages are undefined', () => {
      const eventUpdates: GameStateUpdates = {};
      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.messages).toBeUndefined();
    });

    it('should not modify updates when eventUpdates is undefined', () => {
      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(undefined, updates, currentMessages);

      expect(Object.keys(updates)).toHaveLength(0);
    });

    it('should not modify updates when eventUpdates is void', () => {
      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(undefined, updates, currentMessages);

      expect(Object.keys(updates)).toHaveLength(0);
    });

    it('should apply followingTarget when present', () => {
      const eventUpdates: GameStateUpdates = {
        followingTarget: { target_name: 'Alice', target_type: 'player' },
      };

      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.followingTarget).toEqual({ target_name: 'Alice', target_type: 'player' });
    });

    it('should apply loginGracePeriodActive and loginGracePeriodRemaining when present', () => {
      const eventUpdates: GameStateUpdates = {
        loginGracePeriodActive: true,
        loginGracePeriodRemaining: 30,
      };

      const updates: Partial<GameState> = {};
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.loginGracePeriodActive).toBe(true);
      expect(updates.loginGracePeriodRemaining).toBe(30);
    });

    it('should apply followingTarget null when explicitly set', () => {
      const eventUpdates: GameStateUpdates = { followingTarget: null };

      const updates: Partial<GameState> = { followingTarget: { target_name: 'Old', target_type: 'player' } };
      const currentMessages: ChatMessage[] = [];

      applyEventUpdates(eventUpdates, updates, currentMessages);

      expect(updates.followingTarget).toBeNull();
    });
  });

  describe('sanitizeAndApplyUpdates', () => {
    it('should not call setGameState when updates are empty', () => {
      const setGameState = vi.fn();

      sanitizeAndApplyUpdates({}, setGameState);

      expect(setGameState).not.toHaveBeenCalled();
    });

    it('should call setGameState with merged updates', () => {
      const setGameState = vi.fn(updater => {
        const prevState: GameState = {
          player: null,
          room: null,
          messages: [],
          commandHistory: [],
        };
        if (typeof updater === 'function') {
          return updater(prevState);
        }
        return updater;
      });

      const updates: Partial<GameState> = {
        player: { id: 'player1', name: 'Player' } as Player,
      };

      sanitizeAndApplyUpdates(updates, setGameState);

      expect(setGameState).toHaveBeenCalled();
    });

    it('should merge room state when room update is present', () => {
      const setGameState = vi.fn(updater => {
        const prevState: GameState = {
          player: null,
          room: { id: 'room1', name: 'Old Room', description: 'Old', exits: {} },
          messages: [],
          commandHistory: [],
        };
        if (typeof updater === 'function') {
          return updater(prevState);
        }
        return updater;
      });

      const updates: Partial<GameState> = {
        room: { id: 'room1', name: 'New Room', description: 'New', exits: {} },
      };

      sanitizeAndApplyUpdates(updates, setGameState);

      expect(setGameState).toHaveBeenCalled();
    });

    it('should preserve previous player when update has no player', () => {
      const prevPlayer = { id: 'player1', name: 'Player' } as Player;
      const setGameState = vi.fn(updater => {
        const prevState: GameState = {
          player: prevPlayer,
          room: null,
          messages: [],
          commandHistory: [],
        };
        if (typeof updater === 'function') {
          return updater(prevState);
        }
        return updater;
      });

      const updates: Partial<GameState> = {
        messages: [{ text: 'Test', timestamp: new Date().toISOString(), isHtml: false }],
      };

      sanitizeAndApplyUpdates(updates, setGameState);

      expect(setGameState).toHaveBeenCalled();
      const callArg = setGameState.mock.calls[0][0];
      const result =
        typeof callArg === 'function'
          ? callArg({ player: prevPlayer, room: null, messages: [], commandHistory: [] } as GameState)
          : callArg;
      expect(result.player).toEqual(prevPlayer);
    });
  });
});
