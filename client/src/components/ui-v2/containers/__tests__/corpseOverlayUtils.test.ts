/**
 * Unit tests for corpseOverlayUtils.ts (#711): grace-period / decay countdown math.
 */

import { describe, expect, it, vi } from 'vitest';
import type { RoomContainerSummary } from '../../types';
import {
  calculateTimeRemaining,
  formatTimeRemaining,
  getCorpseTiming,
  isCorpseOwner,
  isGracePeriodActive,
} from '../corpseOverlayUtils';

function corpse(overrides: Partial<RoomContainerSummary> = {}): RoomContainerSummary {
  return {
    container_id: 'c1',
    source_type: 'corpse',
    owner_id: 'owner-1',
    ...overrides,
  };
}

describe('formatTimeRemaining', () => {
  it('shows hours and minutes when over an hour remains', () => {
    expect(formatTimeRemaining(3725)).toBe('1h 2m');
  });

  it('shows minutes and seconds when under an hour remains', () => {
    expect(formatTimeRemaining(125)).toBe('2m 5s');
  });

  it('shows only seconds when under a minute remains', () => {
    expect(formatTimeRemaining(45)).toBe('45s');
  });

  it('shows Expired at zero or negative', () => {
    expect(formatTimeRemaining(0)).toBe('Expired');
    expect(formatTimeRemaining(-10)).toBe('Expired');
  });
});

describe('calculateTimeRemaining', () => {
  it('returns null for a missing target date', () => {
    expect(calculateTimeRemaining(undefined)).toBeNull();
    expect(calculateTimeRemaining(null)).toBeNull();
  });

  it('computes hours/minutes/seconds/totalSeconds for a future date', () => {
    const target = new Date(Date.now() + 3725_000).toISOString();
    const result = calculateTimeRemaining(target);
    expect(result?.totalSeconds).toBeGreaterThanOrEqual(3724);
    expect(result?.totalSeconds).toBeLessThanOrEqual(3725);
    expect(result?.hours).toBe(1);
  });

  it('clamps a past date to zero rather than going negative', () => {
    const result = calculateTimeRemaining(new Date(Date.now() - 10_000).toISOString());
    expect(result?.totalSeconds).toBe(0);
  });
});

describe('isCorpseOwner', () => {
  it('is true when owner_id matches the given player id', () => {
    expect(isCorpseOwner(corpse({ owner_id: 'p1' }), 'p1')).toBe(true);
  });

  it('is false for a different player, or an undefined player id', () => {
    expect(isCorpseOwner(corpse({ owner_id: 'p1' }), 'p2')).toBe(false);
    expect(isCorpseOwner(corpse({ owner_id: 'p1' }), undefined)).toBe(false);
  });

  it('is false when the corpse has no owner, even for an unidentified viewer', () => {
    // Regression (#711): `undefined === undefined` made every viewer the owner, which dropped the
    // grace-period lock for everyone the moment either id was missing from a room summary.
    expect(isCorpseOwner(corpse({ owner_id: null }), undefined)).toBe(false);
    expect(isCorpseOwner(corpse({ owner_id: null }), 'p1')).toBe(false);
    expect(isCorpseOwner(corpse({ owner_id: 'p1' }), '')).toBe(false);
  });

  it('keeps a non-owner locked out during grace when ownership cannot be proven', () => {
    const start = new Date().toISOString();
    const timing = getCorpseTiming(
      corpse({ owner_id: null, metadata: { grace_period_start: start, grace_period_seconds: 300 } }),
      undefined
    );
    expect(timing.canOpen).toBe(false);
  });
});

describe('isGracePeriodActive', () => {
  it('is false when there is no grace_period_start in metadata', () => {
    expect(isGracePeriodActive(corpse({ metadata: {} }))).toBe(false);
  });

  it('is true within the grace window, false after it elapses', () => {
    const active = corpse({
      metadata: { grace_period_start: new Date().toISOString(), grace_period_seconds: 300 },
    });
    expect(isGracePeriodActive(active)).toBe(true);

    const elapsed = corpse({
      metadata: { grace_period_start: new Date(Date.now() - 400_000).toISOString(), grace_period_seconds: 300 },
    });
    expect(isGracePeriodActive(elapsed)).toBe(false);
  });

  it('defaults grace_period_seconds to 300 when metadata omits it', () => {
    const withinDefault = corpse({ metadata: { grace_period_start: new Date(Date.now() - 100_000).toISOString() } });
    expect(isGracePeriodActive(withinDefault)).toBe(true);
    const pastDefault = corpse({ metadata: { grace_period_start: new Date(Date.now() - 400_000).toISOString() } });
    expect(isGracePeriodActive(pastDefault)).toBe(false);
  });
});

describe('getCorpseTiming', () => {
  it('canOpen is true for the owner even during an active grace period', () => {
    const c = corpse({
      owner_id: 'owner-1',
      metadata: { grace_period_start: new Date().toISOString(), grace_period_seconds: 300 },
    });
    const timing = getCorpseTiming(c, 'owner-1');
    expect(timing.canOpen).toBe(true);
    expect(timing.graceRemaining?.totalSeconds).toBeGreaterThan(0);
  });

  it('canOpen is false for a non-owner during an active grace period', () => {
    const c = corpse({
      owner_id: 'owner-1',
      metadata: { grace_period_start: new Date().toISOString(), grace_period_seconds: 300 },
    });
    expect(getCorpseTiming(c, 'someone-else').canOpen).toBe(false);
  });

  it('canOpen is true for anyone once grace period has elapsed', () => {
    const c = corpse({
      owner_id: 'owner-1',
      metadata: { grace_period_start: new Date(Date.now() - 400_000).toISOString(), grace_period_seconds: 300 },
    });
    expect(getCorpseTiming(c, 'someone-else').canOpen).toBe(true);
  });

  it('computes decayRemaining from decay_at', () => {
    // Pin the clock: with a live clock, the milliseconds between building decay_at and
    // getCorpseTiming reading Date.now() left 59:59.x, which floored to 0 hours (flaky).
    vi.useFakeTimers();
    try {
      vi.setSystemTime(new Date('2026-01-01T00:00:00Z'));
      const c = corpse({ decay_at: new Date(Date.now() + 3600_000).toISOString(), metadata: {} });
      const timing = getCorpseTiming(c, 'owner-1');
      expect(timing.decayRemaining?.hours).toBe(1);
    } finally {
      vi.useRealTimers();
    }
  });
});
