import React, { useCallback, useEffect, useMemo } from 'react';

import type { HealthStatus } from '../../types/health';
import { deriveHealthStatusFromPlayer } from '../../types/health';
import { deriveLucidityStatusFromPlayer, type LucidityStatus } from '../../types/lucidity';
import { GameClientV2AuxiliaryPanels } from './GameClientV2AuxiliaryPanels';
import { HeaderBar } from './HeaderBar';
import { ChatHistoryPanel } from './panels/ChatHistoryPanel';
import { GameInfoPanel } from './panels/GameInfoPanel';
import { LocationPanel } from './panels/LocationPanel';
import { OccupantsPanel } from './panels/OccupantsPanel';
import { QuestLogPanel } from './panels/QuestLogPanel';
import { RoomDescriptionPanel } from './panels/RoomDescriptionPanel';
import { PanelContainer } from './PanelSystem/PanelContainer';
import { PanelManagerProvider } from './PanelSystem/PanelManager';
import { usePanelManager } from './PanelSystem/usePanelManager';
import type { ChatMessage, MythosTimeState, Player, QuestLogEntry, Room } from './types';
import { getGameInfoPanelCombatClassName } from './utils/characterInfoPanelOutline';
import { createDefaultPanelLayout } from './utils/panelLayout';
import type { ActiveEffectDisplay } from './utils/stateUpdateUtils';

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
  return players.length + npcs.length;
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
  activeEffects?: ActiveEffectDisplay[];
  followingTarget?: { target_name: string; target_type: 'player' | 'npc' } | null;
  /** Quest log (from game_state.quest_log). */
  questLog?: QuestLogEntry[];
  /** Called when user clicks minimap to open full map. */
  onMapClick?: () => void;
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
  activeEffects = [],
  followingTarget = null,
  questLog = [],
  onMapClick,
  authToken,
}) => {
  const panelManager = usePanelManager();

  // Prefer container-derived status; fall back to projector-authoritative player stats only.
  const derivedHealthStatus = useMemo<HealthStatus | null>(
    () => healthStatus ?? deriveHealthStatusFromPlayer(player, undefined),
    [healthStatus, player]
  );

  const derivedLucidityStatus = useMemo<LucidityStatus | null>(
    () => lucidityStatus ?? deriveLucidityStatusFromPlayer(player, undefined),
    [lucidityStatus, player]
  );

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
    let resizeTimeout: ReturnType<typeof setTimeout>;
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
  const questLogPanel = panelManager.getPanel('questLog');
  const minimapPanel = panelManager.getPanel('minimap');

  // Render panels only if they exist in the panel manager
  return (
    <div className="h-screen min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden flex flex-col">
      <HeaderBar
        playerName={playerName}
        isConnected={isConnected}
        isConnecting={isConnecting}
        error={error}
        reconnectAttempts={reconnectAttempts}
        mythosTime={mythosTime}
        onLogout={onLogout || (() => {})}
        isLoggingOut={isLoggingOut}
        activeEffects={activeEffects}
        followingTarget={followingTarget}
      />

      {/* Main Content Area - Panels: flex-1 min-h-0 so panel area is bounded and scroll/overflow work */}
      <div className="flex-1 min-h-0 pt-12 relative">
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
            className={getGameInfoPanelCombatClassName(Boolean(player?.in_combat))}
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <GameInfoPanel
              messages={messages}
              onClearMessages={onClearMessages}
              onDownloadLogs={onDownloadLogs}
              inCombat={Boolean(player?.in_combat)}
            />
          </PanelContainer>
        )}

        {questLogPanel && questLogPanel.isVisible && (
          <PanelContainer
            id={questLogPanel.id}
            title={questLogPanel.title}
            position={questLogPanel.position}
            size={questLogPanel.size}
            zIndex={questLogPanel.zIndex}
            isMinimized={questLogPanel.isMinimized}
            isMaximized={questLogPanel.isMaximized}
            isVisible={questLogPanel.isVisible}
            minSize={questLogPanel.minSize}
            variant="default"
            onPositionChange={panelManager.updatePosition}
            onSizeChange={panelManager.updateSize}
            onMinimize={panelManager.toggleMinimize}
            onMaximize={panelManager.toggleMaximize}
            onFocus={panelManager.focusPanel}
          >
            <QuestLogPanel questLog={questLog} />
          </PanelContainer>
        )}

        <GameClientV2AuxiliaryPanels
          panelManager={panelManager}
          characterInfoPanel={characterInfoPanel}
          minimapPanel={minimapPanel}
          commandHistoryPanel={commandHistoryPanel}
          commandInputPanel={commandInputPanel}
          player={player}
          derivedHealthStatus={derivedHealthStatus}
          derivedLucidityStatus={derivedLucidityStatus}
          room={room}
          authToken={authToken}
          onMapClick={onMapClick}
          commandHistory={commandHistory}
          onClearHistory={onClearHistory}
          onSelectCommand={handleSelectCommand}
          onSendCommand={onSendCommand}
          isConnected={isConnected}
        />
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
