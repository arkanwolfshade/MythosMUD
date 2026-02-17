// Player status effects hook (death/delirium detection)
// Extracted from GameClientV2Container to reduce complexity

import { useCallback, useEffect } from 'react';
import type { LucidityStatus } from '../../../types/lucidity';
import { logger } from '../../../utils/logger';
import type { Player, Room } from '../types';

interface UsePlayerStatusEffectsParams {
  player: Player | null;
  room: Room | null;
  lucidityStatus: LucidityStatus | null;
  isDead: boolean;
  isDelirious: boolean;
  setIsDead: (dead: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setDeliriumLocation: (location: string) => void;
  hasRespawned: boolean;
  setHasRespawned: (hasRespawned: boolean) => void;
}

export const usePlayerStatusEffects = ({
  player,
  room,
  lucidityStatus,
  isDead,
  isDelirious,
  setIsDead,
  setIsDelirious,
  setDeliriumLocation,
  hasRespawned,
  setHasRespawned,
}: UsePlayerStatusEffectsParams) => {
  // Helper function to get current lucidity value
  const getCurrentLucidity = useCallback((player: Player | null, lucidityStatus: LucidityStatus | null): number => {
    if (lucidityStatus && lucidityStatus.current !== undefined) {
      return lucidityStatus.current;
    }
    if (player && player.stats && player.stats.lucidity !== undefined) {
      return player.stats.lucidity;
    }
    return 100;
  }, []);

  // Helper function to handle delirium entry
  const handleDeliriumEntry = useCallback(
    (currentLucidity: number, roomId: string | undefined) => {
      setIsDelirious(true);
      setDeliriumLocation(roomId || 'Unknown Location');
      logger.info('GameClientV2Container', 'Player detected as delirious', {
        currentLucidity,
        roomId,
      });
    },
    [setIsDelirious, setDeliriumLocation]
  );

  // Helper function to handle delirium exit
  const handleDeliriumExit = useCallback(
    (currentLucidity: number, roomId: string | undefined) => {
      setIsDelirious(false);
      logger.info('GameClientV2Container', 'Player detected as lucid', {
        currentLucidity,
        roomId,
      });
    },
    [setIsDelirious]
  );

  // Check if player is dead based on DP or room location
  useEffect(() => {
    if (!player) return;

    const currentDp = player.stats?.current_dp ?? 0;
    const roomId = room?.id;
    const isInLimbo = roomId === 'limbo_death_void_limbo_death_void';
    // Respawn destination room: when we've already respawned in this session and are currently not dead,
    // do not set isDead true here. This prevents a stale player (current_dp <= -10) from event-log
    // re-projection from re-opening the respawn modal after a successful respawn.
    const isRespawnRoom = roomId === 'earth_arkhamcity_sanitarium_room_foyer_001';
    const skipDeadInRespawnRoom = isRespawnRoom && !isDead && hasRespawned;

    // Player is dead only when DP <= -10 (server only moves to limbo at -10).
    // Do not use isInLimbo alone: event ordering can deliver room=limbo before the -10 DP update,
    // which would show the respawn modal at 0 DP.
    // CRITICAL: Only set isDead when currentDp is actually <= -10, never at 0 DP
    // Defensive check: ensure currentDp is a number and explicitly check it's <= -10
    const currentDpNum = typeof currentDp === 'number' ? currentDp : 0;
    const isActuallyDead = currentDpNum <= -10;

    if (isActuallyDead && !skipDeadInRespawnRoom) {
      if (!isDead) {
        setIsDead(true);
        setHasRespawned(false);
        logger.info('GameClientV2Container', 'Player detected as dead', {
          currentDp: currentDpNum,
          roomId,
          isInLimbo,
        });
      }
    } else if (isDead && (currentDpNum > -10 || !isInLimbo)) {
      // Player is no longer dead
      setIsDead(false);
      logger.info('GameClientV2Container', 'Player detected as alive', {
        currentDp,
        roomId,
      });
    }
  }, [player, room, isDead, setIsDead, hasRespawned, setHasRespawned]);

  // Check if player is delirious based on lucidity
  useEffect(() => {
    if (!player) return;

    const currentLucidity = getCurrentLucidity(player, lucidityStatus);
    const roomId = room ? room.id : undefined;
    const shouldBeDelirious = currentLucidity <= -10;

    if (shouldBeDelirious && !isDelirious) {
      handleDeliriumEntry(currentLucidity, roomId);
    } else if (!shouldBeDelirious && isDelirious) {
      handleDeliriumExit(currentLucidity, roomId);
    }
  }, [player, room, lucidityStatus, isDelirious, getCurrentLucidity, handleDeliriumEntry, handleDeliriumExit]);
};
