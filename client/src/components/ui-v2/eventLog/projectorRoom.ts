// Pure room derivation from events (no context refs)
// Used by the event-sourced projector; logic aligned with roomHandlers

import type { GameEvent } from '../eventHandlers/types';
import type { Room } from '../types';

function extractRoomMetadata(roomData: Room): Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'> {
  // Omit occupant fields via destructuring (eslint: unused names intentional)
  /* eslint-disable-next-line @typescript-eslint/no-unused-vars */
  const { players: _p, npcs: _n, occupants: _o, occupant_count: _c, ...meta } = roomData;
  return meta;
}

function hasOccupantData(room: Room): boolean {
  return (
    (room.players != null && room.players.length > 0) ||
    (room.npcs != null && room.npcs.length > 0) ||
    (room.occupants != null && room.occupants.length > 0)
  );
}

function getRoomDataFromEvent(event: GameEvent): Room | null {
  const raw = (event.data.room || event.data.room_data) as Room | undefined;
  if (!raw) return null;
  const topOccupants = event.data.occupants as string[] | undefined;
  const topPlayers = event.data.players as string[] | undefined;
  const topNpcs = event.data.npcs as string[] | undefined;
  const topCount = event.data.occupant_count as number | undefined;
  if (topOccupants === undefined && topPlayers === undefined && topNpcs === undefined && topCount === undefined) {
    return raw as Room;
  }
  return {
    ...(raw as Room),
    ...(topOccupants != null && { occupants: topOccupants, occupant_count: topCount ?? topOccupants.length }),
    ...(topPlayers != null && { players: topPlayers }),
    ...(topNpcs != null && { npcs: topNpcs }),
  } as Room;
}

function createInitialRoomState(
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomData?: Room
): Room {
  const players = roomData?.players ?? [];
  const npcs = roomData?.npcs;
  const occupants = roomData?.occupants ?? [];
  const fallbackCount =
    occupants.length > 0 ? occupants.length : (Array.isArray(players) ? players.length : 0) + (npcs?.length ?? 0);
  const occupant_count = roomData?.occupant_count ?? fallbackCount;
  return {
    ...roomMetadata,
    players: Array.isArray(players) ? players : [],
    npcs: Array.isArray(npcs) ? npcs : undefined,
    occupants: Array.isArray(occupants) ? occupants : [],
    occupant_count: Number(occupant_count) || 0,
  };
}

function createRoomUpdateWithPreservedOccupants(
  existingRoom: Room,
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomIdChanged: boolean,
  payloadRoom?: Room
): Room {
  const usePayloadOccupants = payloadRoom != null && hasOccupantData(payloadRoom);
  const roomUpdate: Room = {
    ...existingRoom,
    ...roomMetadata,
    players: usePayloadOccupants ? (payloadRoom?.players ?? []) : (existingRoom.players ?? []),
    npcs: usePayloadOccupants ? payloadRoom?.npcs : existingRoom.npcs,
    occupants: usePayloadOccupants ? (payloadRoom?.occupants ?? []) : (existingRoom.occupants ?? []),
    occupant_count: usePayloadOccupants ? (payloadRoom?.occupant_count ?? 0) : (existingRoom.occupant_count ?? 0),
  };
  if (roomIdChanged) {
    roomUpdate.players = [];
    roomUpdate.npcs = undefined;
    roomUpdate.occupants = [];
    roomUpdate.occupant_count = 0;
  }
  return roomUpdate;
}

