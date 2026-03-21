// Player status side-effects and command handlers for GameClientV2Container.

import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useCommandHandlers } from './useCommandHandlers';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';
import { usePlayerStatusEffects } from './usePlayerStatusEffects';

export function useGameClientV2ContainerPlayerAndCommands(
  slice: GameClientV2MergedSlice,
  net: GameClientV2NetworkPhase
) {
  usePlayerStatusEffects({
    player: slice.gameState.player,
    room: slice.gameState.room,
    lucidityStatus: slice.lucidityStatus,
    isDead: slice.isDead,
    isDelirious: slice.isDelirious,
    setIsDead: slice.setIsDead,
    setIsDelirious: slice.setIsDelirious,
    setDeliriumLocation: slice.setDeliriumLocation,
    hasRespawned: slice.hasRespawned,
    setHasRespawned: slice.setHasRespawned,
  });

  return useCommandHandlers({
    isConnected: net.isConnected,
    sendCommand: net.sendCommand,
    setGameState: slice.setGameState,
  });
}
