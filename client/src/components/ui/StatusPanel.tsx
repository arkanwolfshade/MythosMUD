import React, { createContext, ReactNode, useContext } from 'react';

// Context for sharing state between compound components
interface StatusPanelContextType {
  player: {
    id: string;
    name: string;
    stats: {
      current_dp?: number;
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

// Helper function to get connection status text and class
const getConnectionStatus = (isConnected: boolean, isConnecting: boolean) => {
  if (isConnected) {
    return { text: 'Connected', className: 'text-mythos-terminal-success' };
  }
  if (isConnecting) {
    return { text: 'Connecting...', className: 'text-mythos-terminal-error' };
  }
  return { text: 'Disconnected', className: 'text-mythos-terminal-error' };
};

// Type helper for player stats
type PlayerStats = NonNullable<StatusPanelContextType['player']>['stats'];

// Helper function to check if a stat exists
const hasStat = (stats: PlayerStats | undefined, key: string): boolean => {
  if (!stats) return false;
  return stats[key as keyof typeof stats] !== undefined;
};

// Helper function to get stat value
const getStatValue = (stats: PlayerStats | undefined, key: string): number | undefined => {
  if (!stats) return undefined;
  return stats[key as keyof typeof stats] as number | undefined;
};

// Main compound component
export interface StatusPanelProps {
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

// Reusable single stat display component
interface SingleStatProps {
  label: string;
  value: number | string | undefined;
}

const SingleStat: React.FC<SingleStatProps> = ({ label, value }) => {
  if (value === undefined) return null;

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">{label}:</span>
      <span className="text-base text-mythos-terminal-text">{value}</span>
    </div>
  );
};

// Connection status sub-component
export const ConnectionStatus: React.FC = () => {
  const { isConnected, isConnecting } = useStatusPanel();
  const { text, className } = getConnectionStatus(isConnected, isConnecting);

  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">Connection:</span>
      <div className="flex items-center space-x-2">
        <span className={`text-base ${className}`}>{text}</span>
      </div>
    </div>
  );
};

// Player name sub-component
export const PlayerName: React.FC = () => {
  const { playerName } = useStatusPanel();
  return <SingleStat label="Player" value={playerName} />;
};

// Health stat sub-component
export const HealthStat: React.FC = () => {
  const { player } = useStatusPanel();
  const currentHealth = player?.stats?.current_dp;
  const maxHealth = player?.stats?.max_health ?? 100;

  if (currentHealth === undefined) return null;

  return <SingleStat label="Health" value={`${currentHealth} / ${maxHealth}`} />;
};

// Lucidity stat sub-component
export const LucidityStat: React.FC = () => {
  const { player } = useStatusPanel();
  const lucidity = player?.stats?.lucidity;
  return <SingleStat label="Lucidity" value={lucidity} />;
};

// Reusable stat group component
interface StatGroupProps {
  title: string;
  stats: Array<{ key: string; label: string }>;
  playerStats: PlayerStats | undefined;
}

const StatGroup: React.FC<StatGroupProps> = ({ title, stats, playerStats }) => {
  const availableStats = stats.filter(stat => hasStat(playerStats, stat.key));

  if (availableStats.length === 0) return null;

  return (
    <div className="border-t border-mythos-terminal-border pt-2">
      <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">{title}:</h5>
      <div className="grid grid-cols-2 gap-1 text-sm">
        {availableStats.map(stat => {
          const value = getStatValue(playerStats, stat.key);
          return (
            <div key={stat.key} className="flex justify-between">
              <span className="text-mythos-terminal-text-secondary">{stat.label}:</span>
              <span className="text-mythos-terminal-text">{value}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

// Core attributes configuration
const CORE_ATTRIBUTES = [
  { key: 'strength', label: 'STR' },
  { key: 'dexterity', label: 'DEX' },
  { key: 'constitution', label: 'CON' },
  { key: 'intelligence', label: 'INT' },
  { key: 'wisdom', label: 'WIS' },
  { key: 'charisma', label: 'CHA' },
];

// Horror stats configuration
const HORROR_STATS = [
  { key: 'occult_knowledge', label: 'Occult' },
  { key: 'fear', label: 'Fear' },
  { key: 'corruption', label: 'Corruption' },
  { key: 'cult_affiliation', label: 'Cult' },
];

// Core attributes sub-component
export const CoreAttributes: React.FC = () => {
  const { player } = useStatusPanel();
  return <StatGroup title="Core Attributes" stats={CORE_ATTRIBUTES} playerStats={player?.stats} />;
};

// Horror stats sub-component
export const HorrorStats: React.FC = () => {
  const { player } = useStatusPanel();
  return <StatGroup title="Horror Stats" stats={HORROR_STATS} playerStats={player?.stats} />;
};

// Messages count sub-component
export const MessagesCount: React.FC = () => {
  const { messagesCount } = useStatusPanel();
  return <SingleStat label="Messages" value={messagesCount} />;
};

// Commands count sub-component
export const CommandsCount: React.FC = () => {
  const { commandsCount } = useStatusPanel();
  return <SingleStat label="Commands" value={commandsCount} />;
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
