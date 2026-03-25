// UI + game model + survival state for GameClientV2Container (split for Lizard NLOC).

import { useState } from 'react';

import type { HealthStatus } from '../../../types/health';
import type { HallucinationMessage, LucidityStatus, RescueState } from '../../../types/lucidity';
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

export function useGameClientV2SurvivalAndTimeState() {
  const [isMortallyWounded, setIsMortallyWounded] = useState(false);
  const [isDead, setIsDead] = useState(false);
  const [deathLocation] = useState<string>('Unknown Location');
  const [isRespawning, setIsRespawning] = useState(false);
  const [isDelirious, setIsDelirious] = useState(false);
  const [deliriumLocation, setDeliriumLocation] = useState<string>('Unknown Location');
  const [isDeliriumRespawning, setIsDeliriumRespawning] = useState(false);
  const [lucidityStatus] = useState<LucidityStatus | null>(null);
  const [healthStatus, setHealthStatus] = useState<HealthStatus | null>(null);
  const [, setHallucinationFeed] = useState<HallucinationMessage[]>([]);
  const [rescueState, setRescueState] = useState<RescueState | null>(null);
  const [mythosTime, setMythosTime] = useState<MythosTimeState | null>(null);
  const [hasRespawned, setHasRespawned] = useState(false);

  return {
    isMortallyWounded,
    setIsMortallyWounded,
    isDead,
    setIsDead,
    deathLocation,
    isRespawning,
    setIsRespawning,
    isDelirious,
    setIsDelirious,
    deliriumLocation,
    setDeliriumLocation,
    isDeliriumRespawning,
    setIsDeliriumRespawning,
    lucidityStatus,
    healthStatus,
    setHealthStatus,
    setHallucinationFeed,
    rescueState,
    setRescueState,
    mythosTime,
    setMythosTime,
    hasRespawned,
    setHasRespawned,
  };
}
