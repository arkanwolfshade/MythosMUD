import React, { useEffect, useMemo, useRef, useState } from 'react';
import { useContainerStore } from '../../stores/containerStore';
import type { HealthStatus } from '../../types/health';
import { determineDpTier } from '../../types/health';
import type { HallucinationMessage, LucidityStatus, RescueState } from '../../types/lucidity';
import type { MythosTimeState } from '../../types/mythosTime';
import { logger } from '../../utils/logger';
import { useMemoryMonitor } from '../../utils/memoryMonitor';
import { DeathInterstitial } from '../DeathInterstitial';
import { DeliriumInterstitial } from '../DeliriumInterstitial';
import { MainMenuModal } from '../MainMenuModal';
import { MapView } from '../MapView';
import { AsciiMinimap } from '../map/AsciiMinimap';
import { ModalContainer } from '../ui/ModalContainer';
import { GameClientV2 } from './GameClientV2';
import { TabbedInterfaceOverlay } from './components/TabbedInterfaceOverlay';
import { useCommandHandlers } from './hooks/useCommandHandlers';
import { useEventProcessing } from './hooks/useEventProcessing';
import { useGameConnectionManagement } from './hooks/useGameConnectionManagement';
import { useHallucinationFeedCleanup } from './hooks/useHallucinationFeedCleanup';
import { useMythosTimeBootstrap } from './hooks/useMythosTimeBootstrap';
import { usePlayerStatusEffects } from './hooks/usePlayerStatusEffects';
import { useRefSynchronization } from './hooks/useRefSynchronization';
import { useRespawnHandlers } from './hooks/useRespawnHandlers';
import type { ChatMessage, Player, Room } from './types';
import { useTabbedInterface } from './useTabbedInterface';
import type { ActiveEffectDisplay, GameState } from './utils/stateUpdateUtils';

