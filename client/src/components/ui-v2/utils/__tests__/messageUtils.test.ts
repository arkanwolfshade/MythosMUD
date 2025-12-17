/**
 * Tests for messageUtils.
 */

import { describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../types';
import { sanitizeChatMessageForState } from '../messageUtils';

// Mock security utils
vi.mock('../../../utils/security', () => ({
  inputSanitizer: {
    sanitizeIncomingHtml: (html: string) => html,
  },
}));

describe('messageUtils', () => {
  describe('sanitizeChatMessageForState', () => {
    it('should sanitize message with rawText', () => {
      const message: ChatMessage = {
        text: 'Original text',
        timestamp: new Date().toISOString(),
        isHtml: false,
        rawText: 'Raw text',
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.rawText).toBe('Raw text');
      expect(result.text).toBe('Raw text');
    });

    it('should use text when rawText is not provided', () => {
      const message: ChatMessage = {
        text: 'Original text',
        timestamp: new Date().toISOString(),
        isHtml: false,
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.text).toBe('Original text');
    });

    it('should sanitize HTML messages', () => {
      const message: ChatMessage = {
        text: '<b>Bold</b>',
        timestamp: new Date().toISOString(),
        isHtml: true,
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.isHtml).toBe(true);
    });

    it('should extract message type', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
        type: 'system',
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.type).toBe('system');
    });

    it('should default to system type when type is missing', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.type).toBe('system');
    });

    it('should extract channel', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
        channel: 'local',
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.channel).toBe('local');
    });

    it('should default to system channel when channel is missing', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.channel).toBe('system');
    });

    it('should extract messageType', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType: 'chat',
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.messageType).toBe('chat');
    });

    it('should use type as fallback for messageType', () => {
      const message: ChatMessage = {
        text: 'Test',
        timestamp: new Date().toISOString(),
        isHtml: false,
        type: 'error',
      };

      const result = sanitizeChatMessageForState(message);
      expect(result.messageType).toBe('error');
    });
  });
});
