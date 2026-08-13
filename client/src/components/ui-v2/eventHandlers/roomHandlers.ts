// Room-related event handlers
// As documented in "Room State Architecture" - Dr. Armitage, 1928
// State derivation is now in the event-sourced projector (eventLog/projector.ts); these handlers
// are kept for unit tests and optional validation/side effects.

import { logger } from '../../../utils/logger';
import type { Player, Room } from '../types';
import type { EventHandler } from './types';

/** Gate for occupant debug logs; set true only when debugging enter-room / occupant ordering. */
let _occupantDebug = false;
/** Test-only setter to exercise OCCUPANT_DEBUG branches; not used in production. */
export function __setOccupantDebugForTests(value: boolean): void {
  _occupantDebug = value;
}

function normalizeOccupantArrays(players: unknown, npcs: unknown): { playersArr: string[]; npcsArr: string[] } {
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  return { playersArr, npcsArr };
}

function roomWithNormalizedOccupants(room: Room): Room {
  const { playersArr, npcsArr } = normalizeOccupantArrays(room.players, room.npcs);
  const occupants = [...playersArr, ...npcsArr];
  return {
    ...room,
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: room.occupant_count ?? occupants.length,
  };
}

function extractGraceAndFollowFields(event: { data: Record<string, unknown> }) {
  const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
  const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
  const following = event.data.following as { target_name: string; target_type: 'player' | 'npc' } | null | undefined;
  return { loginGracePeriodActive, loginGracePeriodRemaining, following };
}

function isValidPlayer(playerData: unknown): playerData is Player {
  const player = playerData as Player;
  return typeof player === 'object' && player !== null && 'name' in player && typeof player.name === 'string';
}

function buildGameStateResult(
  player: Player | null,
  room: Room,
  graceAndFollow: ReturnType<typeof extractGraceAndFollowFields>
) {
  const { loginGracePeriodActive, loginGracePeriodRemaining, following } = graceAndFollow;
  return {
    player,
    room,
    ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
    ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
    ...(following !== undefined && { followingTarget: following ?? null }),
  };
}

function logGameStateOccupantDebug(room: Room): void {
  if (!_occupantDebug) return;
  logger.info('roomHandlers', 'OCCUPANT_DEBUG: game_state setting room', {
    occupants_from_payload: room.occupants?.length ?? 0,
    result_occupant_count: room.occupants?.length ?? 0,
  });
}

function resolveGameStatePlayer(playerData: unknown): Player | null {
  if (!playerData) return null;
  if (isValidPlayer(playerData)) return playerData;
  logger.warn('roomHandlers', 'handleGameState: invalid player data, missing name property');
  return null;
}

export const handleGameState: EventHandler = (event, _context) => {
  const graceAndFollow = extractGraceAndFollowFields(event);
  const roomData = event.data.room as unknown;
  if (!roomData) {
    return graceAndFollow.following !== undefined ? { followingTarget: graceAndFollow.following ?? null } : undefined;
  }

  // Missing or null player: do not emit partial game_state (tests / prior contract).
  // Invalid player objects still yield a result with player: null so room occupants apply.
  const rawPlayer = event.data.player;
  if (rawPlayer === undefined || rawPlayer === null) {
    return graceAndFollow.following !== undefined ? { followingTarget: graceAndFollow.following ?? null } : undefined;
  }

  const roomWithOccupants = roomWithNormalizedOccupants(roomData as Room);
  logGameStateOccupantDebug(roomWithOccupants);
  return buildGameStateResult(resolveGameStatePlayer(rawPlayer), roomWithOccupants, graceAndFollow);
};

/** Apply follow_state event (who I am following). */
export const handleFollowState: EventHandler = event => {
  const following = event.data.following as { target_name: string; target_type: 'player' | 'npc' } | null | undefined;
  return { followingTarget: following ?? null };
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

/** True when room has players or NPCs (used to prefer payload over existing). */
function hasOccupantData(room: Room): boolean {
  const hasPlayers = room.players != null && room.players.length > 0;
  const hasNpcs = room.npcs != null && room.npcs.length > 0;
  return hasPlayers || hasNpcs;
}

/**
 * Creates a room update. When payloadRoom has occupant data (e.g. entering-player room_update),
 * use it; otherwise preserve existing room occupants.
 */
function resolvePayloadNpcs(payloadRoom: Room | undefined, existingRoom: Room): string[] | undefined {
  if (payloadRoom?.npcs === undefined) {
    return existingRoom.npcs;
  }
  return Array.isArray(payloadRoom.npcs) ? payloadRoom.npcs : [];
}

function resolveOccupantsForRoomUpdate(
  existingRoom: Room,
  payloadRoom: Room | undefined,
  usePayloadOccupants: boolean
): { players: string[]; npcs: string[] | undefined; occupants: string[]; occupant_count: number } {
  const players = usePayloadOccupants ? (payloadRoom?.players ?? []) : (existingRoom.players ?? []);
  const npcs = usePayloadOccupants ? resolvePayloadNpcs(payloadRoom, existingRoom) : existingRoom.npcs;
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...players, ...npcsArr];
  const occupant_count = usePayloadOccupants ? (payloadRoom?.occupant_count ?? occupants.length) : occupants.length;
  return { players, npcs, occupants, occupant_count };
}

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

  const resolved = resolveOccupantsForRoomUpdate(existingRoom, payloadRoom, usePayloadOccupants);
  if (!roomIdChanged) {
    return { ...existingRoom, ...roomMetadata, ...resolved } as Room;
  }

  return {
    ...existingRoom,
    ...roomMetadata,
    players: [],
    npcs: undefined,
    occupants: [],
    occupant_count: 0,
  } as Room;
}

