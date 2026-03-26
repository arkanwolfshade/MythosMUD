import { assertServerCharacterResponseArray, type ServerCharacterResponse } from '../utils/apiTypeGuards.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import type { CharacterInfo } from '../types/auth.js';
import { API_V1_BASE } from '../utils/config.js';
import { errorMessageFromApiBody } from './apiErrorMessage.js';
import { isObject } from './guards.js';
import { isServerUnavailable } from './serverAvailability.js';
import { toCharacterInfoFromList } from './mapServerCharacters.js';
import { requestDeleteCharacter } from './characterSessionApi.js';

export type DeleteCharacterFlowResult =
  | { outcome: 'ok'; characters: CharacterInfo[] }
  | { outcome: 'server_unavailable' }
  | { outcome: 'delete_failed'; message: string }
  | { outcome: 'refresh_failed'; message: string; deleteStatus: number; deleteStatusText: string };

export async function runDeleteCharacterFlow(
  authToken: string,
  characterId: string
): Promise<DeleteCharacterFlowResult> {
  const response = await requestDeleteCharacter(API_V1_BASE, authToken, characterId);

  if (!response.ok) {
    if (isServerUnavailable(null, response)) {
      return { outcome: 'server_unavailable' };
    }
    const fallback = 'Failed to delete character';
    let errorMessage = fallback;
    try {
      const rawData: unknown = await response.json();
      errorMessage = errorMessageFromApiBody(rawData, fallback);
    } catch {
      // use default
    }
    return { outcome: 'delete_failed', message: errorMessage };
  }

  const charactersResponse = await fetch(`${API_V1_BASE}/api/players/characters`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${authToken}`,
    },
  });

  if (charactersResponse.ok) {
    const rawData: unknown = await charactersResponse.json();
    const charactersList = assertServerCharacterResponseArray(
      rawData,
      'Invalid API response: expected ServerCharacterResponse[]'
    );
    const mappedCharacters = charactersList.map((c: ServerCharacterResponse) => toCharacterInfoFromList(c));
    return { outcome: 'ok', characters: mappedCharacters };
  }

  if (isServerUnavailable(null, charactersResponse)) {
    return { outcome: 'server_unavailable' };
  }

  let errorMessage = 'Character deleted, but failed to refresh character list';
  try {
    const rawData: unknown = await charactersResponse.json();
    if (isErrorResponse(rawData)) {
      errorMessage = getErrorMessage(rawData);
    } else if (isObject(rawData)) {
      const errorData = rawData as Record<string, unknown>;
      errorMessage =
        typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
          ? String((errorData.detail as Record<string, unknown>).message)
          : typeof errorData.detail === 'string'
            ? errorData.detail
            : errorMessage;
    }
  } catch {
    // default message
  }
  return {
    outcome: 'refresh_failed',
    message: errorMessage,
    deleteStatus: response.status,
    deleteStatusText: response.statusText,
  };
}

export type DeleteCharacterNextStep =
  | { step: 'return_to_login' }
  | { step: 'throw'; message: string }
  | { step: 'throw_refresh'; message: string; deleteStatus: number; deleteStatusText: string }
  | { step: 'commit'; characters: CharacterInfo[] };

export function nextStepForDeleteResult(result: DeleteCharacterFlowResult): DeleteCharacterNextStep {
  if (result.outcome === 'server_unavailable') {
    return { step: 'return_to_login' };
  }
  if (result.outcome === 'delete_failed') {
    return { step: 'throw', message: result.message };
  }
  if (result.outcome === 'refresh_failed') {
    return {
      step: 'throw_refresh',
      message: result.message,
      deleteStatus: result.deleteStatus,
      deleteStatusText: result.deleteStatusText,
    };
  }
  return { step: 'commit', characters: result.characters };
}
