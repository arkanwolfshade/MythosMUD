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
    max_dp: number;
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

function parseSlashPair(line: string, prefix: string): { current: number; max: number } | null {
  const pairStr = line.replace(prefix, '').trim();
  const [current, max] = pairStr.split('/').map(v => parseInt(v.trim(), 10));
  if (isNaN(current) || isNaN(max)) {
    return null;
  }
  return { current, max };
}

function parseIntField(line: string, prefix: string): number | null {
  const value = parseInt(line.replace(prefix, '').trim(), 10);
  return isNaN(value) ? null : value;
}

function ensureProfession(data: ParsedPlayerData): NonNullable<ParsedPlayerData['profession']> {
  data.profession = data.profession ?? { name: '', description: '', flavor_text: '' };
  return data.profession;
}

type StatusLineHandler = (line: string, data: ParsedPlayerData) => void;

const STATUS_LINE_HANDLERS: StatusLineHandler[] = [
  (line, data) => {
    if (line.startsWith('Name:')) data.name = line.replace('Name:', '').trim();
  },
  (line, data) => {
    if (line.startsWith('Location:')) data.location = line.replace('Location:', '').trim();
  },
  (line, data) => {
    if (!line.startsWith('Health:')) return;
    const health = parseSlashPair(line, 'Health:');
    if (health) data.health = health;
  },
  (line, data) => {
    if (!line.startsWith('lucidity:')) return;
    const lucidity = parseSlashPair(line, 'lucidity:');
    if (lucidity) data.lucidity = lucidity;
  },
  (line, data) => {
    if (line.startsWith('Profession:')) ensureProfession(data).name = line.replace('Profession:', '').trim();
  },
  (line, data) => {
    if (line.startsWith('Description:') && data.profession) {
      data.profession.description = line.replace('Description:', '').trim();
    }
  },
  (line, data) => {
    if (line.startsWith('Background:') && data.profession) {
      data.profession.flavor_text = line.replace('Background:', '').trim();
    }
  },
  (line, data) => {
    if (!line.startsWith('Fear:')) return;
    const fear = parseIntField(line, 'Fear:');
    if (fear !== null) data.fear = fear;
  },
  (line, data) => {
    if (!line.startsWith('Corruption:')) return;
    const corruption = parseIntField(line, 'Corruption:');
    if (corruption !== null) data.corruption = corruption;
  },
  (line, data) => {
    if (!line.startsWith('Occult Knowledge:')) return;
    const occult = parseIntField(line, 'Occult Knowledge:');
    if (occult !== null) data.occult_knowledge = occult;
  },
  (line, data) => {
    if (line.startsWith('Position:')) data.position = line.replace('Position:', '').trim().toLowerCase();
  },
  (line, data) => {
    if (line.startsWith('In Combat:')) {
      data.in_combat = line.replace('In Combat:', '').trim() === 'Yes';
    }
  },
  (line, data) => {
    if (!line.startsWith('XP:')) return;
    const xp = parseIntField(line, 'XP:');
    if (xp !== null) data.xp = xp;
  },
];

/**
 * Parses a status command response string to extract player data
 */
export function parseStatusResponse(statusResponse: string): ParsedPlayerData {
  const lines = statusResponse
    .split('\n')
    .map(line => line.trim())
    .filter(line => line.length > 0);
  const playerData: ParsedPlayerData = {};

  for (const line of lines) {
    for (const handler of STATUS_LINE_HANDLERS) {
      handler(line, playerData);
    }
  }

  return playerData;
}

/**
 * Converts parsed player data to the format expected by the Player interface
 */
export function convertToPlayerInterface(parsedData: ParsedPlayerData): PlayerWithProfession {
  const player: PlayerWithProfession = {
    name: parsedData.name || '',
    profession_name: parsedData.profession?.name,
    profession_description: parsedData.profession?.description,
    profession_flavor_text: parsedData.profession?.flavor_text,
    stats: {
      current_dp: parsedData.health?.current || 100,
      max_dp: parsedData.health?.max || 100,
      lucidity: parsedData.lucidity?.current || 100,
      max_lucidity: parsedData.lucidity?.max || 100,
      fear: parsedData.fear || 0,
      corruption: parsedData.corruption || 0,
      occult_knowledge: parsedData.occult_knowledge || 0,
      position: parsedData.position,
    },
    position: parsedData.position,
  };

  if (parsedData.in_combat !== undefined) {
    player.in_combat = parsedData.in_combat;
  }

  if (parsedData.xp !== undefined) {
    player.xp = parsedData.xp;
  }

  return player;
}
