import React, { useEffect, useState } from 'react';
import { debugLogger } from '../utils/debugLogger';
import { DraggablePanel } from './DraggablePanel';
import { MotdContent } from './MotdContent';
import { RoomInfoPanel } from './RoomInfoPanel';
import { ChatPanel } from './panels/ChatPanel';
import { CommandPanel } from './panels/CommandPanel';
import { GameLogPanel } from './panels/GameLogPanel';

export interface GameTerminalPresentationProps {
  // Connection state
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;

  // Session state
  playerName: string;
  characterName: string;
  isAuthenticated: boolean;
  hasCharacter: boolean;

  // Game state
  player: {
    id: string;
    name: string;
    stats: {
      current_health: number;
      sanity: number;
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
    };
    level?: number;
  } | null;
  room: {
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
  } | null;
  messages: Array<{
    text: string;
    timestamp: string;
    isHtml: boolean;
    isCompleteHtml?: boolean;
    messageType?: string;
    aliasChain?: Array<{
      original: string;
      expanded: string;
      alias_name: string;
    }>;
  }>;
  commandHistory: string[];

  // Event handlers
  onSendCommand: (command: string) => void;
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages: () => void;
  onClearHistory: () => void;
  onDownloadLogs: () => void;
}

/**
 * Presentational component for GameTerminal.
 * This component is responsible only for rendering the UI and handling
 * user interactions, while all business logic is handled by the container.
 *
 * This component is pure and stateless regarding business logic,
 * making it easy to test and reason about.
 */
export const GameTerminalPresentation: React.FC<GameTerminalPresentationProps> = ({
  playerName,
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  room,
  player,
  messages,
  commandHistory,
  onDownloadLogs,
  onSendCommand,
  onSendChatMessage,
  onClearMessages,
  onClearHistory,
}) => {
  const [showMotd, setShowMotd] = useState(true);
  const debug = debugLogger('GameTerminalPresentation');

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
      className="min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden"
      style={{ minHeight: '100vh', width: '100%' }}
    >
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 h-12 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-10">
        {/* Connection Status */}
        <div className="connection-status">
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

      {/* MOTD Overlay (preserved styles) */}
      {showMotd && (
        <div
          className="motd-display"
          style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', zIndex: 100000 }}
        >
          <div className="motd-content">
            <MotdContent />
          </div>
          <div className="motd-actions">
            <button className="continue-button" onClick={() => setShowMotd(false)}>
              Continue
            </button>
          </div>
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
              isConnected={isConnected}
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
            defaultSize={{ width: 300, height: 200 }}
            defaultPosition={{ x: 950, y: 50 }}
            onClose={() => console.log('Status panel closed')}
            onMinimize={() => console.log('Status panel minimized')}
            onMaximize={() => console.log('Status panel maximized')}
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-base text-mythos-terminal-text-secondary">Connection:</span>
                <div className="flex items-center space-x-2">
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
              {player?.stats && (
                <>
                  <div className="flex items-center justify-between">
                    <span className="text-base text-mythos-terminal-text-secondary">Health:</span>
                    <span className="text-base text-mythos-terminal-text">{player.stats.current_health}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-base text-mythos-terminal-text-secondary">Sanity:</span>
                    <span className="text-base text-mythos-terminal-text">{player.stats.sanity}</span>
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
            </div>
          </DraggablePanel>
        </div>
      </div>
    </div>
  );
};
