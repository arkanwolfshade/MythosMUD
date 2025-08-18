// import { ThemeProvider } from '@mui/material/styles';
import React, { useEffect, useState } from 'react';
import { GameTerminal } from './GameTerminal';
import { PanelManager } from './PanelManager';
// import mythosTheme from '../theme/mythosTheme';
import { logger } from '../utils/logger';

interface GameTerminalWithPanelsProps {
  playerId: string;
  playerName: string;
  authToken: string;
}

export const GameTerminalWithPanels: React.FC<GameTerminalWithPanelsProps> = ({ playerId, playerName, authToken }) => {
  const [isConnected, setIsConnected] = useState(false);
  // const [connectionError, setConnectionError] = useState<string | null>(null);

  useEffect(() => {
    logger.info('GameTerminalWithPanels', 'Component mounted', { playerId, playerName });
    // Simulate connection for now
    setIsConnected(true);
  }, [playerId, playerName]);

  return (
    <div className="h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono">
      <PanelManager>
        <GameTerminal playerId={playerId} playerName={playerName} authToken={authToken} isConnected={isConnected} />
      </PanelManager>
    </div>
  );
};
