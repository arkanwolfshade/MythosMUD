import { useEffect } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import { assertStatsRollResponse } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import type { Stats } from './useStatsRolling';

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

const PROFESSION_TIMEOUT_MESSAGE =
  "The cosmic forces resist your chosen path. The eldritch energies have failed to align with your profession's requirements within the allotted time. You must manually reroll to find stats worthy of your chosen calling.";

function parseRetryAfter(rawData: unknown): number {
  let retryAfter = 60;
  try {
    if (typeof rawData === 'object' && rawData !== null) {
      const errorData = rawData as Record<string, unknown>;
      if (typeof errorData.detail === 'object' && errorData.detail !== null && 'retry_after' in errorData.detail) {
        const detail = errorData.detail as Record<string, unknown>;
        const retryAfterValue = detail.retry_after;
        retryAfter = typeof retryAfterValue === 'number' ? retryAfterValue : 60;
      }
    }
  } catch {
    // use default
  }
  return retryAfter;
}

function messageFromDetail(detail: unknown): string | null {
  if (typeof detail === 'string') return detail;
  if (typeof detail !== 'object' || detail === null || !('message' in detail)) return null;
  return String((detail as Record<string, unknown>).message);
}

function parseErrorMessage(rawData: unknown, defaultMessage: string): string {
  try {
    if (isErrorResponse(rawData)) return getErrorMessage(rawData);
    if (typeof rawData !== 'object' || rawData === null) return defaultMessage;
    return messageFromDetail((rawData as Record<string, unknown>).detail) ?? defaultMessage;
  } catch {
    return defaultMessage;
  }
}

function handleNetworkError(
  errorMessage: string,
  onError: ((msg: string) => void) | undefined,
  setError: (msg: string) => void,
  logContext: string
): void {
  const errorLower = errorMessage.toLowerCase();
  if (SERVER_UNAVAILABLE_PATTERNS.some(pattern => errorLower.includes(pattern))) {
    const msg = 'Server is unavailable. Please try again later.';
    setError(msg);
    onError?.(msg);
    logger.error('useStatsRolling', logContext, { error: errorMessage });
  } else {
    const msg = 'Failed to connect to server';
    setError(msg);
    onError?.(msg);
    logger.error('useStatsRolling', logContext, { error: errorMessage });
  }
}

interface PerformStatsRollParams {
  isReroll: boolean;
  baseUrl: string;
  authToken: string;
  professionId?: number;
  profession?: Profession | null;
  onError?: (error: string) => void;
  setCurrentStats: (stats: Stats) => void;
  setIsLoading: (loading: boolean) => void;
  setIsRerolling: (rerolling: boolean) => void;
  setRerollCooldown: (seconds: number) => void;
  setErrorState: (error: string) => void;
  setTimeoutMessage: (message: string) => void;
}

async function applyOkStatsRoll(response: Response, params: PerformStatsRollParams): Promise<void> {
  const { isReroll, profession, setCurrentStats, setTimeoutMessage } = params;
  const data = assertStatsRollResponse(
    await response.json(),
    isReroll ? 'Invalid stats reroll response from server' : 'Invalid stats roll response from server'
  );
  setCurrentStats(data.stats);
  const showTimeout = !isReroll && data.meets_requirements === false && Boolean(profession);
  setTimeoutMessage(showTimeout ? PROFESSION_TIMEOUT_MESSAGE : '');
  logger.info('useStatsRolling', isReroll ? 'Stats rerolled successfully' : 'Stats rolled successfully', {
    stats: data.stats,
    meets_requirements: data.meets_requirements,
  });
}

async function applyFailedStatsRoll(response: Response, params: PerformStatsRollParams): Promise<void> {
  const { isReroll, onError, setRerollCooldown, setErrorState } = params;
  if (response.status >= 500 && response.status < 600) {
    const msg = 'Server is unavailable. Please try again later.';
    setErrorState(msg);
    onError?.(msg);
    logger.error('useStatsRolling', 'Server unavailable when rolling stats', { status: response.status });
    return;
  }
  const rawData: unknown = await response.json();
  if (response.status === 429) {
    const retryAfter = parseRetryAfter(rawData);
    setErrorState(`Rate limit exceeded. Please wait ${retryAfter} seconds before trying again.`);
    setRerollCooldown(retryAfter);
    return;
  }
  const errorMessage = parseErrorMessage(rawData, isReroll ? 'Failed to reroll stats' : 'Failed to roll stats');
  setErrorState(errorMessage);
  logger.error('useStatsRolling', isReroll ? 'Failed to reroll stats' : 'Failed to roll stats', {
    error: errorMessage,
  });
}

async function handleStatsRollResponse(response: Response, params: PerformStatsRollParams): Promise<void> {
  if (response.ok) {
    await applyOkStatsRoll(response, params);
    return;
  }
  await applyFailedStatsRoll(response, params);
}

export async function performStatsRoll(params: PerformStatsRollParams): Promise<void> {
  const { isReroll, baseUrl, authToken, professionId, onError, setIsLoading, setIsRerolling, setErrorState } = params;
  if (isReroll) {
    setIsRerolling(true);
    params.setRerollCooldown(1);
  } else {
    setIsLoading(true);
  }
  setErrorState('');

  try {
    const response = await fetch(`${baseUrl}/api/players/roll-stats`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({ method: '3d6', profession_id: professionId }),
    });
    await handleStatsRollResponse(response, params);
  } catch (err) {
    const errorMessage = err instanceof Error ? err.message : String(err);
    handleNetworkError(
      errorMessage,
      onError,
      setErrorState,
      isReroll ? 'Network error rerolling stats' : 'Network error rolling stats'
    );
  } finally {
    setIsLoading(false);
    setIsRerolling(false);
  }
}

export function useRerollCooldownTimer(
  rerollCooldown: number,
  setRerollCooldown: (value: number | ((prev: number) => number)) => void
): void {
  useEffect(() => {
    if (rerollCooldown <= 0) return;
    const timer = setTimeout(() => setRerollCooldown(prev => prev - 1), 1000);
    return () => clearTimeout(timer);
  }, [rerollCooldown, setRerollCooldown]);
}
