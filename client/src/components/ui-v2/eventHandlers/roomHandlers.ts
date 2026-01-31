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
    const roomWithOccupants = {
      ...(roomData as Room),
      ...(occupants && { occupants, occupant_count: occupants.length }),
    };
    const occupantCount = roomWithOccupants.occupants?.length ?? roomWithOccupants.occupant_count ?? 0;
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: game_state setting room', {
      occupants_from_payload: occupants?.length ?? 0,
      result_occupant_count: occupantCount,
    });
    // Validate that playerData has at least the required 'name' property
    const player = playerData as Player;
    if (typeof player === 'object' && player !== null && 'name' in player && typeof player.name === 'string') {
      return {
        player,
        room: roomWithOccupants,
        ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
        ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
      };
    }
    logger.warn('roomHandlers', 'handleGameState: invalid player data, missing name property');
    return {
      player: null,
      room: roomWithOccupants,
      ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
      ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
    };
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

/** True when room has at least one player, NPC, or occupant (used to prefer payload over existing). */
function hasOccupantData(room: Room): boolean {
  const hasPlayers = room.players != null && room.players.length > 0;
  const hasNpcs = room.npcs != null && room.npcs.length > 0;
  const hasOccupants = room.occupants != null && room.occupants.length > 0;
  return hasPlayers || hasNpcs || hasOccupants;
}

/**
 * Creates a room update. When payloadRoom has occupant data (e.g. entering-player room_update),
 * use it; otherwise preserve existing room occupants.
 */
function createRoomUpdateWithPreservedOccupants(
  existingRoom: Room,
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomIdChanged: boolean,
  payloadRoom?: Room
): Room {
  const usePayloadOccupants = payloadRoom != null && hasOccupantData(payloadRoom);
  if (usePayloadOccupants) {
    logger.debug('roomHandlers', 'room_update: using payload occupants (entering-player fix)', {
      occupants: payloadRoom?.occupants?.length ?? 0,
      players: payloadRoom?.players?.length ?? 0,
    });
  }
  const roomUpdate: Partial<Room> = {
    ...existingRoom,
    ...roomMetadata,
    players: usePayloadOccupants ? (payloadRoom?.players ?? []) : (existingRoom.players ?? []),
    npcs: usePayloadOccupants ? payloadRoom?.npcs : existingRoom.npcs,
    occupants: usePayloadOccupants ? (payloadRoom?.occupants ?? []) : (existingRoom.occupants ?? []),
    occupant_count: usePayloadOccupants
      ? (payloadRoom?.occupant_count ?? 0)
      : (existingRoom.occupant_count ?? 0),
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
 * Creates initial room state. Uses roomData.players/occupants when present (entering-player room_update with occupants).
 */
function createInitialRoomState(
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomData?: Room
): Room {
  const players = roomData?.players ?? [];
  const npcs = roomData?.npcs;
  const occupants = roomData?.occupants ?? [];
  const fallbackCount = occupants.length > 0 ? occupants.length : players.length + (npcs?.length ?? 0);
  const occupant_count = roomData?.occupant_count ?? fallbackCount;
  return {
    ...roomMetadata,
    players: Array.isArray(players) ? players : [],
    npcs: Array.isArray(npcs) ? npcs : undefined,
    occupants: Array.isArray(occupants) ? occupants : [],
    occupant_count: Number(occupant_count) || 0,
  };
}

/** Build unified room from event: room may be in data.room or data.room_data; occupants may be top-level. */
function getRoomDataFromEvent(event: { data: Record<string, unknown> }): Room | null {
  const raw = (event.data.room || event.data.room_data) as Room | undefined;
  if (!raw) return null;
  const topOccupants = event.data.occupants as string[] | undefined;
  const topPlayers = event.data.players as string[] | undefined;
  const topNpcs = event.data.npcs as string[] | undefined;
  const topCount = event.data.occupant_count as number | undefined;
  if (
    topOccupants === undefined &&
    topPlayers === undefined &&
    topNpcs === undefined &&
    topCount === undefined
  ) {
    return raw as Room;
  }
  return {
    ...(raw as Room),
    ...(topOccupants != null && { occupants: topOccupants, occupant_count: topCount ?? topOccupants.length }),
    ...(topPlayers != null && { players: topPlayers }),
    ...(topNpcs != null && { npcs: topNpcs }),
  } as Room;
}

export const handleRoomUpdate: EventHandler = (event, context) => {
  const roomData = getRoomDataFromEvent(event);
  if (!roomData) {
    return;
  }

  const roomMetadata = extractRoomMetadata(roomData);
  const existingRoom = context.currentRoomRef.current;
  const payloadOccupantCount =
    (roomData.occupants?.length ?? 0) || (roomData.occupant_count ?? 0);
  const payloadHasOccupants = hasOccupantData(roomData);

  if (!existingRoom) {
    const room = createInitialRoomState(roomMetadata, roomData);
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_update branch=initial (no existingRoom)', {
      payload_occupants: payloadOccupantCount,
      result_occupants: room.occupants?.length ?? 0,
    });
    return { room };
  }

  const roomIdChanged = roomData.id !== existingRoom.id;
  const room = createRoomUpdateWithPreservedOccupants(
    existingRoom,
    roomMetadata,
    roomIdChanged,
    roomData
  );
  logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_update branch=merge (had existingRoom)', {
    payload_occupants: payloadOccupantCount,
    payload_has_occupants: payloadHasOccupants,
    result_occupants: room.occupants?.length ?? 0,
  });
  return { room };
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

