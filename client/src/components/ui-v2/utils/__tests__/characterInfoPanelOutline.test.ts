import { describe, expect, it } from 'vitest';
import type { HealthStatus } from '../../../../types/health';
import type { Player } from '../../types';
import { getCharacterInfoPanelOutlineClassName, getGameInfoPanelCombatClassName } from '../characterInfoPanelOutline';

describe('characterInfoPanelOutline', () => {
  const basePlayer = (overrides: Partial<Player['stats']> = {}): Player => ({
    id: 'p1',
    name: 'x',
    stats: {
      current_dp: 80,
      max_dp: 100,
      lucidity: 50,
      magic_points: 20,
      max_magic_points: 20,
      ...overrides,
    },
  });

  it('uses amber outline when DP is steady even if MP is full', () => {
    const health: HealthStatus = {
      current: 50,
      max: 100,
      tier: 'steady',
    };
    const player = basePlayer({ magic_points: 20, max_magic_points: 20 });
    const cls = getCharacterInfoPanelOutlineClassName(health, player);
    expect(cls).toContain('border-amber-400');
    expect(cls).toContain('animate-mythos-glow-amber');
  });

  it('uses emerald outline when DP is vigorous and MP is healthy', () => {
    const health: HealthStatus = {
      current: 90,
      max: 100,
      tier: 'vigorous',
    };
    const player = basePlayer({ magic_points: 20, max_magic_points: 20 });
    const cls = getCharacterInfoPanelOutlineClassName(health, player);
    expect(cls).toContain('border-emerald-500');
    expect(cls).toContain('animate-mythos-glow-emerald');
  });

  it('escalates to worst of DP and MP', () => {
    const health: HealthStatus = {
      current: 90,
      max: 100,
      tier: 'vigorous',
    };
    const player = basePlayer({ magic_points: 1, max_magic_points: 20 });
    const cls = getCharacterInfoPanelOutlineClassName(health, player);
    expect(cls).toContain('border-orange-500');
  });

  it('returns empty string when no DP tier and no MP stats', () => {
    const player = { id: 'p1', name: 'x', stats: { current_dp: 0, max_dp: 100 } } as Player;
    expect(getCharacterInfoPanelOutlineClassName(null, player)).toBe('');
  });

  it('adds combat class for Game Info when in combat', () => {
    expect(getGameInfoPanelCombatClassName(false)).toBe('');
    expect(getGameInfoPanelCombatClassName(true)).toContain('animate-mythos-glow-combat');
  });
});
