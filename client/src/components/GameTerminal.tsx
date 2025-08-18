import React, { useState } from 'react';
import { DraggablePanel } from './DraggablePanel';
import { MotdContent } from './MotdContent';
import { ChatPanel } from './panels/ChatPanel';
import { CommandPanel } from './panels/CommandPanel';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';

interface Player {
  name: string;
  stats?: {
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
}

interface Room {
  id: string;
  name: string;
  description: string;
  exits: Record<string, string>;
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
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
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
  onConnect: () => void;
  onDisconnect: () => void;
  onLogout: () => void;
  onDownloadLogs: () => void;
  onSendCommand: (command: string) => void;
  onClearMessages: () => void;
  onClearHistory: () => void;
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
  onDownloadLogs,
  onSendCommand,
  onClearMessages,
  onClearHistory,
}) => {
  const [showMotd, setShowMotd] = useState(true);

  return (
    <div
      className="min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden"
      style={{ minHeight: '100vh', width: '100%' }}
    >
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 h-12 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-10">
        <div className="flex items-center gap-3">
          <EldritchIcon name={MythosIcons.connection} size={20} variant={isConnected ? 'success' : 'error'} />
          <h1 className="text-lg font-bold text-mythos-terminal-primary">MythosMUD Terminal</h1>
        </div>
        <div className="flex items-center gap-4 text-sm">
          <span className="text-mythos-terminal-text-secondary">Player: {playerName}</span>
          <span
            className={`px-2 py-1 rounded text-xs ${isConnected ? 'bg-mythos-terminal-success text-black' : 'bg-mythos-terminal-error text-white'}`}
          >
            {isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected'}
          </span>
          {error && <span className="text-mythos-terminal-error text-xs">{error}</span>}
          {reconnectAttempts > 0 && (
            <span className="text-mythos-terminal-warning text-xs">Reconnect: {reconnectAttempts}</span>
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

      {/* Main Content Area */}
      <div className="pt-12 min-h-screen">
        {/* Chat Panel */}
        <DraggablePanel
          title="Chat"
          defaultPosition={{ x: 50, y: 50 }}
          defaultSize={{ width: 400, height: 300 }}
          minSize={{ width: 200, height: 150 }}
          maxSize={{ width: 800, height: 600 }}
          variant="eldritch"
          onClose={() => console.log('Chat panel closed')}
          onMinimize={() => console.log('Chat panel minimized')}
          onMaximize={() => console.log('Chat panel maximized')}
        >
          <ChatPanel messages={messages} onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
        </DraggablePanel>

        {/* Command Panel */}
        <DraggablePanel
          title="Commands"
          defaultPosition={{ x: 500, y: 50 }}
          defaultSize={{ width: 350, height: 250 }}
          minSize={{ width: 200, height: 150 }}
          maxSize={{ width: 600, height: 500 }}
          variant="elevated"
          onClose={() => console.log('Command panel closed')}
          onMinimize={() => console.log('Command panel minimized')}
          onMaximize={() => console.log('Command panel maximized')}
        >
          <CommandPanel
            commandHistory={commandHistory}
            onSendCommand={onSendCommand}
            onClearHistory={onClearHistory}
            isConnected={isConnected}
          />
        </DraggablePanel>

        {/* Room Info Panel */}
        {room && (
          <DraggablePanel
            title="Room Info"
            defaultPosition={{ x: 50, y: 400 }}
            defaultSize={{ width: 300, height: 200 }}
            minSize={{ width: 200, height: 100 }}
            maxSize={{ width: 500, height: 400 }}
            variant="default"
            onClose={() => console.log('Room panel closed')}
            onMinimize={() => console.log('Room panel minimized')}
            onMaximize={() => console.log('Room panel maximized')}
          >
            <div className="space-y-4">
              <div>
                <h4 className="text-mythos-terminal-primary font-bold mb-2">{room.name}</h4>
                <p className="text-sm text-mythos-terminal-text-secondary">{room.description}</p>
              </div>
              {room.exits && Object.keys(room.exits).length > 0 && (
                <div>
                  <h5 className="text-mythos-terminal-primary text-sm font-bold mb-1">Exits:</h5>
                  <div className="text-xs text-mythos-terminal-text-secondary">
                    {Object.entries(room.exits).map(([direction, destination]) => (
                      <div key={direction}>
                        {direction}: {destination}
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {room.entities && room.entities.length > 0 && (
                <div>
                  <h5 className="text-mythos-terminal-primary text-sm font-bold mb-1">Entities:</h5>
                  <div className="text-xs text-mythos-terminal-text-secondary">
                    {room.entities.map((entity, index) => (
                      <div key={index}>
                        {entity.name} ({entity.type})
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </DraggablePanel>
        )}

        {/* Player Status Panel */}
        <DraggablePanel
          title="Status"
          defaultPosition={{ x: 400, y: 400 }}
          defaultSize={{ width: 300, height: 200 }}
          minSize={{ width: 200, height: 100 }}
          maxSize={{ width: 500, height: 400 }}
          variant="default"
          onClose={() => console.log('Status panel closed')}
          onMinimize={() => console.log('Status panel minimized')}
          onMaximize={() => console.log('Status panel maximized')}
        >
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-sm text-mythos-terminal-text-secondary">Connection:</span>
              <div className="flex items-center space-x-2">
                <EldritchIcon name={MythosIcons.connection} size={20} variant={isConnected ? 'success' : 'error'} />
                <span
                  className={`text-sm ${isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error'}`}
                >
                  {isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected'}
                </span>
              </div>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-mythos-terminal-text-secondary">Player:</span>
              <span className="text-sm text-mythos-terminal-text">{playerName}</span>
            </div>
            {player?.stats && (
              <>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Health:</span>
                  <span className="text-sm text-mythos-terminal-text">{player.stats.current_health}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Sanity:</span>
                  <span className="text-sm text-mythos-terminal-text">{player.stats.sanity}</span>
                </div>
                {/* Core Attributes */}
                <div className="border-t border-mythos-terminal-border pt-2">
                  <h5 className="text-xs text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
                  <div className="grid grid-cols-2 gap-1 text-xs">
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
                  <h5 className="text-xs text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
                  <div className="grid grid-cols-2 gap-1 text-xs">
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
            <div className="flex items-center justify-between">
              <span className="text-sm text-mythos-terminal-text-secondary">Messages:</span>
              <span className="text-sm text-mythos-terminal-text">{messages.length}</span>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm text-mythos-terminal-text-secondary">Commands:</span>
              <span className="text-sm text-mythos-terminal-text">{commandHistory.length}</span>
            </div>
          </div>
        </DraggablePanel>
      </div>
    </div>
  );
};
