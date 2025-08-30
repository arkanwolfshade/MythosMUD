import { useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnection';
import { logger } from '../utils/logger';
import { CommandHelpDrawer } from './CommandHelpDrawer';
import { GameTerminal } from './GameTerminal';

interface GameTerminalWithPanelsProps {
  playerName: string;
  authToken: string;
}

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

interface GameState {
  room: Room | null;
  player: Player | null;
  messages: Array<{
    text: string;
    timestamp: string;
    isHtml: boolean;
    messageType?: string;
  }>;
}

export const GameTerminalWithPanels: React.FC<GameTerminalWithPanelsProps> = ({ playerName, authToken }) => {
  const [gameState, setGameState] = useState<GameState>({
    room: null,
    player: null,
    messages: [],
  });
  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [helpDrawerOpen, setHelpDrawerOpen] = useState(false);
  const hasAttemptedConnection = useRef(false);

  // Use the game connection hook for real server communication
  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    playerName,
    authToken,
    onEvent: event => {
      logger.info('GameTerminalWithPanels', 'Game event received', { event_type: event.event_type });

      // Handle different event types
      switch (event.event_type) {
        case 'game_state':
          logger.info('GameTerminalWithPanels', 'Game state received', {
            room_data: event.data.room,
            room_id: (event.data.room as Room)?.id,
            room_name: (event.data.room as Room)?.name,
          });
          setGameState(prev => ({
            ...prev,
            room: (event.data.room as Room) ?? prev.room,
            player: (event.data.player as Player) ?? prev.player,
          }));
          break;
        case 'room_update':
          logger.info('GameTerminalWithPanels', 'Room update received', {
            room_data: event.data.room,
            room_id: (event.data.room as Room)?.id,
            room_name: (event.data.room as Room)?.name,
          });
          setGameState(prev => ({
            ...prev,
            room: event.data.room as Room,
          }));
          break;
        case 'player_update':
          setGameState(prev => ({
            ...prev,
            player: event.data.player as Player,
          }));
          break;
        case 'chat_message':
        case 'system_message': {
          // Extract channel and target information for proper message formatting
          const channel = event.data.channel as string;
          const senderName = event.data.player_name as string;
          const targetName = event.data.target_name as string;
          const rawMessage = event.data.message as string;

          // Determine if this is a whisper message and format accordingly
          let formattedMessage = rawMessage;
          let messageType = event.event_type === 'chat_message' ? 'chat' : 'system';

          if (channel === 'whisper') {
            messageType = 'whisper';

            // Check if current player is the sender or target
            if (senderName === playerName) {
              // Current player is the sender - format as outgoing whisper
              formattedMessage = `You whisper to ${targetName}: ${event.data.content || rawMessage}`;
            } else if (targetName === playerName) {
              // Current player is the target - format as incoming whisper
              formattedMessage = `${senderName} whispers to you: ${event.data.content || rawMessage}`;
            } else {
              // This shouldn't happen, but fallback to generic whisper format
              formattedMessage = `${senderName} whispers: ${event.data.content || rawMessage}`;
            }
          }

          const message = {
            text: formattedMessage,
            timestamp: event.timestamp,
            isHtml: (event.data.is_html as boolean) || false,
            messageType: messageType,
          };
          setGameState(prev => ({
            ...prev,
            messages: [...prev.messages, message],
          }));
          break;
        }
        case 'command_response': {
          // Server uses `result` as the payload key
          const resultText = (event.data.result as string) ?? '';
          const response = {
            text: resultText,
            timestamp: event.timestamp,
            isHtml: Boolean(event.data.is_html),
            messageType: 'system',
          };
          setGameState(prev => ({
            ...prev,
            messages: [...prev.messages, response],
          }));
          break;
        }
        case 'player_entered': {
          const playerName = event.data.player_name as string;
          if (playerName) {
            const message = {
              text: `${playerName} enters the room.`,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system',
            };
            setGameState(prev => ({
              ...prev,
              messages: [...prev.messages, message],
            }));
          }
          break;
        }
        case 'player_left': {
          const playerName = event.data.player_name as string;
          if (playerName) {
            const message = {
              text: `${playerName} leaves the room.`,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system',
            };
            setGameState(prev => ({
              ...prev,
              messages: [...prev.messages, message],
            }));
          }
          break;
        }
        case 'player_entered_game': {
          const playerName = event.data.player_name as string;
          if (playerName) {
            const message = {
              text: `${playerName} has entered the game.`,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system',
            };
            setGameState(prev => ({
              ...prev,
              messages: [...prev.messages, message],
            }));
          }
          break;
        }
        case 'player_left_game': {
          const playerName = event.data.player_name as string;
          if (playerName) {
            const message = {
              text: `${playerName} has left the game.`,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system',
            };
            setGameState(prev => ({
              ...prev,
              messages: [...prev.messages, message],
            }));
          }
          break;
        }
      }
    },
    onConnect: () => {
      logger.info('GameTerminalWithPanels', 'Connected to game server');
      // Clear messages on successful connection to start fresh
      setGameState(prev => ({ ...prev, messages: [] }));
    },
    onDisconnect: () => {
      logger.info('GameTerminalWithPanels', 'Disconnected from game server');
    },
    onError: error => {
      logger.error('GameTerminalWithPanels', 'Game connection error', { error });
    },
  });

  // Connect once on mount; disconnect on unmount.
  // Important: Avoid including changing dependencies (like connect/disconnect identity or state)
  // which would trigger cleanup on every render and cause immediate disconnects.
  useEffect(() => {
    if (!hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameTerminalWithPanels', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
      });
      connect();
    }

    return () => {
      logger.info('GameTerminalWithPanels', 'Cleaning up connection on unmount');
      disconnect();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleCommandSubmit = async (command: string) => {
    if (!command.trim() || !isConnected) return;

    let normalized = command.trim();
    const lower = normalized.toLowerCase();
    const dirMap: Record<string, string> = {
      n: 'north',
      s: 'south',
      e: 'east',
      w: 'west',
      ne: 'northeast',
      nw: 'northwest',
      se: 'southeast',
      sw: 'southwest',
      u: 'up',
      d: 'down',
      up: 'up',
      down: 'down',
    };

    // Normalize slash prefix
    if (lower.startsWith('/')) {
      normalized = normalized.slice(1).trim();
    }

    // Expand shorthand for movement and look
    const parts = normalized.split(/\s+/);
    if (parts.length === 1 && dirMap[lower]) {
      normalized = `go ${dirMap[lower]}`;
    } else if (parts.length === 2) {
      const [verb, arg] = [parts[0].toLowerCase(), parts[1].toLowerCase()];
      if ((verb === 'go' || verb === 'look') && dirMap[arg]) {
        normalized = `${verb} ${dirMap[arg]}`;
      }
    }

    // Add to command history
    setCommandHistory(prev => [...prev, normalized]);

    // Parse command for sending to server
    const commandParts = normalized.split(/\s+/);
    const commandName = commandParts[0];
    const commandArgs = commandParts.slice(1);

    // Send command to server
    const success = await sendCommand(commandName, commandArgs);
    if (!success) {
      logger.error('GameTerminalWithPanels', 'Failed to send command', { command: commandName, args: commandArgs });
    }
  };

  const handleClearMessages = () => {
    setGameState(prev => ({ ...prev, messages: [] }));
  };

  const handleClearHistory = () => {
    setCommandHistory([]);
  };

  const handleLogout = () => {
    disconnect();
    // Note: App.tsx will handle the logout state
  };

  return (
    <div className="game-terminal-container">
      <GameTerminal
        playerName={playerName}
        isConnected={isConnected}
        isConnecting={isConnecting}
        error={error}
        reconnectAttempts={reconnectAttempts}
        room={gameState.room}
        player={gameState.player}
        messages={gameState.messages}
        commandHistory={commandHistory}
        onConnect={connect}
        onDisconnect={disconnect}
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
};
