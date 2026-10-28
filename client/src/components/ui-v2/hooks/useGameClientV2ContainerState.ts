// UI + game model + survival state for GameClientV2Container (split for Lizard NLOC).

import { useState } from 'react';

import type { HealthStatus } from '../../../types/health';
import type { MythosTimeState } from '../../../types/mythosTime';
import { useTabbedInterface } from '../useTabbedInterface';
import type { GameState } from '../utils/stateUpdateUtils';

export function useGameClientV2UiAndTabsState() {
  const [isMainMenuOpen, setIsMainMenuOpen] = useState(false);
  const [showMap, setShowMap] = useState(false);
  const [clearedFollowRequestId, setClearedFollowRequestId] = useState<string | null>(null);
  const [clearedPartyInviteId, setClearedPartyInviteId] = useState<string | null>(null);
  const { tabs, activeTabId, addTab, closeTab, setActiveTab } = useTabbedInterface([]);
  return {
    isMainMenuOpen,
    setIsMainMenuOpen,
    showMap,
    setShowMap,
    clearedFollowRequestId,
    setClearedFollowRequestId,
    clearedPartyInviteId,
    setClearedPartyInviteId,
    tabs,
    activeTabId,
    addTab,
    closeTab,
    setActiveTab,
  };
}

export function useGameClientV2GameModelState() {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
    loginGracePeriodActive: false,
    loginGracePeriodRemaining: 0,
  });
  return { gameState, setGameState };
}

/**
 * Only "is the respawn HTTP call in flight" is real local UI state; death/delirium/lucidity are
 * server-authoritative and live in GameState (set by the projector from player_died, rescue_update,
 * player_respawned, game_state, lucidity_change -- see .cursor/rules/server-authority.mdc).
 */
export function useGameClientV2SurvivalAndTimeState() {
  const [isRespawning, setIsRespawning] = useState(false);
  const [isDeliriumRespawning, setIsDeliriumRespawning] = useState(false);
  const [healthStatus, setHealthStatus] = useState<HealthStatus | null>(null);
  const [mythosTime, setMythosTime] = useState<MythosTimeState | null>(null);

  return {
    isRespawning,
    setIsRespawning,
    isDeliriumRespawning,
    setIsDeliriumRespawning,
    healthStatus,
    setHealthStatus,
    mythosTime,
    setMythosTime,
  };
}
