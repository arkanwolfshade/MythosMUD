import React, { useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnection';
import { ansiToHtmlWithBreaks } from '../utils/ansiToHtml';
import { logger } from '../utils/logger';
import './GameTerminal.css';
import { RoomInfoPanel } from './RoomInfoPanel';

interface GameTerminalProps {
  playerId: string;
  playerName: string;
  authToken: string;
}

interface Player {
  name: string;
  stats?: {
    current_health: number;
    sanity: number;
  };
  level?: number;
}

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits?: Record<string, string | null>;
}

interface Entity {
  name: string;
}

interface GameEvent {
  event_type: string;
  data: Record<string, unknown>;
  alias_chain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface GameState {
  player: Player | null;
  room: Room | null;
  entities: Entity[];
  messages: Array<{
    text: string;
    timestamp: string;
    isHtml: boolean;
    isCompleteHtml?: boolean;
    aliasChain?: Array<{
      original: string;
      expanded: string;
      alias_name: string;
    }>;
  }>;
}

export function GameTerminal({ playerId, playerName, authToken }: GameTerminalProps) {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    entities: [],
    messages: [],
  });

  const [commandInput, setCommandInput] = useState('');
  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState(-1);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    playerId,
    playerName,
    authToken,
    onEvent: handleGameEvent,
    onConnect: () => addMessage('Connected to MythosMUD...'),
    onDisconnect: () => addMessage('Disconnected from MythosMUD'),
    onError: error => addMessage(`Error: ${error}`),
  });

  function handleGameEvent(event: GameEvent) {
    console.log('Game event received:', event);

    switch (event.event_type) {
      case 'game_state':
        setGameState(prev => ({
          ...prev,
          player: event.data.player as Player,
          room: event.data.room as Room,
        }));
        addMessage(`Welcome to ${(event.data.room as Room)?.name || 'Unknown Room'}`);
        break;

      case 'motd':
        // Display the Message of the Day
        console.log('MOTD received:', event.data.message);
        console.log('MOTD contains ANSI:', (event.data.message as string).includes('\x1b['));
        console.log('MOTD length:', (event.data.message as string).length);
        addMessage(event.data.message as string);
        break;

      case 'room_update':
        console.log('Room update received:', event.data);
        setGameState(prev => ({
          ...prev,
          room: event.data.room as Room,
          entities: (event.data.entities as Entity[]) || [],
        }));
        addMessage(`Room updated: ${(event.data.room as Room)?.name}`);
        break;

      case 'player_entered':
        addMessage(`${event.data.player_name as string} enters the room.`);
        break;

      case 'player_left':
        addMessage(`${event.data.player_name as string} leaves the room.`);
        break;

      case 'combat_event':
        addMessage(`[COMBAT] ${event.data.message as string}`);
        break;

      case 'chat_message':
        addMessage(
          `[${event.data.channel as string}] ${event.data.player_name as string}: ${event.data.message as string}`
        );
        break;

      case 'game_tick':
        // Show tick updates every 10th tick for debugging
        if ((event.data.tick_number as number) % 10 === 0) {
          addMessage(`[TICK] Game tick ${event.data.tick_number as number}`);
        }
        break;

      case 'command_response': {
        // Handle command response with potential alias chain information
        const result = event.data.result as string;
        const aliasChain = event.alias_chain;
        addMessage(result, aliasChain);
        break;
      }

      case 'heartbeat':
        // Silent heartbeat - just keep connection alive
        break;

      default:
        // Log unknown event types for debugging but don't display to user
        console.log('Unknown event type:', event.event_type, event.data);
        break;
    }
  }

  function addMessage(message: string, aliasChain?: Array<{ original: string; expanded: string; alias_name: string }>) {
    // Check if message contains ANSI escape sequences
    const hasAnsi = message.includes('\x1b[');
    console.log('addMessage called with:', message.substring(0, 100) + '...');
    console.log('hasAnsi:', hasAnsi);

    // Count ANSI sequences manually
    let ansiCount = 0;
    for (let i = 0; i < message.length - 1; i++) {
      if (message[i] === '\x1b' && message[i + 1] === '[') {
        ansiCount++;
      }
    }
    console.log('ANSI sequences count:', ansiCount);

    // Check if message contains HTML tags
    const hasHtml = /<[^>]*>/.test(message);
    console.log('hasHtml:', hasHtml);

    // Check if this is a complete HTML document (starts with <!DOCTYPE or <html)
    const isCompleteHtml = message.trim().startsWith('<!DOCTYPE') || message.trim().startsWith('<html');
    console.log('isCompleteHtml:', isCompleteHtml);

    setGameState(prev => ({
      ...prev,
      messages: [
        ...prev.messages,
        {
          text: message,
          timestamp: new Date().toLocaleTimeString(),
          isHtml: hasAnsi || hasHtml,
          isCompleteHtml: isCompleteHtml,
          aliasChain: aliasChain,
        },
      ].slice(-100), // Keep last 100 messages
    }));
  }

  function handleCommandSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!commandInput.trim()) return;

    const command = commandInput.trim();

    // Add to history
    setCommandHistory(prev => [...prev, command].slice(-50)); // Keep last 50 commands
    setHistoryIndex(-1);

    // Parse command into command name and arguments
    const parts = command.split(/\s+/);
    const commandName = parts[0];
    const args = parts.slice(1);

    // Send command
    const success = sendCommand(commandName, args);
    if (success) {
      addMessage(`> ${command}`);
    } else {
      addMessage('Failed to send command - not connected');
    }

    setCommandInput('');
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        const newIndex = historyIndex + 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setCommandInput('');
      }
    }
  }

  function handleConnect() {
    addMessage('Attempting to connect...');
    connect();
  }

  function handleDisconnect() {
    addMessage('Disconnecting...');
    disconnect();
  }

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [gameState.messages]);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
    // Show welcome message and connection instructions
    addMessage('Welcome to MythosMUD! You are now authenticated.');
    addMessage("Click the 'Connect' button in the left sidebar to join the game.");
    addMessage('Once connected, you can enter commands in the input field at the bottom.');
  }, []);

  // Remove auto-connect to prevent infinite loop
  // useEffect(() => {
  //   if (playerId && authToken) {
  //     addMessage("Auto-connecting to MythosMUD...");
  //     connect();
  //   }
  // }, [playerId, authToken, connect]);

  return (
    <div className="game-terminal">
      {/* Main content area - two columns */}
      <div className="game-content">
        {/* Left sidebar */}
        <div className="left-sidebar">
          {/* Connection Status */}
          <div className="connection-status">
            <div className={`status-indicator ${isConnected ? 'connected' : 'disconnected'}`}>
              {isConnecting ? 'Connecting...' : isConnected ? 'Connected' : 'Disconnected'}
            </div>
            {error && <div className="error-message">{error}</div>}
            {reconnectAttempts > 0 && <div className="reconnect-info">Reconnect attempt {reconnectAttempts}</div>}
          </div>

          {/* Connection Instructions */}
          {!isConnected && !isConnecting && (
            <div className="connection-instructions">
              <h4>Getting Started</h4>
              <p>You are authenticated and ready to play!</p>
              <p>Click the "Connect" button below to join the game world.</p>
            </div>
          )}

          {/* Connection Controls - grouped together */}
          <div className="connection-controls">
            {!isConnected && !isConnecting && (
              <button onClick={handleConnect} className="connect-btn">
                Connect to Game
              </button>
            )}
            {isConnected && (
              <button onClick={handleDisconnect} className="disconnect-btn">
                Disconnect
              </button>
            )}
            <button
              onClick={() => {
                // Proper logout - redirect to login page
                window.location.href = '/';
              }}
              className="logout-btn"
            >
              Logout
            </button>
            <button
              onClick={() => {
                logger.downloadLogs();
              }}
              className="download-logs-btn"
            >
              Download Logs
            </button>
          </div>

          {/* Room Information Panel */}
          <RoomInfoPanel room={gameState.room} />

          {/* Game State Display */}
          {gameState.player && (
            <div className="player-info">
              <h3>{gameState.player.name}</h3>
              <div className="stats">
                <span>Level: {gameState.player.level || 1}</span>
                {gameState.player.stats && (
                  <div className="stats-grid">
                    {(() => {
                      let statsObj = gameState.player.stats;

                      // If stats is a string, try to parse it as JSON
                      if (typeof statsObj === 'string') {
                        try {
                          statsObj = JSON.parse(statsObj);
                        } catch (e) {
                          console.error('Failed to parse stats JSON:', e);
                        }
                      }

                      // If we have a valid object, display the stats
                      if (typeof statsObj === 'object' && statsObj !== null) {
                        return Object.entries(statsObj).map(([key, value]) => (
                          <div key={key} className="stat-item">
                            <span className="stat-label">
                              {key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}:
                            </span>
                            <span className="stat-value">{value}</span>
                          </div>
                        ));
                      } else {
                        return (
                          <div className="stat-item">
                            <span className="stat-label">Stats:</span>
                            <span className="stat-value">Loading...</span>
                          </div>
                        );
                      }
                    })()}
                  </div>
                )}
              </div>
            </div>
          )}
        </div>

        {/* Right terminal area */}
        <div className="terminal-area">
          {/* Message Log */}
          <div className="message-log">
            <div className="messages">
              {gameState.messages.map((message, index) => (
                <div key={index} className="message">
                  {/* Show alias expansion information if available */}
                  {message.aliasChain && message.aliasChain.length > 0 && (
                    <div className="alias-expansion">
                      <span className="alias-indicator">🔗</span>
                      {message.aliasChain.map((alias, chainIndex) => (
                        <span key={chainIndex} className="alias-chain">
                          <span className="alias-original">{alias.original}</span>
                          <span className="alias-arrow">→</span>
                          <span className="alias-expanded">{alias.expanded}</span>
                        </span>
                      ))}
                    </div>
                  )}

                  {/* Regular message content */}
                  {message.isHtml ? (
                    <span
                      dangerouslySetInnerHTML={{
                        __html: message.isCompleteHtml
                          ? message.text
                          : `[${message.timestamp}] ${ansiToHtmlWithBreaks(message.text)}`,
                      }}
                    />
                  ) : (
                    `[${message.timestamp}] ${message.text}`
                  )}
                </div>
              ))}
              <div ref={messagesEndRef} />
            </div>
          </div>
        </div>
      </div>

      {/* Command Input - full width at bottom */}
      <form onSubmit={handleCommandSubmit} className="command-input">
        <input
          ref={inputRef}
          type="text"
          value={commandInput}
          onChange={e => setCommandInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter command..."
          disabled={!isConnected}
        />
        <button type="submit" disabled={!isConnected || !commandInput.trim()}>
          Send
        </button>
      </form>
    </div>
  );
}
