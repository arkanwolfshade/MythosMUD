/**
 * useProfessions: fetches and exposes profession list for character creation.
 * Separates data fetching from ProfessionSelectionScreen (Rule 3: smart/dumb components).
 */

import { useCallback, useEffect, useState } from 'react';
import { assertProfessionArray } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';
import type { Profession } from '../components/ProfessionCard.jsx';

const SERVER_UNAVAILABLE_PATTERNS = [
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

export interface UseProfessionsOptions {
  baseUrl: string;
  authToken: string;
  onError?: (error: string) => void;
}

export interface UseProfessionsResult {
  professions: Profession[];
  isLoading: boolean;
  error: string;
  fetchProfessions: () => Promise<void>;
}

export function useProfessions({ baseUrl, authToken, onError }: UseProfessionsOptions): UseProfessionsResult {
  const [professions, setProfessions] = useState<Profession[]>([]);
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

      logger.info('useProfessions', 'Professions loaded successfully', {
        count: professionsArray.length,
        professions: professionsArray.map((p: Profession) => p.name),
      });
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      const errorLower = errorMessage.toLowerCase();

      if (SERVER_UNAVAILABLE_PATTERNS.some(pattern => errorLower.includes(pattern))) {
        const unavailableMessage = 'Server is unavailable. Please try again later.';
        onError?.(unavailableMessage);
        setError(unavailableMessage);
        return;
      }

      setError(errorMessage);
      onError?.(`Failed to load professions: ${errorMessage}`);
      logger.error('useProfessions', 'Failed to load professions', { error: errorMessage });
    } finally {
      setIsLoading(false);
    }
  }, [baseUrl, authToken, onError]);

  useEffect(() => {
    void fetchProfessions();
  }, [fetchProfessions]);

  return { professions, isLoading, error, fetchProfessions };
}
