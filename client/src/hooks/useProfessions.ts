/**
 * useProfessions: fetches and exposes profession list for character creation.
 * Separates data fetching from ProfessionSelectionScreen (Rule 3: smart/dumb components).
 */

import { useCallback, useEffect, useRef, useState, type MutableRefObject } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import { assertProfessionArray } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

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

function parseDetailMessage(errorData: Record<string, unknown>): string | null {
  if (Array.isArray(errorData.detail)) {
    return (errorData.detail as Array<Record<string, unknown>>)
      .map(err =>
        typeof err.msg === 'string' ? err.msg : typeof err.message === 'string' ? err.message : 'Validation error'
      )
      .join(', ');
  }
  if (typeof errorData.detail === 'object' && errorData.detail !== null) {
    const detail = errorData.detail as Record<string, unknown>;
    return typeof detail.message === 'string' ? detail.message : 'Validation error';
  }
  if (typeof errorData.detail === 'string') {
    return errorData.detail;
  }
  return null;
}

async function parseProfessionsErrorResponse(response: Response): Promise<string> {
  if (response.status >= 500 && response.status < 600) {
    throw new Error('Server is unavailable. Please try again later.');
  }

  const errorMessage = 'Failed to load professions';
  try {
    const rawData: unknown = await response.json();
    if (isErrorResponse(rawData)) {
      return getErrorMessage(rawData);
    }
    if (typeof rawData === 'object' && rawData !== null) {
      const parsed = parseDetailMessage(rawData as Record<string, unknown>);
      if (parsed) return parsed;
    }
  } catch {
    // Use default error message if JSON parsing fails
  }
  return errorMessage;
}

function parseProfessionsBody(rawData: unknown): Profession[] {
  if (Array.isArray(rawData)) {
    return assertProfessionArray(rawData, 'Invalid API response: expected Profession[]');
  }
  if (typeof rawData === 'object' && rawData !== null && 'professions' in rawData) {
    const data = rawData as { professions: unknown };
    return assertProfessionArray(data.professions, 'Invalid API response: expected professions array');
  }
  throw new Error('Invalid API response: expected Profession[] or { professions: Profession[] }');
}

function handleProfessionsFetchError(
  err: unknown,
  onErrorRef: MutableRefObject<UseProfessionsOptions['onError']>,
  setError: (message: string) => void
): void {
  const errorMessage = err instanceof Error ? err.message : 'Unknown error';
  const errorLower = errorMessage.toLowerCase();

  if (SERVER_UNAVAILABLE_PATTERNS.some(pattern => errorLower.includes(pattern))) {
    const unavailableMessage = 'Server is unavailable. Please try again later.';
    onErrorRef.current?.(unavailableMessage);
    setError(unavailableMessage);
    return;
  }

  setError(errorMessage);
  onErrorRef.current?.(`Failed to load professions: ${errorMessage}`);
  logger.error('useProfessions', 'Failed to load professions', { error: errorMessage });
}

async function loadProfessions(
  baseUrl: string,
  authToken: string,
  onErrorRef: MutableRefObject<UseProfessionsOptions['onError']>,
  setProfessions: (professions: Profession[]) => void,
  setIsLoading: (loading: boolean) => void,
  setError: (message: string) => void
): Promise<void> {
  try {
    setIsLoading(true);
    setError('');

    const storageToken = secureTokenStorage.getToken();
    const tokenToUse = authToken || storageToken || '';
    const response = await fetch(`${baseUrl}/professions`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${tokenToUse}`,
      },
    });

    if (!response.ok) {
      throw new Error(await parseProfessionsErrorResponse(response));
    }

    const rawData: unknown = await response.json();
    const professionsArray = parseProfessionsBody(rawData);
    setProfessions(professionsArray);
    logger.info('useProfessions', 'Professions loaded successfully', {
      count: professionsArray.length,
      professions: professionsArray.map((p: Profession) => p.name),
    });
  } catch (err) {
    handleProfessionsFetchError(err, onErrorRef, setError);
  } finally {
    setIsLoading(false);
  }
}

export function useProfessions(options: UseProfessionsOptions): UseProfessionsResult {
  const { baseUrl, authToken, onError } = options;
  const [professions, setProfessions] = useState<Profession[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  const onErrorRef = useRef<UseProfessionsOptions['onError']>(onError);

  useEffect(() => {
    onErrorRef.current = onError;
  }, [onError]);

  const fetchProfessions = useCallback(
    () => loadProfessions(baseUrl, authToken, onErrorRef, setProfessions, setIsLoading, setError),
    [baseUrl, authToken]
  );

  useEffect(() => {
    void fetchProfessions();
  }, [fetchProfessions]);

  return { professions, isLoading, error, fetchProfessions };
}
