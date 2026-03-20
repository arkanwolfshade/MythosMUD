/**
 * Unit tests for pure combat/message mapping helpers.
 */

import { describe, expect, it } from 'vitest';

import type { Player } from '../../types';
import {
  formatNpcAttackedLine,
  formatPlayerAttackedLine,
  mergePlayerDpFromPlayerAttackedPayload,
} from '../messageMapper';

describe('messageMapper', () => {
  describe('formatPlayerAttackedLine', () => {
    it('includes DP parenthetical when target DP present', () => {
      const line = formatPlayerAttackedLine({
        attacker_name: 'Deep One',
        action_type: 'auto_attack',
        damage: 5,
        target_current_dp: 40,
        target_max_dp: 100,
      });
      expect(line).toContain('40/100');
      expect(line).toContain('Deep One');
    });
  });

  describe('formatNpcAttackedLine', () => {
    it('includes DP parenthetical when target DP present', () => {
      const line = formatNpcAttackedLine({
        npc_name: 'Cultist',
        action_type: 'auto_attack',
        damage: 3,
        target_current_dp: 12,
        target_max_dp: 50,
      });
      expect(line).toContain('12/50');
    });
  });

  describe('mergePlayerDpFromPlayerAttackedPayload', () => {
    it('returns null when player or target_current_dp missing', () => {
      expect(mergePlayerDpFromPlayerAttackedPayload(null, { target_current_dp: 5 })).toBeNull();
      const p: Player = {
        name: 'x',
        stats: { current_dp: 10, lucidity: 50 },
      };
      expect(mergePlayerDpFromPlayerAttackedPayload(p, {})).toBeNull();
    });

    it('merges target_current_dp and target_max_dp into player stats', () => {
      const prev: Player = {
        name: 'Hero',
        stats: { current_dp: 100, max_dp: 100, lucidity: 50 },
      };
      const next = mergePlayerDpFromPlayerAttackedPayload(prev, {
        target_current_dp: 42,
        target_max_dp: 100,
      });
      expect(next?.stats?.current_dp).toBe(42);
      expect(next?.stats?.max_dp).toBe(100);
      expect(next?.stats?.lucidity).toBe(50);
    });
  });
});
