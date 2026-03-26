import { API_V1_BASE } from '../utils/config.js';
import { errorMessageFromApiBody } from './apiErrorMessage.js';
import { isServerUnavailable } from './serverAvailability.js';
import { parseSelectCharacterResult, postSelectCharacter } from './characterSessionApi.js';

export type SelectCharacterResult =
  | { outcome: 'ok'; selectedId: string; selectedName: string }
  | { outcome: 'server_unavailable' }
  | { outcome: 'error'; message: string }
  | { outcome: 'network_error'; error: unknown };

export async function runSelectCharacterFlow(authToken: string, characterId: string): Promise<SelectCharacterResult> {
  try {
    const response = await postSelectCharacter(API_V1_BASE, authToken, characterId);

    if (!response.ok) {
      if (isServerUnavailable(null, response)) {
        return { outcome: 'server_unavailable' };
      }
      const fallback = 'Failed to select character';
      let errorMessage = fallback;
      try {
        const rawData: unknown = await response.json();
        errorMessage = errorMessageFromApiBody(rawData, fallback);
      } catch {
        // default
      }
      return { outcome: 'error', message: errorMessage };
    }

    const rawData: unknown = await response.json();
    const { selectedId, selectedName } = parseSelectCharacterResult(rawData, characterId);
    return { outcome: 'ok', selectedId, selectedName };
  } catch (error) {
    if (isServerUnavailable(error, null)) {
      return { outcome: 'server_unavailable' };
    }
    return { outcome: 'network_error', error };
  }
}

export function selectCharacterNetworkErrorMessage(error: unknown): string {
  return error instanceof Error ? error.message : 'Failed to select character';
}
