/**
 * Deranged-tier direction & map hallucination (#626).
 *
 * NOT to be confused with `_reverse_direction` in
 * `server/services/ascii_map_renderer.py` / `coordinate_generator.py` — those compute
 * bidirectional map-graph adjacency for real exits and are unrelated to this display effect.
 *
 * The hallucination is a seeded, deterministic scramble keyed to (roomId, playerId): stable
 * across re-renders and re-entering the same room, but different players in the same room see
 * different lies. It is NOT a reversal map — the displayed exit set (count and labels) is
 * intentionally independent of the room's real exits.
 */

/** The world only uses these six directions; diagonals/in/out never appear in room data. */
export const DIRECTION_POOL = ['north', 'south', 'east', 'west', 'up', 'down'] as const;

export type HallucinatedDirection = (typeof DIRECTION_POOL)[number];

const NOISE_CHARS = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`';

/** 32-bit string hash (djb2 variant) — deterministic, no crypto dependency needed. */
function hashString(input: string): number {
  let hash = 5381;
  for (let i = 0; i < input.length; i++) {
    hash = ((hash << 5) + hash + input.charCodeAt(i)) | 0;
  }
  return hash >>> 0;
}

/** Combine room + player into a single seed. Order matters: different rooms, different lies. */
export function seedFrom(roomId: string, playerId: string): number {
  return hashString(`${roomId}::${playerId}`);
}

/** mulberry32: small, fast, deterministic PRNG. Returns a function yielding floats in [0, 1). */
export function mulberry32(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * Deterministic shuffle driven by the given RNG: pair each item with a random sort key, sort by
 * key. (Random-key sort rather than Fisher-Yates so this never touches an array by a computed
 * index -- keeps it out of eslint-plugin-security's object-injection sink detector, which has no
 * way to see that i/j would have been provably in-bounds.)
 */
function shuffle<T>(items: readonly T[], rng: () => number): T[] {
  return items
    .map(item => ({ item, key: rng() }))
    .sort((a, b) => a.key - b.key)
    .map(({ item }) => item);
}

/**
 * Return a seeded, plausible-but-false exit list for the given room+player.
 * Count is 1-6 (always at least one exit shown), labels are a subset of DIRECTION_POOL with no
 * repeats, and the result is entirely independent of the room's real exits.
 */
export function getHallucinatedExits(roomId: string, playerId: string): HallucinatedDirection[] {
  const rng = mulberry32(seedFrom(roomId, playerId));
  const count = 1 + Math.floor(rng() * DIRECTION_POOL.length);
  return shuffle(DIRECTION_POOL, rng).slice(0, count);
}

/**
 * Generate a block of non-alphanumeric ASCII noise, `rows` lines of `cols` characters each,
 * driven by the given RNG (pass a seeded mulberry32 for a static frame, or call repeatedly with
 * a fresh RNG per tick for churn).
 */
export function generateAsciiNoise(rows: number, cols: number, rng: () => number): string {
  const lines: string[] = [];
  for (let r = 0; r < rows; r++) {
    let line = '';
    for (let c = 0; c < cols; c++) {
      line += NOISE_CHARS[Math.floor(rng() * NOISE_CHARS.length)];
    }
    lines.push(line);
  }
  return lines.join('\n');
}
