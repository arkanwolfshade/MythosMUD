// Styled spans inside one message line (#1025). The server (or a client-composed combat line) supplies
// `segments`; this module is the one place they are checked, so a bad payload costs colour, never words.

import { MESSAGE_CATEGORIES, type MessageCategory } from '../../../types/messageCategory';
import { logger } from '../../../utils/logger';
import type { MessageSegment } from '../types';

const KNOWN_CATEGORIES: ReadonlySet<string> = new Set(MESSAGE_CATEGORIES);
const warnedJoinMismatch = new Set<string>();

/** A plain string or a styled span, as a client-composed line is assembled. */
export type SegmentPart = string | MessageSegment;

function toSegment(raw: unknown): MessageSegment | null {
  if (typeof raw !== 'object' || raw === null) {
    return null;
  }
  const { text, category } = raw as Record<string, unknown>;
  if (typeof text !== 'string') {
    return null;
  }
  // An unknown category renders as plain text inside the line; the line's other spans keep their style.
  return typeof category === 'string' && KNOWN_CATEGORIES.has(category)
    ? { text, category: category as MessageCategory }
    : { text };
}

function warnJoinMismatch(eventHint: string): void {
  if (import.meta.env.DEV && !warnedJoinMismatch.has(eventHint)) {
    warnedJoinMismatch.add(eventHint);
    logger.warn('messageSegments', 'Dropping segments that do not join back to the message text', { eventHint });
  }
}

/**
 * The spans to render for `text`, or undefined when there is nothing safe to style.
 *
 * Rejects (drops all segments) unless every span is well formed and the texts join to exactly `text`, so the
 * panels never show words that search, history and `data-message-text` do not. Also undefined when no span
 * carries a category, since an unstyled list adds nothing over the plain text.
 */
export function validateSegments(raw: unknown, text: string, eventHint = 'message'): MessageSegment[] | undefined {
  if (!Array.isArray(raw)) {
    return undefined;
  }
  const segments = raw.map(toSegment);
  if (segments.some(segment => segment === null)) {
    return undefined;
  }
  const valid = segments as MessageSegment[];
  if (valid.map(segment => segment.text).join('') !== text) {
    warnJoinMismatch(eventHint);
    return undefined;
  }
  return valid.some(segment => segment.category !== undefined) ? valid : undefined;
}

/** The plain text of a line assembled from parts, and its segments when any part is styled. */
export function buildLine(parts: SegmentPart[]): { text: string; segments?: MessageSegment[] } {
  const spans = parts.map((part): MessageSegment => (typeof part === 'string' ? { text: part } : part));
  const text = spans.map(span => span.text).join('');
  return spans.some(span => span.category !== undefined) ? { text, segments: spans } : { text };
}
