// Message-building helpers for the projector (split from projector.ts for file-nloc)

import type { ChatMessage } from '../types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';

export const GAME_LOG_CHANNEL = 'game-log';

const CHANNEL_TO_TYPE: Record<string, 'whisper' | 'shout' | 'emote' | 'say'> = {
  whisper: 'whisper',
  shout: 'shout',
  emote: 'emote',
};

function channelToMessageType(channel: string): 'whisper' | 'shout' | 'emote' | 'say' {
  return CHANNEL_TO_TYPE[channel] ?? 'say';
}

export function buildChatMessage(
  text: string,
  timestamp: string,
  opts: { isHtml?: boolean; messageType?: string; channel?: string } = {}
): ChatMessage {
  const { messageType = 'system', channel = 'game', isHtml = false } = opts;
  const type = channelToMessageType(channel);
  return { text, timestamp, isHtml, messageType, channel, type };
}

export function appendMessage(prevMessages: ChatMessage[], message: ChatMessage): ChatMessage[] {
  return [...prevMessages, sanitizeChatMessageForState(message)];
}

/** Dedupe window (ms): same movement text within this window is treated as duplicate. */
const MOVEMENT_DEDUPE_MS = 2000;

export function appendMovementMessage(prevMessages: ChatMessage[], message: ChatMessage): ChatMessage[] {
  const sanitized = sanitizeChatMessageForState(message);
  const last = prevMessages[prevMessages.length - 1];
  if (last?.text === sanitized.text) {
    const lastTs = new Date(last.timestamp).getTime();
    const newTs = new Date(sanitized.timestamp).getTime();
    if (Math.abs(newTs - lastTs) <= MOVEMENT_DEDUPE_MS) {
      return prevMessages;
    }
  }
  return [...prevMessages, sanitized];
}
