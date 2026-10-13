/**
 * Semantic categories for player-visible text, assigned by the server.
 *
 * Mirrors `MessageCategory` in server/constants/message_category.py; a server unit test
 * (server/tests/unit/constants/test_message_category.py) fails if the two drift apart. Keep one literal per line.
 */
export const MESSAGE_CATEGORIES = [
  'chat.say',
  'chat.local',
  'chat.global',
  'chat.party',
  'chat.whisper',
  'chat.shout',
  'chat.emote',
  'chat.admin',
  'combat.hit',
  'combat.hurt',
  'combat.miss',
  'combat.death',
  'combat.status',
  'room.name',
  'room.description',
  'room.exits',
  'room.movement',
  'system.info',
  'system.warning',
  'system.error',
  'status.lucidity',
  'status.health',
  'status.rescue',
  'command.output',
  'npc.shopkeeper',
  'npc.quest_giver',
  'npc.passive_mob',
  'npc.aggressive_mob',
] as const;

export type MessageCategory = (typeof MESSAGE_CATEGORIES)[number];

/** What a player should expect of an NPC on sight; the kind of the matching `npc.<disposition>` category. */
export const NPC_DISPOSITIONS = ['shopkeeper', 'quest_giver', 'passive_mob', 'aggressive_mob'] as const;

export type NpcDisposition = (typeof NPC_DISPOSITIONS)[number];

/** An NPC in a room's `npcs` list. The server is authoritative for `disposition` (phantoms are `aggressive_mob`). */
export interface NpcOccupant {
  name: string;
  disposition: NpcDisposition;
}

export const DEFAULT_NPC_DISPOSITION: NpcDisposition = 'passive_mob';

export function isNpcDisposition(value: unknown): value is NpcDisposition {
  return typeof value === 'string' && (NPC_DISPOSITIONS as readonly string[]).includes(value);
}

export function npcCategory(disposition: NpcDisposition): MessageCategory {
  return `npc.${disposition}`;
}
