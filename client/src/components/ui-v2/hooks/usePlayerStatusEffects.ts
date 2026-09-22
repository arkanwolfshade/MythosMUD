// Player status effects hook (death/delirium detection)
// Extracted from GameClientV2Container to reduce complexity

import { useCallback, useEffect, useRef } from 'react';
import type { LucidityStatus } from '../../../types/lucidity';
import { logger } from '../../../utils/logger';
import type { Player, Room } from '../types';

interface PlayerStatusSetters {
  setIsDead: (dead: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setDeliriumLocation: (location: string) => void;
  setDeathLocation: (location: string) => void;
  setHasRespawned: (hasRespawned: boolean) => void;
}

interface UsePlayerStatusEffectsParams {
  player: Player | null;
  room: Room | null;
  lucidityStatus: LucidityStatus | null;
  isDead: boolean;
  isDelirious: boolean;
  hasRespawned: boolean;
  setters: PlayerStatusSetters;
  /** Shared with event processing so player_died can fall back when server sends limbo. */
  lastNonLimboRoomNameRef?: React.MutableRefObject<string | null>;
}

const LIMBO_ROOM_ID = 'limbo_death_void_limbo_death_void';
/** Foyer id — only used to skip re-marking dead right after a successful respawn. */
const RESPAWN_ROOM_ID = 'earth_arkhamcity_sanitarium_room_foyer_001';

export function isUnusableDeathLocation(loc: string): boolean {
  const trimmed = loc.trim();
  if (!trimmed || trimmed === 'Unknown Location') {
    return true;
  }
  if (trimmed === LIMBO_ROOM_ID || trimmed.startsWith('limbo_')) {
    return true;
  }
  // Limbo display name from room data
  return /spaces between/i.test(trimmed);
}

function getCurrentLucidity(player: Player | null, lucidityStatus: LucidityStatus | null): number {
  if (lucidityStatus?.current !== undefined) {
    return lucidityStatus.current;
  }
  if (player?.stats?.lucidity !== undefined) {
    return player.stats.lucidity;
  }
  return 100;
}

function currentDpOf(player: Player): number {
  return typeof player.stats?.current_dp === 'number' ? player.stats.current_dp : 0;
}

function skipDeadInRespawnRoom(roomId: string | undefined, isDead: boolean, hasRespawned: boolean): boolean {
  return roomId === RESPAWN_ROOM_ID && !isDead && hasRespawned;
}

/** Prefer current room name; fall back to last non-limbo room. */
function resolveDeathLocationDisplay(room: Room | null, lastNonLimboRoomName: string | null): string | null {
  const roomId = room?.id;
  if (roomId && roomId !== LIMBO_ROOM_ID) {
    const fromRoom = room?.name || roomId;
    if (!isUnusableDeathLocation(fromRoom)) {
      return fromRoom;
    }
  }
  if (lastNonLimboRoomName && !isUnusableDeathLocation(lastNonLimboRoomName)) {
    return lastNonLimboRoomName;
  }
  return null;
}

function markPlayerDead(
  setters: PlayerStatusSetters,
  currentDpNum: number,
  room: Room | null,
  lastNonLimboRoomName: string | null
): void {
  const roomId = room?.id;
  setters.setIsDead(true);
  setters.setHasRespawned(false);
  const chosen = resolveDeathLocationDisplay(room, lastNonLimboRoomName);
  if (chosen) {
    setters.setDeathLocation(chosen);
  }
  logger.info('GameClientV2Container', 'Player detected as dead', {
    currentDp: currentDpNum,
    roomId,
    isInLimbo: roomId === LIMBO_ROOM_ID,
  });
}

function syncDeathState(
  player: Player,
  room: Room | null,
  isDead: boolean,
  hasRespawned: boolean,
  setters: PlayerStatusSetters,
  lastNonLimboRoomName: string | null
): void {
  const currentDpNum = currentDpOf(player);
  const roomId = room?.id;
  if (currentDpNum <= -10 && !skipDeadInRespawnRoom(roomId, isDead, hasRespawned)) {
    if (!isDead) markPlayerDead(setters, currentDpNum, room, lastNonLimboRoomName);
    return;
  }
  if (isDead && (currentDpNum > -10 || roomId !== LIMBO_ROOM_ID)) {
    setters.setIsDead(false);
    logger.info('GameClientV2Container', 'Player detected as alive', { currentDp: currentDpNum, roomId });
  }
}

function syncDeliriumState(
  player: Player,
  room: Room | null,
  lucidityStatus: LucidityStatus | null,
  isDelirious: boolean,
  setters: PlayerStatusSetters
): void {
  const currentLucidity = getCurrentLucidity(player, lucidityStatus);
  const roomId = room?.id;
  const shouldBeDelirious = currentLucidity <= -10;

  if (shouldBeDelirious && !isDelirious) {
    setters.setIsDelirious(true);
    setters.setDeliriumLocation(roomId || 'Unknown Location');
    logger.info('GameClientV2Container', 'Player detected as delirious', { currentLucidity, roomId });
    return;
  }

  if (!shouldBeDelirious && isDelirious) {
    setters.setIsDelirious(false);
    logger.info('GameClientV2Container', 'Player detected as lucid', { currentLucidity, roomId });
  }
}

export const usePlayerStatusEffects = (params: UsePlayerStatusEffectsParams) => {
  const { player, room, lucidityStatus, isDead, isDelirious, hasRespawned, setters, lastNonLimboRoomNameRef } = params;
  const { setIsDead, setIsDelirious, setDeliriumLocation, setDeathLocation, setHasRespawned } = setters;

  const internalLastRoomRef = useRef<string | null>(null);
  const lastRoomRef = lastNonLimboRoomNameRef ?? internalLastRoomRef;

  useEffect(() => {
    // Track any non-limbo room, including foyer (valid place of death).
    if (room?.id && room.id !== LIMBO_ROOM_ID && room.name) {
      lastRoomRef.current = room.name;
    }
  }, [room, lastRoomRef]);

  const statusSetters = useCallback(
    (): PlayerStatusSetters => ({
      setIsDead,
      setIsDelirious,
      setDeliriumLocation,
      setDeathLocation,
      setHasRespawned,
    }),
    [setIsDead, setIsDelirious, setDeliriumLocation, setDeathLocation, setHasRespawned]
  );

  useEffect(() => {
    if (!player) return;
    syncDeathState(player, room, isDead, hasRespawned, statusSetters(), lastRoomRef.current);
  }, [player, room, isDead, hasRespawned, statusSetters, lastRoomRef]);

  useEffect(() => {
    if (!player) return;
    syncDeliriumState(player, room, lucidityStatus, isDelirious, statusSetters());
  }, [player, room, lucidityStatus, isDelirious, statusSetters]);
};
