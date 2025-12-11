import React, { useCallback, useEffect, useMemo } from 'react';
import type { HealthStatus } from '../../types/health';
import { determineHealthTier } from '../../types/health';
import type { LucidityStatus } from '../../types/lucidity';
import { HeaderBar } from './HeaderBar';
import { PanelContainer } from './PanelSystem/PanelContainer';
import { PanelManagerProvider } from './PanelSystem/PanelManager';
import { usePanelManager } from './PanelSystem/usePanelManager';
import { CharacterInfoPanel } from './panels/CharacterInfoPanel';
import { ChatHistoryPanel } from './panels/ChatHistoryPanel';
import { CommandHistoryPanel } from './panels/CommandHistoryPanel';
import { CommandInputPanel } from './panels/CommandInputPanel';
import { GameInfoPanel } from './panels/GameInfoPanel';
import { LocationPanel } from './panels/LocationPanel';
import { OccupantsPanel } from './panels/OccupantsPanel';
import { RoomDescriptionPanel } from './panels/RoomDescriptionPanel';
import type { ChatMessage, MythosTimeState, Player, Room } from './types';
import { createDefaultPanelLayout } from './utils/panelLayout';

// Helper function to calculate occupant count from room data
// Extracted to reduce cyclomatic complexity
const calculateOccupantCount = (room: Room | null): number => {
  if (!room) {
    return 0;
  }
  if (typeof room.occupant_count === 'number') {
    return room.occupant_count;
  }
  const players = room.players ?? [];
  const npcs = room.npcs ?? [];
  const calculatedCount = players.length + npcs.length;
  if (calculatedCount > 0) {
    return calculatedCount;
  }
  const legacyOccupants = room.occupants ?? [];
  return legacyOccupants.length;
};

interface GameClientV2Props {
  playerName: string;
  authToken: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
  // Game state props (will be passed from parent that manages game state)
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  mythosTime: MythosTimeState | null;
  healthStatus: HealthStatus | null;
  lucidityStatus: LucidityStatus | null;
  // Event handlers
  onSendCommand: (command: string) => void;
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages: () => void;
  onClearHistory: () => void;
  onDownloadLogs: () => void;
}

