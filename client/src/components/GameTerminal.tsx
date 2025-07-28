import React, { useEffect, useRef, useState } from "react";
import { useGameConnection } from "../hooks/useGameConnection";
import { ansiToHtmlWithBreaks } from "../utils/ansiToHtml";
import "./GameTerminal.css";

interface GameTerminalProps {
  playerId: string;
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
  name: string;
  description: string;
}

interface Entity {
  name: string;
}

interface GameEvent {
  event_type: string;
  data: Record<string, unknown>;
}

interface GameState {
  player: Player | null;
  room: Room | null;
  entities: Entity[];
  messages: Array<{
    text: string;
    timestamp: string;
    isHtml: boolean;
  }>;
}

export function GameTerminal({ playerId, authToken }: GameTerminalProps) {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    entities: [],
    messages: [],
  });

  const [commandInput, setCommandInput] = useState("");
  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState(-1);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    playerId,
    authToken,
    onEvent: handleGameEvent,
    onConnect: () => addMessage("Connected to MythosMUD..."),
    onDisconnect: () => addMessage("Disconnected from MythosMUD"),
    onError: (error) => addMessage(`Error: ${error}`),
  });

  function handleGameEvent(event: GameEvent) {
    console.log("Game event received:", event);

    switch (event.event_type) {
      case "game_state":
        setGameState((prev) => ({
          ...prev,
          player: event.data.player as Player,
          room: event.data.room as Room,
        }));
        addMessage(`Welcome to ${(event.data.room as Room)?.name || "Unknown Room"}`);
        break;

      case "motd":
        // Display the Message of the Day
        console.log("MOTD received:", event.data.message);
        console.log("MOTD contains ANSI:", (event.data.message as string).includes("\x1b["));
        console.log("MOTD length:", (event.data.message as string).length);
        addMessage(event.data.message as string);
        break;

      case "room_update":
        setGameState((prev) => ({
          ...prev,
          room: event.data.room as Room,
          entities: (event.data.entities as Entity[]) || [],
        }));
        addMessage(`Room updated: ${(event.data.room as Room)?.name}`);
        break;

      case "player_entered":
        addMessage(`${event.data.player_name as string} enters the room.`);
        break;

      case "player_left":
        addMessage(`${event.data.player_name as string} leaves the room.`);
        break;

      case "combat_event":
        addMessage(`[COMBAT] ${event.data.message as string}`);
        break;

      case "chat_message":
        addMessage(
          `[${event.data.channel as string}] ${event.data.player_name as string}: ${event.data.message as string}`,
        );
        break;

      case "game_tick":
        // Optional: Show tick updates for debugging
        if ((event.data.tick_number as number) % 60 === 0) {
          // Every minute
          addMessage(`[TICK] Game tick ${event.data.tick_number as number}`);
        }
        break;

      case "command_response":
        addMessage(event.data.result as string);
        break;

      case "heartbeat":
        // Silent heartbeat - just keep connection alive
        break;

      default:
        addMessage(`[EVENT] ${event.event_type}: ${JSON.stringify(event.data)}`);
    }
  }

  function addMessage(message: string) {
    // Check if message contains ANSI escape sequences
    const hasAnsi = message.includes("\x1b[");
    console.log("addMessage called with:", message.substring(0, 100) + "...");
    console.log("hasAnsi:", hasAnsi);

    // Count ANSI sequences manually
    let ansiCount = 0;
    for (let i = 0; i < message.length - 1; i++) {
      if (message[i] === "\x1b" && message[i + 1] === "[") {
        ansiCount++;
      }
    }
    console.log("ANSI sequences count:", ansiCount);

    setGameState((prev) => ({
      ...prev,
      messages: [
        ...prev.messages,
        {
          text: message,
          timestamp: new Date().toLocaleTimeString(),
          isHtml: hasAnsi,
        },
      ].slice(-100), // Keep last 100 messages
    }));
  }

  function handleCommandSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!commandInput.trim()) return;

    const command = commandInput.trim();

    // Add to history
    setCommandHistory((prev) => [...prev, command].slice(-50)); // Keep last 50 commands
    setHistoryIndex(-1);

    // Send command
    const success = sendCommand(command, []);
    if (success) {
      addMessage(`> ${command}`);
    } else {
      addMessage("Failed to send command - not connected");
    }

    setCommandInput("");
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "ArrowUp") {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        const newIndex = historyIndex + 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      }
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setCommandInput("");
      }
    }
  }

  function handleConnect() {
    addMessage("Attempting to connect...");
    connect();
  }

  function handleDisconnect() {
    addMessage("Disconnecting...");
    disconnect();
  }

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [gameState.messages]);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
    // Show manual connection message
    addMessage("Welcome to MythosMUD! Click 'Connect' to join the game.");
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
            <div className={`status-indicator ${isConnected ? "connected" : "disconnected"}`}>
              {isConnecting ? "Connecting..." : isConnected ? "Connected" : "Disconnected"}
            </div>
            {error && <div className="error-message">{error}</div>}
            {reconnectAttempts > 0 && <div className="reconnect-info">Reconnect attempt {reconnectAttempts}</div>}
          </div>

          {/* Connection Controls - grouped together */}
          <div className="connection-controls">
            {!isConnected && !isConnecting && (
              <button onClick={handleConnect} className="connect-btn">
                Connect
              </button>
            )}
            {isConnected && (
              <button onClick={handleDisconnect} className="disconnect-btn">
                Disconnect
              </button>
            )}
            <button onClick={() => (window.location.href = "/logout")} className="logout-btn">
              Logout
            </button>
            <button
              onClick={() => {
                /* TODO: Implement download logs */
              }}
              className="download-logs-btn"
            >
              Download Logs
            </button>
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
        </div>

        {/* Right terminal area */}
        <div className="terminal-area">
          {/* Message Log */}
          <div className="message-log">
            <div className="messages">
              {gameState.messages.map((message, index) => (
                <div key={index} className="message">
                  {message.isHtml ? (
                    <span
                      dangerouslySetInnerHTML={{
                        __html: `[${message.timestamp}] ${ansiToHtmlWithBreaks(message.text)}`,
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
          onChange={(e) => setCommandInput(e.target.value)}
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
