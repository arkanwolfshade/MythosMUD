import { describe, expect, it } from 'vitest';
import {
  computeChannelMessages,
  computeFilteredMessages,
  computeUnreadCounts,
  filterNonSystemMessages,
  isDisplayableChatMessage,
  resolveMessageChannel,
} from '../chatPanelRefactoredDerived';
import type { ChatPanelRefactoredMessage } from '../chatPanelRefactoredTypes';

const base = (over: Partial<ChatPanelRefactoredMessage>): ChatPanelRefactoredMessage => ({
  text: '',
  timestamp: '',
  isHtml: false,
  ...over,
});

describe('chatPanelRefactoredDerived', () => {
  it('filterNonSystemMessages drops system', () => {
    const messages = [base({ messageType: 'system' }), base({ messageType: 'chat', text: 'hi' })];
    expect(filterNonSystemMessages(messages)).toHaveLength(1);
  });

  it('resolveMessageChannel uses channel then extract fallback', () => {
    const m = base({ channel: 'global', text: 'x' });
    expect(resolveMessageChannel(m, 'local')).toBe('global');
  });

  it('computeChannelMessages returns all when isAllSelected', () => {
    const non = [base({ messageType: 'chat', channel: 'local', text: 'a' })];
    expect(computeChannelMessages(non, 'local', true)).toBe(non);
  });

  it('computeChannelMessages filters by channel', () => {
    const non = [
      base({ messageType: 'chat', channel: 'local', text: 'a' }),
      base({ messageType: 'chat', channel: 'global', text: 'b' }),
    ];
    expect(computeChannelMessages(non, 'local', false)).toHaveLength(1);
  });

  it('computeUnreadCounts is empty when all channel selected', () => {
    const non = [base({ messageType: 'chat', channel: 'global', text: 'b' })];
    expect(computeUnreadCounts(non, 'local', {}, true)).toEqual({});
  });

  it('computeUnreadCounts counts other-channel chat after cleared index', () => {
    const non = [
      base({ messageType: 'chat', channel: 'local', text: 'a' }),
      base({ messageType: 'chat', channel: 'global', text: 'b' }),
    ];
    expect(computeUnreadCounts(non, 'local', {}, false)).toEqual({ global: 1 });
    expect(computeUnreadCounts(non, 'local', { global: 2 }, false)).toEqual({});
  });

  it('computeFilteredMessages respects chatFilter all', () => {
    const non = [base({ messageType: 'chat', channel: 'local', text: 'a' })];
    expect(computeFilteredMessages(non, 'all', 'say', false)).toBe(non);
  });

  it('isDisplayableChatMessage identifies chat and command with chat content', () => {
    expect(isDisplayableChatMessage(base({ messageType: 'chat', text: 'x' }))).toBe(true);
    expect(isDisplayableChatMessage(base({ messageType: 'command', text: 'You say: hello' }))).toBe(true);
    expect(isDisplayableChatMessage(base({ messageType: 'error', text: 'x' }))).toBe(false);
  });
});
