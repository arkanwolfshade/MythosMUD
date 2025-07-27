import React, { useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnection';

interface GameTerminalProps {
  playerId: string;
  authToken: string;
}

interface GameState {
  player: any;
  room: any;
  entities: any[];
  messages: string[];
}

export function GameTerminal({ playerId, authToken }: GameTerminalProps) {
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

  const {
    isConnected,
    isConnecting,
    lastEvent,
    error,
    reconnectAttempts,
    sendCommand,
  } = useGameConnection({
    playerId,
    authToken,
    onEvent: handleGameEvent,
    onConnect: () => addMessage('Connected to MythosMUD...'),
    onDisconnect: () => addMessage('Disconnected from MythosMUD'),
    onError: (error) => addMessage(`Error: ${error}`),
  });

  function handleGameEvent(event: any) {
    console.log('Game event received:', event);
    
    switch (event.event_type) {
      case 'game_state':
        setGameState(prev => ({
          ...prev,
          player: event.data.player,
          room: event.data.room,
        }));
        addMessage(`Welcome to ${event.data.room?.name || 'Unknown Room'}`);
        break;
        
      case 'room_update':
        setGameState(prev => ({
          ...prev,
          room: event.data.room,
          entities: event.data.entities || [],
        }));
        addMessage(`Room updated: ${event.data.room?.name}`);
        break;
        
      case 'player_entered':
        addMessage(`${event.data.player_name} enters the room.`);
        break;
        
      case 'player_left':
        addMessage(`${event.data.player_name} leaves the room.`);
        break;
        
      case 'combat_event':
        addMessage(`[COMBAT] ${event.data.message}`);
        break;
        
      case 'chat_message':
        addMessage(`[${event.data.channel}] ${event.data.player_name}: ${event.data.message}`);
        break;
        
      case 'game_tick':
        // Optional: Show tick updates for debugging
        if (event.data.tick_number % 60 === 0) { // Every minute
          addMessage(`[TICK] Game tick ${event.data.tick_number}`);
        }
        break;
        
      case 'command_response':
        addMessage(event.data.result);
        break;
        
      case 'heartbeat':
        // Silent heartbeat - just keep connection alive
        break;
        
      default:
        addMessage(`[EVENT] ${event.event_type}: ${JSON.stringify(event.data)}`);
    }
  }

  function addMessage(message: string) {
    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, `[${new Date().toLocaleTimeString()}] ${message}`].slice(-100), // Keep last 100 messages
    }));
  }

  function handleCommandSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!commandInput.trim()) return;

    const command = commandInput.trim();
    
    // Add to history
    setCommandHistory(prev => [...prev, command].slice(-50)); // Keep last 50 commands
    setHistoryIndex(-1);
    
    // Send command
    const success = sendCommand(command, []);
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

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [gameState.messages]);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return (
    <div className="game-terminal">
      {/* Connection Status */}
      <div className="connection-status">
        <div className={`status-indicator ${isConnected ? 'connected' : 'disconnected'}`}>
          {isConnecting ? 'Connecting...' : isConnected ? 'Connected' : 'Disconnected'}
        </div>
        {error && <div className="error-message">{error}</div>}
        {reconnectAttempts > 0 && (
          <div className="reconnect-info">Reconnect attempt {reconnectAttempts}</div>
        )}
      </div>

      {/* Game State Display */}
      {gameState.player && (
        <div className="player-info">
          <h3>{gameState.player.name}</h3>
          <div className="stats">
            <span>HP: {gameState.player.stats?.current_health || 0}</span>
            <span>Sanity: {gameState.player.stats?.sanity || 0}</span>
            <span>Level: {gameState.player.level || 1}</span>
          </div>
        </div>
      )}

      {/* Room Information */}
      {gameState.room && (
        <div className="room-info">
          <h4>{gameState.room.name}</h4>
          <p>{gameState.room.description}</p>
          {gameState.entities.length > 0 && (
            <div className="entities">
              <strong>Entities in room:</strong>
              <ul>
                {gameState.entities.map((entity, index) => (
                  <li key={index}>{entity.name}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      {/* Message Log */}
      <div className="message-log">
        {gameState.messages.map((message, index) => (
          <div key={index} className="message">
            {message}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Command Input */}
      <form onSubmit={handleCommandSubmit} className="command-input">
        <input
          ref={inputRef}
          type="text"
          value={commandInput}
          onChange={(e) => setCommandInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter command (look, go north, say hello, etc.)"
          disabled={!isConnected}
        />
        <button type="submit" disabled={!isConnected || !commandInput.trim()}>
          Send
        </button>
      </form>

      {/* Quick Commands */}
      <div className="quick-commands">
        <button onClick={() => sendCommand('look')} disabled={!isConnected}>
          Look
        </button>
        <button onClick={() => sendCommand('inventory')} disabled={!isConnected}>
          Inventory
        </button>
        <button onClick={() => sendCommand('stats')} disabled={!isConnected}>
          Stats
        </button>
        <button onClick={() => sendCommand('help')} disabled={!isConnected}>
          Help
        </button>
      </div>
    </div>
  );
} 