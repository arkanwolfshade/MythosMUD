/**
 * Tests for messageUtils.
 */

import { describe, expect, it } from 'vitest';
import type { ChatMessage } from '../../types';
import { sanitizeChatMessageForState } from '../messageUtils';

const base = (extra: Partial<ChatMessage> = {}): ChatMessage => ({
  text: 'Original text',
  timestamp: new Date().toISOString(),
  isHtml: false,
  category: 'command.output',
  ...extra,
});

describe('messageUtils', () => {
  describe('sanitizeChatMessageForState', () => {
    it('should prefer rawText when provided', () => {
      const result = sanitizeChatMessageForState(base({ rawText: 'Raw text' }));
      expect(result.rawText).toBe('Raw text');
      expect(result.text).toBe('Raw text');
    });

    it('should use text when rawText is not provided', () => {
      const result = sanitizeChatMessageForState(base());
      expect(result.text).toBe('Original text');
      expect(result.rawText).toBe('Original text');
    });

    it('should sanitize HTML messages and keep the unsanitized rawText', () => {
      const raw = '<b>Bold</b><script>alert(1)</script>';
      const result = sanitizeChatMessageForState(base({ text: raw, isHtml: true }));
      expect(result.isHtml).toBe(true);
      expect(result.text).toContain('<b>Bold</b>');
      expect(result.text).not.toContain('<script');
      expect(result.rawText).toBe(raw);
    });

    it('should leave plain text untouched', () => {
      const result = sanitizeChatMessageForState(base({ text: '<b>not markup</b>' }));
      expect(result.text).toBe('<b>not markup</b>');
    });

    it('should keep the category and channel exactly as given', () => {
      const result = sanitizeChatMessageForState(base({ category: 'chat.local', channel: 'local' }));
      expect(result.category).toBe('chat.local');
      expect(result.channel).toBe('local');
    });

    it('should not invent a channel, type or messageType for a message without one', () => {
      const result = sanitizeChatMessageForState(base());
      expect(result).not.toHaveProperty('channel');
      expect(result).not.toHaveProperty('type');
      expect(result).not.toHaveProperty('messageType');
    });

    it('should handle message with empty rawText', () => {
      const result = sanitizeChatMessageForState(base({ text: 'Original', rawText: '' }));
      expect(result.rawText).toBe('');
      expect(result.text).toBe('');
    });
  });
});
