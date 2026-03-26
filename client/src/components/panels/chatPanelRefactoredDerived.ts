/**
 * Pure helpers for ChatPanelRefactored message filtering and unread math.
 * Agent-readable: each function stays small for Lizard CCN limits.
 */
import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import type { ChatPanelRefactoredMessage } from './chatPanelRefactoredTypes';

export function filterNonSystemMessages(messages: ChatPanelRefactoredMessage[]): ChatPanelRefactoredMessage[] {
  return messages.filter(m => m.messageType !== 'system');
}

export function isDisplayableChatMessage(message: ChatPanelRefactoredMessage): boolean {
  return message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text));
}

export function resolveMessageChannel(message: ChatPanelRefactoredMessage, fallback: string): string {
  return message.channel || extractChannelFromMessage(message.text) || fallback;
}

export function computeChannelMessages(
  nonSystem: ChatPanelRefactoredMessage[],
  normalizedChannel: string,
  isAllSelected: boolean
): ChatPanelRefactoredMessage[] {
  if (isAllSelected) {
    return nonSystem;
  }
  return nonSystem.filter(m => resolveMessageChannel(m, normalizedChannel) === normalizedChannel);
}

export function computeUnreadCounts(
  nonSystem: ChatPanelRefactoredMessage[],
  normalizedChannel: string,
  clearedChannels: Record<string, number>,
  isAllSelected: boolean
): Record<string, number> {
  if (isAllSelected) {
    return {};
  }

  const counts: Record<string, number> = {};

  nonSystem.forEach((message, index) => {
    if (!isDisplayableChatMessage(message)) {
      return;
    }
    const channelId = resolveMessageChannel(message, normalizedChannel);
    if (channelId === normalizedChannel) {
      return;
    }
    const clearedBefore = clearedChannels[channelId] ?? 0;
    if (index < clearedBefore) {
      return;
    }
    counts[channelId] = (counts[channelId] ?? 0) + 1;
  });

  return counts;
}

export function computeFilteredMessages(
  nonSystem: ChatPanelRefactoredMessage[],
  chatFilter: string,
  normalizedChannel: string,
  isAllSelected: boolean
): ChatPanelRefactoredMessage[] {
  if (chatFilter === 'all' || isAllSelected) {
    return nonSystem;
  }

  return nonSystem.filter(message => {
    if (!isDisplayableChatMessage(message)) {
      return false;
    }
    const messageChannel = resolveMessageChannel(message, 'local');
    return messageChannel === normalizedChannel;
  });
}