// Main game client component with three-column layout
// Based on findings from "Unified Interface Architecture" - Dr. Armitage, 1928
const GameClientV2Content: React.FC<GameClientV2Props> = ({
  playerName,
  onLogout,
  isLoggingOut = false,
  player,
  room,
  messages,
  commandHistory,
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  mythosTime,
  healthStatus,
  lucidityStatus,
  onSendCommand,
  onSendChatMessage,
  onClearMessages,
  onClearHistory,
  onDownloadLogs,
}) => {
  const panelManager = usePanelManager();

  // Derive health and lucidity status (similar to GameTerminal)
  const derivedHealthStatus = useMemo<HealthStatus | null>(() => {
    if (healthStatus) {
      return healthStatus;
    }
    if (player?.stats?.current_dp !== undefined) {
      const maxHealth = player.stats.max_health ?? 100;
      return {
        current: player.stats.current_dp,
        max: maxHealth,
        tier: determineHealthTier(player.stats.current_dp, maxHealth),
        posture: player.stats.position,
        inCombat: player.in_combat ?? false,
      };
    }
    return null;
  }, [healthStatus, player]);

  const derivedLucidityStatus = useMemo<LucidityStatus | null>(() => {
    if (lucidityStatus) {
      return lucidityStatus;
    }
    if (player?.stats?.lucidity !== undefined) {
      return {
        current: player.stats.lucidity,
        max: player.stats.max_lucidity ?? 100,
        tier: 'lucid',
        liabilities: [],
      };
    }
    return null;
  }, [lucidityStatus, player]);

  // Handle window resize - scale panels proportionally based on viewport
  // Maintains three-column layout structure from wireframe
  // As noted in "Proportional Scaling in Non-Euclidean Interfaces" - Dr. Armitage, 1928
  useEffect(() => {
    const handleResize = () => {
      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;

      // Scale panels to new viewport size using default layout function
      panelManager.scalePanelsToViewport(viewportWidth, viewportHeight, createDefaultPanelLayout);
    };

    // Use debounce to avoid excessive updates during resize
    let resizeTimeout: number;
    const debouncedHandleResize = () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(handleResize, 150);
    };

    window.addEventListener('resize', debouncedHandleResize);
    return () => {
      window.removeEventListener('resize', debouncedHandleResize);
      clearTimeout(resizeTimeout);
    };
  }, [panelManager]);

  // Handle command selection from history
  const handleSelectCommand = useCallback((_command: string) => {
    // Command selection handler - currently unused but kept for future use
  }, []);

  // Calculate occupants panel title with count
  // Derived from occupant count calculation logic described in room occupancy studies
  const occupantsTitle = useMemo(() => {
    const totalCount = calculateOccupantCount(room);
    if (totalCount > 0) {
      return `Occupants (${totalCount})`;
    }
    return 'Occupants';
  }, [room]);

  // Get panel state for each panel
  const chatHistoryPanel = panelManager.getPanel('chatHistory');
  const locationPanel = panelManager.getPanel('location');
  const roomDescriptionPanel = panelManager.getPanel('roomDescription');
  const occupantsPanel = panelManager.getPanel('occupants');
  const gameInfoPanel = panelManager.getPanel('gameInfo');
  const characterInfoPanel = panelManager.getPanel('characterInfo');
  const commandHistoryPanel = panelManager.getPanel('commandHistory');
  const commandInputPanel = panelManager.getPanel('commandInput');

  // Render panels only if they exist in the panel manager
  return (
    <div className="min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden">
      <HeaderBar
        playerName={playerName}
        isConnected={isConnected}
        isConnecting={isConnecting}
        error={error}
        reconnectAttempts={reconnectAttempts}
        mythosTime={mythosTime}
        onLogout={onLogout || (() => {})}
        isLoggingOut={isLoggingOut}
      />

      {/* Main Content Area - Panels */}
      <div className="pt-12">
        {chatHistoryPanel && chatHistoryPanel.isVisible && (
          <PanelContainer
            id={chatHistoryPanel.id}
            title={chatHistoryPanel.title}
            position={chatHistoryPanel.position}
            size={chatHistoryPanel.size}
            zIndex={chatHistoryPanel.zIndex}
            isMinimized={chatHistoryPanel.isMinimized}
            isMaximized={chatHistoryPanel.isMaximized}
            isVisible={chatHistoryPanel.isVisible}
            minSize={chatHistoryPanel.minSize}
            variant="eldritch"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <ChatHistoryPanel
              messages={messages}
              onSendChatMessage={onSendChatMessage}
              onClearMessages={onClearMessages}
              onDownloadLogs={onDownloadLogs}
              isConnected={isConnected}
            />
          </PanelContainer>
        )}

        {locationPanel && locationPanel.isVisible && (
          <PanelContainer
            id={locationPanel.id}
            title={locationPanel.title}
            position={locationPanel.position}
            size={locationPanel.size}
            zIndex={locationPanel.zIndex}
            isMinimized={locationPanel.isMinimized}
            isMaximized={locationPanel.isMaximized}
            isVisible={locationPanel.isVisible}
            minSize={locationPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <LocationPanel room={room} />
          </PanelContainer>
        )}

        {roomDescriptionPanel && roomDescriptionPanel.isVisible && (
          <PanelContainer
            id={roomDescriptionPanel.id}
            title={roomDescriptionPanel.title}
            position={roomDescriptionPanel.position}
            size={roomDescriptionPanel.size}
            zIndex={roomDescriptionPanel.zIndex}
            isMinimized={roomDescriptionPanel.isMinimized}
            isMaximized={roomDescriptionPanel.isMaximized}
            isVisible={roomDescriptionPanel.isVisible}
            minSize={roomDescriptionPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <RoomDescriptionPanel room={room} />
          </PanelContainer>
        )}

        {occupantsPanel && occupantsPanel.isVisible && (
          <PanelContainer
            id={occupantsPanel.id}
            title={occupantsTitle}
            position={occupantsPanel.position}
            size={occupantsPanel.size}
            zIndex={occupantsPanel.zIndex}
            isMinimized={occupantsPanel.isMinimized}
            isMaximized={occupantsPanel.isMaximized}
            isVisible={occupantsPanel.isVisible}
            minSize={occupantsPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <OccupantsPanel room={room} />
          </PanelContainer>
        )}

        {gameInfoPanel && gameInfoPanel.isVisible && (
          <PanelContainer
            id={gameInfoPanel.id}
            title={gameInfoPanel.title}
            position={gameInfoPanel.position}
            size={gameInfoPanel.size}
            zIndex={gameInfoPanel.zIndex}
            isMinimized={gameInfoPanel.isMinimized}
            isMaximized={gameInfoPanel.isMaximized}
            isVisible={gameInfoPanel.isVisible}
            minSize={gameInfoPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <GameInfoPanel messages={messages} onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
          </PanelContainer>
        )}

        {characterInfoPanel && characterInfoPanel.isVisible && (
          <PanelContainer
            id={characterInfoPanel.id}
            title={characterInfoPanel.title}
            position={characterInfoPanel.position}
            size={characterInfoPanel.size}
            zIndex={characterInfoPanel.zIndex}
            isMinimized={characterInfoPanel.isMinimized}
            isMaximized={characterInfoPanel.isMaximized}
            isVisible={characterInfoPanel.isVisible}
            minSize={characterInfoPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <CharacterInfoPanel
              player={player}
              healthStatus={derivedHealthStatus}
              lucidityStatus={derivedLucidityStatus}
            />
          </PanelContainer>
        )}

        {commandHistoryPanel && commandHistoryPanel.isVisible && (
          <PanelContainer
            id={commandHistoryPanel.id}
            title={commandHistoryPanel.title}
            position={commandHistoryPanel.position}
            size={commandHistoryPanel.size}
            zIndex={commandHistoryPanel.zIndex}
            isMinimized={commandHistoryPanel.isMinimized}
            isMaximized={commandHistoryPanel.isMaximized}
            isVisible={commandHistoryPanel.isVisible}
            minSize={commandHistoryPanel.minSize}
            variant="elevated"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <CommandHistoryPanel
              commandHistory={commandHistory}
              onClearHistory={onClearHistory}
              onSelectCommand={handleSelectCommand}
            />
          </PanelContainer>
        )}

        {commandInputPanel && commandInputPanel.isVisible && (
          <PanelContainer
            id={commandInputPanel.id}
            title={commandInputPanel.title}
            position={commandInputPanel.position}
            size={commandInputPanel.size}
            zIndex={commandInputPanel.zIndex}
            isMinimized={commandInputPanel.isMinimized}
            isMaximized={commandInputPanel.isMaximized}
            isVisible={commandInputPanel.isVisible}
            minSize={commandInputPanel.minSize}
            variant="elevated"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <CommandInputPanel onSendCommand={onSendCommand} disabled={!isConnected} isConnected={isConnected} />
          </PanelContainer>
        )}
      </div>
    </div>
  );
};

// Main component with PanelManagerProvider
export const GameClientV2: React.FC<GameClientV2Props> = props => {
  // Create default panel layout based on viewport
  const defaultPanels = useMemo(() => {
    const viewportWidth = typeof window !== 'undefined' ? window.innerWidth : 1920;
    const viewportHeight = typeof window !== 'undefined' ? window.innerHeight : 1080;
    return createDefaultPanelLayout(viewportWidth, viewportHeight);
  }, []);

  return (
    <PanelManagerProvider defaultPanels={defaultPanels}>
      <GameClientV2Content {...props} />
    </PanelManagerProvider>
  );
};
