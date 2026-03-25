// Logout and respawn handlers for GameClientV2Container.

import { performGameClientLogout } from './gameClientLogout';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';
import type { GameClientV2RefsBundle } from './useGameClientV2ContainerRefsAndBootstrap';
import { useRespawnHandlers } from './useRespawnHandlers';

export function useGameClientV2ContainerLogoutAndRespawn(
  props: GameClientV2ContainerProps,
  slice: GameClientV2MergedSlice,
  refs: GameClientV2RefsBundle,
  net: GameClientV2NetworkPhase
) {
  const handleLogout = () =>
    performGameClientLogout(net.isConnected, props.onLogout, net.disconnect, net.sendCommand, v => {
      refs.intentionalExitInProgressRef.current = v;
    });

  const { handleRespawn, handleDeliriumRespawn } = useRespawnHandlers({
    authToken: props.authToken,
    setGameState: slice.setGameState,
    setIsDead: slice.setIsDead,
    setIsMortallyWounded: slice.setIsMortallyWounded,
    setIsRespawning: slice.setIsRespawning,
    setIsDelirious: slice.setIsDelirious,
    setIsDeliriumRespawning: slice.setIsDeliriumRespawning,
    setHasRespawned: slice.setHasRespawned,
    appendRespawnEvent: net.handleGameEvent,
  });

  return { handleLogout, handleRespawn, handleDeliriumRespawn };
}
