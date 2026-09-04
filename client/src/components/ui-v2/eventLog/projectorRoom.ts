// Pure room derivation from events (no context refs)
// Used by the event-sourced projector; logic aligned with roomHandlers
// AI: keep each function CCN low; prefer if/else over ?? chains (Lizard inflates ??).

import type { GameEvent } from '../eventHandlers/types';
import type { Room } from '../types';

type RoomMeta = Omit<Room, 'players' | 'npcs' | 'occupants' | 'occupant_count'>;
type RoomOrNull = Room | null;
type OccupantPair = { players: string[]; npcsArr: string[] };

function extractRoomMetadata(roomData: Room): RoomMeta {
  // Omit occupant fields via destructuring (eslint: unused names intentional)
  /* eslint-disable-next-line @typescript-eslint/no-unused-vars */
  const { players: _p, npcs: _n, occupants: _o, occupant_count: _c, ...meta } = roomData;
  return meta;
}

function hasOccupantData(room: Room): boolean {
  const hasPlayers = room.players != null && room.players.length > 0;
  const hasNpcs = room.npcs != null && room.npcs.length > 0;
  return hasPlayers || hasNpcs;
}

function normalizeOccupantArrays(players: unknown, npcs: unknown): OccupantPair {
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  return { players: playersArr, npcsArr };
}

function coalesceCount(a?: number, b?: number, fallback = 0): number {
  if (a !== undefined) {
    return a;
  }
  if (b !== undefined) {
    return b;
  }
  return fallback;
}

function preferOccupantList(preferred?: string[], secondary?: string[]): string[] {
  if (preferred !== undefined) {
    return preferred;
  }
  if (secondary !== undefined) {
    return secondary;
  }
  return [];
}

function attachOccupants(room: Room, playersArr: string[], npcsArr: string[], occupantCount: number): Room {
  return {
    ...room,
    players: playersArr,
    npcs: npcsArr,
    occupants: playersArr.concat(npcsArr),
    occupant_count: occupantCount,
  };
}

function roomWithOccupantsFromArrays(roomData: Room): Room {
  const pair = normalizeOccupantArrays(roomData.players, roomData.npcs);
  const length = pair.players.length + pair.npcsArr.length;
  const count = coalesceCount(roomData.occupant_count, undefined, length);
  return attachOccupants(roomData, pair.players, pair.npcsArr, count);
}

function mergeTopLevelOccupants(raw: Room, event: GameEvent): Room {
  const topPlayers = Array.isArray(event.data.players) ? event.data.players : undefined;
  const topNpcs = Array.isArray(event.data.npcs) ? event.data.npcs : undefined;
  const playersSrc = topPlayers !== undefined ? topPlayers : raw.players;
  const npcsSrc = topNpcs !== undefined ? topNpcs : raw.npcs;
  const pair = normalizeOccupantArrays(playersSrc, npcsSrc);
  const length = pair.players.length + pair.npcsArr.length;
  const topCount = typeof event.data.occupant_count === 'number' ? event.data.occupant_count : undefined;
  const altCount = typeof event.data.count === 'number' ? event.data.count : undefined;
  const occupantCount = coalesceCount(topCount, altCount, length);
  return attachOccupants(raw, pair.players, pair.npcsArr, occupantCount);
}

function getRoomDataFromEvent(event: GameEvent): RoomOrNull {
  const candidate = event.data.room ? event.data.room : event.data.room_data;
  if (!candidate) {
    return null;
  }
  const raw = candidate as Room;
  if (event.data.players !== undefined || event.data.npcs !== undefined) {
    return mergeTopLevelOccupants(raw, event);
  }
  return raw;
}

function resolvePayloadNpcs(existingRoom: Room, payloadRoom?: Room): string[] {
  if (payloadRoom === undefined || payloadRoom.npcs === undefined) {
    return preferOccupantList(undefined, existingRoom.npcs);
  }
  if (Array.isArray(payloadRoom.npcs)) {
    return payloadRoom.npcs;
  }
  return [];
}

function roomAfterIdChange(existingRoom: Room, roomMetadata: RoomMeta): Room {
  return {
    ...existingRoom,
    ...roomMetadata,
    players: [],
    npcs: undefined,
    occupants: [],
    occupant_count: 0,
  };
}

function resolvePreservedOccupantArrays(
  existingRoom: Room,
  usePayloadOccupants: boolean,
  payloadRoom?: Room
): OccupantPair {
  if (!usePayloadOccupants) {
    return {
      players: preferOccupantList(undefined, existingRoom.players),
      npcsArr: preferOccupantList(undefined, existingRoom.npcs),
    };
  }
  const playersFromPayload = payloadRoom === undefined ? undefined : payloadRoom.players;
  const players = preferOccupantList(playersFromPayload, undefined);
  const npcsArr = resolvePayloadNpcs(existingRoom, payloadRoom);
  return { players, npcsArr };
}

function resolvePreservedOccupantCount(usePayloadOccupants: boolean, length: number, payloadCount?: number): number {
  if (!usePayloadOccupants) {
    return length;
  }
  return coalesceCount(payloadCount, undefined, length);
}

