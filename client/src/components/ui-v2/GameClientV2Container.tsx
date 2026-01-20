import React, { useEffect, useRef, useState } from 'react';
import { useContainerStore } from '../../stores/containerStore';
import type { HealthStatus } from '../../types/health';
import type { HallucinationMessage, LucidityStatus, RescueState } from '../../types/lucidity';
import type { MythosTimeState } from '../../types/mythosTime';
import { logger } from '../../utils/logger';
import { useMemoryMonitor } from '../../utils/memoryMonitor';
import { DeathInterstitial } from '../DeathInterstitial';
import { DeliriumInterstitial } from '../DeliriumInterstitial';
import { MainMenuModal } from '../MainMenuModal';
import { MapView } from '../MapView';
import { AsciiMinimap } from '../map/AsciiMinimap';
import { GameClientV2 } from './GameClientV2';
import { LoginGracePeriodBanner } from './LoginGracePeriodBanner';
import { TabbedInterfaceOverlay } from './components/TabbedInterfaceOverlay';
import type { EventHandlerContext } from './eventHandlers/types';
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
import type { GameState } from './utils/stateUpdateUtils';

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
  const [deathLocation, setDeathLocation] = useState<string>('Unknown Location');
  const [isRespawning, setIsRespawning] = useState(false);
  const [isDelirious, setIsDelirious] = useState(false);
  const [deliriumLocation, setDeliriumLocation] = useState<string>('Unknown Location');
  const [isDeliriumRespawning, setIsDeliriumRespawning] = useState(false);
  const [lucidityStatus, setLucidityStatus] = useState<LucidityStatus | null>(null);
  const [healthStatus, setDpStatus] = useState<HealthStatus | null>(null);
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
  const lastHourRef = useRef<number | null>(null);
  const lastQuarterHourRef = useRef<number | null>(null);
  const lastHolidayIdsRef = useRef<string[]>([]);
  const rescueTimeoutRef = useRef<number | null>(null);
  const lastRoomUpdateTime = useRef<number>(0);
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);

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

  // Create event handler context
  const context: EventHandlerContext = {
    currentPlayerRef,
    currentRoomRef,
    currentMessagesRef,
    healthStatusRef,
    lucidityStatusRef,
    lastDaypartRef,
    lastHourRef,
    lastQuarterHourRef,
    lastHolidayIdsRef,
    lastRoomUpdateTime,
    setDpStatus: setDpStatus,
    setLucidityStatus,
    setMythosTime,
    setIsDead,
    setIsMortallyWounded,
    setIsRespawning,
    setIsDelirious,
    setIsDeliriumRespawning,
    setDeathLocation,
    setDeliriumLocation,
    setRescueState,
    onLogout,
  };

  // Event processing hook
  const { handleGameEvent } = useEventProcessing({
    currentMessagesRef,
    setGameState,
    context,
  });

  // Game connection management
  const { isConnected, isConnecting, error, reconnectAttempts, sendCommand, disconnect } = useGameConnectionManagement({
    authToken,
    playerName,
    characterId,
    onLogout,
    onGameEvent: handleGameEvent,
    setGameState,
  });

  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand]);

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
  });

  // Command handlers
  const { handleCommandSubmit, handleChatMessage, handleClearMessages, handleClearHistory } = useCommandHandlers({
    isConnected,
    sendCommand,
    setGameState,
  });

  const handleLogout = async () => {
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
          mythosTime={mythosTime}
          healthStatus={healthStatus}
          lucidityStatus={lucidityStatus}
          onSendCommand={handleCommandSubmit}
          onSendChatMessage={handleChatMessage}
          onClearMessages={handleClearMessages}
          onClearHistory={handleClearHistory}
          onDownloadLogs={() => {
            logger.downloadLogs();
          }}
        />
      )}

      {/* Login Grace Period Banner */}
      {gameState.loginGracePeriodActive && gameState.loginGracePeriodRemaining !== undefined && (
        <LoginGracePeriodBanner
          remainingSeconds={gameState.loginGracePeriodRemaining}
          className="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 max-w-md"
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
