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
  | { outcome: 'refresh_failed'; message: string; characterId: string };

async function fetchCharacterList(authToken: string): Promise<Response> {
  return fetch(`${API_V1_BASE}/api/players/characters`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${authToken}`,
    },
  });
}

function mapCharactersResponse(rawData: unknown): CharacterInfo[] {
  const charactersList = assertServerCharacterResponseArray(
    rawData,
    'Invalid API response: expected ServerCharacterResponse[]'
  );
  return charactersList.map((c: ServerCharacterResponse) => toCharacterInfoFromList(c));
}

async function parseDeleteFailure(response: Response): Promise<string> {
  const fallback = 'Failed to delete character';
  try {
    const rawData: unknown = await response.json();
    return errorMessageFromApiBody(rawData, fallback);
  } catch {
    return fallback;
  }
}

async function parseRefreshFailure(charactersResponse: Response): Promise<string> {
  const errorMessage = 'Character deleted, but failed to refresh character list';
  try {
    const rawData: unknown = await charactersResponse.json();
    if (isErrorResponse(rawData)) {
      return getErrorMessage(rawData);
    }
    if (isObject(rawData)) {
      const errorData = rawData as Record<string, unknown>;
      if (typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail) {
        return String((errorData.detail as Record<string, unknown>).message);
      }
      if (typeof errorData.detail === 'string') {
        return errorData.detail;
      }
    }
  } catch {
    // default message
  }
  return errorMessage;
}

export async function runDeleteCharacterFlow(
  authToken: string,
  characterId: string
): Promise<DeleteCharacterFlowResult> {
  const response = await requestDeleteCharacter(API_V1_BASE, authToken, characterId);

  if (!response.ok) {
    if (isServerUnavailable(null, response)) {
      return { outcome: 'server_unavailable' };
    }
    return { outcome: 'delete_failed', message: await parseDeleteFailure(response) };
  }

  const charactersResponse = await fetchCharacterList(authToken);

  if (charactersResponse.ok) {
    const rawData: unknown = await charactersResponse.json();
    return { outcome: 'ok', characters: mapCharactersResponse(rawData) };
  }

  if (isServerUnavailable(null, charactersResponse)) {
    return { outcome: 'server_unavailable' };
  }

  // The DELETE already succeeded (response.ok above) -- the server has confirmed this
  // character is gone. A failed refetch of the list is a secondary read failure, not
  // evidence the delete didn't happen, so the caller removes it locally (#777 follow-up:
  // this used to leave the deleted character's card stranded in the UI forever whenever
  // this refetch hiccuped).
  return {
    outcome: 'refresh_failed',
    message: await parseRefreshFailure(charactersResponse),
    characterId,
  };
}

export type DeleteCharacterNextStep =
  | { step: 'return_to_login' }
  | { step: 'throw'; message: string }
  | { step: 'commit_remove_locally'; characterId: string; message: string }
  | { step: 'commit'; characters: CharacterInfo[] };

export function nextStepForDeleteResult(result: DeleteCharacterFlowResult): DeleteCharacterNextStep {
  if (result.outcome === 'server_unavailable') {
    return { step: 'return_to_login' };
  }
  if (result.outcome === 'delete_failed') {
    return { step: 'throw', message: result.message };
  }
  if (result.outcome === 'refresh_failed') {
    return { step: 'commit_remove_locally', characterId: result.characterId, message: result.message };
  }
  return { step: 'commit', characters: result.characters };
}
