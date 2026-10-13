// Message-building helpers for the projector (split from projector.ts for file-nloc)

import { MESSAGE_CATEGORIES, type MessageCategory } from '../../../types/messageCategory';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import type { ChatMessage } from '../types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import { validateSegments } from '../utils/messageSegments';

const KNOWN_CATEGORIES: ReadonlySet<string> = new Set(MESSAGE_CATEGORIES);
const FALLBACK_CATEGORY: MessageCategory = 'command.output';
const warnedEventTypes = new Set<string>();

/**
 * The server-assigned category on an event payload. A missing or unknown value falls back to
 * `command.output` and, in development only, logs one warning per event type.
 */
export function readCategory(data: Record<string, unknown> | undefined, eventType: string): MessageCategory {
  const value = data?.category;
  if (typeof value === 'string' && KNOWN_CATEGORIES.has(value)) return value as MessageCategory;
  if (import.meta.env.DEV && !warnedEventTypes.has(eventType)) {
    warnedEventTypes.add(eventType);
    logger.warn(
      'projector',
      `Event "${eventType}" carried ${value === undefined ? 'no' : 'an unknown'} message category; using ${FALLBACK_CATEGORY}`,
      { category: value }
    );
  }
  return FALLBACK_CATEGORY;
}

export function buildChatMessage(
  text: string,
  timestamp: string,
  opts: {
    /** True when `text` is finished HTML (e.g. help); otherwise it renders as plain text. */
    isHtml?: boolean;
    /** Conversation identity; required on chat.* messages, absent otherwise. */
    channel?: string;
    category: MessageCategory;
    /** Raw `segments` from the wire (or a client-composed line); validated here, the one place it is checked. */
    segments?: unknown;
  }
): ChatMessage {
  const { isHtml = false, channel, category, segments } = opts;
  // HTML lines are sanitized as a whole, so spans over their text cannot be trusted to line up.
  const validSegments = isHtml ? undefined : validateSegments(segments, text);
  return {
    text,
    timestamp,
    isHtml,
    category,
    ...(channel ? { channel } : {}),
    ...(validSegments ? { segments: validSegments } : {}),
  };
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
export function buildLocalMessageEvent(text: string, category: MessageCategory = 'system.info'): GameEvent {
  return {
    event_type: 'client_message',
    timestamp: new Date().toISOString(),
    sequence_number: 0,
    data: { text, category },
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
