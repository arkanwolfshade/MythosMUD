// Health status derived from projector-authoritative player stats.

import { useEffect, useMemo } from 'react';

import { deriveHealthStatusFromPlayer } from '../../../types/health';
import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';

export function useGameClientV2ContainerHealthSync(slice: GameClientV2MergedSlice): void {
  const { gameState, healthStatus, setHealthStatus } = slice;

  const derivedHealthStatus = useMemo(
    () => deriveHealthStatusFromPlayer(gameState.player, healthStatus?.lastChange),
    [gameState.player, healthStatus?.lastChange]
  );

  useEffect(() => {
    setHealthStatus(derivedHealthStatus);
  }, [derivedHealthStatus, setHealthStatus]);
}
