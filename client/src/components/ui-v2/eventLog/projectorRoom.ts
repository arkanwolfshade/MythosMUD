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
  return (room.players != null && room.players.length > 0) || (room.npcs != null && room.npcs.length > 0);
}

function getRoomDataFromEvent(event: GameEvent): Room | null {
  const raw = (event.data.room || event.data.room_data) as Room | undefined;
  if (!raw) return null;
  const topPlayers = event.data.players as string[] | undefined;
  const topNpcs = event.data.npcs as string[] | undefined;
  if (topPlayers === undefined && topNpcs === undefined) {
    return raw as Room;
  }
  const players = topPlayers ?? raw.players ?? [];
  const npcs = topNpcs ?? raw.npcs ?? [];
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...playersArr, ...npcsArr];
  const topCount = event.data.occupant_count as number | undefined;
  const count = event.data.count as number | undefined;
  const occupantCount = topCount ?? count ?? occupants.length;
  return {
    ...(raw as Room),
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: occupantCount,
  } as Room;
}

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

function createRoomUpdateWithPreservedOccupants(
  existingRoom: Room,
  roomMetadata: Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>,
  roomIdChanged: boolean,
  payloadRoom?: Room
): Room {
  const usePayloadOccupants = payloadRoom != null && hasOccupantData(payloadRoom);
  const players = usePayloadOccupants ? (payloadRoom?.players ?? []) : (existingRoom.players ?? []);
  const npcs = usePayloadOccupants ? (payloadRoom?.npcs ?? []) : (existingRoom.npcs ?? []);
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...players, ...npcsArr];
  const roomUpdate: Room = {
    ...existingRoom,
    ...roomMetadata,
    players,
    npcs: npcsArr,
    occupants,
    occupant_count: usePayloadOccupants ? (payloadRoom?.occupant_count ?? occupants.length) : occupants.length,
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

/** Derive room from game_state event */
export function deriveRoomFromGameState(event: GameEvent): Room | null {
  const roomData = event.data.room as Room | undefined;
  if (!roomData) return null;
  const players = roomData.players ?? [];
  const npcs = roomData.npcs ?? [];
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...playersArr, ...npcsArr];
  return {
    ...roomData,
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: roomData.occupant_count ?? occupants.length,
  };
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
  if (!roomData) return null;
  const players = roomData.players ?? [];
  const npcs = roomData.npcs ?? [];
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...playersArr, ...npcsArr];
  const occupantCount = event.data.occupant_count as number | undefined;
  return {
    ...roomData,
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: occupantCount ?? roomData.occupant_count ?? occupants.length,
  } as Room;
}

/** Derive room from room_occupants event (pure; uses existingRoom) */
export function deriveRoomFromRoomOccupants(event: GameEvent, existingRoom: Room | null): Room | null {
  const players = event.data.players as string[] | undefined;
  const npcs = event.data.npcs as string[] | undefined;
  const occupantCount = event.data.count as number | undefined;
  const eventRoomId = event.room_id as string | undefined;

  if (!existingRoom) {
    if (eventRoomId && (players !== undefined || npcs !== undefined)) {
      return createMinimalRoomFromOccupantsEvent(eventRoomId, players, npcs, occupantCount);
    }
    return null;
  }

  if (!validateRoomIdMatch(eventRoomId, existingRoom.id, npcs?.length ?? 0)) {
    return null;
  }
  if (players !== undefined || npcs !== undefined) {
    return handleStructuredOccupantsFormat(existingRoom, players, npcs, occupantCount);
  }
  return null;
}
