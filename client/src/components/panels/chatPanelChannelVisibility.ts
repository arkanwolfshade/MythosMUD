import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import type { ChatPanelMessage } from './chatPanelRuntimeUtils';

const EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW = new Set(['system', 'combat']);

/** Smaller helpers first so Lizard attributes complexity per function (TS parser quirk). */
function matchesChannelSelection(messageChannel: string, normalizedSelectedChannel: string): boolean {
  if (messageChannel === 'whisper') {
    return normalizedSelectedChannel === 'whisper';
  }
  if (messageChannel === 'party') {
    return normalizedSelectedChannel === 'party';
  }
  return messageChannel === normalizedSelectedChannel;
}

function resolveMessageChannelForFilter(message: ChatPanelMessage): string {
  return message.channel || extractChannelFromMessage(message.text) || 'local';
}

function isGloballyExcludedFromChannelView(message: ChatPanelMessage): boolean {
  if (message.channel === 'game-log') {
    return true;
  }
  const t = message.messageType;
  return t !== undefined && EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW.has(t);
}

export function isVisibleInChannelView(
  message: ChatPanelMessage,
  normalizedSelectedChannel: string,
  isAllChannelSelected: boolean
): boolean {
  if (isGloballyExcludedFromChannelView(message)) {
    return false;
  }
  if (isAllChannelSelected) {
    return true;
  }
  if (message.messageType === 'command') {
    return false;
  }
  const messageChannel = resolveMessageChannelForFilter(message);
  if (message.messageType === 'error') {
    return messageChannel === normalizedSelectedChannel;
  }
  const isChatMessage = message.messageType === 'chat' || isChatContent(message.text);
  if (!isChatMessage) {
    return false;
  }
  return matchesChannelSelection(messageChannel, normalizedSelectedChannel);
}
