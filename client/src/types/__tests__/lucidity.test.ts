/**
 * Tests for lucidity type definitions and utilities
 *
 * These tests verify that the type definitions are correctly structured
 * and can be used in TypeScript code.
 */

import { describe, expect, it } from 'vitest';
import type { LucidityChangeMeta, LucidityStatus, LucidityTier } from '../lucidity';

describe('Lucidity Types', () => {
  describe('LucidityTier', () => {
    it('should accept valid lucidity tier values', () => {
      const tiers: LucidityTier[] = ['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic'];

      tiers.forEach(tier => {
        expect(typeof tier).toBe('string');
        expect(['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic']).toContain(tier);
      });
    });
  });

  describe('LucidityStatus', () => {
    it('should create valid LucidityStatus object', () => {
      const status: LucidityStatus = {
        current: 50,
        max: 100,
        tier: 'uneasy',
        liabilities: ['anxiety', 'paranoia'],
      };

      expect(status.current).toBe(50);
      expect(status.max).toBe(100);
      expect(status.tier).toBe('uneasy');
      expect(status.liabilities).toEqual(['anxiety', 'paranoia']);
    });

    it('should accept optional lastChange property', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: -10,
        reason: 'Witnessed eldritch horror',
        source: 'combat',
        timestamp: new Date().toISOString(),
      };

      const status: LucidityStatus = {
        current: 40,
        max: 100,
        tier: 'fractured',
        liabilities: [],
        lastChange: changeMeta,
      };

      expect(status.lastChange).toBeDefined();
      expect(status.lastChange?.delta).toBe(-10);
      expect(status.lastChange?.reason).toBe('Witnessed eldritch horror');
    });
  });

  describe('LucidityChangeMeta', () => {
    it('should create valid LucidityChangeMeta object', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: -15,
        reason: 'Read forbidden tome',
        source: 'item',
        timestamp: new Date().toISOString(),
      };

      expect(changeMeta.delta).toBe(-15);
      expect(changeMeta.reason).toBe('Read forbidden tome');
      expect(changeMeta.source).toBe('item');
      expect(typeof changeMeta.timestamp).toBe('string');
    });

    it('should accept optional reason and source', () => {
      const changeMeta: LucidityChangeMeta = {
        delta: 5,
        timestamp: new Date().toISOString(),
      };

      expect(changeMeta.delta).toBe(5);
      expect(changeMeta.reason).toBeUndefined();
      expect(changeMeta.source).toBeUndefined();
    });
  });

  describe('Type Compatibility', () => {
    it('should allow LucidityStatus to be used in arrays', () => {
      const statuses: LucidityStatus[] = [
        {
          current: 100,
          max: 100,
          tier: 'lucid',
          liabilities: [],
        },
        {
          current: 50,
          max: 100,
          tier: 'uneasy',
          liabilities: ['anxiety'],
        },
      ];

      expect(statuses.length).toBe(2);
      expect(statuses[0].tier).toBe('lucid');
      expect(statuses[1].tier).toBe('uneasy');
    });
  });
});
