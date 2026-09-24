// Command handlers for GameClientV2Container. Death/delirium status is server-authoritative and
// lives directly in gameState (see stateUpdateUtils.GameState) -- no client-side derivation here.

import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useCommandHandlers } from './useCommandHandlers';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';

export function useGameClientV2ContainerPlayerAndCommands(
  slice: GameClientV2MergedSlice,
  net: GameClientV2NetworkPhase
) {
  return useCommandHandlers({
    isConnected: net.isConnected,
    sendCommand: net.sendCommand,
    setGameState: slice.setGameState,
    handleGameEvent: net.handleGameEvent,
  });
}