/**
 * Creates minimal room state from room_occupants event when no current room exists.
 * Fixes race where room_occupants arrives before application of room_update for entering player.
 */
function createMinimalRoomFromOccupantsEvent(
  eventRoomId: string,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupants: string[] | undefined,
  occupantCount: number | undefined
): Room {
  const finalPlayers = players ?? [];
  const finalNpcs = npcs ?? [];
  const finalOccupants =
    occupants && Array.isArray(occupants) ? occupants : [...finalPlayers, ...finalNpcs];
  const count =
    occupantCount !== undefined ? occupantCount : finalOccupants.length;
  return {
    id: eventRoomId,
    name: '',
    description: '',
    exits: {},
    players: finalPlayers,
    npcs: finalNpcs,
    occupants: finalOccupants,
    occupant_count: count,
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
    // room_occupants can arrive before room_update is applied (entering player race). Apply occupants by creating minimal room state.
    if (eventRoomId && (players !== undefined || npcs !== undefined || (occupants && Array.isArray(occupants)))) {
      const minimalRoom = createMinimalRoomFromOccupantsEvent(
        eventRoomId,
        players,
        npcs,
        occupants,
        occupantCount
      );
      logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_occupants branch=minimal (no currentRoom)', {
        result_occupants: minimalRoom.occupants?.length ?? 0,
      });
      return { room: minimalRoom };
    }
    logger.warn('roomHandlers', 'room_occupants event received but no room state available');
    return;
  }

  // Only update if room IDs match
  if (!validateRoomIdMatch(eventRoomId, currentRoom.id, npcs?.length ?? 0)) {
    return;
  }

  // Use structured format if available
  if (players !== undefined || npcs !== undefined) {
    const room = handleStructuredOccupantsFormat(currentRoom, players, npcs, occupantCount);
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_occupants branch=structured', {
      result_occupants: room.occupants?.length ?? 0,
    });
    return { room };
  }

  // Legacy format
  if (occupants && Array.isArray(occupants)) {
    const room = handleLegacyOccupantsFormat(currentRoom, occupants, occupantCount);
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_occupants branch=legacy', {
      result_occupants: room.occupants?.length ?? 0,
    });
    return { room };
  }
};
