import React, { createContext, ReactNode, useContext } from 'react';

// Context for sharing state between compound components
interface StatusPanelContextType {
  player: {
    id: string;
    name: string;
    stats: {
      current_health: number;
      max_health?: number;
      lucidity: number;
      max_lucidity?: number;
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
      position?: string;
    };
    level?: number;
    position?: string;
  } | null;
  isConnected: boolean;
  isConnecting: boolean;
  playerName: string;
  messagesCount: number;
  commandsCount: number;
}

const StatusPanelContext = createContext<StatusPanelContextType | null>(null);

// Hook to use the status panel context
const useStatusPanel = () => {
  const context = useContext(StatusPanelContext);
  if (!context) {
    throw new Error('useStatusPanel must be used within a StatusPanel');
  }
  return context;
};

// Main compound component
interface StatusPanelProps {
  player: StatusPanelContextType['player'];
  isConnected: boolean;
  isConnecting: boolean;
  playerName: string;
  messagesCount: number;
  commandsCount: number;
  children: ReactNode;
}

export const StatusPanel: React.FC<StatusPanelProps> = ({
  player,
  isConnected,
  isConnecting,
  playerName,
  messagesCount,
  commandsCount,
  children,
}) => {
  const contextValue: StatusPanelContextType = {
    player,
    isConnected,
    isConnecting,
    playerName,
    messagesCount,
    commandsCount,
  };

  return (
    <StatusPanelContext.Provider value={contextValue}>
      <div className="space-y-4">{children}</div>
    </StatusPanelContext.Provider>
  );
};

// Connection status sub-component
export const ConnectionStatus: React.FC = () => {
  const { isConnected, isConnecting } = useStatusPanel();

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Connection:</span>
      <div className="flex items-center space-x-2">
        <span className={`text-base ${isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error'}`}>
          {isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected'}
        </span>
      </div>
    </div>
  );
};

// Player name sub-component
export const PlayerName: React.FC = () => {
  const { playerName } = useStatusPanel();

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Player:</span>
      <span className="text-base text-mythos-terminal-text">{playerName}</span>
    </div>
  );
};

// Health stat sub-component
export const HealthStat: React.FC = () => {
  const { player } = useStatusPanel();

  if (player?.stats?.current_health === undefined) return null;

  const maxHealth = player.stats.max_health ?? 100;

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Health:</span>
      <span className="text-base text-mythos-terminal-text">
        {player.stats.current_health} / {maxHealth}
      </span>
    </div>
  );
};

// Lucidity stat sub-component
export const LucidityStat: React.FC = () => {
  const { player } = useStatusPanel();

  if (!player?.stats?.lucidity) return null;

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Lucidity:</span>
      <span className="text-base text-mythos-terminal-text">{player.stats.lucidity}</span>
    </div>
  );
};

// Core attributes sub-component
export const CoreAttributes: React.FC = () => {
  const { player } = useStatusPanel();

  if (!player?.stats) return null;

  const attributes = [
    { key: 'strength', label: 'STR' },
    { key: 'dexterity', label: 'DEX' },
    { key: 'constitution', label: 'CON' },
    { key: 'intelligence', label: 'INT' },
    { key: 'wisdom', label: 'WIS' },
    { key: 'charisma', label: 'CHA' },
  ];

  const availableAttributes = attributes.filter(
    attr => player.stats[attr.key as keyof typeof player.stats] !== undefined
  );

  if (availableAttributes.length === 0) return null;

  return (
    <div className="border-t border-mythos-terminal-border pt-2">
      <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
      <div className="grid grid-cols-2 gap-1 text-sm">
        {availableAttributes.map(attr => (
          <div key={attr.key} className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">{attr.label}:</span>
            <span className="text-mythos-terminal-text">{player.stats[attr.key as keyof typeof player.stats]}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

// Horror stats sub-component
export const HorrorStats: React.FC = () => {
  const { player } = useStatusPanel();

  if (!player?.stats) return null;

  const horrorStats = [
    { key: 'occult_knowledge', label: 'Occult' },
    { key: 'fear', label: 'Fear' },
    { key: 'corruption', label: 'Corruption' },
    { key: 'cult_affiliation', label: 'Cult' },
  ];

  const availableHorrorStats = horrorStats.filter(
    stat => player.stats[stat.key as keyof typeof player.stats] !== undefined
  );

  if (availableHorrorStats.length === 0) return null;

  return (
    <div className="border-t border-mythos-terminal-border pt-2">
      <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
      <div className="grid grid-cols-2 gap-1 text-sm">
        {availableHorrorStats.map(stat => (
          <div key={stat.key} className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">{stat.label}:</span>
            <span className="text-mythos-terminal-text">{player.stats[stat.key as keyof typeof player.stats]}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

// Messages count sub-component
export const MessagesCount: React.FC = () => {
  const { messagesCount } = useStatusPanel();

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Messages:</span>
      <span className="text-base text-mythos-terminal-text">{messagesCount}</span>
    </div>
  );
};

// Commands count sub-component
export const CommandsCount: React.FC = () => {
  const { commandsCount } = useStatusPanel();

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Commands:</span>
      <span className="text-base text-mythos-terminal-text">{commandsCount}</span>
    </div>
  );
};

// Player stats group sub-component
export const PlayerStats: React.FC = () => {
  const { player } = useStatusPanel();

  if (!player?.stats) return null;

  return (
    <>
      <HealthStat />
      <LucidityStat />
      <CoreAttributes />
      <HorrorStats />
    </>
  );
};

// All stats group sub-component
export const AllStats: React.FC = () => {
  return (
    <>
      <ConnectionStatus />
      <PlayerName />
      <PlayerStats />
      <MessagesCount />
      <CommandsCount />
    </>
  );
};
