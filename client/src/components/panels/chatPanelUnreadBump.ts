import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import type { ChatPanelMessage } from './chatPanelRuntimeUtils';

function messageIsEligibleForUnreadCount(message: ChatPanelMessage): boolean {
  if (message.messageType === 'chat') {
    return true;
  }
  if (message.messageType === 'command') {
    return isChatContent(message.text);
  }
  return false;
}

function unreadChannelIdForMessage(message: ChatPanelMessage, normalizedSelectedChannel: string): string {
  return message.channel || extractChannelFromMessage(message.text) || normalizedSelectedChannel;
}

function canIncrementUnreadForChannel(
  channelId: string,
  index: number,
  normalizedSelectedChannel: string,
  clearedChannels: Record<string, number>
): boolean {
  if (channelId === normalizedSelectedChannel) {
    return false;
  }
  return index >= (clearedChannels[channelId] ?? 0);
}

export function bumpUnreadCountForMessage(
  message: ChatPanelMessage,
  index: number,
  normalizedSelectedChannel: string,
  clearedChannels: Record<string, number>,
  counts: Record<string, number>
): void {
  if (!messageIsEligibleForUnreadCount(message)) {
    return;
  }
  const channelId = unreadChannelIdForMessage(message, normalizedSelectedChannel);
  if (!canIncrementUnreadForChannel(channelId, index, normalizedSelectedChannel, clearedChannels)) {
    return;
  }
  counts[channelId] = (counts[channelId] ?? 0) + 1;
}
