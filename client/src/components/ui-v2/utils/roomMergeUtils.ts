// Room state merge utilities
// As documented in "Room State Architecture" - Dr. Armitage, 1928

import type { NpcOccupant } from '../../../types/messageCategory';
import type { Room } from '../types';
import { normalizeNpcOccupants, npcNames } from './npcOccupants';

/**
 * Gets players array from room, returning empty array if not available
 */
const getPlayersArray = (room: Room): string[] => {
  return room.players ?? [];
};

/**
 * Gets NPCs array from room, returning empty array if not available
 */
const getNpcsArray = (room: Room): NpcOccupant[] => {
  return room.npcs ?? [];
};

/**
 * Determines which players array to use based on update state.
 * Uses updates when it provides an array (including empty); preserves prev only when
 * updates omits the key (undefined) so room_occupants can clear occupants authoritatively.
 */
const selectPlayersArray = (updatesRoom: Room, prevRoom: Room, roomIdChanged: boolean): string[] => {
  const updatesPlayersRaw = updatesRoom.players;
  const prevPlayers = getPlayersArray(prevRoom);
  const updatesIsValidArray = Array.isArray(updatesPlayersRaw);

  if (roomIdChanged) {
    return updatesIsValidArray ? updatesPlayersRaw : prevPlayers;
  }
  if (updatesPlayersRaw === undefined) {
    return prevPlayers;
  }
  if (!updatesIsValidArray) {
    return prevPlayers;
  }
  return updatesPlayersRaw;
};

/**
 * Determines which NPCs array to use based on update state.
 * Uses updates when it provides an array (including empty); preserves prev only when
 * updates omits the key (undefined) so room_occupants can clear occupants authoritatively.
 */
const selectNpcsArray = (updatesRoom: Room, prevRoom: Room, roomIdChanged: boolean): NpcOccupant[] => {
  const updatesNpcsRaw = Array.isArray(updatesRoom.npcs) ? normalizeNpcOccupants(updatesRoom.npcs) : updatesRoom.npcs;
  const prevNpcs = getNpcsArray(prevRoom);
  const updatesIsValidArray = Array.isArray(updatesNpcsRaw);

  if (roomIdChanged) {
    return updatesIsValidArray ? updatesNpcsRaw : prevNpcs;
  }
  if (updatesNpcsRaw === undefined) {
    return prevNpcs;
  }
  if (!updatesIsValidArray) {
    return prevNpcs;
  }
  return updatesNpcsRaw;
};

/**
 * Merges room updates with existing room state, preserving occupant data correctly
 * ARCHITECTURE: Single authoritative source for occupant data
 * - room_occupants events set players/npcs (authoritative)
 * - room_update events update metadata only (preserves existing occupants)
 */
export const mergeRoomState = (updatesRoom: Room | undefined, prevRoom: Room | null): Room | null => {
  if (!updatesRoom && !prevRoom) {
    return null;
  }

  if (!updatesRoom) {
    return prevRoom;
  }

  if (!prevRoom) {
    return updatesRoom;
  }

  // Check if room ID changed
  const roomIdChanged = updatesRoom.id !== prevRoom.id;

  // Calculate merged arrays
  const mergedPlayers = selectPlayersArray(updatesRoom, prevRoom, roomIdChanged);
  const mergedNpcs = selectNpcsArray(updatesRoom, prevRoom, roomIdChanged);

  // Calculate merged occupants array
  const mergedOccupants = [...mergedPlayers, ...npcNames(mergedNpcs)];

  // Calculate occupant count from merged values
  const mergedOccupantCount = updatesRoom.occupant_count ?? mergedOccupants.length;

  return {
    ...updatesRoom,
    players: mergedPlayers,
    npcs: mergedNpcs,
    occupants: mergedOccupants,
    occupant_count: mergedOccupantCount,
  };
};
