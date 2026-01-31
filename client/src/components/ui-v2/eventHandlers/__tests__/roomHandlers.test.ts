/**
 * Tests for roomHandlers.
 */

import { describe, expect, it, vi } from 'vitest';
import type { Room } from '../../types';
import { handleGameState, handleRoomOccupants, handleRoomUpdate } from '../roomHandlers';
import type { EventHandlerContext } from '../types';

// Mock logger
vi.mock('../../../utils/logger', () => ({
  logger: {
    warn: vi.fn(),
  },
}));

describe('roomHandlers', () => {
  const mockContext: EventHandlerContext = {
    currentPlayerRef: { current: null },
    currentRoomRef: { current: null },
    currentMessagesRef: { current: [] },
    healthStatusRef: { current: null },
    lucidityStatusRef: { current: null },
    lastDaypartRef: { current: null },
    lastHourRef: { current: null },
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

    it('should include occupants when provided', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const occupants = ['player1', 'player2'];
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData, occupants },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupants).toEqual(occupants);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should not include occupants when occupants is undefined', () => {
      const playerData = { id: 'player1', name: 'TestPlayer' };
      const roomData = { id: 'room1', name: 'Test Room' };
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData }, // occupants not provided
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupants).toBeUndefined();
      expect(result?.room?.occupant_count).toBeUndefined();
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

    it('should include occupants when player is null but occupants are provided', () => {
      const playerData = { id: 'player1' }; // Missing name, will be null
      const roomData = { id: 'room1', name: 'Test Room' };
      const occupants = ['player1', 'player2'];
      const event = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: playerData, room: roomData, occupants },
      };
      const result = handleGameState(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.player).toBeNull();
      expect(result?.room?.occupants).toEqual(occupants);
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
      const existingRoom: Partial<Room> = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: null, // null value
        npcs: undefined, // undefined value
        occupants: null,
        occupant_count: null,
      };
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

    it('should use top-level occupants when room_update has data.occupants (initial room state shape)', () => {
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
      expect(result?.room?.occupants).toEqual(['Alice', 'Bob']);
      expect(result?.room?.occupant_count).toBe(2);
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

    it('should handle legacy format with occupants array', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { occupants: ['player1', 'player2'], count: 2 },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupants).toEqual(['player1', 'player2']);
      expect(result?.room?.occupant_count).toBe(2);
    });

    it('should use existing players and npcs when handling legacy format', () => {
      // Set up room with existing players and npcs
      mockContext.currentRoomRef.current = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test Room Description',
        exits: {},
        players: ['existingPlayer'],
        npcs: ['existingNpc'],
        occupants: ['existingPlayer', 'existingNpc'],
        occupant_count: 2,
      } as Room;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { occupants: ['player1', 'player2'] }, // Legacy format
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      // Should preserve existing players and npcs (truthy values use || operator)
      expect(result?.room?.players).toEqual(['existingPlayer']);
      expect(result?.room?.npcs).toEqual(['existingNpc']);
      expect(result?.room?.occupants).toEqual(['player1', 'player2']); // New occupants from event
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

    it('should handle event with only occupants and no count', () => {
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { occupants: ['player1', 'player2'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeDefined();
      expect(result?.room?.occupant_count).toBe(2);
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
