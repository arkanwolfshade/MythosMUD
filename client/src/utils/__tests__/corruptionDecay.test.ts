import { describe, expect, it } from 'vitest';
import { ageBucket, decayMessageText, MYTHOS_GLYPHS } from '../corruptionDecay';

const FIVE_MIN_MS = 5 * 60 * 1000;

function timestampMinutesAgo(minutes: number, now: number): string {
  return new Date(now - minutes * 60 * 1000).toISOString();
}

describe('ageBucket', () => {
  const now = Date.now();

  it('is 0 for a brand-new message', () => {
    expect(ageBucket(new Date(now).toISOString(), now)).toBe(0);
  });

  it('advances one bucket per 5 minutes', () => {
    expect(ageBucket(timestampMinutesAgo(5, now), now)).toBe(1);
    expect(ageBucket(timestampMinutesAgo(12, now), now)).toBe(2);
  });

  it('caps at the maximum bucket for very old messages', () => {
    expect(ageBucket(timestampMinutesAgo(1000, now), now)).toBe(6);
  });

  it('treats an unparsable timestamp as brand-new (bucket 0)', () => {
    expect(ageBucket('not-a-date', now)).toBe(0);
  });
});

describe('decayMessageText', () => {
  const now = Date.now();
  const oldTimestamp = timestampMinutesAgo(60, now); // well past the max bucket

  it('returns text unchanged at zero corruption regardless of age', () => {
    const text = 'The stars are wrong tonight';
    expect(decayMessageText(text, 0, oldTimestamp, now)).toBe(text);
  });

  it('returns text unchanged for a brand-new message regardless of corruption', () => {
    const text = 'The stars are wrong tonight';
    expect(decayMessageText(text, 100, new Date(now).toISOString(), now)).toBe(text);
  });

  it('is deterministic for the same inputs', () => {
    const text = 'The stars are wrong tonight and the walls are breathing';
    const first = decayMessageText(text, 80, oldTimestamp, now);
    const second = decayMessageText(text, 80, oldTimestamp, now);
    expect(first).toBe(second);
  });

  it('never alters numbers', () => {
    const text = 'You take 42 damage and lose 7 gold';
    const decayed = decayMessageText(text, 100, oldTimestamp, now);
    expect(decayed).toContain('42');
    expect(decayed).toContain('7');
  });

  it('never alters capitalized tokens (best-effort name protection)', () => {
    const text = 'ArkanWolfshade says: the ritual is complete';
    const decayed = decayMessageText(text, 100, oldTimestamp, now);
    expect(decayed).toContain('ArkanWolfshade');
  });

  it('never replaces more than 25% of eligible words, even at maximum intensity', () => {
    const text = 'one two three four five six seven eight nine ten eleven twelve';
    const eligibleWordCount = text.split(' ').length; // all lowercase, all eligible
    const decayed = decayMessageText(text, 100, oldTimestamp, now);
    const glyphCount = MYTHOS_GLYPHS.reduce((count, glyph) => count + decayed.split(glyph).length - 1, 0);
    expect(glyphCount).toBeLessThanOrEqual(Math.round(eligibleWordCount * 0.25));
  });

  it('produces only glyphs from the shared vocabulary when it does substitute', () => {
    const text = 'one two three four five six seven eight nine ten eleven twelve';
    const decayed = decayMessageText(text, 100, oldTimestamp, now);
    const decayedWords = decayed.split(/\s+/);
    for (const word of decayedWords) {
      const isOriginal = text.split(/\s+/).includes(word);
      if (!isOriginal) {
        expect(MYTHOS_GLYPHS).toContain(word);
      }
    }
  });
});

// Sanity: age buckets are exactly 5 minutes, matching the design doc.
describe('AGE_BUCKET_MS assumption', () => {
  it('one bucket boundary is exactly 5 minutes', () => {
    const now = Date.now();
    const justUnder = new Date(now - (FIVE_MIN_MS - 1000)).toISOString();
    const justOver = new Date(now - (FIVE_MIN_MS + 1000)).toISOString();
    expect(ageBucket(justUnder, now)).toBe(0);
    expect(ageBucket(justOver, now)).toBe(1);
  });
});
