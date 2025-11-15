import React, { useEffect, useMemo, useRef, useState } from 'react';

import { DEFAULT_CHANNEL } from '../config/channels';
import { debugLogger } from '../utils/debugLogger';
import { DraggablePanel } from './DraggablePanel';
import { RoomInfoPanel } from './RoomInfoPanel';
import { ChatPanel } from './panels/ChatPanel';
import { CommandPanel } from './panels/CommandPanel';
import { GameLogPanel } from './panels/GameLogPanel';
import { SanityMeter, HallucinationTicker, RescueStatusBanner } from './sanity';
import { HealthMeter } from './health';
import type { SanityStatus, HallucinationMessage, RescueState } from '../types/sanity';
import type { HealthStatus } from '../types/health';
import { determineHealthTier } from '../types/health';

const formatPosture = (value?: string): string => {
  if (!value) {
    return '';
  }
  const spaced = value.replace(/_/g, ' ');
  return spaced.charAt(0).toUpperCase() + spaced.slice(1);
};

interface Player {
  name: string;
  profession_id?: number;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats?: {
    current_health: number;
    max_health?: number;
    sanity: number;
    max_sanity?: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    intelligence?: number;
    wisdom?: number;
    charisma?: number;
    occult_knowledge?: number;
    fear?: number;
    corruption?: number;
    cult_affiliation?: number;
    position?: string;
  };
  level?: number;
  xp?: number;
  in_combat?: boolean;
}

const buildHealthStatus = (
  player: Player | null,
  lastChange: HealthStatus['lastChange'] | undefined
): HealthStatus | null => {
  const stats = player?.stats;
  if (!stats || stats.current_health === undefined) {
    return null;
  }

  const maxHealth = stats.max_health ?? 100;
  return {
    current: stats.current_health,
    max: maxHealth,
    tier: determineHealthTier(stats.current_health, maxHealth),
    lastChange,
    posture: stats.position,
    inCombat: player?.in_combat ?? false,
  };
};

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits: Record<string, string>;
  occupants?: string[];
  occupant_count?: number;
  entities?: Array<{
    name: string;
    type: string;
  }>;
}

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  rawText?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
  tags?: string[];
}

interface GameTerminalProps {
  playerName: string;
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  room: Room | null;
  player: Player | null;
  messages: ChatMessage[];
  commandHistory: string[];
  sanityStatus: SanityStatus | null;
  healthStatus?: HealthStatus | null;
  hallucinations: HallucinationMessage[];
  rescueState: RescueState | null;
  onDismissHallucination?: (id: string) => void;
  onDismissRescue?: () => void;
  onConnect: () => void;
  onDisconnect: () => void;
  onLogout: () => void;
  isLoggingOut?: boolean;
  onDownloadLogs: () => void;
  onSendCommand: (command: string) => void;
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages: () => void;
  onClearHistory: () => void;
  isMortallyWounded?: boolean;
  isDead?: boolean;
}

