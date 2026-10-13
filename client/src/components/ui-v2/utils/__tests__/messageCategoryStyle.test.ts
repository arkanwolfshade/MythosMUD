import { afterEach, describe, expect, it, vi } from 'vitest';
import { logger } from '../../../../utils/logger';
import { getMessageCategoryClass, getSegmentClass, isPlainRegisterCategory } from '../messageCategoryStyle';

describe('getMessageCategoryClass', () => {
  it('builds cat, domain, kind and register classes', () => {
    expect(getMessageCategoryClass('chat.whisper')).toBe('cat cat-chat cat-chat-whisper cat-reg-private');
    expect(getMessageCategoryClass('combat.hurt')).toBe('cat cat-combat cat-combat-hurt cat-reg-alert');
    expect(getMessageCategoryClass('room.name')).toBe('cat cat-room cat-room-name cat-reg-heading');
    expect(getMessageCategoryClass('system.info')).toBe('cat cat-system cat-system-info cat-reg-meta');
    expect(getMessageCategoryClass('chat.emote')).toBe('cat cat-chat cat-chat-emote cat-reg-action');
    expect(getMessageCategoryClass('command.output')).toBe('cat cat-command cat-command-output cat-reg-plain');
  });

  it('returns undefined for a missing category', () => {
    expect(getMessageCategoryClass(undefined)).toBeUndefined();
  });

  describe('unknown categories', () => {
    afterEach(() => {
      vi.restoreAllMocks();
    });

    it('returns undefined and warns only once per unknown value in development', () => {
      const warn = vi.spyOn(logger, 'warn').mockImplementation(() => undefined);
      expect(getMessageCategoryClass('lore.tome')).toBeUndefined();
      expect(getMessageCategoryClass('lore.tome')).toBeUndefined();
      expect(isPlainRegisterCategory('lore.tome')).toBe(false);
      expect(warn).toHaveBeenCalledTimes(1);
    });

    it('does not mistake Object.prototype members for categories', () => {
      vi.spyOn(logger, 'warn').mockImplementation(() => undefined);
      expect(getMessageCategoryClass('constructor')).toBeUndefined();
      expect(getMessageCategoryClass('toString')).toBeUndefined();
    });
  });
});

describe('isPlainRegisterCategory', () => {
  it('is true for speech and ambient categories', () => {
    for (const c of ['chat.say', 'chat.local', 'chat.global', 'chat.party', 'chat.shout', 'room.description']) {
      expect(isPlainRegisterCategory(c)).toBe(true);
    }
  });

  it('is false for alert, private, action, meta and heading categories', () => {
    for (const c of [
      'system.error',
      'combat.hurt',
      'status.lucidity',
      'chat.whisper',
      'chat.emote',
      'system.info',
      'chat.admin',
      'room.name',
    ]) {
      expect(isPlainRegisterCategory(c)).toBe(false);
    }
    expect(isPlainRegisterCategory(undefined)).toBe(false);
  });
});

describe('getSegmentClass', () => {
  it('styles an npc.* span by disposition, with no glyph or label class', () => {
    expect(getSegmentClass('npc.aggressive_mob')).toBe('seg seg-npc-aggressive_mob');
    expect(getSegmentClass('npc.quest_giver')).toBe('seg seg-npc-quest_giver');
    expect(getSegmentClass('npc.shopkeeper')).toBe('seg seg-npc-shopkeeper');
    expect(getSegmentClass('npc.passive_mob')).toBe('seg seg-npc-passive_mob');
  });

  it('leaves everything else as plain text', () => {
    expect(getSegmentClass(undefined)).toBeUndefined();
    expect(getSegmentClass('chat.say')).toBeUndefined();
    expect(getSegmentClass('npc.unheard_of')).toBeUndefined();
  });
});
