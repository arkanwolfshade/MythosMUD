// Maps a server-assigned MessageCategory to the CSS classes in styles/messageCategories.css.
// Styling is a pure function of the category (#714/ADR-024): nothing here may depend on whether
// a message was real or hallucinated.

import type { MessageCategory } from '../../../types/messageCategory';
import { logger } from '../../../utils/logger';

type MessageRegister = 'alert' | 'private' | 'action' | 'meta' | 'plain' | 'heading';

// Typography register per category (rationale in the a11y notes atop messageCategories.css).
// Record<MessageCategory, ...> makes the compiler flag any category added without a register.
const CATEGORY_REGISTER: Record<MessageCategory, MessageRegister> = {
  'chat.say': 'plain',
  'chat.local': 'plain',
  'chat.global': 'plain',
  'chat.party': 'plain',
  'chat.whisper': 'private',
  'chat.shout': 'plain',
  'chat.emote': 'action',
  'chat.admin': 'meta',
  'combat.hit': 'action',
  'combat.hurt': 'alert',
  'combat.miss': 'action',
  'combat.death': 'alert',
  'combat.status': 'alert',
  'room.name': 'heading',
  'room.description': 'plain',
  'room.exits': 'plain',
  'room.movement': 'plain',
  'system.info': 'meta',
  'system.warning': 'alert',
  'system.error': 'alert',
  'quest.info': 'meta',
  'status.lucidity': 'alert',
  'status.health': 'alert',
  'status.rescue': 'alert',
  'command.output': 'plain',
  'npc.shopkeeper': 'plain',
  'npc.quest_giver': 'plain',
  'npc.passive_mob': 'plain',
  'npc.aggressive_mob': 'plain',
};

const warnedUnknown = new Set<string>();

function lookupRegister(category: string | undefined): MessageRegister | undefined {
  if (category === undefined) return undefined;
  const register = Object.hasOwn(CATEGORY_REGISTER, category)
    ? CATEGORY_REGISTER[category as MessageCategory]
    : undefined;
  if (register === undefined && import.meta.env.DEV && !warnedUnknown.has(category)) {
    warnedUnknown.add(category);
    logger.warn('messageCategoryStyle', `Unknown message category "${category}"; using default style`);
  }
  return register;
}

/** `cat cat-<domain> cat-<domain>-<kind> cat-reg-<register>`; undefined for a missing or unknown category. */
export function getMessageCategoryClass(category: string | undefined): string | undefined {
  const register = lookupRegister(category);
  if (category === undefined || register === undefined) return undefined;
  const [domain] = category.split('.');
  return `cat cat-${domain} cat-${category.replace('.', '-')} cat-reg-${register}`;
}

/**
 * `seg seg-npc-<disposition>` for a styled span inside a line (#1025); undefined for a plain span.
 * Only `npc.*` spans are styled. Unlike `getMessageCategoryClass` there is no glyph or Text-labels word:
 * those belong to the line, and repeating them on every name would be noise.
 */
export function getSegmentClass(category: string | undefined): string | undefined {
  if (category === undefined || !category.startsWith('npc.') || lookupRegister(category) === undefined) {
    return undefined;
  }
  return `seg seg-${category.replace('.', '-')}`;
}

/** True when the category is in the plain (speech/ambient) register, the only one #804's corruption tint may touch. */
export function isPlainRegisterCategory(category: string | undefined): boolean {
  return lookupRegister(category) === 'plain';
}
