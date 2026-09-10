import { describe, expect, it } from 'vitest';
import { computeCorruptionTier } from '../corruptionTier';

describe('computeCorruptionTier', () => {
  it.each([
    [0, 'pure'],
    [24, 'pure'],
    [25, 'marked'],
    [49, 'marked'],
    [50, 'corrupted'],
    [74, 'corrupted'],
    [75, 'warped'],
    [100, 'warped'],
  ] as const)('computeCorruptionTier(%i) === %s', (value, expected) => {
    expect(computeCorruptionTier(value)).toBe(expected);
  });

  it('matches the server floor for is_corrupted() (>= 50)', () => {
    expect(computeCorruptionTier(49)).not.toBe('corrupted');
    expect(computeCorruptionTier(50)).toBe('corrupted');
  });
});
