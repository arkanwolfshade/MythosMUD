import React, { useCallback, useEffect, useState } from 'react';
import { assertStatsRollResponse } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import type { Profession } from './ProfessionCard.jsx';
import './StatsRollingScreen.css';

interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  size: number;
  intelligence: number;
  power: number;
  education: number;
  charisma: number;
  luck: number;
}

interface StatsRollingScreenProps {
  characterName?: string; // MULTI-CHARACTER: Made optional - character name is now entered by user
  onStatsAccepted: (stats: Stats, characterName: string) => void;
  onError: (error: string) => void;
  onBack?: () => void;
  baseUrl: string;
  authToken: string;
  professionId?: number;
  profession?: Profession;
}

export const StatsRollingScreen: React.FC<StatsRollingScreenProps> = ({
  characterName: initialCharacterName,
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
  // MULTI-CHARACTER: Character name is now entered by user
  const [characterName, setCharacterName] = useState(initialCharacterName || '');

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
        const rawData: unknown = await response.json();
        const data = assertStatsRollResponse(rawData, 'Invalid stats roll response from server');
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
      } else if (response.status >= 500 && response.status < 600) {
        // Server unavailability
        const errorMessage = 'Server is unavailable. Please try again later.';
        setError(errorMessage);
        onError(errorMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when rolling stats', { status: response.status });
      } else if (response.status === 429) {
        // Rate limit exceeded
        let retryAfter = 60;
        try {
          const rawData: unknown = await response.json();
          if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            if (
              typeof errorData.detail === 'object' &&
              errorData.detail !== null &&
              'retry_after' in errorData.detail
            ) {
              const detail = errorData.detail as Record<string, unknown>;
              const retryAfterValue = detail.retry_after;
              retryAfter = typeof retryAfterValue === 'number' ? retryAfterValue : 60;
            }
          }
        } catch {
          // Use default retry after if JSON parsing fails
        }
        setError(`Rate limit exceeded. Please wait ${retryAfter} seconds before trying again.`);
        setRerollCooldown(retryAfter);
      } else {
        let errorMessage = 'Failed to roll stats';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to roll stats', { error: errorMessage });
      }
    } catch (error) {
      // Check if error indicates server unavailability
      const errorMessage = error instanceof Error ? error.message : String(error);
      const errorLower = errorMessage.toLowerCase();
      const serverUnavailablePatterns = [
        'failed to fetch',
        'network error',
        'network request failed',
        'connection refused',
        'connection reset',
        'connection closed',
        'connection timeout',
        'server is unavailable',
        'service unavailable',
        'bad gateway',
        'gateway timeout',
      ];

      if (serverUnavailablePatterns.some(pattern => errorLower.includes(pattern))) {
        const unavailableMessage = 'Server is unavailable. Please try again later.';
        setError(unavailableMessage);
        onError(unavailableMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when rolling stats', {
          error: errorMessage,
        });
      } else {
        const connectMessage = 'Failed to connect to server';
        setError(connectMessage);
        onError(connectMessage);
        logger.error('StatsRollingScreen', 'Network error rolling stats', {
          error: errorMessage,
        });
      }
    } finally {
      setIsLoading(false);
    }
  }, [authToken, baseUrl, professionId, profession, onError]);

  // Roll initial stats when component mounts and authToken is available
  useEffect(() => {
    if (authToken) {
      void rollStats();
    }
  }, [authToken, rollStats, professionId]);

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
        const rawData: unknown = await response.json();
        const data = assertStatsRollResponse(rawData, 'Invalid stats reroll response from server');
        setCurrentStats(data.stats);
        logger.info('StatsRollingScreen', 'Stats rerolled successfully', { stats: data.stats });
      } else if (response.status >= 500 && response.status < 600) {
        // Server unavailability
        const errorMessage = 'Server is unavailable. Please try again later.';
        setError(errorMessage);
        onError(errorMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when rerolling stats', { status: response.status });
      } else if (response.status === 429) {
        // Rate limit exceeded
        let retryAfter = 60;
        try {
          const rawData: unknown = await response.json();
          if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            if (
              typeof errorData.detail === 'object' &&
              errorData.detail !== null &&
              'retry_after' in errorData.detail
            ) {
              const detail = errorData.detail as Record<string, unknown>;
              const retryAfterValue = detail.retry_after;
              retryAfter = typeof retryAfterValue === 'number' ? retryAfterValue : 60;
            }
          }
        } catch {
          // Use default retry after if JSON parsing fails
        }
        setError(`Rate limit exceeded. Please wait ${retryAfter} seconds before trying again.`);
        setRerollCooldown(retryAfter);
      } else {
        let errorMessage = 'Failed to reroll stats';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to reroll stats', { error: errorMessage });
      }
    } catch (error) {
      // Check if error indicates server unavailability
      const errorMessage = error instanceof Error ? error.message : String(error);
      const errorLower = errorMessage.toLowerCase();
      const serverUnavailablePatterns = [
        'failed to fetch',
        'network error',
        'network request failed',
        'connection refused',
        'connection reset',
        'connection closed',
        'connection timeout',
        'server is unavailable',
        'service unavailable',
        'bad gateway',
        'gateway timeout',
      ];

      if (serverUnavailablePatterns.some(pattern => errorLower.includes(pattern))) {
        const unavailableMessage = 'Server is unavailable. Please try again later.';
        setError(unavailableMessage);
        onError(unavailableMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when rerolling stats', {
          error: errorMessage,
        });
      } else {
        const connectMessage = 'Failed to connect to server';
        setError(connectMessage);
        onError(connectMessage);
        logger.error('StatsRollingScreen', 'Network error rerolling stats', {
          error: errorMessage,
        });
      }
    } finally {
      setIsRerolling(false);
    }
  };

  const handleAcceptStats = async () => {
    if (!currentStats) {
      setError('No stats to accept');
      return;
    }

    // Validate character name
    const trimmedName = characterName.trim();
    if (!trimmedName) {
      setError('Please enter a character name');
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
          name: trimmedName,
          stats: currentStats,
          profession_id: professionId || 0, // Include profession_id, default to 0 (Tramp)
        }),
      });

      if (response.ok) {
        const rawData: unknown = await response.json();
        // Character creation response may be a simple success response or character data
        // Extract player ID safely
        let playerId: string | undefined;
        if (typeof rawData === 'object' && rawData !== null) {
          const data = rawData as Record<string, unknown>;
          playerId =
            (typeof data.id === 'string' ? data.id : null) ||
            (typeof data.player_id === 'string' ? data.player_id : undefined);
        }
        logger.info('StatsRollingScreen', 'Character created successfully', {
          characterName: trimmedName,
          playerId: playerId || 'unknown',
        });
        onStatsAccepted(currentStats, trimmedName);
      } else if (response.status >= 500 && response.status < 600) {
        // Server unavailability
        const errorMessage = 'Server is unavailable. Please try again later.';
        setError(errorMessage);
        onError(errorMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when creating character', { status: response.status });
      } else {
        let errorMessage = 'Failed to create character';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            // Handle different error response formats
            if (errorData.detail) {
              if (Array.isArray(errorData.detail)) {
                // FastAPI validation errors - array of error objects
                errorMessage = (errorData.detail as Array<Record<string, unknown>>)
                  .map((err: Record<string, unknown>) =>
                    typeof err.msg === 'string'
                      ? err.msg
                      : typeof err.message === 'string'
                        ? err.message
                        : 'Validation error'
                  )
                  .join(', ');
              } else if (typeof errorData.detail === 'object' && errorData.detail !== null) {
                const detail = errorData.detail as Record<string, unknown>;
                errorMessage = typeof detail.message === 'string' ? detail.message : 'Validation error';
              } else if (typeof errorData.detail === 'string') {
                errorMessage = errorData.detail;
              }
            }
          }
        } catch {
          // Use default error message if JSON parsing fails
        }

        setError(errorMessage);
        logger.error('StatsRollingScreen', 'Failed to create character', { error: errorMessage });
      }
    } catch (error) {
      // Check if error indicates server unavailability
      const errorMessage = error instanceof Error ? error.message : String(error);
      const errorLower = errorMessage.toLowerCase();
      const serverUnavailablePatterns = [
        'failed to fetch',
        'network error',
        'network request failed',
        'connection refused',
        'connection reset',
        'connection closed',
        'connection timeout',
        'server is unavailable',
        'service unavailable',
        'bad gateway',
        'gateway timeout',
      ];

      if (serverUnavailablePatterns.some(pattern => errorLower.includes(pattern))) {
        const unavailableMessage = 'Server is unavailable. Please try again later.';
        setError(unavailableMessage);
        onError(unavailableMessage);
        logger.error('StatsRollingScreen', 'Server unavailable when creating character', {
          error: errorMessage,
        });
      } else {
        const connectMessage = 'Failed to connect to server';
        setError(connectMessage);
        onError(connectMessage);
        logger.error('StatsRollingScreen', 'Network error creating character', {
          error: errorMessage,
        });
      }
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
        {/* MULTI-CHARACTER: Character name input field */}
        <div className="character-name-input-container">
          <label htmlFor="character-name-input" className="character-name-label">
            Character Name:
          </label>
          <input
            id="character-name-input"
            type="text"
            value={characterName}
            onChange={e => {
              setCharacterName(e.target.value);
            }}
            placeholder="Enter your character's name"
            maxLength={50}
            minLength={1}
            className="character-name-input"
            disabled={isLoading}
          />
          {characterName.trim() && <p className="character-name-preview">Preview: {characterName.trim()}</p>}
        </div>
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
