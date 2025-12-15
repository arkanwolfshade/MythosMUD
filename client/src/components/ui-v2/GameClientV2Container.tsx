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
import { GameClientV2 } from './GameClientV2';
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
import { sanitizeChatMessageForState } from './utils/messageUtils';
import type { GameState } from './utils/stateUpdateUtils';

interface GameClientV2ContainerProps {
  playerName: string;
  authToken: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

// Container component that manages game state and renders GameClientV2
// Based on findings from "State Management Patterns" - Dr. Armitage, 1928
export const GameClientV2Container: React.FC<GameClientV2ContainerProps> = ({
  playerName,
  authToken,
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
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _openContainer = useContainerStore(state => state.openContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _closeContainer = useContainerStore(state => state.closeContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _updateContainer = useContainerStore(state => state.updateContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _handleContainerDecayed = useContainerStore(state => state.handleContainerDecayed);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _getContainer = useContainerStore(state => state.getContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _isContainerOpen = useContainerStore(state => state.isContainerOpen);

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

  const handleLogout = () => {
    const logoutMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'You have been logged out of the MythosMUD server.',
      timestamp: new Date().toISOString(),
      messageType: 'system',
      isHtml: false,
    });

    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, logoutMessage],
    }));

    setTimeout(() => {
      if (onLogout) {
        onLogout();
      } else {
        disconnect();
      }
    }, 500);
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
        onClose={() => setIsMainMenuOpen(false)}
        onMapClick={() => {
          // Add map as a tab in the tabbed interface
          if (gameState.room) {
            addTab({
              id: `map-${gameState.room.id}`,
              label: 'Map',
              content: (
                <MapView
                  isOpen={true}
                  onClose={() => closeTab(`map-${gameState.room?.id}`)}
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
    </div>
  );
};