export const GameTerminal: React.FC<GameTerminalProps> = ({
  playerName,
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  room,
  player,
  messages,
  commandHistory,
  sanityStatus,
  healthStatus,
  hallucinations,
  rescueState,
  onDismissHallucination,
  onDismissRescue,
  onConnect: _onConnect,
  onDisconnect: _onDisconnect,
  onLogout,
  isLoggingOut = false,
  onDownloadLogs,
  isMortallyWounded = false,
  isDead = false,
  onSendCommand,
  onSendChatMessage,
  onClearMessages,
  onClearHistory,
}) => {
  // MOTD is now handled by the interstitial screen in App.tsx
  const debug = debugLogger('GameTerminal');
  const [selectedChatChannel, setSelectedChatChannel] = useState(DEFAULT_CHANNEL);
  const [healthChange, setHealthChange] = useState<HealthStatus['lastChange']>();
  const previousHealthRef = useRef<number | null>(null);

  const derivedSanityStatus = useMemo<SanityStatus | null>(() => {
    if (sanityStatus) {
      return sanityStatus;
    }

    if (player?.stats?.sanity !== undefined) {
      return {
        current: player.stats.sanity,
        max: 100,
        tier: 'lucid',
        liabilities: [],
      };
    }

    return null;
  }, [player, sanityStatus]);

  const derivedHealthStatus = useMemo<HealthStatus | null>(() => {
    if (healthStatus) {
      return healthStatus;
    }
    return buildHealthStatus(player, healthChange);
  }, [healthStatus, player, healthChange]);

  useEffect(() => {
    if (!healthStatus) {
      return;
    }
    previousHealthRef.current = healthStatus.current;
  }, [healthStatus]);

  /* eslint-disable react-hooks/set-state-in-effect -- health change derives from server snapshots */
  useEffect(() => {
    if (healthStatus) {
      return;
    }

    const currentHealth = player?.stats?.current_health;
    if (typeof currentHealth !== 'number') {
      previousHealthRef.current = null;
      setHealthChange(undefined);
      return;
    }

    if (previousHealthRef.current !== null && previousHealthRef.current !== currentHealth) {
      const delta = currentHealth - previousHealthRef.current;
      const reason = player?.in_combat ? 'combat' : undefined;
      setHealthChange({
        delta,
        reason,
        timestamp: new Date().toISOString(),
      });
    }

    previousHealthRef.current = currentHealth;
  }, [player, healthStatus]);
  /* eslint-enable react-hooks/set-state-in-effect */

  const recentHallucinations = useMemo(() => hallucinations.slice(0, 3), [hallucinations]);

  // Responsive panel sizing based on viewport
  useEffect(() => {
    const calculatePanelSizes = () => {
      // Panel sizing is now handled by CSS Grid layout
      // This effect is kept for potential future use
    };

    // Calculate initial sizes
    calculatePanelSizes();

    // Handle window resize
    const handleResize = () => {
      calculatePanelSizes();
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []); // No dependencies to prevent infinite recursion

  return (
    <div
      data-testid="game-terminal"
      className="min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden"
      style={{ minHeight: '100vh', width: '100%' }}
    >
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 h-12 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-10">
        {/* Connection Status */}
        <div className="connection-status">
          {/* Temporarily disabled EldritchIcon to test WebSocket connection */}
          {/* <EldritchIcon name={MythosIcons.connection} size={20} variant={isConnected ? 'success' : 'error'} /> */}
          <span className={`status-text ${isConnected ? 'connected' : 'disconnected'}`}>
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
        <div className="flex items-center gap-4 text-base">
          <span className="text-mythos-terminal-text-secondary">Player: {playerName}</span>
          <span
            className={`px-2 py-1 rounded text-sm ${isConnected ? 'bg-mythos-terminal-success text-black' : 'bg-mythos-terminal-error text-white'}`}
          >
            {isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected'}
          </span>
          {error && <span className="text-mythos-terminal-error text-sm">{error}</span>}
          {reconnectAttempts > 0 && (
            <span className="text-mythos-terminal-warning text-sm">Reconnect: {reconnectAttempts}</span>
          )}
        </div>
      </div>

      {/* MOTD is now handled by the interstitial screen in App.tsx */}

      {rescueState && rescueState.status !== 'idle' && (
        <div className="absolute left-0 right-0 top-12 z-20 px-4">
          <RescueStatusBanner state={rescueState} onDismiss={onDismissRescue} />
        </div>
      )}

      {/* Main Content Area with Responsive Panel Layout */}
      <div className="game-terminal-container">
        <div className="game-terminal-panels">
          {/* Chat Panel */}
          <DraggablePanel
            title="Chat"
            className="panel-chat"
            variant="eldritch"
            defaultSize={{ width: 500, height: 400 }}
            defaultPosition={{ x: 50, y: 50 }}
            onClose={() => console.log('Chat panel closed')}
            onMinimize={() => console.log('Chat panel minimized')}
            onMaximize={() => console.log('Chat panel maximized')}
          >
            <ChatPanel
              messages={messages}
              onSendChatMessage={onSendChatMessage}
              onClearMessages={onClearMessages}
              onDownloadLogs={onDownloadLogs}
              isConnected={isConnected}
              selectedChannel={selectedChatChannel}
              onChannelSelect={setSelectedChatChannel}
            />
          </DraggablePanel>

          {/* Game Log Panel */}
          <DraggablePanel
            title="Game Log"
            className="panel-gameLog"
            variant="default"
            defaultSize={{ width: 500, height: 400 }}
            defaultPosition={{ x: 600, y: 50 }}
            autoSize={true}
            onClose={() => console.log('Game Log panel closed')}
            onMinimize={() => console.log('Game Log panel minimized')}
            onMaximize={() => console.log('Game Log panel maximized')}
          >
            <GameLogPanel messages={messages} onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
          </DraggablePanel>

          {/* Command Panel */}
          <DraggablePanel
            title="Commands"
            className="panel-command"
            variant="elevated"
            defaultSize={{ width: 500, height: 200 }}
            defaultPosition={{ x: 50, y: 500 }}
            onClose={() => console.log('Command panel closed')}
            onMinimize={() => console.log('Command panel minimized')}
            onMaximize={() => console.log('Command panel maximized')}
          >
            {/* Debug logging for isConnected prop passing */}
            {(() => {
              debug.debug('Passing isConnected to CommandPanel', {
                isConnected,
                isConnecting,
                error,
                reconnectAttempts,
              });
              return null;
            })()}
            <CommandPanel
              commandHistory={commandHistory}
              onSendCommand={onSendCommand}
              onClearHistory={onClearHistory}
              onLogout={onLogout}
              selectedChannel={selectedChatChannel}
              onChannelSelect={setSelectedChatChannel}
              isConnected={isConnected}
              isLoggingOut={isLoggingOut}
              disabled={isMortallyWounded || isDead}
            />
          </DraggablePanel>

          {/* Room Info Panel */}
          <DraggablePanel
            title="Room Info"
            className="panel-roomInfo"
            variant="default"
            defaultSize={{ width: 300, height: 300 }}
            defaultPosition={{ x: 600, y: 500 }}
            onClose={() => console.log('Room panel closed')}
            onMinimize={() => console.log('Room panel minimized')}
            onMaximize={() => console.log('Room panel maximized')}
          >
            <RoomInfoPanel
              room={room}
              debugInfo={{
                hasRoom: !!room,
                roomType: typeof room,
                roomKeys: room ? Object.keys(room) : [],
                timestamp: new Date().toISOString(),
              }}
            />
          </DraggablePanel>

          {/* Player Status Panel */}
          <DraggablePanel
            title="Status"
            className="panel-status"
            variant="default"
            defaultSize={{ width: 300, height: 150 }}
            defaultPosition={{ x: 950, y: 250 }}
            onClose={() => console.log('Status panel closed')}
            onMinimize={() => console.log('Status panel minimized')}
            onMaximize={() => console.log('Status panel maximized')}
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-base text-mythos-terminal-text-secondary">Connection:</span>
                <div className="flex items-center space-x-2">
                  {/* Temporarily disabled EldritchIcon to test WebSocket connection */}
                  {/* <EldritchIcon
                    name={MythosIcons.connection}
                    size={20}
                    variant={isConnected ? 'success' : 'error'}
                  /> */}
                  <span
                    className={`text-base ${isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error'}`}
                  >
                    {isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected'}
                  </span>
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-base text-mythos-terminal-text-secondary">Player:</span>
                <span className="text-base text-mythos-terminal-text">{playerName}</span>
              </div>
              {player?.stats?.position && (
                <div className="flex items-center justify-between">
                  <span className="text-base text-mythos-terminal-text-secondary">Position:</span>
                  <span className="text-base text-mythos-terminal-text">{formatPosture(player.stats.position)}</span>
                </div>
              )}
              {player?.profession_name && (
                <div className="border-t border-mythos-terminal-border pt-2">
                  <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Profession:</h5>
                  <div className="space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-mythos-terminal-text-secondary">Name:</span>
                      <span className="text-sm text-mythos-terminal-text font-medium">{player.profession_name}</span>
                    </div>
                    {player.profession_description && (
                      <div className="text-xs text-mythos-terminal-text-secondary italic">
                        {player.profession_description}
                      </div>
                    )}
                    {player.profession_flavor_text && (
                      <div className="text-xs text-mythos-terminal-text-secondary">
                        "{player.profession_flavor_text}"
                      </div>
                    )}
                  </div>
                </div>
              )}
              {player?.stats && (
                <>
                  <HealthMeter status={derivedHealthStatus} />
                  <SanityMeter status={derivedSanityStatus} className="mt-2" />
                  <div className="flex items-center justify-between">
                    <span className="text-base text-mythos-terminal-text-secondary">XP:</span>
                    <span className="text-base text-mythos-terminal-text">{player.xp || 0}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-base text-mythos-terminal-text-secondary">In Combat:</span>
                    <span className="text-base text-mythos-terminal-text">{player.in_combat ? 'Yes' : 'No'}</span>
                  </div>
                  {/* Core Attributes */}
                  <div className="border-t border-mythos-terminal-border pt-2">
                    <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
                    <div className="grid grid-cols-2 gap-1 text-sm">
                      {player.stats.strength !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">STR:</span>
                          <span className="text-mythos-terminal-text">{player.stats.strength}</span>
                        </div>
                      )}
                      {player.stats.dexterity !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">DEX:</span>
                          <span className="text-mythos-terminal-text">{player.stats.dexterity}</span>
                        </div>
                      )}
                      {player.stats.constitution !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">CON:</span>
                          <span className="text-mythos-terminal-text">{player.stats.constitution}</span>
                        </div>
                      )}
                      {player.stats.intelligence !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">INT:</span>
                          <span className="text-mythos-terminal-text">{player.stats.intelligence}</span>
                        </div>
                      )}
                      {player.stats.wisdom !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">WIS:</span>
                          <span className="text-mythos-terminal-text">{player.stats.wisdom}</span>
                        </div>
                      )}
                      {player.stats.charisma !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">CHA:</span>
                          <span className="text-mythos-terminal-text">{player.stats.charisma}</span>
                        </div>
                      )}
                    </div>
                  </div>
                  {/* Horror Stats */}
                  <div className="border-t border-mythos-terminal-border pt-2">
                    <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
                    <div className="grid grid-cols-2 gap-1 text-sm">
                      {player.stats.occult_knowledge !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">Occult:</span>
                          <span className="text-mythos-terminal-text">{player.stats.occult_knowledge}</span>
                        </div>
                      )}
                      {player.stats.fear !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">Fear:</span>
                          <span className="text-mythos-terminal-text">{player.stats.fear}</span>
                        </div>
                      )}
                      {player.stats.corruption !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">Corruption:</span>
                          <span className="text-mythos-terminal-text">{player.stats.corruption}</span>
                        </div>
                      )}
                      {player.stats.cult_affiliation !== undefined && (
                        <div className="flex justify-between">
                          <span className="text-mythos-terminal-text-secondary">Cult:</span>
                          <span className="text-mythos-terminal-text">{player.stats.cult_affiliation}</span>
                        </div>
                      )}
                    </div>
                  </div>
                </>
              )}
              <HallucinationTicker
                hallucinations={recentHallucinations}
                onDismiss={onDismissHallucination}
                className="border-t border-mythos-terminal-border/60 pt-3"
              />
            </div>
          </DraggablePanel>
        </div>
      </div>
    </div>
  );
};
