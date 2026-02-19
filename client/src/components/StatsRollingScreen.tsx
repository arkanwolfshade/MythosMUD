import React from 'react';
import { useStatsRolling, type Stats } from '../hooks/useStatsRolling.js';
import { logger } from '../utils/logger.js';
import type { Profession } from './ProfessionCard.jsx';
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

export const StatsRollingScreen: React.FC<StatsRollingScreenProps> = ({
  onStatsAccepted,
  onError,
  onBack,
  baseUrl,
  authToken,
  professionId,
  profession,
}) => {
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
          <p>Rolling your character's stats...</p>
        </div>
      </div>
    );
  }

  if (!currentStats) {
    return (
      <div className="stats-rolling-screen" data-testid="stats-rolling-screen">
        <div className="error-container">
          <p>Failed to load stats. Please try again.</p>
          {error && <p className="error-message">{error}</p>}
          <button onClick={rollStats} className="retry-button">
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

      <div className="stats-display">
        <h3>Your Character's Stats</h3>
        <div className="stats-grid">
          <div className="stat-item">
            <label>Strength:</label>
            <span className="stat-value">{currentStats.strength}</span>
          </div>
          <div className="stat-item">
            <label>Dexterity:</label>
            <span className="stat-value">{currentStats.dexterity}</span>
          </div>
          <div className="stat-item">
            <label>Constitution:</label>
            <span className="stat-value">{currentStats.constitution}</span>
          </div>
          <div className="stat-item">
            <label>Size:</label>
            <span className="stat-value">{currentStats.size}</span>
          </div>
          <div className="stat-item">
            <label>Intelligence:</label>
            <span className="stat-value">{currentStats.intelligence}</span>
          </div>
          <div className="stat-item">
            <label>Power:</label>
            <span className="stat-value">{currentStats.power}</span>
          </div>
          <div className="stat-item">
            <label>Education:</label>
            <span className="stat-value">{currentStats.education}</span>
          </div>
          <div className="stat-item">
            <label>Charisma:</label>
            <span className="stat-value">{currentStats.charisma}</span>
          </div>
          <div className="stat-item">
            <label>Luck:</label>
            <span className="stat-value">{currentStats.luck}</span>
          </div>
        </div>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="stats-actions">
        {onBack && (
          <button onClick={onBack} className="back-button">
            Back
          </button>
        )}

        <button
          onClick={rerollStats}
          disabled={rerollCooldown > 0 || isRerolling || isLoading}
          className="reroll-button"
        >
          {isRerolling ? 'Rerolling...' : rerollCooldown > 0 ? `Reroll (${rerollCooldown}s)` : 'Reroll Stats'}
        </button>

        <button onClick={handleAcceptStats} className="accept-button">
          Accept Stats
        </button>
      </div>

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
    </div>
  );
};
