// Splits public return assembly so Lizard NLOC stays under per-method limits.

import type { ActiveEffectDisplay } from '../utils/stateUpdateUtils';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import type { GameClientV2NetworkPhase } from './useGameClientV2ContainerNetworkPhase';

export function buildSliceAndPropsPublicFields(props: GameClientV2ContainerProps, slice: GameClientV2MergedSlice) {
  return {
    playerName: props.playerName,
    authToken: props.authToken,
    isLoggingOut: props.isLoggingOut ?? false,
    gameState: slice.gameState,
    mythosTime: slice.mythosTime,
    healthStatus: slice.healthStatus,
    lucidityStatus: slice.lucidityStatus,
    isMortallyWounded: slice.isMortallyWounded,
    isDead: slice.isDead,
    deathLocation: slice.deathLocation,
    isRespawning: slice.isRespawning,
    isDelirious: slice.isDelirious,
    deliriumLocation: slice.deliriumLocation,
    isDeliriumRespawning: slice.isDeliriumRespawning,
    isMainMenuOpen: slice.isMainMenuOpen,
    setIsMainMenuOpen: slice.setIsMainMenuOpen,
    showMap: slice.showMap,
    setShowMap: slice.setShowMap,
    tabs: slice.tabs,
    activeTabId: slice.activeTabId,
    addTab: slice.addTab,
    closeTab: slice.closeTab,
    setActiveTab: slice.setActiveTab,
    clearedFollowRequestId: slice.clearedFollowRequestId,
    setClearedFollowRequestId: slice.setClearedFollowRequestId,
    clearedPartyInviteId: slice.clearedPartyInviteId,
    setClearedPartyInviteId: slice.setClearedPartyInviteId,
    setGameState: slice.setGameState,
  };
}

export function buildNetPublicFields(net: GameClientV2NetworkPhase) {
  return {
    clearPendingFollowRequest: net.clearPendingFollowRequest,
    sendMessage: net.sendMessage,
    isConnected: net.isConnected,
    isConnecting: net.isConnecting,
    error: net.error,
    reconnectAttempts: net.reconnectAttempts,
  };
}

export function buildHandlerPublicFields(
  handleLogout: () => Promise<void>,
  handleCommandSubmit: (command: string) => Promise<void>,
  handleChatMessage: (message: string, channel: string) => Promise<void>,
  handleClearMessages: () => void,
  handleClearHistory: () => void,
  handleRespawn: () => Promise<void>,
  handleDeliriumRespawn: () => Promise<void>,
  activeEffects: ActiveEffectDisplay[]
) {
  return {
    handleLogout,
    handleCommandSubmit,
    handleChatMessage,
    handleClearMessages,
    handleClearHistory,
    handleRespawn,
    handleDeliriumRespawn,
    activeEffects,
  };
}
