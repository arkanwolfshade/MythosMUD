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
    // #region agent log
    if (typeof fetch !== 'undefined') {
      fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: 'usePlayerStatusEffects.ts:useEffect:run',
          message: 'status effect effect run',
          data: { currentDp, roomId, isInLimbo, isDead },
          timestamp: Date.now(),
          sessionId: 'debug-session',
          hypothesisId: 'H2',
        }),
      }).catch(() => {});
    }
    // #endregion

    // Player is dead if DP <= -10 or in limbo
    if (currentDp <= -10 || isInLimbo) {
      if (!isDead) {
        // #region agent log
        if (typeof fetch !== 'undefined') {
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'usePlayerStatusEffects.ts:useEffect:setIsDead(true)',
              message: 'status effect setting isDead=true',
              data: { currentDp, roomId, isInLimbo },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              hypothesisId: 'H2',
            }),
          }).catch(() => {});
        }
        // #endregion
        setIsDead(true);
        logger.info('GameClientV2Container', 'Player detected as dead', {
          currentDp,
          roomId,
          isInLimbo,
        });
      }
    } else if (isDead && currentDp > -10 && !isInLimbo) {
      // Player is no longer dead
      // #region agent log
      if (typeof fetch !== 'undefined') {
        fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            location: 'usePlayerStatusEffects.ts:useEffect:setIsDead(false)',
            message: 'status effect setting isDead=false',
            data: { currentDp, roomId },
            timestamp: Date.now(),
            sessionId: 'debug-session',
            hypothesisId: 'H2',
          }),
        }).catch(() => {});
      }
      // #endregion
      setIsDead(false);
      logger.info('GameClientV2Container', 'Player detected as alive', {
        currentDp,
        roomId,
      });
    }
  }, [player, room, isDead, setIsDead]);

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
