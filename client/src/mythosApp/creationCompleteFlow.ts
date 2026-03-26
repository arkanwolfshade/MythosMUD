import { assertServerCharacterResponseArray, type ServerCharacterResponse } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import type { CharacterInfo } from '../types/auth.js';
import { API_V1_BASE } from '../utils/config.js';
import { isObject } from './guards.js';
import { isServerUnavailable } from './serverAvailability.js';
import { toCharacterInfoFromList } from './mapServerCharacters.js';

export type CreationRefreshResult =
  | { outcome: 'ok'; characters: CharacterInfo[] }
  | { outcome: 'server_unavailable' }
  | { outcome: 'http_error'; response: Response }
  | { outcome: 'network_error'; error: unknown };

export async function refreshCharactersAfterCreation(authToken: string): Promise<CreationRefreshResult> {
  try {
    const response = await fetch(`${API_V1_BASE}/api/players/characters`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authToken}`,
      },
    });

    if (response.ok) {
      const rawData: unknown = await response.json();
      const charactersList = assertServerCharacterResponseArray(
        rawData,
        'Invalid API response: expected ServerCharacterResponse[]'
      );
      const mappedCharacters = charactersList.map((c: ServerCharacterResponse) => toCharacterInfoFromList(c));
      return { outcome: 'ok', characters: mappedCharacters };
    }

    if (isServerUnavailable(null, response)) {
      return { outcome: 'server_unavailable' };
    }

    return { outcome: 'http_error', response };
  } catch (error) {
    if (isServerUnavailable(error, null)) {
      return { outcome: 'server_unavailable' };
    }
    return { outcome: 'network_error', error };
  }
}

export function messageFromCreationRefreshHttpError(response: Response): Promise<string> {
  const fallback = 'Character created, but failed to refresh character list';
  return (async () => {
    try {
      const rawData: unknown = await response.json();
      if (isErrorResponse(rawData)) {
        return getErrorMessage(rawData);
      }
      if (isObject(rawData)) {
        const errorData = rawData as Record<string, unknown>;
        return typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
          ? String((errorData.detail as Record<string, unknown>).message)
          : typeof errorData.detail === 'string'
            ? errorData.detail
            : fallback;
      }
    } catch {
      // ignore
    }
    return fallback;
  })();
}
