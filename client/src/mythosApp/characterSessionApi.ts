import { isServerCharacterResponse, isServerCharacterResponseArray } from '../utils/apiTypeGuards.js';
import type { CharacterInfo } from '../types/auth.js';
import { isObject } from './guards.js';
import { toCharacterInfoFromList } from './mapServerCharacters.js';

function pickString(value: unknown): string | null {
  return typeof value === 'string' ? value : null;
}

function resolveSelectedId(candidateId: unknown, candidatePlayerId: unknown, fallbackId: string): string {
  return pickString(candidateId) ?? pickString(candidatePlayerId) ?? fallbackId;
}

export function parseSelectCharacterResult(
  rawData: unknown,
  characterId: string
): { selectedId: string; selectedName: string } {
  if (isServerCharacterResponse(rawData)) {
    return {
      selectedId: resolveSelectedId(rawData.player_id, rawData.id, characterId),
      selectedName: rawData.name,
    };
  }

  if (isObject(rawData)) {
    return {
      selectedId: resolveSelectedId(rawData.id, rawData.player_id, characterId),
      selectedName: pickString(rawData.name) ?? '',
    };
  }

  return { selectedId: characterId, selectedName: '' };
}

export async function postSelectCharacter(apiBase: string, token: string, characterId: string): Promise<Response> {
  return fetch(`${apiBase}/api/players/select-character`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ character_id: characterId }),
  });
}

export async function requestDeleteCharacter(apiBase: string, token: string, characterId: string): Promise<Response> {
  return fetch(`${apiBase}/api/players/characters/${characterId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });
}

export async function restoreCharactersOnMount(
  apiBase: string,
  token: string
): Promise<CharacterInfo[] | null | 'unauthorized'> {
  const response = await fetch(`${apiBase}/api/players/characters`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });
  if (response.ok) {
    const rawData: unknown = await response.json();
    if (!isServerCharacterResponseArray(rawData)) {
      throw new Error('Invalid API response: expected ServerCharacterResponse[]');
    }
    return rawData.map(toCharacterInfoFromList);
  }
  if (response.status === 401) {
    return 'unauthorized';
  }
  // Other failures: leave session intact (same as previous App.tsx behavior).
  return null;
}
