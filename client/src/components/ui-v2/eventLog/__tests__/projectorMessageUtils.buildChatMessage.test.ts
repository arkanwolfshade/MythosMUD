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

  it('sets only the channel it was given: non-chat messages carry none', () => {
    const chat = buildChatMessage('Bob says: hi', TS, { category: 'chat.say', channel: 'say' });
    expect(chat.channel).toBe('say');
    const plain = buildChatMessage('A plain line.', TS, { category: 'command.output' });
    expect('channel' in plain).toBe(false);
    expect(plain.isHtml).toBe(false);
  });

  it('carries no legacy messageType, type, tags or isCompleteHtml fields', () => {
    const message = buildChatMessage('<b>Help</b>', TS, { category: 'command.output', isHtml: true });
    expect(Object.keys(message).sort()).toEqual(['category', 'isHtml', 'text', 'timestamp']);
  });

  it('keeps the category through appendMessage sanitization', () => {
    const message = buildChatMessage('You are hit for 3 damage.', TS, { category: 'combat.hurt' });
    const [stored] = appendMessage([], message);
    expect(stored.category).toBe('combat.hurt');
  });
});
