import type { ChatPanelMessage } from './chatPanelRuntimeUtils';
import { bumpUnreadCountForMessage } from './chatPanelUnreadBump';

export function computeUnreadChatCounts(
  messages: ChatPanelMessage[],
  normalizedSelectedChannel: string,
  clearedChannels: Record<string, number>,
  isAllChannelSelected: boolean
): Record<string, number> {
  if (isAllChannelSelected) {
    return {};
  }
  const counts: Record<string, number> = {};
  for (let index = 0; index < messages.length; index += 1) {
    bumpUnreadCountForMessage(messages[index], index, normalizedSelectedChannel, clearedChannels, counts);
  }
  return counts;
}
