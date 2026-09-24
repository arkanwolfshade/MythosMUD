// Message-building helpers for the projector (split from projector.ts for file-nloc)

import type { GameEvent } from '../eventHandlers/types';
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

/**
 * Build a client-local event for UI-only messages (connection lost, respawn errors, etc). The
 * `client_` prefix marks it as never coming from the server -- see .cursor/rules/server-authority.mdc.
 * `sequence_number: 0` matches how the event log already treats other locally-appended events.
 */
export function buildLocalMessageEvent(text: string, messageType: string = 'system'): GameEvent {
  return {
    event_type: 'client_message',
    timestamp: new Date().toISOString(),
    sequence_number: 0,
    data: { text, messageType },
  };
}

/** Build the client-local event that clears the message log (e.g. the user clicked "Clear"). */
export function buildLocalClearMessagesEvent(): GameEvent {
  return {
    event_type: 'client_messages_cleared',
    timestamp: new Date().toISOString(),
    sequence_number: 0,
    data: {},
  };
}
