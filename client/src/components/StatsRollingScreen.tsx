import React from 'react';
import { useStatsRolling, type Stats } from '../hooks/useStatsRolling.js';
import { logger } from '../utils/logger.js';
import type { Profession } from './ProfessionCard.tsx';
import './StatsRollingScreen.css';

/** Plan 10.6 F2: Stats-first flow; name and create-character happen on CharacterNameScreen. */
interface StatsRollingScreenProps {
  onStatsAccepted: (stats: Stats) => void;
  onError: (error: string) => void;
  onBack?: () => void;
  baseUrl: string;
  authToken: string;
  /** Optional: when set, roll uses profession for preview; when omitted, raw roll (stats-first step). */
  professionId?: number;
  profession?: Profession;
}

const STAT_ROWS: Array<{ key: keyof Stats; label: string }> = [
  { key: 'strength', label: 'Strength' },
  { key: 'dexterity', label: 'Dexterity' },
  { key: 'constitution', label: 'Constitution' },
  { key: 'size', label: 'Size' },
  { key: 'intelligence', label: 'Intelligence' },
  { key: 'power', label: 'Power' },
  { key: 'education', label: 'Education' },
  { key: 'charisma', label: 'Charisma' },
  { key: 'luck', label: 'Luck' },
];

function StatsGrid({ stats }: { stats: Stats }) {
  return (
    <div className="stats-display">
      <h3>Your Character's Stats</h3>
      <div className="stats-grid">
        {STAT_ROWS.map(row => (
          <div key={row.key} className="stat-item">
            <span className="stat-name">{row.label}:</span>
            <span className="stat-value">{stats[row.key]}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function StatsActions({
  onBack,
  onReroll,
  onAccept,
  rerollCooldown,
  isRerolling,
  isLoading,
}: {
  onBack?: () => void;
  onReroll: () => void;
  onAccept: () => void;
  rerollCooldown: number;
  isRerolling: boolean;
  isLoading: boolean;
}) {
  const rerollLabel = isRerolling
    ? 'Rerolling...'
    : rerollCooldown > 0
      ? `Reroll (${rerollCooldown}s)`
      : 'Reroll Stats';
  return (
    <div className="stats-actions">
      {onBack && (
        <button onClick={onBack} className="back-button" type="button">
          Back
        </button>
      )}
      <button
        onClick={onReroll}
        disabled={rerollCooldown > 0 || isRerolling || isLoading}
        className="reroll-button"
        type="button"
      >
        {rerollLabel}
      </button>
      <button onClick={onAccept} className="accept-button" type="button">
        Accept Stats
      </button>
    </div>
  );
}

function StatsInfo() {
  return (
    <div className="stats-info">
      <p>Stats generated using methods:</p>
      <ul className="stats-info-list">
        <li>Most stats: Rolled 15-90 (scaled percentile)</li>
        <li>Size: Rolled using CoC formula: (2D6+6)*5 (range 40-90)</li>
        <li>Determination Points max = (CON + SIZ) / 5</li>
        <li>Magic Points max = 20% of Power (ceiling rounded)</li>
      </ul>
      <p>You can reroll as many times as you like, with a 1-second cooldown between rolls.</p>
    </div>
  );
}

export const StatsRollingScreen: React.FC<StatsRollingScreenProps> = props => {
  const { onStatsAccepted, onError, onBack, baseUrl, authToken, professionId, profession } = props;
  const {
    currentStats,
    isLoading,
    isRerolling,
    error,
    setError,
    rerollCooldown,
    timeoutMessage,
    rollStats,
    rerollStats,
  } = useStatsRolling({
    baseUrl,
    authToken,
    professionId,
    profession,
    onError,
    rollOnMount: true,
  });

  const handleAcceptStats = () => {
    if (!currentStats) {
      setError('No stats to accept');
      return;
    }
    setError('');
    logger.info('StatsRollingScreen', 'Stats accepted', { hasStats: true });
    onStatsAccepted(currentStats);
  };

  if (isLoading && !currentStats) {
    return (
      <div className="stats-rolling-screen" data-testid="stats-rolling-screen">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Rolling your starting stats...</p>
        </div>
      </div>
    );
  }

  if (!currentStats) {
    return (
      <div className="stats-rolling-screen" data-testid="stats-rolling-screen">
        <div className="error-container">
          <p>Unable to load stats. Please try again.</p>
          {error && (
            <p className="error-message" role="alert" aria-live="assertive">
              {error}
            </p>
          )}
          <button onClick={rollStats} className="retry-button" type="button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="stats-rolling-screen" data-testid="stats-rolling-screen">
      <div className="stats-header">
        <h2>Character Creation</h2>
        {profession && (
          <div className="profession-display">
            <p className="profession-name">Profession: {profession.name}</p>
            <p className="profession-description">{profession.description}</p>
          </div>
        )}
        {timeoutMessage && (
          <div className="timeout-message">
            <p className="timeout-text">{timeoutMessage}</p>
          </div>
        )}
      </div>
      <StatsGrid stats={currentStats} />
      {error && (
        <div className="error-message" role="alert" aria-live="assertive">
          {error}
        </div>
      )}
      <StatsActions
        onBack={onBack}
        onReroll={rerollStats}
        onAccept={handleAcceptStats}
        rerollCooldown={rerollCooldown}
        isRerolling={isRerolling}
        isLoading={isLoading}
      />
      <StatsInfo />
    </div>
  );
};