/**
 * Creates initial room state. Uses roomData.players/occupants when present
 * (entering-player room_update with occupants).
 */
function createInitialRoomState(
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomData?: Room
): Room {
  const players = roomData?.players ?? [];
  const npcs = roomData?.npcs ?? [];
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...playersArr, ...npcsArr];
  const occupant_count = roomData?.occupant_count ?? occupants.length;
  return {
    ...roomMetadata,
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: Number(occupant_count) || 0,
  };
}

function mergeTopLevelOccupants(raw: Room, event: { data: Record<string, unknown> }): Room {
  const topPlayers = event.data.players as string[] | undefined;
  const topNpcs = event.data.npcs as string[] | undefined;
  const { playersArr, npcsArr } = normalizeOccupantArrays(topPlayers ?? raw.players, topNpcs ?? raw.npcs);
  const occupants = [...playersArr, ...npcsArr];
  const topCount = event.data.occupant_count as number | undefined;
  const count = event.data.count as number | undefined;
  return {
    ...(raw as Room),
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: topCount ?? count ?? occupants.length,
  } as Room;
}

/** Build unified room from event: room may be in data.room or data.room_data; occupants derived from players+npcs. */
function getRoomDataFromEvent(event: { data: Record<string, unknown> }): Room | null {
  const raw = (event.data.room || event.data.room_data) as Room | undefined;
  if (!raw) return null;
  const topPlayers = event.data.players as string[] | undefined;
  const topNpcs = event.data.npcs as string[] | undefined;
  if (topPlayers === undefined && topNpcs === undefined) {
    return raw as Room;
  }
  return mergeTopLevelOccupants(raw, event);
}

export const handleRoomUpdate: EventHandler = (event, context) => {
  const roomData = getRoomDataFromEvent(event);
  if (!roomData) {
    return;
  }

  const roomMetadata = extractRoomMetadata(roomData);
  const existingRoom = context.currentRoomRef.current;
  const payloadOccupantCount = (roomData.occupants?.length ?? 0) || (roomData.occupant_count ?? 0);
  const payloadHasOccupants = hasOccupantData(roomData);

  if (!existingRoom) {
    const room = createInitialRoomState(roomMetadata, roomData);
    if (_occupantDebug) {
      logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_update branch=initial (no existingRoom)', {
        payload_occupants: payloadOccupantCount,
        result_occupants: room.occupants?.length ?? 0,
      });
    }
    return { room };
  }

  const roomIdChanged = roomData.id !== existingRoom.id;
  const room = createRoomUpdateWithPreservedOccupants(existingRoom, roomMetadata, roomIdChanged, roomData);
  if (_occupantDebug) {
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_update branch=merge (had existingRoom)', {
      payload_occupants: payloadOccupantCount,
      payload_has_occupants: payloadHasOccupants,
      result_occupants: room.occupants?.length ?? 0,
    });
  }
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
 * Creates minimal room state from room_occupants event when no current room exists.
 * Fixes race where room_occupants arrives before application of room_update for entering player.
 */
function createMinimalRoomFromOccupantsEvent(
  eventRoomId: string,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupantCount: number | undefined
): Room {
  const finalPlayers = players ?? [];
  const finalNpcs = npcs ?? [];
  const occupants = [...finalPlayers, ...finalNpcs];
  const count = occupantCount !== undefined ? occupantCount : occupants.length;
  return {
    id: eventRoomId,
    name: '',
    description: '',
    exits: {},
    players: finalPlayers,
    npcs: finalNpcs,
    occupants,
    occupant_count: count,
  };
}

function handleOccupantsWithoutCurrentRoom(
  eventRoomId: string | undefined,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupantCount: number | undefined
) {
  if (!eventRoomId || (players === undefined && npcs === undefined)) {
    logger.warn('roomHandlers', 'room_occupants event received but no room state available');
    return undefined;
  }
  const minimalRoom = createMinimalRoomFromOccupantsEvent(eventRoomId, players, npcs, occupantCount);
  if (_occupantDebug) {
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_occupants branch=minimal (no currentRoom)', {
      result_occupants: minimalRoom.occupants?.length ?? 0,
    });
  }
  return { room: minimalRoom };
}

export const handleRoomOccupants: EventHandler = (event, context) => {
  const players = event.data.players as string[] | undefined;
  const npcs = event.data.npcs as string[] | undefined;
  const occupantCount = event.data.count as number | undefined;
  const eventRoomId = event.room_id as string | undefined;
  const currentRoom = context.currentRoomRef.current;

  if (!currentRoom) {
    return handleOccupantsWithoutCurrentRoom(eventRoomId, players, npcs, occupantCount);
  }

  if (!validateRoomIdMatch(eventRoomId, currentRoom.id, npcs?.length ?? 0)) {
    return;
  }

  if (players === undefined && npcs === undefined) {
    return;
  }

  const room = handleStructuredOccupantsFormat(currentRoom, players, npcs, occupantCount);
  if (_occupantDebug) {
    logger.info('roomHandlers', 'OCCUPANT_DEBUG: room_occupants branch=structured', {
      result_occupants: room.occupants?.length ?? 0,
    });
  }
  return { room };
};
