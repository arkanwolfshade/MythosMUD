/**
 * Client-side corruption message decay (#804, #145's "existing messages change over time").
 *
 * Pure, deterministic pass over already-buffered chat history: given a corruption value and a
 * message's age, some of its words are replaced with glyphs. Same inputs always produce the same
 * output (seeded by the message's own timestamp+text), so re-renders never flicker as new
 * messages arrive. This never touches the server-stored copy or re-fetches history -- it only
 * changes what the client renders (SUBSYSTEM_CORRUPTION_DESIGN.md §5.3).
 *
 * The global filter driven by --corruption-intensity (ChatHistoryPanel.tsx) is a separate,
 * always-on effect; this decay pass is the "messages change over time" piece specifically.
 */

import { hashString, mulberry32 } from './directionHallucination';

/** Same glyph vocabulary as the server's lucidity dampening effect (visual continuity, #714). */
export const MYTHOS_GLYPHS = ['☁', '☂', '☃', '☄', '★', '☆', '☇', '☈'];

/** Accessibility floor (SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md §3.1): never garble more
 * than 25% of a message's content. */
const MAX_DECAY_FRACTION = 0.25;

/** Coarse age buckets (5 minutes) so decay advances in discrete steps, not continuously -- a
 * continuously-changing render would itself be motion. Reaches full age weight after 30 minutes. */
const AGE_BUCKET_MS = 5 * 60 * 1000;
const MAX_AGE_BUCKETS = 6;

/** How many 5-minute buckets old a message is, capped at MAX_AGE_BUCKETS. */
export function ageBucket(messageTimestamp: string, now: number = Date.now()): number {
  const ts = Date.parse(messageTimestamp);
  if (Number.isNaN(ts)) return 0;
  return Math.min(MAX_AGE_BUCKETS, Math.floor(Math.max(0, now - ts) / AGE_BUCKET_MS));
}

/**
 * Best-effort "don't corrupt this token" check (§3.2: names and numbers are never corrupted).
 * There is no client-side player/room/item name roster to check against, so a capitalized token
 * is treated as a proper noun -- this also protects the leading "Name says:" prefix chat messages
 * are typically formatted with.
 */
function isProtectedToken(token: string): boolean {
  if (/^\d+$/.test(token)) return true;
  if (/^[A-Z]/.test(token)) return true;
  if (!/[a-zA-Z]/.test(token)) return true; // punctuation-only, nothing to protect or corrupt
  return false;
}

/**
 * Decay a message's text based on corruption (0-100) and its own age. Returns the text unchanged
 * when corruption is 0, the message is fresh, or nothing eligible is found to alter.
 */
export function decayMessageText(text: string, corruption: number, messageTimestamp: string, now?: number): string {
  const corruptionFraction = Math.max(0, Math.min(1, corruption / 100));
  const ageFraction = ageBucket(messageTimestamp, now) / MAX_AGE_BUCKETS;
  const intensity = corruptionFraction * ageFraction;
  if (intensity <= 0) return text;

  const tokens = text.split(/(\s+)/); // whitespace runs kept as their own entries, for reassembly
  const eligibleIndices = tokens
    .map((token, index) => ({ token, index }))
    .filter(({ token }) => token.trim().length > 0 && !isProtectedToken(token))
    .map(({ index }) => index);
  if (eligibleIndices.length === 0) return text;

  const budget = Math.round(eligibleIndices.length * Math.min(MAX_DECAY_FRACTION, intensity));
  if (budget <= 0) return text;

  const rng = mulberry32(hashString(`${messageTimestamp}::${text}`));
  const chosen = new Set(
    eligibleIndices
      .map(index => ({ index, key: rng() }))
      .sort((a, b) => a.key - b.key)
      .slice(0, budget)
      .map(({ index }) => index)
  );

  return tokens
    .map((token, index) => (chosen.has(index) ? MYTHOS_GLYPHS[Math.floor(rng() * MYTHOS_GLYPHS.length)] : token))
    .join('');
}
