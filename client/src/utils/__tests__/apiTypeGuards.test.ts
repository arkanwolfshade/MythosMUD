/**
 * Tests for apiTypeGuards.
 * Covers type guard branches to improve global branch coverage.
 */

import { describe, expect, it } from 'vitest';
import {
  assertRefreshTokenResponse,
  assertServerCharacterResponseArray,
  assertStatsRollResponse,
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
});
