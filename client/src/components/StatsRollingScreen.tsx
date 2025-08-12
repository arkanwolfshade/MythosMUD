import React, { useEffect, useState } from 'react';
import { logger } from '../utils/logger';
import './StatsRollingScreen.css';

interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
}

interface StatsRollingScreenProps {
  characterName: string;
  onStatsAccepted: (stats: Stats) => void;
  onError: (error: string) => void;
  baseUrl: string;
  authToken: string;
}

export const StatsRollingScreen: React.FC<StatsRollingScreenProps> = ({
  characterName,
  onStatsAccepted,
  onError,
  baseUrl,
  authToken,
}) => {
  const [currentStats, setCurrentStats] = useState<Stats | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isRerolling, setIsRerolling] = useState(false);
  const [rerollCooldown, setRerollCooldown] = useState(0);
  const [error, setError] = useState('');

  // Roll initial stats when component mounts and authToken is available
  useEffect(() => {
    if (authToken) {
      rollStats();
    }
  }, [authToken]); // eslint-disable-line react-hooks/exhaustive-deps

  // Handle reroll cooldown
  useEffect(() => {
    if (rerollCooldown > 0) {
      const timer = setTimeout(() => {
        setRerollCooldown(rerollCooldown - 1);
      }, 1000);
      return () => clearTimeout(timer);
    }
  }, [rerollCooldown]);

  const rollStats = async () => {
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch(`${baseUrl}/players/roll-stats`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          method: '3d6',
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setCurrentStats(data.stats);
        logger.info('StatsRollingScreen', 'Stats rolled successfully', { stats: data.stats });
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
  };

  const handleReroll = async () => {
    if (rerollCooldown > 0) {
      return; // Still in cooldown
    }

    setIsRerolling(true);
    setRerollCooldown(1); // 1 second cooldown

    try {
      const response = await fetch(`${baseUrl}/players/roll-stats`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          method: '3d6',
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

    setIsLoading(true);
    setError('');

    try {
      const response = await fetch(`${baseUrl}/players/create-character`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          name: characterName, // This is the username from registration
          stats: currentStats,
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
      <div className="stats-rolling-screen">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Rolling your character's stats...</p>
        </div>
      </div>
    );
  }

  if (!currentStats) {
    return (
      <div className="stats-rolling-screen">
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
    <div className="stats-rolling-screen">
      <div className="stats-header">
        <h2>Character Creation</h2>
        <p className="character-name">Character: {characterName}</p>
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
            <label>Intelligence:</label>
            <span className="stat-value">{currentStats.intelligence}</span>
          </div>
          <div className="stat-item">
            <label>Wisdom:</label>
            <span className="stat-value">{currentStats.wisdom}</span>
          </div>
          <div className="stat-item">
            <label>Charisma:</label>
            <span className="stat-value">{currentStats.charisma}</span>
          </div>
        </div>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="stats-actions">
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
        <p>These stats were generated using the 3d6 method.</p>
        <p>You can reroll as many times as you like, with a 1-second cooldown between rolls.</p>
      </div>
    </div>
  );
};
