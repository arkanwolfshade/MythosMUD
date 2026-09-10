/**
 * Corruption tier names (#804, #815), mirroring `server/models/corruption.py`'s `compute_tier`.
 * Display-only on the client -- the server is authoritative for anything that reads the tier as
 * game state; this exists so the character sheet can show a name next to the raw number.
 */

export type CorruptionTier = 'pure' | 'touched' | 'marked' | 'corrupted' | 'warped';

export function computeCorruptionTier(value: number): CorruptionTier {
  if (value >= 75) return 'warped';
  if (value >= 50) return 'corrupted';
  if (value >= 25) return 'marked';
  if (value >= 1) return 'touched';
  return 'pure';
}
