// Commands, respawn, and assembled return for GameClientV2Container.

import { useMemo } from 'react';

import { deriveActiveEffectsForHeader } from './gameClientV2ContainerActiveEffects';
import {
  buildGameClientV2ContainerReturn,
  type GameClientV2ContainerPublicApi,
} from './gameClientV2ContainerBuildReturn';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useGameClientV2ContainerEscapeMenuEffect } from './useGameClientV2ContainerEscapeMenuEffect';
import { useGameClientV2ContainerLogoutAndRespawn } from './useGameClientV2ContainerLogoutAndRespawn';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';
import { useGameClientV2ContainerPlayerAndCommands } from './useGameClientV2ContainerPlayerAndCommands';
import type { GameClientV2RefsBundle } from './useGameClientV2ContainerRefsAndBootstrap';

export function useGameClientV2ContainerLifecycle(
  props: GameClientV2ContainerProps,
  slice: GameClientV2MergedSlice,
  refs: GameClientV2RefsBundle,
  net: GameClientV2NetworkPhase
): GameClientV2ContainerPublicApi {
  const { handleCommandSubmit, handleChatMessage, handleClearMessages, handleClearHistory } =
    useGameClientV2ContainerPlayerAndCommands(slice, net);

  const { handleLogout, handleRespawn, handleDeliriumRespawn } = useGameClientV2ContainerLogoutAndRespawn(
    props,
    slice,
    refs,
    net
  );

  useGameClientV2ContainerEscapeMenuEffect(slice);

  const activeEffects = useMemo(() => deriveActiveEffectsForHeader(slice.gameState), [slice.gameState]);

  return buildGameClientV2ContainerReturn(
    props,
    slice,
    net,
    activeEffects,
    handleLogout,
    handleCommandSubmit,
    handleChatMessage,
    handleClearMessages,
    handleClearHistory,
    handleRespawn,
    handleDeliriumRespawn
  );
}
