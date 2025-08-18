import React from 'react';

interface GameTerminalProps {
  playerId: string;
  playerName: string;
  authToken: string;
  isConnected: boolean;
}

export const GameTerminal: React.FC<GameTerminalProps> = ({ playerId, playerName, isConnected }) => {
  return (
    <div className="h-full w-full bg-mythos-terminal-background text-mythos-terminal-text p-4">
      <div className="text-center">
        <h1 className="text-2xl font-bold text-mythos-terminal-primary mb-4">MythosMUD Terminal</h1>
        <p className="text-mythos-terminal-text-secondary mb-2">Player: {playerName}</p>
        <p className="text-mythos-terminal-text-secondary mb-4">Status: {isConnected ? 'Connected' : 'Disconnected'}</p>
        <p className="text-mythos-terminal-text">This is a simplified terminal view for testing TailwindCSS setup.</p>
      </div>
    </div>
  );
};
