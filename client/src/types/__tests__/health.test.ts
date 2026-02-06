import { describe, expect, it } from 'vitest';
import { determineDpTier } from '../health';

describe('determineHealthTier', () => {
  describe('vigorous tier', () => {
    it('should return vigorous when ratio is exactly 0.75', () => {
      expect(determineDpTier(75, 100)).toBe('vigorous');
    });

    it('should return vigorous when ratio is above 0.75', () => {
      expect(determineDpTier(80, 100)).toBe('vigorous');
      expect(determineDpTier(100, 100)).toBe('vigorous');
      expect(determineDpTier(90, 100)).toBe('vigorous');
    });

    it('should return vigorous for high health values', () => {
      expect(determineDpTier(150, 200)).toBe('vigorous');
      expect(determineDpTier(300, 400)).toBe('vigorous');
    });
  });

  describe('steady tier', () => {
    it('should return steady when ratio is exactly 0.45', () => {
      expect(determineDpTier(45, 100)).toBe('steady');
    });

    it('should return steady when ratio is between 0.45 and 0.75', () => {
      expect(determineDpTier(50, 100)).toBe('steady');
      expect(determineDpTier(60, 100)).toBe('steady');
      expect(determineDpTier(74, 100)).toBe('steady');
    });

    it('should return steady for moderate health values', () => {
      expect(determineDpTier(90, 200)).toBe('steady');
      expect(determineDpTier(100, 200)).toBe('steady');
      expect(determineDpTier(140, 200)).toBe('steady');
    });
  });

  describe('wounded tier', () => {
    it('should return wounded when ratio is exactly 0.2', () => {
      expect(determineDpTier(20, 100)).toBe('wounded');
    });

    it('should return wounded when ratio is between 0.2 and 0.45', () => {
      expect(determineDpTier(25, 100)).toBe('wounded');
      expect(determineDpTier(30, 100)).toBe('wounded');
      expect(determineDpTier(44, 100)).toBe('wounded');
    });

    it('should return wounded for low health values', () => {
      expect(determineDpTier(40, 200)).toBe('wounded');
      expect(determineDpTier(80, 200)).toBe('wounded');
    });
  });

  describe('incapacitated tier', () => {
    it('should return incapacitated when current DP is zero or negative', () => {
      expect(determineDpTier(0, 100)).toBe('incapacitated');
      expect(determineDpTier(-10, 100)).toBe('incapacitated');
      expect(determineDpTier(-5, 100)).toBe('incapacitated');
    });
  });

  describe('critical tier', () => {
    it('should return critical when ratio is below 0.2 but current > 0', () => {
      expect(determineDpTier(10, 100)).toBe('critical');
      expect(determineDpTier(19, 100)).toBe('critical');
    });

    it('should return critical when max is zero or negative', () => {
      expect(determineDpTier(100, 0)).toBe('critical');
      expect(determineDpTier(50, 0)).toBe('critical');
      expect(determineDpTier(0, 0)).toBe('critical');
      expect(determineDpTier(100, -10)).toBe('critical');
    });

    it('should return critical for very low health values (1% to 19%)', () => {
      expect(determineDpTier(1, 100)).toBe('critical');
      expect(determineDpTier(5, 100)).toBe('critical');
      expect(determineDpTier(19, 100)).toBe('critical');
    });
  });

  describe('edge cases', () => {
    it('should handle very large numbers', () => {
      expect(determineDpTier(750000, 1000000)).toBe('vigorous');
      expect(determineDpTier(450000, 1000000)).toBe('steady');
      expect(determineDpTier(200000, 1000000)).toBe('wounded');
      expect(determineDpTier(100000, 1000000)).toBe('critical');
    });

    it('should handle decimal values', () => {
      expect(determineDpTier(75.5, 100)).toBe('vigorous');
      expect(determineDpTier(45.5, 100)).toBe('steady');
      expect(determineDpTier(20.5, 100)).toBe('wounded');
      expect(determineDpTier(19.5, 100)).toBe('critical');
    });

    it('should handle boundary values correctly', () => {
      // Boundary between vigorous and steady
      expect(determineDpTier(75, 100)).toBe('vigorous');
      expect(determineDpTier(74.99, 100)).toBe('steady');

      // Boundary between steady and wounded
      expect(determineDpTier(45, 100)).toBe('steady');
      expect(determineDpTier(44.99, 100)).toBe('wounded');

      // Boundary between wounded and critical
      expect(determineDpTier(20, 100)).toBe('wounded');
      expect(determineDpTier(19.99, 100)).toBe('critical');
    });
  });
});
