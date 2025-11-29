import { describe, expect, it } from 'vitest';
import { determineHealthTier } from '../health';

describe('determineHealthTier', () => {
  describe('vigorous tier', () => {
    it('should return vigorous when ratio is exactly 0.75', () => {
      expect(determineHealthTier(75, 100)).toBe('vigorous');
    });

    it('should return vigorous when ratio is above 0.75', () => {
      expect(determineHealthTier(80, 100)).toBe('vigorous');
      expect(determineHealthTier(100, 100)).toBe('vigorous');
      expect(determineHealthTier(90, 100)).toBe('vigorous');
    });

    it('should return vigorous for high health values', () => {
      expect(determineHealthTier(150, 200)).toBe('vigorous');
      expect(determineHealthTier(300, 400)).toBe('vigorous');
    });
  });

  describe('steady tier', () => {
    it('should return steady when ratio is exactly 0.45', () => {
      expect(determineHealthTier(45, 100)).toBe('steady');
    });

    it('should return steady when ratio is between 0.45 and 0.75', () => {
      expect(determineHealthTier(50, 100)).toBe('steady');
      expect(determineHealthTier(60, 100)).toBe('steady');
      expect(determineHealthTier(74, 100)).toBe('steady');
    });

    it('should return steady for moderate health values', () => {
      expect(determineHealthTier(90, 200)).toBe('steady');
      expect(determineHealthTier(100, 200)).toBe('steady');
      expect(determineHealthTier(140, 200)).toBe('steady');
    });
  });

  describe('wounded tier', () => {
    it('should return wounded when ratio is exactly 0.2', () => {
      expect(determineHealthTier(20, 100)).toBe('wounded');
    });

    it('should return wounded when ratio is between 0.2 and 0.45', () => {
      expect(determineHealthTier(25, 100)).toBe('wounded');
      expect(determineHealthTier(30, 100)).toBe('wounded');
      expect(determineHealthTier(44, 100)).toBe('wounded');
    });

    it('should return wounded for low health values', () => {
      expect(determineHealthTier(40, 200)).toBe('wounded');
      expect(determineHealthTier(80, 200)).toBe('wounded');
    });
  });

  describe('critical tier', () => {
    it('should return critical when ratio is below 0.2', () => {
      expect(determineHealthTier(0, 100)).toBe('critical');
      expect(determineHealthTier(10, 100)).toBe('critical');
      expect(determineHealthTier(19, 100)).toBe('critical');
    });

    it('should return critical when max is zero or negative', () => {
      expect(determineHealthTier(100, 0)).toBe('critical');
      expect(determineHealthTier(50, 0)).toBe('critical');
      expect(determineHealthTier(0, 0)).toBe('critical');
      expect(determineHealthTier(100, -10)).toBe('critical');
    });

    it('should return critical for very low health values', () => {
      expect(determineHealthTier(1, 100)).toBe('critical');
      expect(determineHealthTier(5, 100)).toBe('critical');
      expect(determineHealthTier(19, 100)).toBe('critical');
    });

    it('should return critical when current is negative', () => {
      expect(determineHealthTier(-10, 100)).toBe('critical');
      expect(determineHealthTier(-5, 100)).toBe('critical');
    });
  });

  describe('edge cases', () => {
    it('should handle very large numbers', () => {
      expect(determineHealthTier(750000, 1000000)).toBe('vigorous');
      expect(determineHealthTier(450000, 1000000)).toBe('steady');
      expect(determineHealthTier(200000, 1000000)).toBe('wounded');
      expect(determineHealthTier(100000, 1000000)).toBe('critical');
    });

    it('should handle decimal values', () => {
      expect(determineHealthTier(75.5, 100)).toBe('vigorous');
      expect(determineHealthTier(45.5, 100)).toBe('steady');
      expect(determineHealthTier(20.5, 100)).toBe('wounded');
      expect(determineHealthTier(19.5, 100)).toBe('critical');
    });

    it('should handle boundary values correctly', () => {
      // Boundary between vigorous and steady
      expect(determineHealthTier(75, 100)).toBe('vigorous');
      expect(determineHealthTier(74.99, 100)).toBe('steady');

      // Boundary between steady and wounded
      expect(determineHealthTier(45, 100)).toBe('steady');
      expect(determineHealthTier(44.99, 100)).toBe('wounded');

      // Boundary between wounded and critical
      expect(determineHealthTier(20, 100)).toBe('wounded');
      expect(determineHealthTier(19.99, 100)).toBe('critical');
    });
  });
});
