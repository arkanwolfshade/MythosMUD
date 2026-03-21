// Assembles the public return object for useGameClientV2Container (pure, for Lizard NLOC).

import type { ActiveEffectDisplay, GameState } from '../utils/stateUpdateUtils';
import {
  buildHandlerPublicFields,
  buildNetPublicFields,
  buildSliceAndPropsPublicFields,
} from './gameClientV2ContainerReturnParts';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';

export interface GameClientV2ContainerPublicApi {
  playerName: string;
  authToken: string;
  isLoggingOut: boolean;
  gameState: GameState;
  mythosTime: GameClientV2MergedSlice['mythosTime'];
  healthStatus: GameClientV2MergedSlice['healthStatus'];
  lucidityStatus: GameClientV2MergedSlice['lucidityStatus'];
  isMortallyWounded: boolean;
  isDead: boolean;
  deathLocation: string;
  isRespawning: boolean;
  isDelirious: boolean;
  deliriumLocation: string;
  isDeliriumRespawning: boolean;
  isMainMenuOpen: boolean;
  setIsMainMenuOpen: GameClientV2MergedSlice['setIsMainMenuOpen'];
  showMap: boolean;
  setShowMap: GameClientV2MergedSlice['setShowMap'];
  tabs: GameClientV2MergedSlice['tabs'];
  activeTabId: GameClientV2MergedSlice['activeTabId'];
  addTab: GameClientV2MergedSlice['addTab'];
  closeTab: GameClientV2MergedSlice['closeTab'];
  setActiveTab: GameClientV2MergedSlice['setActiveTab'];
  clearedFollowRequestId: GameClientV2MergedSlice['clearedFollowRequestId'];
  setClearedFollowRequestId: GameClientV2MergedSlice['setClearedFollowRequestId'];
  clearedPartyInviteId: GameClientV2MergedSlice['clearedPartyInviteId'];
  setClearedPartyInviteId: GameClientV2MergedSlice['setClearedPartyInviteId'];
  setGameState: GameClientV2MergedSlice['setGameState'];
  clearPendingFollowRequest: GameClientV2NetworkPhase['clearPendingFollowRequest'];
  sendMessage: GameClientV2NetworkPhase['sendMessage'];
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  handleLogout: () => Promise<void>;
  handleCommandSubmit: (command: string) => Promise<void>;
  handleChatMessage: (message: string, channel: string) => Promise<void>;
  handleClearMessages: () => void;
  handleClearHistory: () => void;
  handleRespawn: () => Promise<void>;
  handleDeliriumRespawn: () => Promise<void>;
  activeEffects: ActiveEffectDisplay[];
}

export function buildGameClientV2ContainerReturn(
  props: GameClientV2ContainerProps,
  slice: GameClientV2MergedSlice,
  net: GameClientV2NetworkPhase,
  activeEffects: ActiveEffectDisplay[],
  handleLogout: () => Promise<void>,
  handleCommandSubmit: (command: string) => Promise<void>,
  handleChatMessage: (message: string, channel: string) => Promise<void>,
  handleClearMessages: () => void,
  handleClearHistory: () => void,
  handleRespawn: () => Promise<void>,
  handleDeliriumRespawn: () => Promise<void>
): GameClientV2ContainerPublicApi {
  return {
    ...buildSliceAndPropsPublicFields(props, slice),
    ...buildNetPublicFields(net),
    ...buildHandlerPublicFields(
      handleLogout,
      handleCommandSubmit,
      handleChatMessage,
      handleClearMessages,
      handleClearHistory,
      handleRespawn,
      handleDeliriumRespawn,
      activeEffects
    ),
  };
}
