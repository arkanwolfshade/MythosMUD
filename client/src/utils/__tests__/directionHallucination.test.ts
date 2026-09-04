import { describe, expect, it } from 'vitest';
import {
  DIRECTION_POOL,
  generateAsciiNoise,
  getHallucinatedExits,
  mulberry32,
  seedFrom,
} from '../directionHallucination';

describe('seedFrom', () => {
  it('is deterministic for the same room+player', () => {
    expect(seedFrom('room-1', 'player-1')).toBe(seedFrom('room-1', 'player-1'));
  });

  it('differs across rooms for the same player', () => {
    expect(seedFrom('room-1', 'player-1')).not.toBe(seedFrom('room-2', 'player-1'));
  });

  it('differs across players for the same room', () => {
    expect(seedFrom('room-1', 'player-1')).not.toBe(seedFrom('room-1', 'player-2'));
  });
});

describe('mulberry32', () => {
  it('is deterministic for a given seed', () => {
    const rngA = mulberry32(42);
    const rngB = mulberry32(42);
    const seqA = [rngA(), rngA(), rngA()];
    const seqB = [rngB(), rngB(), rngB()];
    expect(seqA).toEqual(seqB);
  });

  it('produces values in [0, 1)', () => {
    const rng = mulberry32(7);
    for (let i = 0; i < 50; i++) {
      const v = rng();
      expect(v).toBeGreaterThanOrEqual(0);
      expect(v).toBeLessThan(1);
    }
  });
});

describe('getHallucinatedExits', () => {
  it('is stable across repeated calls for the same room+player (re-render / re-entering room)', () => {
    const first = getHallucinatedExits('room-1', 'player-1');
    const second = getHallucinatedExits('room-1', 'player-1');
    expect(second).toEqual(first);
  });

  it('differs between two players in the same room (very likely, not guaranteed by design)', () => {
    // Deterministic fixture pair known to diverge; guards against silently collapsing to reversal-map behavior.
    const a = getHallucinatedExits('room-1', 'player-1');
    const b = getHallucinatedExits('room-1', 'player-2');
    expect(a).not.toEqual(b);
  });

  it('always returns between 1 and 6 directions', () => {
    for (let i = 0; i < 100; i++) {
      const exits = getHallucinatedExits(`room-${i}`, 'player-1');
      expect(exits.length).toBeGreaterThanOrEqual(1);
      expect(exits.length).toBeLessThanOrEqual(DIRECTION_POOL.length);
    }
  });

  it('never repeats a direction within one result', () => {
    for (let i = 0; i < 100; i++) {
      const exits = getHallucinatedExits(`room-${i}`, `player-${i}`);
      expect(new Set(exits).size).toBe(exits.length);
    }
  });

  it('only draws from the 6-direction pool', () => {
    for (let i = 0; i < 100; i++) {
      const exits = getHallucinatedExits(`room-${i}`, 'player-1');
      for (const dir of exits) {
        expect(DIRECTION_POOL).toContain(dir);
      }
    }
  });

  it('is independent of the room’s real exits (pure function of ids only)', () => {
    // The function takes no room-exit data at all -- this is a signature/contract check.
    expect(getHallucinatedExits.length).toBe(2);
  });
});

describe('generateAsciiNoise', () => {
  it('produces the requested dimensions', () => {
    const rng = mulberry32(1);
    const noise = generateAsciiNoise(5, 10, rng);
    const lines = noise.split('\n');
    expect(lines).toHaveLength(5);
    for (const line of lines) {
      expect(line).toHaveLength(10);
    }
  });

  it('contains no alphanumeric characters', () => {
    const rng = mulberry32(2);
    const noise = generateAsciiNoise(8, 40, rng);
    expect(/[a-zA-Z0-9]/.test(noise)).toBe(false);
  });

  it('is deterministic for a seeded rng', () => {
    const noiseA = generateAsciiNoise(4, 12, mulberry32(99));
    const noiseB = generateAsciiNoise(4, 12, mulberry32(99));
    expect(noiseA).toBe(noiseB);
  });
});
