/**
 * Unit tests for the client-local event builders (#752): these mark events that never come from
 * the server (client_ prefix) so local UI messages (connection lost, respawn errors, "clear
 * messages") survive event-log replay instead of being silently reverted.
 */
import { describe, expect, it } from 'vitest';
import { buildLocalClearMessagesEvent, buildLocalMessageEvent } from '../projectorMessageUtils';

describe('buildLocalMessageEvent', () => {
  it('builds a client_message event with the given text and category', () => {
    const event = buildLocalMessageEvent('Connection to server lost.', 'system.error');
    expect(event.event_type).toBe('client_message');
    expect(event.sequence_number).toBe(0);
    expect(event.data).toEqual({ text: 'Connection to server lost.', category: 'system.error' });
    expect(() => new Date(event.timestamp).toISOString()).not.toThrow();
  });

  it('defaults the category to system.info when omitted', () => {
    const event = buildLocalMessageEvent('Just a note.');
    expect(event.data.category).toBe('system.info');
  });
});

describe('buildLocalClearMessagesEvent', () => {
  it('builds a client_messages_cleared event with no data', () => {
    const event = buildLocalClearMessagesEvent();
    expect(event.event_type).toBe('client_messages_cleared');
    expect(event.sequence_number).toBe(0);
    expect(event.data).toEqual({});
  });
});
