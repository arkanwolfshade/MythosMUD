/**
 * Status command response parser utility
 *
 * Parses status command responses to extract player data including profession information
 */

export interface ParsedPlayerData {
  name?: string;
  location?: string;
  health?: {
    current: number;
    max: number;
  };
  lucidity?: {
    current: number;
    max: number;
  };
  profession?: {
    name: string;
    description: string;
    flavor_text: string;
  };
  fear?: number;
  corruption?: number;
  occult_knowledge?: number;
  position?: string;
  in_combat?: boolean;
  xp?: number;
}

export interface PlayerWithProfession {
  name: string;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats: {
    current_dp: number;
    max_health: number;
    lucidity: number;
    max_lucidity: number;
    fear: number;
    corruption: number;
    occult_knowledge: number;
    position?: string;
  };
  position?: string;
  in_combat?: boolean;
  xp?: number;
}

/**
 * Parses a status command response string to extract player data
 *
 * @param statusResponse - The raw status command response string
 * @returns ParsedPlayerData object with extracted information
 */
export function parseStatusResponse(statusResponse: string): ParsedPlayerData {
  const lines = statusResponse
    .split('\n')
    .map(line => line.trim())
    .filter(line => line.length > 0);
  const playerData: ParsedPlayerData = {};

  for (const line of lines) {
    // Parse basic info
    if (line.startsWith('Name:')) {
      playerData.name = line.replace('Name:', '').trim();
    } else if (line.startsWith('Location:')) {
      playerData.location = line.replace('Location:', '').trim();
    } else if (line.startsWith('Health:')) {
      const healthStr = line.replace('Health:', '').trim();
      const [current, max] = healthStr.split('/').map(h => parseInt(h.trim(), 10));
      if (!isNaN(current) && !isNaN(max)) {
        playerData.health = { current, max };
      }
    } else if (line.startsWith('lucidity:')) {
      const LucidityStr = line.replace('lucidity:', '').trim();
      const [current, max] = LucidityStr.split('/').map(s => parseInt(s.trim(), 10));
      if (!isNaN(current) && !isNaN(max)) {
        playerData.lucidity = { current, max };
      }
    } else if (line.startsWith('Profession:')) {
      playerData.profession = playerData.profession || { name: '', description: '', flavor_text: '' };
      playerData.profession.name = line.replace('Profession:', '').trim();
    } else if (line.startsWith('Description:')) {
      if (playerData.profession) {
        playerData.profession.description = line.replace('Description:', '').trim();
      }
    } else if (line.startsWith('Background:')) {
      if (playerData.profession) {
        playerData.profession.flavor_text = line.replace('Background:', '').trim();
      }
    } else if (line.startsWith('Fear:')) {
      const fear = parseInt(line.replace('Fear:', '').trim(), 10);
      if (!isNaN(fear)) {
        playerData.fear = fear;
      }
    } else if (line.startsWith('Corruption:')) {
      const corruption = parseInt(line.replace('Corruption:', '').trim(), 10);
      if (!isNaN(corruption)) {
        playerData.corruption = corruption;
      }
    } else if (line.startsWith('Occult Knowledge:')) {
      const occult = parseInt(line.replace('Occult Knowledge:', '').trim(), 10);
      if (!isNaN(occult)) {
        playerData.occult_knowledge = occult;
      }
    } else if (line.startsWith('Position:')) {
      playerData.position = line.replace('Position:', '').trim().toLowerCase();
    } else if (line.startsWith('In Combat:')) {
      const combatStatus = line.replace('In Combat:', '').trim();
      playerData.in_combat = combatStatus === 'Yes';
    } else if (line.startsWith('XP:')) {
      const xp = parseInt(line.replace('XP:', '').trim(), 10);
      if (!isNaN(xp)) {
        playerData.xp = xp;
      }
    }
  }

  return playerData;
}

/**
 * Converts parsed player data to the format expected by the Player interface
 *
 * @param parsedData - Parsed player data from status response
 * @returns Player object compatible with the client interfaces
 */
export function convertToPlayerInterface(parsedData: ParsedPlayerData): PlayerWithProfession {
  const player: PlayerWithProfession = {
    name: parsedData.name || '',
    profession_name: parsedData.profession?.name,
    profession_description: parsedData.profession?.description,
    profession_flavor_text: parsedData.profession?.flavor_text,
    stats: {
      current_dp: parsedData.health?.current || 100,
      max_health: parsedData.health?.max || 100,
      lucidity: parsedData.lucidity?.current || 100,
      max_lucidity: parsedData.lucidity?.max || 100,
      fear: parsedData.fear || 0,
      corruption: parsedData.corruption || 0,
      occult_knowledge: parsedData.occult_knowledge || 0,
      position: parsedData.position,
    },
    position: parsedData.position,
  };

  // Add combat status if present
  if (parsedData.in_combat !== undefined) {
    player.in_combat = parsedData.in_combat;
  }

  // Add XP if present
  if (parsedData.xp !== undefined) {
    player.xp = parsedData.xp;
  }

  return player;
}
