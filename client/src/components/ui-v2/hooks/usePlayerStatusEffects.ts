// Player status effects hook (death/delirium detection)
// Extracted from GameClientV2Container to reduce complexity

import { useCallback, useEffect } from 'react';
import type { LucidityStatus } from '../../../types/lucidity';
import { logger } from '../../../utils/logger';
import type { Player, Room } from '../types';

interface PlayerStatusSetters {
  setIsDead: (dead: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setDeliriumLocation: (location: string) => void;
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
}

const LIMBO_ROOM_ID = 'limbo_death_void_limbo_death_void';
const RESPAWN_ROOM_ID = 'earth_arkhamcity_sanitarium_room_foyer_001';

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

function markPlayerDead(setters: PlayerStatusSetters, currentDpNum: number, roomId: string | undefined): void {
  setters.setIsDead(true);
  setters.setHasRespawned(false);
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
  setters: PlayerStatusSetters
): void {
  const currentDpNum = currentDpOf(player);
  const roomId = room?.id;
  if (currentDpNum <= -10 && !skipDeadInRespawnRoom(roomId, isDead, hasRespawned)) {
    if (!isDead) markPlayerDead(setters, currentDpNum, roomId);
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
  const { player, room, lucidityStatus, isDead, isDelirious, hasRespawned, setters } = params;
  const { setIsDead, setIsDelirious, setDeliriumLocation, setHasRespawned } = setters;

  const statusSetters = useCallback(
    (): PlayerStatusSetters => ({ setIsDead, setIsDelirious, setDeliriumLocation, setHasRespawned }),
    [setIsDead, setIsDelirious, setDeliriumLocation, setHasRespawned]
  );

  useEffect(() => {
    if (!player) return;
    syncDeathState(player, room, isDead, hasRespawned, statusSetters());
  }, [player, room, isDead, hasRespawned, statusSetters]);

  useEffect(() => {
    if (!player) return;
    syncDeliriumState(player, room, lucidityStatus, isDelirious, statusSetters());
  }, [player, room, lucidityStatus, isDelirious, statusSetters]);
};
