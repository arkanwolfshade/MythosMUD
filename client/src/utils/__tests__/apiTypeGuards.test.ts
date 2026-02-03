/**
 * Tests for apiTypeGuards.
 * Covers type guard branches to improve global branch coverage.
 */

import { describe, expect, it } from 'vitest';
import {
  assertCharacterInfoArray,
  assertLoginResponse,
  assertProfessionArray,
  assertRefreshTokenResponse,
  assertServerCharacterResponseArray,
  assertStatsRollResponse,
  isCharacterInfoArray,
  isLoginResponse,
  isProfessionArray,
  isRefreshTokenResponse,
  isServerCharacterResponse,
  isServerCharacterResponseArray,
  isStatsRollResponse,
} from '../apiTypeGuards';

describe('apiTypeGuards', () => {
  describe('isServerCharacterResponse', () => {
    it('should return true for valid object with id', () => {
      const value = {
        id: 'char-1',
        name: 'Test',
        profession_id: 1,
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(true);
    });

    it('should return true for valid object with player_id', () => {
      const value = {
        player_id: 'player-1',
        name: 'Test',
        profession_id: 1,
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(true);
    });

    it('should return false for non-object', () => {
      expect(isServerCharacterResponse(null)).toBe(false);
      expect(isServerCharacterResponse('string')).toBe(false);
      expect(isServerCharacterResponse(123)).toBe(false);
      expect(isServerCharacterResponse([])).toBe(false);
    });

    it('should return false when name is not a string', () => {
      const value = {
        id: 'char-1',
        name: 123,
        profession_id: 1,
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(false);
    });

    it('should return false when profession_id is not a number', () => {
      const value = {
        id: 'char-1',
        name: 'Test',
        profession_id: '1',
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(false);
    });

    it('should return true for valid object with profession_name string', () => {
      const value = {
        id: 'char-1',
        name: 'Test',
        profession_id: 1,
        profession_name: 'Scholar',
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(true);
    });

    it('should return false when both id and player_id are invalid (not undefined and not string)', () => {
      const value = {
        id: 123,
        player_id: 456,
        name: 'Test',
        profession_id: 1,
        level: 1,
        created_at: '2020-01-01',
        last_active: '2020-01-01',
      };
      expect(isServerCharacterResponse(value)).toBe(false);
    });
  });

  describe('isServerCharacterResponseArray', () => {
    it('should return true for array of valid server character responses', () => {
      const value = [
        {
          id: 'char-1',
          name: 'Test',
          profession_id: 1,
          level: 1,
          created_at: '2020-01-01',
          last_active: '2020-01-01',
        },
      ];
      expect(isServerCharacterResponseArray(value)).toBe(true);
    });

    it('should return false for non-array', () => {
      expect(isServerCharacterResponseArray({})).toBe(false);
      expect(isServerCharacterResponseArray(null)).toBe(false);
    });

    it('should return false when array contains invalid item', () => {
      const value = [
        {
          id: 'char-1',
          name: 123,
          profession_id: 1,
          level: 1,
          created_at: '2020-01-01',
          last_active: '2020-01-01',
        },
      ];
      expect(isServerCharacterResponseArray(value)).toBe(false);
    });
  });

  describe('isStatsRollResponse', () => {
    const validStats = {
      strength: 10,
      dexterity: 10,
      constitution: 10,
      size: 10,
      intelligence: 10,
      power: 10,
      education: 10,
      charisma: 10,
      luck: 10,
    };
    const validStatSummary = { total: 90, average: 10, highest: 12, lowest: 8 };

    it('should return true for valid stats roll response', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(true);
    });

    it('should return true with profession_id and meets_requirements', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        profession_id: 1,
        meets_requirements: true,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(true);
    });

    it('should return false for non-object', () => {
      expect(isStatsRollResponse(null)).toBe(false);
      expect(isStatsRollResponse('string')).toBe(false);
    });

    it('should return false when stats is not an object', () => {
      const value = {
        stats: 'invalid',
        stat_summary: validStatSummary,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(false);
    });

    it('should return false when a stat is not a number', () => {
      const badStats = { ...validStats, strength: '10' };
      const value = {
        stats: badStats,
        stat_summary: validStatSummary,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(false);
    });

    it('should return false when stat_summary is invalid', () => {
      const value = {
        stats: validStats,
        stat_summary: { total: 90 },
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(false);
    });

    it('should return false when method_used is not a string', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        method_used: 123,
      };
      expect(isStatsRollResponse(value)).toBe(false);
    });

    it('should return true with profession_id null and meets_requirements null', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        profession_id: null,
        meets_requirements: null,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(true);
    });

    it('should return true with meets_requirements false', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        profession_id: 1,
        meets_requirements: false,
        method_used: 'standard',
      };
      expect(isStatsRollResponse(value)).toBe(true);
    });
  });

  describe('isRefreshTokenResponse', () => {
    it('should return true for valid response with refresh_token', () => {
      const value = {
        access_token: 'access',
        expires_in: 3600,
        refresh_token: 'refresh',
      };
      expect(isRefreshTokenResponse(value)).toBe(true);
    });

    it('should return true for valid response without refresh_token', () => {
      const value = {
        access_token: 'access',
        expires_in: 3600,
      };
      expect(isRefreshTokenResponse(value)).toBe(true);
    });

    it('should return false for non-object', () => {
      expect(isRefreshTokenResponse(null)).toBe(false);
    });

    it('should return false when access_token is not a string', () => {
      const value = {
        access_token: 123,
        expires_in: 3600,
      };
      expect(isRefreshTokenResponse(value)).toBe(false);
    });

    it('should return false when expires_in is not a number', () => {
      const value = {
        access_token: 'access',
        expires_in: '3600',
      };
      expect(isRefreshTokenResponse(value)).toBe(false);
    });
  });

  describe('assertServerCharacterResponseArray', () => {
    it('should return value when valid', () => {
      const value = [
        {
          id: 'char-1',
          name: 'Test',
          profession_id: 1,
          level: 1,
          created_at: '2020-01-01',
          last_active: '2020-01-01',
        },
      ];
      expect(assertServerCharacterResponseArray(value)).toEqual(value);
    });

    it('should throw with default message when invalid', () => {
      expect(() => assertServerCharacterResponseArray(null)).toThrow(
        'Invalid API response: expected ServerCharacterResponse[]'
      );
    });

    it('should throw with custom message when invalid', () => {
      expect(() => assertServerCharacterResponseArray({}, 'Custom error')).toThrow('Custom error');
    });
  });

  describe('assertStatsRollResponse', () => {
    const validStats = {
      strength: 10,
      dexterity: 10,
      constitution: 10,
      size: 10,
      intelligence: 10,
      power: 10,
      education: 10,
      charisma: 10,
      luck: 10,
    };
    const validStatSummary = { total: 90, average: 10, highest: 12, lowest: 8 };

    it('should return value when valid', () => {
      const value = {
        stats: validStats,
        stat_summary: validStatSummary,
        method_used: 'standard',
      };
      expect(assertStatsRollResponse(value)).toEqual(value);
    });

    it('should throw with custom message when invalid', () => {
      expect(() => assertStatsRollResponse(null, 'Bad stats')).toThrow('Bad stats');
    });
  });

  describe('assertRefreshTokenResponse', () => {
    it('should return value when valid', () => {
      const value = {
        access_token: 'access',
        expires_in: 3600,
      };
      expect(assertRefreshTokenResponse(value)).toEqual(value);
    });

    it('should throw when invalid', () => {
      expect(() => assertRefreshTokenResponse(null)).toThrow();
    });
  });

  describe('isProfession', () => {
    const validProfession = {
      id: 1,
      name: 'Scholar',
      description: 'A seeker of knowledge.',
      flavor_text: 'You have studied the occult.',
      stat_requirements: [] as { stat: string; minimum: number }[],
      mechanical_effects: [] as { effect_type: string; value: number | string; description?: string | null }[],
      is_available: true,
    };

    it('should return true for valid profession with flavor_text string', () => {
      expect(isProfessionArray([validProfession])).toBe(true);
    });

    it('should return true for valid profession with flavor_text null', () => {
      const p = { ...validProfession, flavor_text: null };
      expect(isProfessionArray([p])).toBe(true);
    });

    it('should return false when stat_requirements is not an array', () => {
      const value = [{ ...validProfession, stat_requirements: 'invalid' }];
      expect(isProfessionArray(value)).toBe(false);
    });

    it('should return false when stat_requirements contains invalid item', () => {
      const value = [
        {
          ...validProfession,
          stat_requirements: [{ stat: 'str', minimum: '10' }],
        },
      ];
      expect(isProfessionArray(value)).toBe(false);
    });

    it('should return false when mechanical_effects is not an array', () => {
      const value = [{ ...validProfession, mechanical_effects: {} }];
      expect(isProfessionArray(value)).toBe(false);
    });

    it('should return false when mechanical_effects contains invalid item', () => {
      const value = [
        {
          ...validProfession,
          mechanical_effects: [{ effect_type: 'buff', value: 1, description: 123 }],
        },
      ];
      expect(isProfessionArray(value)).toBe(false);
    });

    it('should return false for non-array', () => {
      expect(isProfessionArray(null)).toBe(false);
      expect(isProfessionArray({})).toBe(false);
    });
  });

  describe('assertCharacterInfoArray', () => {
    it('should throw with custom message when invalid', () => {
      expect(() => assertCharacterInfoArray(null, 'Custom CharacterInfo error')).toThrow('Custom CharacterInfo error');
    });
  });

  describe('assertLoginResponse', () => {
    it('should throw with custom message when invalid', () => {
      expect(() => assertLoginResponse({}, 'Custom LoginResponse error')).toThrow('Custom LoginResponse error');
    });
  });

  describe('assertProfessionArray', () => {
    it('should throw with custom message when invalid', () => {
      expect(() => assertProfessionArray(null, 'Custom ProfessionArray error')).toThrow('Custom ProfessionArray error');
    });
  });

  describe('isCharacterInfoArray', () => {
    it('should return true for valid array of CharacterInfo', () => {
      const value = [
        {
          player_id: 'p1',
          name: 'Test',
          profession_id: 1,
          level: 1,
          created_at: '2020-01-01',
          last_active: '2020-01-01',
        },
      ];
      expect(isCharacterInfoArray(value)).toBe(true);
    });

    it('should return false for non-array', () => {
      expect(isCharacterInfoArray(null)).toBe(false);
    });
  });

  describe('isLoginResponse', () => {
    it('should return true for valid LoginResponse with refresh_token', () => {
      const value = {
        access_token: 'token',
        token_type: 'Bearer',
        user_id: 'u1',
        characters: [
          {
            player_id: 'p1',
            name: 'Test',
            profession_id: 1,
            level: 1,
            created_at: '2020-01-01',
            last_active: '2020-01-01',
          },
        ],
        refresh_token: 'refresh',
      };
      expect(isLoginResponse(value)).toBe(true);
    });

    it('should return false for non-object', () => {
      expect(isLoginResponse(null)).toBe(false);
    });
  });
});
