// Validates the `npcs` list a room payload carries: the one place the wire shape is checked (#1025).
// The server is authoritative; a bare string can only mean a bug now, so it is dropped rather than upgraded.
// An unrecognised disposition falls back to passive_mob, matching the server's own fallback.

import { DEFAULT_NPC_DISPOSITION, isNpcDisposition, type NpcOccupant } from '../../../types/messageCategory';

function toNpcOccupant(entry: unknown): NpcOccupant | null {
  if (typeof entry !== 'object' || entry === null) {
    return null;
  }
  const { name, disposition } = entry as Record<string, unknown>;
  if (typeof name !== 'string' || name === '') {
    return null;
  }
  return { name, disposition: isNpcDisposition(disposition) ? disposition : DEFAULT_NPC_DISPOSITION };
}

/** Keeps every well-formed `{ name, disposition }` entry; anything that is not an array yields []. */
export function normalizeNpcOccupants(raw: unknown): NpcOccupant[] {
  if (!Array.isArray(raw)) {
    return [];
  }
  return raw.map(toNpcOccupant).filter((npc): npc is NpcOccupant => npc !== null);
}

/** Like `normalizeNpcOccupants`, but keeps "omitted" (undefined) distinct from an authoritative empty list. */
export function normalizeOptionalNpcOccupants(raw: unknown): NpcOccupant[] | undefined {
  return raw === undefined ? undefined : normalizeNpcOccupants(raw);
}

export function npcNames(npcs: readonly NpcOccupant[]): string[] {
  return npcs.map(npc => npc.name);
}
