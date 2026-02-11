import React, { useCallback, useEffect, useState } from 'react';
import { assertProfessionArray } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';
import { Profession, ProfessionCard } from './ProfessionCard.jsx';

interface ProfessionSelectionScreenProps {
  characterName?: string; // MULTI-CHARACTER: Made optional - character name is now entered later
  onProfessionSelected: (profession: Profession) => void;
  onError: (error: string) => void;
  onBack: () => void;
  baseUrl: string;
  authToken: string;
}

export const ProfessionSelectionScreen: React.FC<ProfessionSelectionScreenProps> = ({
  characterName,
  onProfessionSelected,
  onError,
  onBack,
  baseUrl,
  authToken,
}) => {
  const [professions, setProfessions] = useState<Profession[]>([]);
  const [selectedProfession, setSelectedProfession] = useState<Profession | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchProfessions = useCallback(async () => {
    try {
      setIsLoading(true);
      setError('');

      const storageToken = secureTokenStorage.getToken();
      const tokenToUse = authToken || storageToken || '';

      const professionsUrl = `${baseUrl}/professions`;

      const response = await fetch(professionsUrl, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${tokenToUse}`,
        },
      });

      if (!response.ok) {
        // Check for server unavailability (5xx errors)
        if (response.status >= 500 && response.status < 600) {
          throw new Error('Server is unavailable. Please try again later.');
        }

        let errorMessage = 'Failed to load professions';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            if (errorData.detail) {
              if (Array.isArray(errorData.detail)) {
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
        throw new Error(errorMessage);
      }

      const rawData: unknown = await response.json();
      // API may return { professions: Profession[] } or Profession[] directly
      let professionsArray: Profession[];
      if (Array.isArray(rawData)) {
        professionsArray = assertProfessionArray(rawData, 'Invalid API response: expected Profession[]');
      } else if (typeof rawData === 'object' && rawData !== null && 'professions' in rawData) {
        const data = rawData as { professions: unknown };
        professionsArray = assertProfessionArray(data.professions, 'Invalid API response: expected professions array');
      } else {
        throw new Error('Invalid API response: expected Profession[] or { professions: Profession[] }');
      }
      setProfessions(professionsArray);

      logger.info('ProfessionSelectionScreen', 'Professions loaded successfully', {
        count: professionsArray.length,
        professions: professionsArray.map((p: Profession) => p.name),
      });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';

      // Check if error indicates server unavailability
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
        // Pass server unavailability error to parent
        onError('Server is unavailable. Please try again later.');
        return;
      }

      setError(errorMessage);
      onError(`Failed to load professions: ${errorMessage}`);

      logger.error('ProfessionSelectionScreen', 'Failed to load professions', { error: errorMessage });
    } finally {
      setIsLoading(false);
    }
  }, [baseUrl, authToken, onError]);

  useEffect(() => {
    void fetchProfessions();
  }, [fetchProfessions]);

  const handleProfessionSelect = (profession: Profession) => {
    setSelectedProfession(profession);
    logger.info('ProfessionSelectionScreen', 'Profession selected', {
      professionId: profession.id,
      professionName: profession.name,
    });
  };

  const handleNext = () => {
    if (selectedProfession) {
      onProfessionSelected(selectedProfession);
    }
  };

  const handleBack = () => {
    onBack();
  };

  if (isLoading) {
    return (
      <div className="profession-selection-screen">
        <div className="loading-container">
          <h2>Loading professions...</h2>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="profession-selection-screen">
        <div className="error-container">
          <h2>Error Loading Professions</h2>
          <p className="error-message">{error}</p>
          <button onClick={fetchProfessions} className="retry-button">
            Retry
          </button>
          <button onClick={handleBack} className="back-button">
            Back
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="profession-selection-screen">
      <div className="profession-selection-container">
        <header className="profession-selection-header">
          <h1>Choose Your Profession</h1>
          {characterName && <p className="character-welcome">Welcome, {characterName}</p>}
          <p className="profession-instructions">
            Select a profession that defines your character's background and abilities. Each profession has different
            stat requirements and will influence your character's development.
          </p>
        </header>

        <div className="professions-grid">
          {professions.map(profession => (
            <ProfessionCard
              key={profession.id}
              profession={profession}
              isSelected={selectedProfession?.id === profession.id}
              onSelect={handleProfessionSelect}
            />
          ))}
        </div>

        <div className="profession-selection-actions">
          <button onClick={handleBack} className="back-button" type="button">
            Back
          </button>

          <button onClick={handleNext} className="next-button" disabled={!selectedProfession} type="button">
            Next
          </button>
        </div>
      </div>
    </div>
  );
};
