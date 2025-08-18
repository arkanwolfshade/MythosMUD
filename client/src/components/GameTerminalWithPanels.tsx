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
        case 'room_update':
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
          const message = {
            text: event.data.message as string,
            timestamp: event.timestamp,
            isHtml: (event.data.is_html as boolean) || false,
            messageType: event.event_type === 'chat_message' ? 'chat' : 'system',
          };
          setGameState(prev => ({
            ...prev,
            messages: [...prev.messages, message],
          }));
          break;
        }
        case 'command_response': {
          const response = {
            text: event.data.response as string,
            timestamp: event.timestamp,
            isHtml: (event.data.is_html as boolean) || false,
            messageType: 'system',
          };
          setGameState(prev => ({
            ...prev,
            messages: [...prev.messages, response],
          }));
          break;
        }
      }
    },
    onConnect: () => {
      logger.info('GameTerminalWithPanels', 'Connected to game server');
    },
    onDisconnect: () => {
      logger.info('GameTerminalWithPanels', 'Disconnected from game server');
    },
    onError: error => {
      logger.error('GameTerminalWithPanels', 'Game connection error', { error });
    },
  });

  // Connect to the game server when component mounts
  useEffect(() => {
    if (authToken && playerName && !isConnected && !isConnecting && !hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameTerminalWithPanels', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
        isConnected,
        isConnecting,
      });
      connect();
    }

    // Cleanup function to disconnect when component unmounts
    return () => {
      if (isConnected) {
        logger.info('GameTerminalWithPanels', 'Cleaning up connection on unmount');
        disconnect();
      }
    };
  }, [authToken, playerName, isConnected, isConnecting, connect, disconnect]);

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

    // Send command to server
    const success = await sendCommand(normalized);
    if (!success) {
      logger.error('GameTerminalWithPanels', 'Failed to send command', { command: normalized });
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
