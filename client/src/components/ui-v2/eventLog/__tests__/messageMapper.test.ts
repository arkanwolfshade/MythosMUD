/**
 * Unit tests for pure combat/message mapping helpers.
 */

import { describe, expect, it } from 'vitest';

import type { Player } from '../../types';
import {
  formatNpcAttackedLine,
  formatNpcTookDamageLine,
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

    const hit = { attacker_name: 'Deep One', target_id: 'me', target_name: 'Ada', damage: 5 };

    it('says "you" when the local player is the target, or when ids are unknown', () => {
      expect(formatPlayerAttackedLine(hit, 'me')).toBe('Deep One attacks you for 5 damage.');
      expect(formatPlayerAttackedLine(hit)).toBe('Deep One attacks you for 5 damage.');
    });

    it('names the target for bystanders (#1056)', () => {
      expect(formatPlayerAttackedLine(hit, 'someone-else')).toBe('Deep One attacks Ada for 5 damage.');
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

    const swing = { attacker_id: 'me', attacker_name: 'Ada', npc_name: 'Cultist', damage: 3 };

    it('says "You attack" for the local attacker, or when ids are unknown', () => {
      expect(formatNpcAttackedLine(swing, 'me')).toBe('You attack Cultist for 3 damage.');
      expect(formatNpcAttackedLine(swing)).toBe('You attack Cultist for 3 damage.');
    });

    it('words the attacker in the third person for bystanders (#1056)', () => {
      expect(formatNpcAttackedLine(swing, 'someone-else')).toBe('Ada attacks Cultist for 3 damage.');
      expect(formatNpcAttackedLine({ ...swing, action_type: 'punch' }, 'someone-else')).toBe(
        'Ada punches Cultist for 3 damage.'
      );
    });
  });

  describe('formatNpcTookDamageLine', () => {
    it('includes current_dp/max_dp for spell damage lines', () => {
      const line = formatNpcTookDamageLine({
        npc_name: 'Nightgaunt',
        damage: 25,
        current_dp: 55,
        max_dp: 80,
      });
      expect(line).toContain('Dealt 25 damage to Nightgaunt');
      expect(line).toContain('55/80');
    });

    it('returns empty string when name or damage missing', () => {
      expect(formatNpcTookDamageLine({ npc_name: 'X' })).toBe('');
      expect(formatNpcTookDamageLine({ damage: 5 })).toBe('');
    });
  });

  describe('mergePlayerDpFromPlayerAttackedPayload', () => {
    it("leaves a bystander's own DP alone when someone else was hit (#1056)", () => {
      const bystander = { id: 'me', name: 'Ada', stats: { current_dp: 50, lucidity: 50 } } as Player;
      expect(
        mergePlayerDpFromPlayerAttackedPayload(bystander, { target_id: 'other', target_current_dp: 5 })
      ).toBeNull();
      expect(
        mergePlayerDpFromPlayerAttackedPayload(bystander, { target_id: 'me', target_current_dp: 5 })?.stats?.current_dp
      ).toBe(5);
    });

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
