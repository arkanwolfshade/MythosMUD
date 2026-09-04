/**
 * Tests for roomHandlers.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { Room } from '../../types';
import {
  __setOccupantDebugForTests,
  handleFollowState,
  handleGameState,
  handleRoomOccupants,
  handleRoomUpdate,
} from '../roomHandlers';
import type { EventHandlerContext } from '../types';

// Mock logger (info/debug used in OCCUPANT_DEBUG paths; warn for validation)
vi.mock('../../../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    debug: vi.fn(),
    warn: vi.fn(),
  },
}));

import { logger } from '../../../../utils/logger';

describe('roomHandlers', () => {
  const mockContext: EventHandlerContext = {
    currentPlayerRef: { current: null },
    currentRoomRef: { current: null },
    currentMessagesRef: { current: [] },
    healthStatusRef: { current: null },
    lucidityStatusRef: { current: null },
    lastDaypartRef: { current: null },
    lastHourRef: { current: null },
    lastQuarterHourRef: { current: null },
    lastHolidayIdsRef: { current: [] },
    lastRoomUpdateTime: { current: 0 },
    setDpStatus: vi.fn(),
    setLucidityStatus: vi.fn(),
    setMythosTime: vi.fn(),
    setIsDead: vi.fn(),
    setIsMortallyWounded: vi.fn(),
    setIsRespawning: vi.fn(),
    setIsDelirious: vi.fn(),
    setIsDeliriumRespawning: vi.fn(),
    setDeathLocation: vi.fn(),
    setDeliriumLocation: vi.fn(),
    setRescueState: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    __setOccupantDebugForTests(false);
  });

  afterEach(() => {
    __setOccupantDebugForTests(false);
  });

  describe('handleGameState', () => {
    it('should return player and room when both are valid', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toEqual(playerData);
      expect(result?.room?.id).toBe('room1');
    });

    it('should include occupants when room has players and npcs', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room', players: ['player1', 'player2'], npcs: [] };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupants).toEqual(['player1', 'player2']);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should derive empty occupants when room has no players or npcs', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should return null player when player name is not a string', () => {
      const playerData = { id: 'player1', name: 123 };
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
      expect(logger.warn).toHaveBeenCalled();
    });

    it('should return null player when player data is invalid (missing name)', () => {
      const playerData = { id: 'player1' }; // Missing name
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
      expect(result?.room?.id).toBe('room1');
    });

    it('should call logger.info when OCCUPANT_DEBUG is enabled (game_state branch)', () => {
      __setOccupantDebugForTests(true);
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room', players: ['p1'], npcs: [] };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(logger.info).toHaveBeenCalled();
    });

    it('should include occupants when player is null but room has players/npcs', () => {
      const playerData = { id: 'player1' }; // Missing name, will be null
      const roomData = { id: 'room1', name: 'Test Room', players: ['player1', 'player2'], npcs: [] };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
      expect(result?.room?.occupants).toEqual(['player1', 'player2']);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should return undefined when player data is missing', () => {
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should return undefined when room data is missing', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should include loginGracePeriodActive and loginGracePeriodRemaining when provided', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: playerData,
          room: roomData,
          login_grace_period_active: true,
          login_grace_period_remaining: 30,
        },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.loginGracePeriodActive).toBe(true);
      expect(result?.loginGracePeriodRemaining).toBe(30);
    });

    it('should include followingTarget when following is provided in game_state', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const following = { target_name: 'Bob', target_type: 'player' as const };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData, following },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.followingTarget).toEqual(following);
    });

    it('should return only followingTarget when player/room missing but following provided', () => {
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { following: { target_name: 'Guard', target_type: 'npc' as const } },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toEqual({ followingTarget: { target_name: 'Guard', target_type: 'npc' } });
    });

    it('should set followingTarget to null when following is null in payload', () => {
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { following: null },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toEqual({ followingTarget: null });
    });
  });

  describe('handleFollowState', () => {
    it('should return followingTarget when following is provided', () => {
      const event = {
        event_type: 'follow_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { following: { target_name: 'Alice', target_type: 'player' as const } },
      };
      const result = handleFollowState(event, mockContext, vi.fn());
      expect(result).toEqual({ followingTarget: { target_name: 'Alice', target_type: 'player' } });
    });

    it('should return followingTarget null when following is null', () => {
      const event = {
        event_type: 'follow_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { following: null },
      };
      const result = handleFollowState(event, mockContext, vi.fn());
      expect(result).toEqual({ followingTarget: null });
    });

    it('should return followingTarget null when following is undefined', () => {
      const event = {
        event_type: 'follow_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const result = handleFollowState(event, mockContext, vi.fn());
      expect(result).toEqual({ followingTarget: null });
    });
  });

  describe('handleRoomUpdate', () => {
    it('should create initial room state when no existing room', () => {
      mockContext.currentRoomRef.current = null;
      const roomData = { id: 'room1', name: 'Test Room', description: 'A test room' };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should preserve occupants when room ID does not change', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: ['player1'],
        npcs: [],
        occupants: ['player1'],
        occupant_count: 1,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = { id: 'room1', name: 'Updated Room', description: 'Updated description' };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.name).toBe('Updated Room');
      expect(result?.room?.occupants).toEqual(['player1']);
      expect(result?.room?.occupant_count).toBe(1);
    });

    it('should use nullish coalescing for players and npcs when they are null/undefined', () => {
      // Room type is string[] | undefined; we pass null to assert handler uses ?? correctly at runtime.
      const existingRoom = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: null,
        npcs: undefined,
        occupants: null,
        occupant_count: null,
      } as unknown as Partial<Room>;
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = { id: 'room1', name: 'Updated Room' };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      // Should use ?? operator to default to [] for players and occupants, 0 for count
      expect(result?.room?.players).toEqual([]);
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
      // npcs can be undefined (no ?? operator for npcs)
      expect(result?.room?.npcs).toBeUndefined();
    });

    it('should clear occupants when room ID changes', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: ['player1'],
        npcs: [],
        occupants: ['player1'],
        occupant_count: 1,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = { id: 'room2', name: 'New Room', description: 'A new room' };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room2');
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should use room_data when room is null (getRoomDataFromEvent fallback)', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: null,
          room_data: { id: 'room1', name: 'Fallback Room', description: '', exits: {}, players: [], npcs: [] },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.name).toBe('Fallback Room');
    });

    it('should handle room_data field instead of room field', () => {
      mockContext.currentRoomRef.current = null;
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room_data: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
    });

    it('should return undefined when room data is missing', () => {
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should use payload occupants when room_update has occupants and existing room had empty (entering-player fix)', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = {
        id: 'room1',
        name: 'Updated Room',
        description: 'Updated description',
        players: ['OtherPlayer'],
        npcs: [],
        occupants: ['OtherPlayer'],
        occupant_count: 1,
      };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.occupants).toEqual(['OtherPlayer']);
      expect(result?.room?.players).toEqual(['OtherPlayer']);
      expect(result?.room?.occupant_count).toBe(1);
    });

    it('should call logger.debug when using payload occupants (createRoomUpdateWithPreservedOccupants branch)', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = {
        id: 'room1',
        name: 'Updated Room',
        players: ['A', 'B'],
        npcs: ['npc1'],
        occupants: ['A', 'B', 'npc1'],
        occupant_count: 3,
      };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      handleRoomUpdate(event, mockContext, vi.fn());
      expect(vi.mocked(logger.debug)).toHaveBeenCalledWith(
        'roomHandlers',
        'room_update: using payload occupants (entering-player fix)',
        expect.objectContaining({ occupants: 3, players: 2 })
      );
    });

    it('should use top-level players and npcs when room_update has data.occupants (legacy removed; prefer structured)', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Test Room', description: 'A room' },
          entities: [],
          occupants: ['Alice', 'Bob'],
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      // Legacy occupants-only format removed; without players/npcs we get empty structured data
      expect(result?.room?.players).toEqual([]);
      expect(result?.room?.npcs).toEqual([]);
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should use top-level players and npcs when room_update has data.players and data.npcs', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Test Room', description: 'A room' },
          players: ['Alice', 'Bob'],
          npcs: ['Guard'],
          occupant_count: 3,
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['Alice', 'Bob']);
      expect(result?.room?.npcs).toEqual(['Guard']);
      expect(result?.room?.occupant_count).toBe(3);
    });

    it('should use payload occupants when payload has only npcs (hasOccupantData via npcs)', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const roomData = {
        id: 'room1',
        name: 'Updated Room',
        description: 'Updated description',
        players: [],
        npcs: ['npc1', 'npc2'],
        occupants: ['npc1', 'npc2'],
        occupant_count: 2,
      };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: roomData },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.npcs).toEqual(['npc1', 'npc2']);
      expect(result?.room?.occupants).toEqual(['npc1', 'npc2']);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should treat raw room npcs as empty array when topNpcs undefined and raw.npcs non-array', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room1',
            name: 'Room',
            description: '',
            exits: {},
            players: ['p1'],
            npcs: 'malformed' as unknown,
          },
          players: ['p1'],
          npcs: undefined,
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.npcs).toEqual([]);
    });

    it('should treat top-level players as empty array when non-array (getRoomDataFromEvent)', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Room', description: '', exits: {} },
          players: 'not-array' as unknown,
          npcs: ['n1'],
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual([]);
      expect(result?.room?.npcs).toEqual(['n1']);
    });

    it('should handle payload with npcs as non-array (getRoomDataFromEvent Array.isArray branch)', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: ['p1'],
        npcs: ['n1'],
        occupants: ['p1', 'n1'],
        occupant_count: 2,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Room', description: '', exits: {} },
          players: ['p1', 'p2'],
          npcs: 'not-an-array' as unknown, // malformed; should fallback to []
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['p1', 'p2']);
      expect(result?.room?.npcs).toEqual([]);
    });

    it('should use existing npcs when payload has players but npcs undefined (createRoomUpdateWithPreservedOccupants)', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: ['p1'],
        npcs: ['n1', 'n2'],
        occupants: ['p1', 'n1', 'n2'],
        occupant_count: 3,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room1',
            name: 'Room',
            description: '',
            exits: {},
            players: ['p1', 'p2'],
            npcs: undefined,
          },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['p1', 'p2']);
      expect(result?.room?.npcs).toEqual(['n1', 'n2']);
    });

    it('should handle room_data with npcs as non-array in createRoomUpdateWithPreservedOccupants', () => {
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: ['p1'],
        npcs: ['n1'],
        occupants: ['p1', 'n1'],
        occupant_count: 2,
      };
      mockContext.currentRoomRef.current = existingRoom as Room;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room_data: {
            id: 'room1',
            name: 'Room',
            description: '',
            exits: {},
            players: ['p1'],
            npcs: 'malformed' as unknown, // hasOccupantData via players; npcs non-array -> []
          },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['p1']);
      expect(result?.room?.npcs).toEqual([]);
    });

    it('should call logger.info when OCCUPANT_DEBUG is enabled (room_update initial branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Test', description: '', exits: {}, players: [], npcs: [] },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(logger.info).toHaveBeenCalled();
    });

    it('should call logger.info when OCCUPANT_DEBUG is enabled (room_update merge branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test',
        description: '',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: { id: 'room1', name: 'Test', description: '', exits: {}, players: ['p1'], npcs: [] },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(logger.info).toHaveBeenCalled();
    });

    it('should call logger.info when OCCUPANT_DEBUG is enabled (room_occupants minimal branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1'], npcs: [] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(logger.info).toHaveBeenCalled();
    });

    it('should call logger.info when OCCUPANT_DEBUG is enabled (room_occupants structured branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test',
        description: '',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1'], npcs: [] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(logger.info).toHaveBeenCalled();
    });

    it('should use raw room when topPlayers and topNpcs both undefined (getRoomDataFromEvent early return)', () => {
      mockContext.currentRoomRef.current = null;
      const rawRoom = {
        id: 'room1',
        name: 'Test Room',
        description: 'A room',
        exits: {},
        players: ['Alice'],
        npcs: ['Guard'],
      };
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: rawRoom },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['Alice']);
      expect(result?.room?.npcs).toEqual(['Guard']);
    });

    it('should create initial room with occupant_count 0 when roomData.occupant_count is 0', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room1',
            name: 'Test Room',
            description: 'A room',
            exits: {},
            players: [],
            npcs: [],
            occupant_count: 0,
          },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should create initial room with empty arrays when roomData.players is not an array', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room1',
            name: 'Test Room',
            description: 'A room',
            players: null,
            npcs: undefined,
            occupants: null,
          },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual([]);
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });

    it('should create initial room with empty arrays when roomData.npcs is not an array', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room1',
            name: 'Test Room',
            description: 'A room',
            players: [],
            npcs: 'not-array' as unknown,
          },
        },
      };
      const result = handleRoomUpdate(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.npcs).toEqual([]);
    });
  });

  describe('handleRoomOccupants', () => {
    beforeEach(() => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
    });

    it('should update room with structured format (players and npcs)', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['player1', 'player2'], npcs: ['npc1'], count: 3 },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['player1', 'player2']);
      expect(result?.room?.npcs).toEqual(['npc1']);
      expect(result?.room?.occupant_count).toBe(3);
      expect(result?.room?.occupants).toEqual(['player1', 'player2', 'npc1']);
    });

    it('should use calculated count when count is not provided', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['player1'], npcs: ['npc1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should not update when room IDs do not match', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room2', // Different room ID
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should return undefined when no current room exists and no occupant data', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: {},
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should return undefined when room_occupants has no players or npcs (both undefined)', () => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: ['p1'],
        npcs: [],
        occupants: ['p1'],
        occupant_count: 1,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: {},
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should return undefined when room_occupants room_id does not match current room', () => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room2',
        data: { players: ['player1'], npcs: [] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
      expect(logger.warn).toHaveBeenCalled();
    });

    it('should create minimal room from room_occupants when no current room (entering-player race fix)', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['player1', 'player2'], npcs: ['npc1'], count: 3 },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.players).toEqual(['player1', 'player2']);
      expect(result?.room?.npcs).toEqual(['npc1']);
      expect(result?.room?.occupants).toEqual(['player1', 'player2', 'npc1']);
      expect(result?.room?.occupant_count).toBe(3);
    });

    it('should create minimal room using occupants.length when count is undefined', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1', 'p2'], npcs: ['n1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupant_count).toBe(3);
    });

    it('should create minimal room with combined players and npcs when occupants is not an array', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1'], npcs: ['n1'], occupants: 'not-an-array' },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.id).toBe('room1');
      expect(result?.room?.players).toEqual(['p1']);
      expect(result?.room?.npcs).toEqual(['n1']);
      expect(result?.room?.occupants).toEqual(['p1', 'n1']);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should preserve existing players when only npcs provided', () => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: ['existingPlayer'],
        npcs: [],
        occupants: ['existingPlayer'],
        occupant_count: 1,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { npcs: ['npc1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['existingPlayer']);
      expect(result?.room?.npcs).toEqual(['npc1']);
    });

    it('should use default empty array when event and room both have no players (getValueOrDefault)', () => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: undefined,
        npcs: ['n1'],
        occupants: ['n1'],
        occupant_count: 1,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { npcs: ['n1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual([]);
    });

    it('should preserve existing npcs when only players provided', () => {
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: [],
        npcs: ['existingNpc'],
        occupants: ['existingNpc'],
        occupant_count: 1,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['player1']);
      expect(result?.room?.npcs).toEqual(['existingNpc']);
    });

    it('should handle event without room_id (should still update)', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.players).toEqual(['player1']);
    });

    it('should handle event with invalid room_id type', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 123 as unknown as string, // Invalid type
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      // Should return undefined when room_id doesn't match (invalid type won't match string)
      expect(result).toBeUndefined();
    });

    it('should handle event with undefined room_id', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: undefined,
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
    });

    it('should return undefined when event has only occupants (legacy format removed)', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { occupants: ['player1', 'player2'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should handle event with non-array occupants', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { occupants: 'not-an-array' },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should return undefined when both players and npcs are undefined and occupants is not an array', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: {}, // No players, npcs, or valid occupants
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should use default empty arrays when both event and room data are undefined', () => {
      // Set up room with undefined players (to test getValueOrDefault default path)
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: undefined, // Room has undefined players
        npcs: undefined, // Room has undefined npcs
        // occupants and occupant_count are also undefined
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: {
          // Provide npcs as empty array to trigger structured format path
          // But players is not provided (undefined), and room also has undefined players
          // This will test getValueOrDefault returning [] when both are undefined
          npcs: [],
          // players is not in data, so it's undefined
        },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      // Should use empty array as default for players (both event and room have undefined)
      // npcs should be [] from event data
      expect(result?.room?.players).toEqual([]);
      expect(result?.room?.npcs).toEqual([]);
      expect(result?.room?.occupants).toEqual([]);
      expect(result?.room?.occupant_count).toBe(0);
    });
  });

  describe('OCCUPANT_DEBUG branches', () => {
    it('should log when OCCUPANT_DEBUG is true in handleGameState', () => {
      __setOccupantDebugForTests(true);
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room', players: ['player1'], npcs: [] };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData },
      };
      handleGameState(event, mockContext, vi.fn());
      expect(vi.mocked(logger.info)).toHaveBeenCalledWith(
        'roomHandlers',
        'OCCUPANT_DEBUG: game_state setting room',
        expect.objectContaining({ occupants_from_payload: 1, result_occupant_count: 1 })
      );
    });

    it('should log when OCCUPANT_DEBUG is true in handleRoomUpdate (initial branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: { id: 'room1', name: 'Test Room', occupants: ['a'] } },
      };
      handleRoomUpdate(event, mockContext, vi.fn());
      expect(vi.mocked(logger.info)).toHaveBeenCalledWith(
        'roomHandlers',
        'OCCUPANT_DEBUG: room_update branch=initial (no existingRoom)',
        expect.any(Object)
      );
    });

    it('should log when OCCUPANT_DEBUG is true in handleRoomUpdate (merge branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
      const event = {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room: { id: 'room1', name: 'Updated Room', occupants: ['a'] } },
      };
      handleRoomUpdate(event, mockContext, vi.fn());
      expect(vi.mocked(logger.info)).toHaveBeenCalledWith(
        'roomHandlers',
        'OCCUPANT_DEBUG: room_update branch=merge (had existingRoom)',
        expect.any(Object)
      );
    });

    it('should log when OCCUPANT_DEBUG is true in handleRoomOccupants (minimal branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1'] },
      };
      handleRoomOccupants(event, mockContext, vi.fn());
      expect(vi.mocked(logger.info)).toHaveBeenCalledWith(
        'roomHandlers',
        'OCCUPANT_DEBUG: room_occupants branch=minimal (no currentRoom)',
        expect.any(Object)
      );
    });

    it('should log when OCCUPANT_DEBUG is true in handleRoomOccupants (structured branch)', () => {
      __setOccupantDebugForTests(true);
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
        players: [],
        npcs: [],
        occupants: [],
        occupant_count: 0,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['p1'], npcs: ['n1'] },
      };
      handleRoomOccupants(event, mockContext, vi.fn());
      expect(vi.mocked(logger.info)).toHaveBeenCalledWith(
        'roomHandlers',
        'OCCUPANT_DEBUG: room_occupants branch=structured',
        expect.any(Object)
      );
    });
  });

  describe('handleGameState edge cases', () => {
    it('should handle player data that is not an object', () => {
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: 'not-an-object', room: { id: 'room1', name: 'Test Room' } },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      // Should return result with null player when player data is invalid
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
    });

    it('should handle player data that is null', () => {
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: null, room: { id: 'room1', name: 'Test Room' } },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
    });

    it('should handle player with name that is not a string', () => {
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: { id: 'player1', name: 123 }, room: { id: 'room1', name: 'Test Room' } },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
    });
  });
});
