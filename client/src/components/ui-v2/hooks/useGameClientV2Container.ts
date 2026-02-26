// Extracted from GameClientV2Container to reduce cyclomatic complexity (hook + helpers).

import { useEffect, useMemo, useRef, useState } from 'react';

import { useContainerStore } from '../../../stores/containerStore';
import type { HealthStatus } from '../../../types/health';
import { determineDpTier } from '../../../types/health';
import type { HallucinationMessage, LucidityStatus, RescueState } from '../../../types/lucidity';
import type { MythosTimeState } from '../../../types/mythosTime';
import type { SendMessageFn } from '../../../utils/clientErrorReporter';
import { OCCUPANTS_PANEL_EMPTY_PLAYERS, reportClientError } from '../../../utils/clientErrorReporter';
import { logger } from '../../../utils/logger';
import { useMemoryMonitor } from '../../../utils/memoryMonitor';
import type { ChatMessage, Player, Room } from '../types';
import { useTabbedInterface } from '../useTabbedInterface';
import type { ActiveEffectDisplay, GameState } from '../utils/stateUpdateUtils';
import { useCommandHandlers } from './useCommandHandlers';
import { useEventProcessing } from './useEventProcessing';
import { useGameConnectionManagement } from './useGameConnectionManagement';
import { useHallucinationFeedCleanup } from './useHallucinationFeedCleanup';
import { useMythosTimeBootstrap } from './useMythosTimeBootstrap';
import { usePlayerStatusEffects } from './usePlayerStatusEffects';
import { useRefSynchronization } from './useRefSynchronization';
import { useRespawnHandlers } from './useRespawnHandlers';

