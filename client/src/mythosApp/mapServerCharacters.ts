import type { ServerCharacterResponse } from '../utils/apiTypeGuards.js';
import type { CharacterInfo } from '../types/auth.js';

export function toCharacterInfoFromList(c: ServerCharacterResponse): CharacterInfo {
  return {
    player_id: c.player_id || c.id || '',
    name: c.name,
    profession_id: c.profession_id,
    profession_name: c.profession_name,
    level: c.level,
    created_at: c.created_at,
    last_active: c.last_active,
  };
}

export function toCharacterInfoFromLogin(c: ServerCharacterResponse): CharacterInfo {
  return {
    ...c,
    player_id: c.id || c.player_id || '',
  };
}
