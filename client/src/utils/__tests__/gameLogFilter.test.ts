import { describe, expect, it } from 'vitest';
import { filterGameLogMessages, messagePassesGameLogFilters } from '../gameLogFilter';

const base = {
  text: 'hello',
  timestamp: '2024-06-15T12:00:00.000Z',
  messageType: 'system' as const,
};

describe('gameLogFilter', () => {
  const fixedNow = new Date('2024-06-15T12:30:00.000Z');

  it('excludes chat messages', () => {
    expect(
      messagePassesGameLogFilters(
        { ...base, messageType: 'chat' },
        { messageFilter: 'all', timeFilter: 'all', searchQuery: '' },
        fixedNow
      )
    ).toBe(false);
  });

  it('filters by message type', () => {
    expect(
      messagePassesGameLogFilters(
        { ...base, messageType: 'emote' },
        { messageFilter: 'emote', timeFilter: 'all', searchQuery: '' },
        fixedNow
      )
    ).toBe(true);
    expect(
      messagePassesGameLogFilters(
        { ...base, messageType: 'system' },
        { messageFilter: 'emote', timeFilter: 'all', searchQuery: '' },
        fixedNow
      )
    ).toBe(false);
  });

  it('filters by numeric minutes window', () => {
    const recent = { ...base, timestamp: '2024-06-15T12:25:00.000Z' };
    const old = { ...base, timestamp: '2024-06-15T11:00:00.000Z' };
    const state = { messageFilter: 'all', timeFilter: '15', searchQuery: '' };
    expect(messagePassesGameLogFilters(recent, state, fixedNow)).toBe(true);
    expect(messagePassesGameLogFilters(old, state, fixedNow)).toBe(false);
  });

  it('filters by named time windows', () => {
    const state = { messageFilter: 'all', timeFilter: 'lastHour', searchQuery: '' };
    const recent = { ...base, timestamp: '2024-06-15T12:00:00.000Z' };
    const old = { ...base, timestamp: '2024-06-15T10:00:00.000Z' };
    expect(messagePassesGameLogFilters(recent, state, fixedNow)).toBe(true);
    expect(messagePassesGameLogFilters(old, state, fixedNow)).toBe(false);
  });

  it('filters by search query', () => {
    const state = { messageFilter: 'all', timeFilter: 'all', searchQuery: 'HEL' };
    expect(messagePassesGameLogFilters({ ...base, text: 'hello' }, state, fixedNow)).toBe(true);
    expect(messagePassesGameLogFilters({ ...base, text: 'goodbye' }, state, fixedNow)).toBe(false);
  });

  it('filterGameLogMessages returns filtered array', () => {
    const messages = [
      { ...base, text: 'a', messageType: 'system' as const },
      { ...base, text: 'b', messageType: 'chat' as const },
    ];
    const out = filterGameLogMessages(messages, {
      messageFilter: 'all',
      timeFilter: 'all',
      searchQuery: '',
    });
    expect(out).toHaveLength(1);
    expect(out[0].text).toBe('a');
  });
});
