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
] as const;

export type MessageCategory = (typeof MESSAGE_CATEGORIES)[number];