interface GameClientV2ContainerProps {
  playerName: string;
  authToken: string;
  characterId?: string; // MULTI-CHARACTER: Selected character ID for WebSocket connection
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

// Container component that manages game state and renders GameClientV2
// Based on findings from "State Management Patterns" - Dr. Armitage, 1928
export const GameClientV2Container: React.FC<GameClientV2ContainerProps> = ({
  playerName,
  authToken,
  characterId,
  onLogout,
  isLoggingOut = false,
  onDisconnect: _onDisconnect,
}) => {
  const [isMainMenuOpen, setIsMainMenuOpen] = useState(false);
  const [showMap, setShowMap] = useState(false);

  /** Server-authority: rely on server follow_request_cleared / party_invite_cleared where possible;
   * cleared* IDs are UX-only so we do not re-show after user dismiss; do not persist across reconnect. */
  const [clearedFollowRequestId, setClearedFollowRequestId] = useState<string | null>(null);
  const [clearedPartyInviteId, setClearedPartyInviteId] = useState<string | null>(null);

  // Tabbed interface for in-app tabs
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

  // Memory monitoring
  const { detector } = useMemoryMonitor('GameClientV2Container');

  // Container store hooks - kept for future use

  const _openContainer = useContainerStore(state => state.openContainer);

  const _closeContainer = useContainerStore(state => state.closeContainer);

  const _updateContainer = useContainerStore(state => state.updateContainer);

  const _handleContainerDecayed = useContainerStore(state => state.handleContainerDecayed);

  const _getContainer = useContainerStore(state => state.getContainer);

  const _isContainerOpen = useContainerStore(state => state.isContainerOpen);

  // Mark as intentionally used to satisfy TypeScript (kept for future use)
  void _openContainer;
  void _closeContainer;
  void _updateContainer;
  void _handleContainerDecayed;
  void _getContainer;
  void _isContainerOpen;

  useEffect(() => {
    detector.start();
    return () => {
      detector.stop();
    };
  }, [detector]);

  // Refs for stable references and event processing
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
  /** Set when user chose Exit (/rest); on socket close we skip reconnection and go to login. */
  const intentionalExitInProgressRef = useRef(false);

  // Ref synchronization
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

  // Bootstrap Mythos time
  useMythosTimeBootstrap({
    authToken,
    setMythosTime,
    lastDaypartRef,
    lastHolidayIdsRef,
  });

  // Clean up hallucination feed
  useHallucinationFeedCleanup(setHallucinationFeed);

  // Event processing hook (event-sourced: EventStore + projector)
  const { handleGameEvent, clearPendingFollowRequest } = useEventProcessing({
    setGameState,
  });

  // Game connection management
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

  // Derive healthStatus from player stats (since event handlers aren't called in projector-only pattern)
  // Use useMemo to avoid cascading renders from setState in useEffect
  const derivedHealthStatus = useMemo(() => {
    const player = gameState.player;
    if (player?.stats) {
      const stats = player.stats;
      const currentDp = stats.current_dp;
      const maxDp = stats.max_dp ?? 100;

      if (currentDp !== undefined) {
        return {
          current: currentDp,
          max: maxDp,
          tier: determineDpTier(currentDp, maxDp),
          posture: stats.position,
          inCombat: player.in_combat ?? false,
          lastChange: healthStatus?.lastChange, // Preserve last change if available
        } as HealthStatus;
      }
    }
    return null;
  }, [gameState.player, healthStatus?.lastChange]);

  // Update healthStatus when derived value changes
  useEffect(() => {
    setHealthStatus(derivedHealthStatus);
  }, [derivedHealthStatus]);

  const [hasRespawned, setHasRespawned] = useState(false);

  // Player status effects (death/delirium detection)
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

  // Command handlers
  const { handleCommandSubmit, handleChatMessage, handleClearMessages, handleClearHistory } = useCommandHandlers({
    isConnected,
    sendCommand,
    setGameState,
  });

  const handleLogout = async () => {
    // Do not clear the event log here: clearing causes the next processEventQueue to
    // project state from only the new post-/rest events, overwriting gameState with
    // no player/room and blanking all panels. Keep the log so panels stay visible
    // through the logout countdown. Clear on actual disconnect/unmount if needed.
    // Send /rest command instead of immediate disconnect
    // The /rest command will handle the countdown and disconnect automatically
    if (!isConnected) {
      // If not connected, fall back to immediate disconnect
      if (onLogout) {
        onLogout();
      } else {
        disconnect();
      }
      return;
    }

    // Signal that this close is intentional so connection layer skips reconnection
    intentionalExitInProgressRef.current = true;
    // Send the /rest command
    const success = await sendCommand('rest', []);
    if (!success) {
      logger.error('GameClientV2Container', 'Failed to send /rest command, falling back to immediate disconnect');
      // Fallback to immediate disconnect if command fails
      if (onLogout) {
        onLogout();
      } else {
        disconnect();
      }
    }
    // If successful, the /rest command will handle the countdown and disconnect
  };

  // Respawn handlers
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

  // Handle ESC key to open/close main menu (only when map is not open)
  useEffect(() => {
    if (isDead || showMap) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setIsMainMenuOpen(prev => !prev);
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isDead, showMap]);

  return (
    <div
      className={`game-terminal-container ${isMortallyWounded ? 'mortally-wounded' : ''} ${isDead ? 'dead' : ''}`}
      data-game-container
    >
      {/* Only show game panels when no tabs are open */}
      {tabs.length === 0 && (
        <GameClientV2
          playerName={playerName}
          authToken={authToken}
          onLogout={handleLogout}
          isLoggingOut={isLoggingOut}
          player={gameState.player}
          room={gameState.room}
          messages={gameState.messages}
          commandHistory={gameState.commandHistory}
          isConnected={isConnected}
          isConnecting={isConnecting}
          error={error}
          reconnectAttempts={reconnectAttempts}
          mythosTime={gameState.mythosTime ?? mythosTime}
          healthStatus={healthStatus}
          lucidityStatus={lucidityStatus}
          activeEffects={
            gameState.activeEffects ??
            (gameState.loginGracePeriodActive && gameState.loginGracePeriodRemaining !== undefined
              ? [
                  {
                    effect_type: 'login_warded',
                    label: 'Warded',
                    remaining_seconds: gameState.loginGracePeriodRemaining,
                  } satisfies ActiveEffectDisplay,
                ]
              : [])
          }
          followingTarget={gameState.followingTarget ?? null}
          onSendCommand={handleCommandSubmit}
          onSendChatMessage={handleChatMessage}
          onClearMessages={handleClearMessages}
          onClearHistory={handleClearHistory}
          onDownloadLogs={() => {
            logger.downloadLogs();
          }}
        />
      )}

      <DeathInterstitial
        isVisible={isDead}
        deathLocation={deathLocation}
        onRespawn={handleRespawn}
        isRespawning={isRespawning}
      />
      <DeliriumInterstitial
        isVisible={isDelirious}
        deliriumLocation={deliriumLocation}
        onRespawn={handleDeliriumRespawn}
        isRespawning={isDeliriumRespawning}
      />

      {/* Follow request prompt: accept/decline when another player wants to follow you */}
      {gameState.pendingFollowRequest && clearedFollowRequestId !== gameState.pendingFollowRequest.request_id && (
        <ModalContainer
          isOpen={true}
          onClose={() => {
            const reqId = gameState.pendingFollowRequest!.request_id;
            setClearedFollowRequestId(reqId);
            setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
            clearPendingFollowRequest(reqId);
            sendMessage('follow_response', { request_id: reqId, accept: false });
          }}
          title="Follow request"
          maxWidth="sm"
          showCloseButton={true}
          overlayZIndex={10000}
          position="center-no-backdrop"
          contentClassName="!bg-black border-2 border-mythos-terminal-primary shadow-2xl"
        >
          <div className="p-4 space-y-4">
            <p className="text-mythos-terminal-text font-medium">
              {gameState.pendingFollowRequest.requestor_name} wants to follow you.
            </p>
            <div className="flex gap-3 justify-end">
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                  text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={() => {
                  const reqId = gameState.pendingFollowRequest!.request_id;
                  setClearedFollowRequestId(reqId);
                  setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
                  clearPendingFollowRequest(reqId);
                  sendMessage('follow_response', { request_id: reqId, accept: false });
                }}
              >
                Decline
              </button>
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                  text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={() => {
                  const reqId = gameState.pendingFollowRequest!.request_id;
                  setClearedFollowRequestId(reqId);
                  setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
                  clearPendingFollowRequest(reqId);
                  sendMessage('follow_response', { request_id: reqId, accept: true });
                }}
              >
                Accept
              </button>
            </div>
          </div>
        </ModalContainer>
      )}

      {/* Party invite prompt: accept/decline when a party leader invites you */}
      {gameState.pendingPartyInvite && clearedPartyInviteId !== gameState.pendingPartyInvite.invite_id && (
        <ModalContainer
          isOpen={true}
          onClose={() => {
            const inviteId = gameState.pendingPartyInvite!.invite_id;
            setClearedPartyInviteId(inviteId);
            setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
            sendMessage('party_invite_response', { invite_id: inviteId, accept: false });
          }}
          title="Party invite"
          maxWidth="sm"
          showCloseButton={true}
          overlayZIndex={10000}
          position="center-no-backdrop"
          contentClassName="!bg-black border-2 border-mythos-terminal-primary shadow-2xl"
        >
          <div className="p-4 space-y-4">
            <p className="text-mythos-terminal-text font-medium">
              {gameState.pendingPartyInvite.inviter_name} has invited you to join their party.
            </p>
            <div className="flex gap-3 justify-end">
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                    text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={() => {
                  const inviteId = gameState.pendingPartyInvite!.invite_id;
                  setClearedPartyInviteId(inviteId);
                  setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
                  sendMessage('party_invite_response', { invite_id: inviteId, accept: false });
                }}
              >
                Decline
              </button>
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                    text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={() => {
                  const inviteId = gameState.pendingPartyInvite!.invite_id;
                  setClearedPartyInviteId(inviteId);
                  setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
                  sendMessage('party_invite_response', { invite_id: inviteId, accept: true });
                }}
              >
                Accept
              </button>
            </div>
          </div>
        </ModalContainer>
      )}

      <MainMenuModal
        isOpen={isMainMenuOpen}
        onClose={() => {
          setIsMainMenuOpen(false);
        }}
        onMapClick={() => {
          // Add map as a tab in the tabbed interface
          if (gameState.room) {
            addTab({
              id: `map-${gameState.room.id}`,
              label: 'Map',
              content: (
                <MapView
                  isOpen={true}
                  onClose={() => {
                    closeTab(`map-${gameState.room?.id}`);
                  }}
                  currentRoom={gameState.room}
                  authToken={authToken}
                  hideHeader={true}
                />
              ),
              closable: true,
            });
          }
        }}
        onLogoutClick={handleLogout}
        currentRoom={
          gameState.room
            ? {
                id: gameState.room.id,
                plane: gameState.room.plane,
                zone: gameState.room.zone,
                subZone: gameState.room.sub_zone,
              }
            : null
        }
        openMapInNewTab={false}
      />

      {/* Tabbed Interface Overlay */}
      <TabbedInterfaceOverlay tabs={tabs} activeTabId={activeTabId} setActiveTab={setActiveTab} closeTab={closeTab} />

      {/* Legacy MapView for backward compatibility (can be removed later) */}
      <MapView
        isOpen={showMap && tabs.length === 0}
        onClose={() => {
          setShowMap(false);
        }}
        currentRoom={gameState.room}
        authToken={authToken}
      />

      {/* ASCII Minimap - always visible when player is in a room */}
      {gameState.room && (
        <AsciiMinimap
          plane={gameState.room.plane || 'earth'}
          zone={gameState.room.zone || 'arkhamcity'}
          subZone={gameState.room.sub_zone}
          currentRoomId={gameState.room.id}
          authToken={authToken}
          size={5}
          position="bottom-right"
          onClick={() => {
            // Open map in a tab or full screen
            if (tabs.length > 0) {
              // If tabs are open, add map as a tab
              addTab({
                id: `map-${gameState.room?.id}`,
                label: 'Map',
                content: (
                  <MapView
                    isOpen={true}
                    onClose={() => {
                      closeTab(`map-${gameState.room?.id}`);
                    }}
                    currentRoom={gameState.room}
                    authToken={authToken}
                    hideHeader={true}
                  />
                ),
                closable: true,
              });
              setActiveTab(`map-${gameState.room?.id}`);
            } else {
              // Otherwise open full screen
              setShowMap(true);
            }
          }}
        />
      )}
    </div>
  );
};
