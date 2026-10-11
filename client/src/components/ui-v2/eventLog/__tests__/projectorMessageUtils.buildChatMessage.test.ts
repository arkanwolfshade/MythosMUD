/**
 * Unit tests for buildChatMessage's `category` pass-through: the server-assigned semantic category
 * must reach panel state intact, since panels style and route on it.
 */
import { describe, expect, it } from 'vitest';
import { appendMessage, buildChatMessage } from '../projectorMessageUtils';

const TS = '2026-01-01T00:00:00.000Z';

describe('buildChatMessage category', () => {
  it('carries the server-assigned category onto the message', () => {
    const message = buildChatMessage('Ithaqua whispers to you: hello', TS, {
      category: 'chat.whisper',
      channel: 'whisper',
    });
    expect(message.category).toBe('chat.whisper');
  });

  it('omits the category key entirely when none was given', () => {
    const message = buildChatMessage('A plain line.', TS);
    expect('category' in message).toBe(false);
  });

  it('keeps the category through appendMessage sanitization', () => {
    const message = buildChatMessage('You are hit for 3 damage.', TS, { category: 'combat.hurt' });
    const [stored] = appendMessage([], message);
    expect(stored.category).toBe('combat.hurt');
  });
});
