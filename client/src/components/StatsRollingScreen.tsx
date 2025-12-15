import React, { useCallback, useEffect, useState } from 'react';
import { logger } from '../utils/logger';
import './StatsRollingScreen.css';

interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  size: number;
  intelligence: number;
  power: number;
  education: number;
  wisdom: number;
  charisma: number;
  luck: number;
}

interface Profession {
  id: number;
  name: string;
  description: string;
  flavor_text: string;
  stat_requirements: Record<string, number>;
  mechanical_effects: Record<string, number>;
  is_available: boolean;
}

interface StatsRollingScreenProps {
  characterName: string;
  onStatsAccepted: (stats: Stats) => void;
  onError: (error: string) => void;
  onBack?: () => void;
  baseUrl: string;
  authToken: string;
  professionId?: number;
  profession?: Profession;
}

export const StatsRollingScreen: React.FC<StatsRollingScreenProps> = ({
  characterName,
  onStatsAccepted,
  onError,
  onBack,
  baseUrl,
  authToken,
  professionId,
  profession,
}) => {
  const [currentStats, setCurrentStats] = useState<Stats | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isRerolling, setIsRerolling] = useState(false);
  const [rerollCooldown, setRerollCooldown] = useState(0);
  const [error, setError] = useState('');
  const [timeoutMessage, setTimeoutMessage] = useState('');

  // Roll initial stats when component mounts and authToken is available
  // AI: useCallback ensures rollStats has stable reference and proper dependency tracking
  const rollStats = useCallback(async () => {
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch(`${baseUrl}/api/players/roll-stats`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          method: '3d6',
          profession_id: professionId,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setCurrentStats(data.stats);

        // Handle timeout message for profession requirements
        if (data.meets_requirements === false && profession) {
          setTimeoutMessage(
            "The cosmic forces resist your chosen path. The eldritch energies have failed to align with your profession's requirements within the allotted time. You must manually reroll to find stats worthy of your chosen calling."
          );
        } else {
          setTimeoutMessage('');
        }

        logger.info('StatsRollingScreen', 'Stats rolled successfully', {
          stats: data.stats,
          meets_requirements: data.meets_requirements,
        });
      } else if (response.status === 429) {
        // Rate limit exceeded
        const errorData = await response.json();
        const retryAfter = errorData.detail?.retry_after || 60;
        setError(`Rate limit exceeded. Please wait ${retryAfter} seconds before trying again.`);
        setRerollCooldown(retryAfter);
      } else {
        const errorData = await response.json();
        const errorMessage = errorData.detail?.message || errorData.detail || 'Failed to roll stats';
        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to roll stats', { error: errorMessage });
      }
    } catch (error) {
      const errorMessage = 'Failed to connect to server';
      setError(errorMessage);
      onError(errorMessage);
      logger.error('StatsRollingScreen', 'Network error rolling stats', {
        error: error instanceof Error ? error.message : String(error),
      });
    } finally {
      setIsLoading(false);
    }
  }, [authToken, baseUrl, professionId, profession, onError]);

  // Roll initial stats when component mounts and authToken is available
  useEffect(() => {
    if (authToken) {
      void rollStats();
    }
  }, [authToken, rollStats]);

  // Handle reroll cooldown
  useEffect(() => {
    if (rerollCooldown > 0) {
      const timer = setTimeout(() => {
        setRerollCooldown(rerollCooldown - 1);
      }, 1000);
      return () => {
        clearTimeout(timer);
      };
    }
  }, [rerollCooldown]);

  const handleReroll = async () => {
    if (rerollCooldown > 0) {
      return; // Still in cooldown
    }

    setIsRerolling(true);
    setRerollCooldown(1); // 1 second cooldown

    try {
      const response = await fetch(`${baseUrl}/api/players/roll-stats`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          method: '3d6',
          profession_id: professionId,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setCurrentStats(data.stats);
        logger.info('StatsRollingScreen', 'Stats rerolled successfully', { stats: data.stats });
      } else if (response.status === 429) {
        // Rate limit exceeded
        const errorData = await response.json();
        const retryAfter = errorData.detail?.retry_after || 60;
        setError(`Rate limit exceeded. Please wait ${retryAfter} seconds before trying again.`);
        setRerollCooldown(retryAfter);
      } else {
        const errorData = await response.json();
        const errorMessage = errorData.detail?.message || errorData.detail || 'Failed to reroll stats';
        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to reroll stats', { error: errorMessage });
      }
    } catch (error) {
      const errorMessage = 'Failed to connect to server';
      setError(errorMessage);
      onError(errorMessage);
      logger.error('StatsRollingScreen', 'Network error rerolling stats', {
        error: error instanceof Error ? error.message : String(error),
      });
    } finally {
      setIsRerolling(false);
    }
  };

  const handleAcceptStats = async () => {
    if (!currentStats) {
      setError('No stats to accept');
      return;
    }

    // Note: Even if stats do not meet profession requirements, allow acceptance
    // Tests expect flow to continue to game while UI indicates requirement status

    setIsLoading(true);
    setError('');

    try {
      const response = await fetch(`${baseUrl}/api/players/create-character`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          name: characterName, // This is the username from registration
          stats: currentStats,
          profession_id: professionId || 0, // Include profession_id, default to 0 (Tramp)
        }),
      });

      if (response.ok) {
        const data = await response.json();
        logger.info('StatsRollingScreen', 'Character created successfully', {
          characterName,
          playerId: data.player?.id,
        });
        onStatsAccepted(currentStats);
      } else {
        const errorData = await response.json();
        let errorMessage = 'Failed to create character';

        // Handle different error response formats
        if (errorData.detail) {
          if (Array.isArray(errorData.detail)) {
            // FastAPI validation errors - array of error objects
            errorMessage = errorData.detail
              .map((err: { msg?: string; message?: string }) => err.msg || err.message || 'Validation error')
              .join(', ');
          } else if (typeof errorData.detail === 'string') {
            // Simple string error
            errorMessage = errorData.detail;
          } else if (errorData.detail.message) {
            // Object with message property
            errorMessage = errorData.detail.message;
          }
        } else if (errorData.error?.message) {
          // Custom error format
          errorMessage = errorData.error.message;
        }

        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to create character', { error: errorData });
      }
    } catch (error) {
      const errorMessage = 'Failed to connect to server';
      setError(errorMessage);
      onError(errorMessage);
      logger.error('StatsRollingScreen', 'Network error creating character', {
        error: error instanceof Error ? error.message : String(error),
      });
    } finally {
      setIsLoading(false);
    }
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
        <p className="character-name">Character: {characterName}</p>
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
          onClick={handleReroll}
          disabled={rerollCooldown > 0 || isRerolling || isLoading}
          className="reroll-button"
        >
          {isRerolling ? 'Rerolling...' : rerollCooldown > 0 ? `Reroll (${rerollCooldown}s)` : 'Reroll Stats'}
        </button>

        <button onClick={handleAcceptStats} disabled={isLoading} className="accept-button">
          {isLoading ? 'Creating Character...' : 'Accept Stats & Create Character'}
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
