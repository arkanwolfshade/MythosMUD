// Room state merge utilities
// As documented in "Room State Architecture" - Dr. Armitage, 1928

import type { Room } from '../types';

/**
 * Checks if an array is populated (defined, is an array, and has length > 0)
 */
const isPopulatedArray = (arr: string[] | undefined): boolean => {
  if (arr === undefined) {
    return false;
  }
  if (!Array.isArray(arr)) {
    return false;
  }
  return arr.length > 0;
};

/**
 * Gets players array from room, returning empty array if not available
 */
const getPlayersArray = (room: Room): string[] => {
  return room.players ?? [];
};

/**
 * Gets NPCs array from room, returning empty array if not available
 */
const getNpcsArray = (room: Room): string[] => {
  return room.npcs ?? [];
};

/**
 * Determines which players array to use based on update state
 */
const selectPlayersArray = (updatesRoom: Room, prevRoom: Room, roomIdChanged: boolean): string[] => {
  const updatesPlayers = getPlayersArray(updatesRoom);
  const prevPlayers = getPlayersArray(prevRoom);
  const updatesHasPlayers = isPopulatedArray(updatesPlayers);
  const prevHasPlayers = isPopulatedArray(prevPlayers);

  // Updates has players - use it (authoritative)
  if (updatesHasPlayers) {
    return updatesPlayers;
  }

  // Room changed - use new room's players
  if (roomIdChanged) {
    return updatesPlayers;
  }

  // Previous has players - preserve them
  if (prevHasPlayers) {
    return prevPlayers;
  }

  // Fallback to updates, then previous, then empty
  return updatesPlayers.length > 0 ? updatesPlayers : prevPlayers;
};

/**
 * Determines which NPCs array to use based on update state
 */
const selectNpcsArray = (updatesRoom: Room, prevRoom: Room, roomIdChanged: boolean): string[] => {
  const updatesNpcs = getNpcsArray(updatesRoom);
  const prevNpcs = getNpcsArray(prevRoom);
  const updatesHasNpcs = isPopulatedArray(updatesNpcs);
  const prevHasNpcs = isPopulatedArray(prevNpcs);

  // Updates has NPCs - use it (authoritative)
  if (updatesHasNpcs) {
    return updatesNpcs;
  }

  // Room changed - use new room's NPCs
  if (roomIdChanged) {
    return updatesNpcs;
  }

  // Previous has NPCs - preserve them
  if (prevHasNpcs) {
    return prevNpcs;
  }

  // Check if updates tried to clear NPCs (empty array) while prev has them
  const updatesClearedNpcs = updatesRoom.npcs !== undefined && updatesNpcs.length === 0;
  if (updatesClearedNpcs && prevHasNpcs) {
    return prevNpcs;
  }

  // Fallback to updates, then previous, then empty
  return updatesNpcs.length > 0 ? updatesNpcs : prevNpcs;
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
  const mergedOccupants = [...mergedPlayers, ...mergedNpcs];

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
