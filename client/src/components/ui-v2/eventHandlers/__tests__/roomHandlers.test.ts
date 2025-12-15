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

    it('should return undefined when no current room exists', () => {
      mockContext.currentRoomRef.current = null;
      const event = {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['player1'] },
      };
      const result = handleRoomOccupants(event, mockContext, vi.fn());
      expect(result).toBeUndefined();
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
  });
});
