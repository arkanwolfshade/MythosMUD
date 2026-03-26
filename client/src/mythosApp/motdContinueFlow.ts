import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { isObject } from './guards.js';
import { isServerUnavailable, errorDetailString } from './serverAvailability.js';
import { postStartLoginGracePeriod } from './startLoginGracePeriod.js';

export async function tryStartLoginGracePeriod(authToken: string, selectedCharacterId: string): Promise<void> {
  const response = await postStartLoginGracePeriod(authToken, selectedCharacterId);

  if (!response.ok) {
    if (isServerUnavailable(null, response)) {
      throw new Error('__SERVER_UNAVAILABLE__');
    }

    try {
      const rawData: unknown = await response.json();
      if (isErrorResponse(rawData)) {
        console.warn('Failed to start login grace period:', getErrorMessage(rawData));
      } else if (isObject(rawData)) {
        const errorData = rawData as Record<string, unknown>;
        const detail = errorDetailString(errorData);
        console.warn('Failed to start login grace period:', detail);
      } else {
        console.warn('Failed to start login grace period: Unknown error');
      }
    } catch {
      console.warn('Failed to start login grace period: Unknown error');
    }
  }
}

export function isGracePeriodServerUnavailableError(e: unknown): boolean {
  return e instanceof Error && e.message === '__SERVER_UNAVAILABLE__';
}