function roomWithPreservedOccupants(existingRoom: Room, roomMetadata: RoomMeta, payloadRoom?: Room): Room {
  const usePayloadOccupants = payloadRoom != null && hasOccupantData(payloadRoom);
  const pair = resolvePreservedOccupantArrays(existingRoom, usePayloadOccupants, payloadRoom);
  const length = pair.players.length + pair.npcsArr.length;
  const payloadCount = payloadRoom === undefined ? undefined : payloadRoom.occupant_count;
  const occupantCount = resolvePreservedOccupantCount(usePayloadOccupants, length, payloadCount);
  return attachOccupants({ ...existingRoom, ...roomMetadata }, pair.players, pair.npcsArr, occupantCount);
}

function createRoomUpdateWithPreservedOccupants(
  existingRoom: Room,
  roomMetadata: RoomMeta,
  roomIdChanged: boolean,
  payloadRoom?: Room
): Room {
  if (roomIdChanged) {
    return roomAfterIdChange(existingRoom, roomMetadata);
  }
  return roomWithPreservedOccupants(existingRoom, roomMetadata, payloadRoom);
}

function createInitialRoomState(roomMetadata: RoomMeta, roomData?: Room): Room {
  const pair = normalizeOccupantArrays(roomData?.players, roomData?.npcs);
  const length = pair.players.length + pair.npcsArr.length;
  const occupancy = coalesceCount(roomData?.occupant_count, undefined, length);
  return attachOccupants({ ...roomMetadata } as Room, pair.players, pair.npcsArr, occupancy);
}

function createMinimalRoomFromOccupantsEvent(
  eventRoomId: string,
  players?: string[],
  npcs?: string[],
  occupantCount?: number
): Room {
  const finalPlayers = preferOccupantList(players, undefined);
  const finalNpcs = preferOccupantList(npcs, undefined);
  const length = finalPlayers.length + finalNpcs.length;
  const count = coalesceCount(occupantCount, undefined, length);
  const base = {
    id: eventRoomId,
    name: '',
    description: '',
    exits: {},
  } as Room;
  return attachOccupants(base, finalPlayers, finalNpcs, count);
}

function validateRoomIdMatch(currentRoomId: string, eventRoomId?: string): boolean {
  if (!eventRoomId) {
    return true;
  }
  return eventRoomId === currentRoomId;
}

function handleStructuredOccupantsFormat(
  currentRoom: Room,
  players?: string[],
  npcs?: string[],
  occupantCount?: number
): Room {
  const finalPlayers = preferOccupantList(players, currentRoom.players);
  const finalNpcs = preferOccupantList(npcs, currentRoom.npcs);
  const length = finalPlayers.length + finalNpcs.length;
  const count = coalesceCount(occupantCount, undefined, length);
  return attachOccupants(currentRoom, finalPlayers, finalNpcs, count);
}

function hasTopLevelOccupantLists(players?: string[], npcs?: string[]): boolean {
  return players !== undefined || npcs !== undefined;
}

function deriveRoomFromOccupantsWithoutExisting(
  eventRoomId?: string,
  players?: string[],
  npcs?: string[],
  occupantCount?: number
): RoomOrNull {
  if (!eventRoomId || !hasTopLevelOccupantLists(players, npcs)) {
    return null;
  }
  return createMinimalRoomFromOccupantsEvent(eventRoomId, players, npcs, occupantCount);
}

/** Derive room from game_state event */
export function deriveRoomFromGameState(event: GameEvent): RoomOrNull {
  if (!event.data.room) {
    return null;
  }
  return roomWithOccupantsFromArrays(event.data.room as Room);
}

/** Derive room from room_update event (pure; uses existingRoom) */
export function deriveRoomFromRoomUpdate(event: GameEvent, existingRoom: RoomOrNull): RoomOrNull {
  const roomData = getRoomDataFromEvent(event);
  if (!roomData) {
    return null;
  }
  const roomMetadata = extractRoomMetadata(roomData);
  if (!existingRoom) {
    return createInitialRoomState(roomMetadata, roomData);
  }
  const roomIdChanged = roomData.id !== existingRoom.id;
  return createRoomUpdateWithPreservedOccupants(existingRoom, roomMetadata, roomIdChanged, roomData);
}

/** Derive room from room_state event (authoritative single source; replace, do not merge) */
export function deriveRoomFromRoomState(event: GameEvent): RoomOrNull {
  if (!event.data.room) {
    return null;
  }
  const base = roomWithOccupantsFromArrays(event.data.room as Room);
  const occupantCount = typeof event.data.occupant_count === 'number' ? event.data.occupant_count : undefined;
  if (occupantCount === undefined) {
    return base;
  }
  return { ...base, occupant_count: occupantCount };
}

/** Derive room from room_occupants event (pure; uses existingRoom) */
export function deriveRoomFromRoomOccupants(event: GameEvent, existingRoom: RoomOrNull): RoomOrNull {
  const players = Array.isArray(event.data.players) ? event.data.players : undefined;
  const npcs = Array.isArray(event.data.npcs) ? event.data.npcs : undefined;
  const occupantCount = typeof event.data.count === 'number' ? event.data.count : undefined;
  const eventRoomId = typeof event.room_id === 'string' ? event.room_id : undefined;

  if (!existingRoom) {
    return deriveRoomFromOccupantsWithoutExisting(eventRoomId, players, npcs, occupantCount);
  }
  if (!validateRoomIdMatch(existingRoom.id, eventRoomId)) {
    return null;
  }
  if (!hasTopLevelOccupantLists(players, npcs)) {
    return null;
  }
  return handleStructuredOccupantsFormat(existingRoom, players, npcs, occupantCount);
}
