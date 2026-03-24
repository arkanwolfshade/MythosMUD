import { isVisibleInChannelView } from './chatPanelChannelVisibility';
import type { ChatPanelMessage } from './chatPanelRuntimeUtils';

export function filterMessagesForChannelView(
  messages: ChatPanelMessage[],
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): ChatPanelMessage[] {
  return messages.filter(message => isVisibleInChannelView(message, normalizedSelectedChannel, isAllChannelSelected));
}