export interface GameClientV2ContainerProps {
  playerName: string;
  authToken: string;
  characterId?: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

function deriveHealthFromPlayer(
  player: GameState['player'],
  previousLastChange: HealthStatus['lastChange']
): HealthStatus | null {
  if (!player?.stats) return null;
  const stats = player.stats;
  const currentDp = stats.current_dp;
  const maxDp = stats.max_dp ?? 100;
  if (currentDp === undefined) return null;
  return {
    current: currentDp,
    max: maxDp,
    tier: determineDpTier(currentDp, maxDp),
    posture: stats.position,
    inCombat: player.in_combat ?? false,
    lastChange: previousLastChange,
  } as HealthStatus;
}

function runEmptyOccupantsReportIfNeeded(
  isConnected: boolean,
  player: Player | null,
  room: Room | null,
  roomFirstSetAt: number | null,
  reportedRoomIds: Set<string>,
  sendMessage: SendMessageFn
): void {
  if (!isConnected || !player || !room?.id) return;
  const players = room.players ?? [];
  if (players.length > 0) return;
  const now = Date.now();
  if (roomFirstSetAt !== null && now - roomFirstSetAt < 2000) return;
  if (reportedRoomIds.has(room.id)) return;
  reportedRoomIds.add(room.id);
  reportClientError(
    sendMessage,
    OCCUPANTS_PANEL_EMPTY_PLAYERS,
    'Occupants panel players list is empty but current player exists',
    {
      player_name: player.name,
      room_id: room.id,
      room_name: room.name,
    }
  );
}

async function performLogout(
  isConnected: boolean,
  onLogout: (() => void) | undefined,
  disconnect: () => void,
  sendCommand: (command: string, args?: string[]) => Promise<boolean>,
  setIntentionalExit: (value: boolean) => void
): Promise<void> {
  if (!isConnected) {
    if (onLogout) onLogout();
    else disconnect();
    return;
  }
  setIntentionalExit(true);
  const success = await sendCommand('rest', []);
  if (!success) {
    logger.error('GameClientV2Container', 'Failed to send /rest command, falling back to immediate disconnect');
    if (onLogout) onLogout();
    else disconnect();
  }
}

export function useGameClientV2Container(props: GameClientV2ContainerProps) {
  const { playerName, authToken, characterId, onLogout, isLoggingOut = false } = props;

  const [isMainMenuOpen, setIsMainMenuOpen] = useState(false);
  const [showMap, setShowMap] = useState(false);
  const [clearedFollowRequestId, setClearedFollowRequestId] = useState<string | null>(null);
  const [clearedPartyInviteId, setClearedPartyInviteId] = useState<string | null>(null);
  const { tabs, activeTabId, addTab, closeTab, setActiveTab } = useTabbedInterface([]);

  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
    loginGracePeriodActive: false,
    loginGracePeriodRemaining: 0,
  });

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

  const { detector } = useMemoryMonitor('GameClientV2Container');

  void useContainerStore(state => state.openContainer);
  void useContainerStore(state => state.closeContainer);
  void useContainerStore(state => state.updateContainer);
  void useContainerStore(state => state.handleContainerDecayed);
  void useContainerStore(state => state.getContainer);
  void useContainerStore(state => state.isContainerOpen);

  useEffect(() => {
    detector.start();
    return () => detector.stop();
  }, [detector]);

  const currentMessagesRef = useRef<ChatMessage[]>([]);
  const currentRoomRef = useRef<Room | null>(null);
  const currentPlayerRef = useRef<Player | null>(null);
  const lucidityStatusRef = useRef<LucidityStatus | null>(null);
  const healthStatusRef = useRef<HealthStatus | null>(null);
  const rescueStateRef = useRef<RescueState | null>(null);
  const lastDaypartRef = useRef<string | null>(null);
  const lastHolidayIdsRef = useRef<string[]>([]);
  const rescueTimeoutRef = useRef<number | null>(null);
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);
  const intentionalExitInProgressRef = useRef(false);
  const roomFirstSetAtRef = useRef<number | null>(null);
  const reportedRoomIdsRef = useRef<Set<string>>(new Set());

  useRefSynchronization({
    gameState,
    healthStatus,
    lucidityStatus,
    rescueState,
    setRescueState,
    currentMessagesRef,
    currentRoomRef,
    currentPlayerRef,
    healthStatusRef,
    lucidityStatusRef,
    rescueStateRef,
    rescueTimeoutRef,
  });

  useMythosTimeBootstrap({ authToken, setMythosTime, lastDaypartRef, lastHolidayIdsRef });
  useHallucinationFeedCleanup(setHallucinationFeed);

  const { handleGameEvent, clearPendingFollowRequest } = useEventProcessing({ setGameState });

  const { isConnected, isConnecting, error, reconnectAttempts, sendCommand, sendMessage, disconnect } =
    useGameConnectionManagement({
      authToken,
      playerName,
      characterId,
      onLogout,
      onGameEvent: handleGameEvent,
      setGameState,
      intentionalExitInProgressRef,
    });

  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand]);

  useEffect(() => {
    if (gameState.room?.id && roomFirstSetAtRef.current === null) roomFirstSetAtRef.current = Date.now();
    if (!gameState.room?.id) roomFirstSetAtRef.current = null;
  }, [gameState.room?.id]);

  useEffect(() => {
    runEmptyOccupantsReportIfNeeded(
      isConnected,
      gameState.player ?? null,
      gameState.room ?? null,
      roomFirstSetAtRef.current,
      reportedRoomIdsRef.current,
      sendMessage
    );
  }, [isConnected, gameState.player, gameState.room, sendMessage]);

  const derivedHealthStatus = useMemo(
    () => deriveHealthFromPlayer(gameState.player, healthStatus?.lastChange),
    [gameState.player, healthStatus?.lastChange]
  );
  useEffect(() => {
    setHealthStatus(derivedHealthStatus);
  }, [derivedHealthStatus]);

  usePlayerStatusEffects({
    player: gameState.player,
    room: gameState.room,
    lucidityStatus,
    isDead,
    isDelirious,
    setIsDead,
    setIsDelirious,
    setDeliriumLocation,
    hasRespawned,
    setHasRespawned,
  });

  const { handleCommandSubmit, handleChatMessage, handleClearMessages, handleClearHistory } = useCommandHandlers({
    isConnected,
    sendCommand,
    setGameState,
  });

  const handleLogout = () =>
    performLogout(isConnected, onLogout, disconnect, sendCommand, v => {
      intentionalExitInProgressRef.current = v;
    });

  const { handleRespawn, handleDeliriumRespawn } = useRespawnHandlers({
    authToken,
    setGameState,
    setIsDead,
    setIsMortallyWounded,
    setIsRespawning,
    setIsDelirious,
    setIsDeliriumRespawning,
    setHasRespawned,
    appendRespawnEvent: handleGameEvent,
  });

  useEffect(() => {
    if (isDead || showMap) return;
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setIsMainMenuOpen(prev => !prev);
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [isDead, showMap]);

  const activeEffects: ActiveEffectDisplay[] =
    gameState.activeEffects ??
    (gameState.loginGracePeriodActive && gameState.loginGracePeriodRemaining !== undefined
      ? [
          {
            effect_type: 'login_warded',
            label: 'Warded',
            remaining_seconds: gameState.loginGracePeriodRemaining,
          } satisfies ActiveEffectDisplay,
        ]
      : []);

  return {
    playerName,
    authToken,
    isLoggingOut,
    gameState,
    mythosTime,
    healthStatus,
    lucidityStatus,
    isMortallyWounded,
    isDead,
    deathLocation,
    isRespawning,
    isDelirious,
    deliriumLocation,
    isDeliriumRespawning,
    isMainMenuOpen,
    setIsMainMenuOpen,
    showMap,
    setShowMap,
    tabs,
    activeTabId,
    addTab,
    closeTab,
    setActiveTab,
    clearedFollowRequestId,
    setClearedFollowRequestId,
    clearedPartyInviteId,
    setClearedPartyInviteId,
    setGameState,
    clearPendingFollowRequest,
    sendMessage,
    isConnected,
    isConnecting,
    error,
    reconnectAttempts,
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
