import { useEffect, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnection';
import { logger } from '../utils/logger';
import { CommandHelpDrawer } from './CommandHelpDrawer';
import './GameTerminalWithPanels.css';
import { MotdContent } from './MotdContent';
import { PanelManager } from './PanelManager';

interface GameTerminalWithPanelsProps {
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
  occupants?: string[];
  occupant_count?: number;
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
  roomOccupants: string[];
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
}

export function GameTerminalWithPanels({ playerId, playerName, authToken }: GameTerminalWithPanelsProps) {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    entities: [],
    roomOccupants: [],
    messages: [],
  });

  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [helpDrawerOpen, setHelpDrawerOpen] = useState(false);
  const [showMotd, setShowMotd] = useState(true);

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

    const filterAndDedupe = (names: string[]): string[] => {
      const filtered = (names || []).filter(n => !!n && n !== playerName);
      return Array.from(new Set(filtered));
    };

    // Safely extract strongly-typed properties from generic event payloads
    const getStringProp = (data: Record<string, unknown>, key: string): string | undefined => {
      const value = data[key];
      return typeof value === 'string' ? value : undefined;
    };

    const getStringArrayProp = (data: Record<string, unknown>, key: string): string[] => {
      const value = data[key];
      if (Array.isArray(value)) {
        return value.filter((v): v is string => typeof v === 'string');
      }
      return [];
    };

    switch (event.event_type) {
      case 'game_state': {
        const roomFromEvent = (event.data.room as Room) || null;
        const occupantsFromEvent = filterAndDedupe((event.data.occupants as string[]) || []);
        const roomWithOccupants = roomFromEvent
          ? {
              ...roomFromEvent,
              occupants: occupantsFromEvent,
              occupant_count: occupantsFromEvent.length,
            }
          : null;

        setGameState(prev => ({
          ...prev,
          player: event.data.player as Player,
          room: roomWithOccupants,
          roomOccupants: occupantsFromEvent,
        }));
        addMessage(`Welcome to ${(roomFromEvent as Room)?.name || 'Unknown Room'}`);
        break;
      }

      case 'motd':
        // Display the Message of the Day
        console.log('MOTD received:', event.data.message);
        console.log('MOTD contains ANSI:', (event.data.message as string).includes('\x1b['));
        console.log('MOTD length:', (event.data.message as string).length);
        addMessage(event.data.message as string);
        break;

      case 'room_update': {
        console.log('Room update received:', event.data);
        const roomFromEvent = (event.data.room as Room) || null;
        const occupantsFromEvent = filterAndDedupe((event.data.occupants as string[]) || []);
        const roomWithOccupants = roomFromEvent
          ? {
              ...roomFromEvent,
              occupants: occupantsFromEvent,
              occupant_count: occupantsFromEvent.length,
            }
          : null;

        setGameState(prev => ({
          ...prev,
          room: roomWithOccupants,
          entities: (event.data.entities as Entity[]) || [],
          roomOccupants: occupantsFromEvent,
        }));
        addMessage(`Room updated: ${(roomFromEvent as Room)?.name}`);
        break;
      }

      case 'player_entered': {
        const name = getStringProp(event.data, 'player_name');
        if (name && name !== playerName) {
          addMessage(`${name} entered the room.`);
          // Optimistically add to occupants
          setGameState(prev => {
            const current = prev.room?.occupants || [];
            const next = Array.from(new Set([...current, name]));
            return {
              ...prev,
              room: prev.room ? { ...prev.room, occupants: next, occupant_count: next.length } : prev.room,
              roomOccupants: next,
            };
          });
        }
        break;
      }

      case 'player_left': {
        const name = getStringProp(event.data, 'player_name');
        if (name && name !== playerName) {
          addMessage(`${name} left the room.`);
          // Optimistically remove from occupants
          setGameState(prev => {
            const current = prev.room?.occupants || [];
            const next = current.filter(n => n !== name);
            return {
              ...prev,
              room: prev.room ? { ...prev.room, occupants: next, occupant_count: next.length } : prev.room,
              roomOccupants: next,
            };
          });
        }
        break;
      }

      case 'player_left_game': {
        const name = getStringProp(event.data, 'player_name');
        if (name && name !== playerName) {
          addMessage(`${name} left the game.`);
          // Optimistically remove from occupants
          setGameState(prev => {
            const current = prev.room?.occupants || [];
            const next = current.filter(n => n !== name);
            return {
              ...prev,
              room: prev.room ? { ...prev.room, occupants: next } : prev.room,
              roomOccupants: next,
            };
          });
        }
        break;
      }

      case 'room_occupants': {
        const occupants = filterAndDedupe(getStringArrayProp(event.data, 'occupants'));
        setGameState(prev => ({
          ...prev,
          room: prev.room ? { ...prev.room, occupants, occupant_count: occupants.length } : prev.room,
          roomOccupants: occupants,
        }));
        break;
      }

      case 'combat_event':
        addMessage(`[COMBAT] ${event.data.message as string}`);
        break;

      case 'chat_message': {
        const channel = event.data.channel as string;
        const playerName = event.data.player_name as string;
        const message = event.data.message as string;

        // Format messages based on channel type
        switch (channel) {
          case 'say':
            addMessage(`${playerName} says: ${message}`);
            break;
          case 'emote':
            // For predefined emotes, the message is already formatted
            // For regular emotes, format as "PlayerName action"
            if (message.includes(' ') && !message.startsWith('*')) {
              // This is likely a predefined emote (e.g., "ArkanWolfshade twibbles around aimlessly.")
              addMessage(`*${message}*`, undefined, 'emote');
            } else {
              // This is a regular emote (e.g., "adjusts spectacles")
              addMessage(`*${playerName} ${message}*`, undefined, 'emote');
            }
            break;
          case 'pose':
            // Format poses to show current status
            addMessage(`${playerName} ${message}`);
            break;
          default:
            // Fallback for unknown channels
            addMessage(`[${channel}] ${playerName}: ${message}`);
            break;
        }
        break;
      }

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

  function addMessage(
    message: string,
    aliasChain?: Array<{ original: string; expanded: string; alias_name: string }>,
    messageType?: string
  ) {
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
          messageType: messageType,
          aliasChain: aliasChain,
        },
      ].slice(-100), // Keep last 100 messages
    }));
  }

  function handleCommandSubmit(command: string) {
    if (!command.trim()) return;

    // Add to history
    setCommandHistory(prev => [...prev, command].slice(-50)); // Keep last 50 commands

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
  }

  function handleConnect() {
    addMessage('Attempting to connect...');
    connect();
  }

  function handleDisconnect() {
    addMessage('Disconnecting...');
    disconnect();
  }

  function handleLogout() {
    // Proper logout - redirect to login page
    window.location.href = '/';
  }

  function handleClearMessages() {
    setGameState(prev => ({ ...prev, messages: [] }));
  }

  function handleClearHistory() {
    setCommandHistory([]);
  }

  const handleMotdContinue = () => {
    logger.info('GameTerminalWithPanels', 'User continued from MOTD and connecting to game');
    setShowMotd(false);
    // Add a welcome message to the game
    addMessage('Welcome to MythosMUD! You are now ready to explore the Dreamlands.');
    // Connect to the game
    connect();
  };

  // Focus input on mount
  useEffect(() => {
    // Show welcome message and connection instructions
    addMessage('Welcome to MythosMUD! You are now authenticated.');
    addMessage("Click the 'Connect' button in the connection panel to join the game.");
    addMessage('Once connected, you can enter commands in the command panel.');
  }, []);

  if (showMotd) {
    return (
      <div className="game-terminal">
        <div className="motd-display">
          <div className="motd-content">
            <MotdContent />
            <div className="motd-actions">
              <button onClick={handleMotdContinue} className="continue-button">
                Enter the Dreamlands
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="game-terminal">
      <PanelManager
        isConnected={isConnected}
        isConnecting={isConnecting}
        error={error}
        reconnectAttempts={reconnectAttempts}
        room={gameState.room}
        player={gameState.player}
        messages={gameState.messages}
        commandHistory={commandHistory}
        onConnect={handleConnect}
        onDisconnect={handleDisconnect}
        onLogout={handleLogout}
        onDownloadLogs={() => logger.downloadLogs()}
        onSendCommand={handleCommandSubmit}
        onClearMessages={handleClearMessages}
        onClearHistory={handleClearHistory}
      />

      {/* Command Help Drawer */}
      <CommandHelpDrawer open={helpDrawerOpen} onClose={() => setHelpDrawerOpen(false)} />
    </div>
  );
}
