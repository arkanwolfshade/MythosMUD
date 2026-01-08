// Room-related event handlers
// As documented in "Room State Architecture" - Dr. Armitage, 1928

import { logger } from '../../../utils/logger';
import type { Player, Room } from '../types';
import type { EventHandler } from './types';

export const handleGameState: EventHandler = (event, _context) => {
  const playerData = event.data.player as unknown;
  const roomData = event.data.room as unknown;
  const occupants = event.data.occupants as string[] | undefined;
  const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
  const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
  if (playerData && roomData) {
    // Validate that playerData has at least the required 'name' property
    const player = playerData as Player;
    if (typeof player === 'object' && player !== null && 'name' in player && typeof player.name === 'string') {
      return {
        player,
        room: {
          ...(roomData as Room),
          ...(occupants && { occupants, occupant_count: occupants.length }),
        },
        ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
        ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
      };
    } else {
      logger.warn('roomHandlers', 'handleGameState: invalid player data, missing name property');
      return {
        player: null,
        room: {
          ...(roomData as Room),
          ...(occupants && { occupants, occupant_count: occupants.length }),
        },
        ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
        ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
      };
    }
  }
};

/**
 * Strips occupant-related fields from room data to prevent data leakage
 */
function extractRoomMetadata(roomData: Room): Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'> {
  /* eslint-disable @typescript-eslint/no-unused-vars */
  const {
    players: _players,
    npcs: _npcs,
    occupants: _occupants,
    occupant_count: _occupant_count,
    ...roomMetadata
  } = roomData;
  /* eslint-enable @typescript-eslint/no-unused-vars */
  return roomMetadata;
}

/**
 * Creates a room update that preserves occupant data from existing room
 */
function createRoomUpdateWithPreservedOccupants(
  existingRoom: Room,
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomIdChanged: boolean
): Room {
  const roomUpdate: Partial<Room> = {
    ...existingRoom,
    ...roomMetadata,
    // Preserve ALL occupant data from existingRoom
    players: existingRoom.players ?? [],
    npcs: existingRoom.npcs,
    occupants: existingRoom.occupants ?? [],
    occupant_count: existingRoom.occupant_count ?? 0,
  };

  // If room ID changed, clear occupants
  if (roomIdChanged) {
    roomUpdate.players = [];
    roomUpdate.npcs = undefined;
    roomUpdate.occupants = [];
    roomUpdate.occupant_count = 0;
  }

  return roomUpdate as Room;
}

/**
 * Creates initial room state without occupants for first room_update
 */
function createInitialRoomState(roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>): Room {
  return {
    ...roomMetadata,
    players: [],
    occupants: [],
    occupant_count: 0,
  };
}

export const handleRoomUpdate: EventHandler = (event, context) => {
  const roomData = (event.data.room || event.data.room_data) as Room;
  if (!roomData) {
    return;
  }

  const roomMetadata = extractRoomMetadata(roomData);
  const existingRoom = context.currentRoomRef.current;

  if (!existingRoom) {
    // First room_update - initialize WITHOUT occupants
    return { room: createInitialRoomState(roomMetadata) };
  }

  const roomIdChanged = roomData.id !== existingRoom.id;
  return { room: createRoomUpdateWithPreservedOccupants(existingRoom, roomMetadata, roomIdChanged) };
};

/**
 * Validates that the event room ID matches the current room ID
 * Returns false if there's a mismatch, true otherwise
 */
function validateRoomIdMatch(eventRoomId: string | undefined, currentRoomId: string, npcsCount: number): boolean {
  if (!eventRoomId) {
    return true;
  }
  if (eventRoomId === currentRoomId) {
    return true;
  }
  // Log mismatch warning with simplified message
  const message =
    `room_occupants event room_id mismatch - ignoring (event: ${eventRoomId}, ` +
    `current: ${currentRoomId}, npcs: ${npcsCount})`;
  logger.warn('roomHandlers', message);
  return false;
}

/**
 * Gets a value from event data or falls back to room data, with empty array as final fallback
 */
function getValueOrDefault<T>(eventValue: T | undefined, roomValue: T | undefined, defaultValue: T): T {
  if (eventValue !== undefined) {
    return eventValue;
  }
  if (roomValue !== undefined) {
    return roomValue;
  }
  return defaultValue;
}

/**
 * Gets the final NPCs list, preferring event data over existing room data
 */
function getFinalNpcs(npcs: string[] | undefined, currentRoom: Room): string[] {
  return getValueOrDefault(npcs, currentRoom.npcs, []);
}

/**
 * Gets the final players list, preferring event data over existing room data
 */
function getFinalPlayers(players: string[] | undefined, currentRoom: Room): string[] {
  return getValueOrDefault(players, currentRoom.players, []);
}

/**
 * Calculates the occupant count, preferring provided count over calculated value
 */
function calculateOccupantCount(occupantCount: number | undefined, players: string[], npcs: string[]): number {
  if (occupantCount !== undefined) {
    return occupantCount;
  }
  return players.length + npcs.length;
}

/**
 * Handles structured format with separate players and npcs arrays
 */
function handleStructuredOccupantsFormat(
  currentRoom: Room,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupantCount: number | undefined
): Room {
  const finalNpcs = getFinalNpcs(npcs, currentRoom);
  const finalPlayers = getFinalPlayers(players, currentRoom);
  const finalOccupantCount = calculateOccupantCount(occupantCount, finalPlayers, finalNpcs);

  return {
    ...currentRoom,
    players: finalPlayers,
    npcs: finalNpcs,
    occupants: [...finalPlayers, ...finalNpcs],
    occupant_count: finalOccupantCount,
  };
}

/**
 * Handles legacy format with a single occupants array
 */
function handleLegacyOccupantsFormat(currentRoom: Room, occupants: string[], occupantCount: number | undefined): Room {
  const finalOccupantCount = occupantCount !== undefined ? occupantCount : occupants.length;
  const finalPlayers = currentRoom.players || [];
  const finalNpcs = currentRoom.npcs || [];

  return {
    ...currentRoom,
    occupants: occupants,
    occupant_count: finalOccupantCount,
    players: finalPlayers,
    npcs: finalNpcs,
  };
}

export const handleRoomOccupants: EventHandler = (event, context) => {
  const players = event.data.players as string[] | undefined;
  const npcs = event.data.npcs as string[] | undefined;
  const occupants = event.data.occupants as string[] | undefined;
  const occupantCount = event.data.count as number | undefined;
  const eventRoomId = event.room_id as string | undefined;

  const currentRoom = context.currentRoomRef.current;
  if (!currentRoom) {
    logger.warn('roomHandlers', 'room_occupants event received but no room state available');
    return;
  }

  // Only update if room IDs match
  if (!validateRoomIdMatch(eventRoomId, currentRoom.id, npcs?.length ?? 0)) {
    return;
  }

  // Use structured format if available
  if (players !== undefined || npcs !== undefined) {
    return { room: handleStructuredOccupantsFormat(currentRoom, players, npcs, occupantCount) };
  }

  // Legacy format
  if (occupants && Array.isArray(occupants)) {
    return { room: handleLegacyOccupantsFormat(currentRoom, occupants, occupantCount) };
  }
};
