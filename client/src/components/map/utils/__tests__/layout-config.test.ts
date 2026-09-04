/**
 * Tests for layout configuration defaults.
 */

import { describe, expect, it } from 'vitest';
import { defaultForceLayoutConfig, defaultGridLayoutConfig } from '../layout';

describe('layout configuration', () => {
  describe('defaultGridLayoutConfig', () => {
    it('should have correct default values', () => {
      expect(defaultGridLayoutConfig.cellWidth).toBe(120);
      expect(defaultGridLayoutConfig.cellHeight).toBe(120);
      expect(defaultGridLayoutConfig.horizontalSpacing).toBe(50);
      expect(defaultGridLayoutConfig.verticalSpacing).toBe(50);
      expect(defaultGridLayoutConfig.groupByZone).toBe(false);
      expect(defaultGridLayoutConfig.groupBySubZone).toBe(true);
    });
  });

  describe('defaultForceLayoutConfig', () => {
    it('should have correct default values', () => {
      expect(defaultForceLayoutConfig.linkDistance).toBe(200);
      expect(defaultForceLayoutConfig.chargeStrength).toBe(-1200);
      expect(defaultForceLayoutConfig.centerStrength).toBe(0.05);
      expect(defaultForceLayoutConfig.iterations).toBe(800);
      expect(defaultForceLayoutConfig.damping).toBe(0.9);
      expect(defaultForceLayoutConfig.minDistance).toBe(120);
      expect(defaultForceLayoutConfig.nodeRadius).toBe(50);
      expect(defaultForceLayoutConfig.collisionStrength).toBe(8.0);
      expect(defaultForceLayoutConfig.minimizeCrossings).toBe(true);
    });
  });
});