function createMinimalRoomFromOccupantsEvent(
  eventRoomId: string,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupants: string[] | undefined,
  occupantCount: number | undefined
): Room {
  const finalPlayers = players ?? [];
  const finalNpcs = npcs ?? [];
  const finalOccupants = occupants && Array.isArray(occupants) ? occupants : [...finalPlayers, ...finalNpcs];
  const count = occupantCount !== undefined ? occupantCount : finalOccupants.length;
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

function validateRoomIdMatch(eventRoomId: string | undefined, currentRoomId: string, _npcsCount: number): boolean {
  if (!eventRoomId || eventRoomId === currentRoomId) return true;
  return false;
}

function handleStructuredOccupantsFormat(
  currentRoom: Room,
  players: string[] | undefined,
  npcs: string[] | undefined,
  occupantCount: number | undefined
): Room {
  const finalPlayers = players ?? currentRoom.players ?? [];
  const finalNpcs = npcs ?? currentRoom.npcs ?? [];
  const count = occupantCount ?? finalPlayers.length + finalNpcs.length;
  return {
    ...currentRoom,
    players: finalPlayers,
    npcs: finalNpcs,
    occupants: [...finalPlayers, ...finalNpcs],
    occupant_count: count,
  };
}

function handleLegacyOccupantsFormat(currentRoom: Room, occupants: string[], occupantCount: number | undefined): Room {
  const count = occupantCount !== undefined ? occupantCount : occupants.length;
  return {
    ...currentRoom,
    occupants,
    occupant_count: count,
    players: currentRoom.players ?? [],
    npcs: currentRoom.npcs ?? [],
  };
}

/** Derive room from game_state event */
export function deriveRoomFromGameState(event: GameEvent): Room | null {
  const roomData = event.data.room as Room | undefined;
  const occupants = event.data.occupants as string[] | undefined;
  if (!roomData) return null;
  const roomWithOccupants: Room = {
    ...roomData,
    ...(occupants && { occupants, occupant_count: occupants.length }),
  };
  return roomWithOccupants;
}

/** Derive room from room_update event (pure; uses existingRoom) */
export function deriveRoomFromRoomUpdate(event: GameEvent, existingRoom: Room | null): Room | null {
  const roomData = getRoomDataFromEvent(event);
  if (!roomData) return null;
  const roomMetadata = extractRoomMetadata(roomData);
  if (!existingRoom) {
    return createInitialRoomState(roomMetadata, roomData);
  }
  const roomIdChanged = roomData.id !== existingRoom.id;
  return createRoomUpdateWithPreservedOccupants(existingRoom, roomMetadata, roomIdChanged, roomData);
}

/** Derive room from room_state event (authoritative single source; replace, do not merge) */
export function deriveRoomFromRoomState(event: GameEvent): Room | null {
  const roomData = event.data.room as Room | undefined;
  const occupants = event.data.occupants as string[] | undefined;
  const occupantCount = event.data.occupant_count as number | undefined;
  if (!roomData) return null;
  return {
    ...roomData,
    ...(occupants != null && { occupants, occupant_count: occupantCount ?? occupants.length }),
  } as Room;
}

/** Derive room from room_occupants event (pure; uses existingRoom) */
export function deriveRoomFromRoomOccupants(event: GameEvent, existingRoom: Room | null): Room | null {
  const players = event.data.players as string[] | undefined;
  const npcs = event.data.npcs as string[] | undefined;
  const occupants = event.data.occupants as string[] | undefined;
  const occupantCount = event.data.count as number | undefined;
  const eventRoomId = event.room_id as string | undefined;

  if (!existingRoom) {
    if (eventRoomId && (players !== undefined || npcs !== undefined || (occupants && Array.isArray(occupants)))) {
      return createMinimalRoomFromOccupantsEvent(eventRoomId, players, npcs, occupants, occupantCount);
    }
    return null;
  }

  if (!validateRoomIdMatch(eventRoomId, existingRoom.id, npcs?.length ?? 0)) {
    return null;
  }
  if (players !== undefined || npcs !== undefined) {
    return handleStructuredOccupantsFormat(existingRoom, players, npcs, occupantCount);
  }
  if (occupants && Array.isArray(occupants)) {
    return handleLegacyOccupantsFormat(existingRoom, occupants, occupantCount);
  }
  return null;
}
