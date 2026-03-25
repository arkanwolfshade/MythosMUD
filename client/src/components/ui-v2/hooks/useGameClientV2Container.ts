// GameClientV2Container state and wiring (orchestrator; split for Lizard NLOC).

import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useGameClientV2ContainerHealthSync } from './useGameClientV2ContainerHealthSync';
import { useGameClientV2ContainerLifecycle } from './useGameClientV2ContainerLifecycle';
import { useGameClientV2ContainerNetworkPhase } from './useGameClientV2ContainerNetworkPhase';
import { useGameClientV2ContainerRefsAndBootstrap } from './useGameClientV2ContainerRefsAndBootstrap';
import {
  useGameClientV2GameModelState,
  useGameClientV2SurvivalAndTimeState,
  useGameClientV2UiAndTabsState,
} from './useGameClientV2ContainerState';
import { useGameClientV2MemoryMonitorEffect } from './useGameClientV2MemoryMonitorEffect';

export type { GameClientV2ContainerPublicApi } from './gameClientV2ContainerBuildReturn';
export type { GameClientV2ContainerProps } from './gameClientV2ContainerTypes';

export function useGameClientV2Container(props: GameClientV2ContainerProps) {
  const ui = useGameClientV2UiAndTabsState();
  const game = useGameClientV2GameModelState();
  const survival = useGameClientV2SurvivalAndTimeState();
  useGameClientV2MemoryMonitorEffect();
  const slice: GameClientV2MergedSlice = { ...ui, ...game, ...survival };
  const refs = useGameClientV2ContainerRefsAndBootstrap(props.authToken, slice);
  const net = useGameClientV2ContainerNetworkPhase(props, slice, refs);
  useGameClientV2ContainerHealthSync(slice);
  return useGameClientV2ContainerLifecycle(props, slice, refs, net);
}
