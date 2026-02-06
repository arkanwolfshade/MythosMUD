import { describe, expect, it } from 'vitest';
import type { HealthStatus } from '../../types/health';
import { HEALTH_LOG_TAGS, buildHealthChangeMessage, buildHealthStatusFromEvent } from '../healthEventUtils';

describe('Health Event Utilities', () => {
  describe('buildHealthStatusFromEvent', () => {
    it('should build health status from event data', () => {
      // Arrange
      const data = {
        old_dp: 100,
        new_dp: 85,
        max_dp: 100,
        reason: 'combat_damage',
        posture: 'standing',
        in_combat: true,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.current).toBe(85);
      expect(result.status.max).toBe(100);
      expect(result.status.tier).toBeDefined();
      expect(result.status.posture).toBe('standing');
      expect(result.status.inCombat).toBe(true);
      expect(result.status.lastChange?.delta).toBe(-15);
      expect(result.status.lastChange?.reason).toBe('combat_damage');
      expect(result.status.lastChange?.timestamp).toBe(timestamp);
      expect(result.delta).toBe(-15);
    });

    it('should handle camelCase property names', () => {
      // Arrange
      const data = {
        oldDp: 100,
        newDp: 85,
        maxDp: 100,
        damageTaken: 15,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.current).toBe(85);
      expect(result.status.max).toBe(100);
      expect(result.delta).toBe(-15);
    });

    it('should use previous status as fallback', () => {
      // Arrange
      const previous: HealthStatus = {
        current: 100,
        max: 100,
        tier: 'vigorous',
        posture: 'standing',
        inCombat: false,
        lastChange: {
          delta: 0,
          reason: undefined,
          timestamp: '2024-01-01T11:00:00Z',
        },
      };
      const data = {
        new_dp: 75,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(previous, data, timestamp);

      // Assert
      expect(result.status.current).toBe(75);
      expect(result.status.max).toBe(100); // From previous
      expect(result.status.posture).toBe('standing'); // From previous
      expect(result.delta).toBe(-25);
    });

    it('should compute reason from delta if not provided', () => {
      // Arrange
      const data = {
        old_dp: 100,
        new_dp: 80,
        damage_taken: 20,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.lastChange?.reason).toBe('damage');
    });

    it('should compute healing reason from positive delta', () => {
      // Arrange
      const data = {
        old_dp: 80,
        new_dp: 100,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.lastChange?.reason).toBe('healing');
      expect(result.delta).toBe(20);
    });

    it('should handle string number values', () => {
      // Arrange
      const data = {
        old_dp: '100',
        new_dp: '85',
        max_dp: '100',
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.current).toBe(85);
      expect(result.status.max).toBe(100);
      expect(result.delta).toBe(-15);
    });

    it('should use default max DP when not provided', () => {
      // Arrange
      const data = {
        new_dp: 50,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.max).toBe(100); // DEFAULT_MAX_DP
    });

    it('should handle zero max DP', () => {
      // Arrange
      const data = {
        new_dp: 50,
        max_dp: 0,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.max).toBe(100); // Falls back to DEFAULT_MAX_DP
    });

    it('should handle invalid number values gracefully', () => {
      // Arrange
      const data = {
        old_dp: 'invalid',
        new_dp: null,
        max_dp: undefined,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(null, data, timestamp);

      // Assert
      expect(result.status.max).toBe(100); // Uses default
      expect(typeof result.status.current).toBe('number');
    });

    it('should preserve posture from previous status', () => {
      // Arrange
      const previous: HealthStatus = {
        current: 100,
        max: 100,
        tier: 'vigorous',
        posture: 'sitting',
        lastChange: {
          delta: 0,
          timestamp: '2024-01-01T11:00:00Z',
        },
      };
      const data = {
        new_dp: 90,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(previous, data, timestamp);

      // Assert
      expect(result.status.posture).toBe('sitting');
    });

    it('should preserve inCombat from previous status', () => {
      // Arrange
      const previous: HealthStatus = {
        current: 100,
        max: 100,
        tier: 'vigorous',
        inCombat: true,
        lastChange: {
          delta: 0,
          timestamp: '2024-01-01T11:00:00Z',
        },
      };
      const data = {
        new_dp: 90,
      };
      const timestamp = '2024-01-01T12:00:00Z';

      // Act
      const result = buildHealthStatusFromEvent(previous, data, timestamp);

      // Assert
      expect(result.status.inCombat).toBe(true);
    });

    it('should set tier to incapacitated and accept posture when new_dp <= 0', () => {
      // DP <= 0 must transition to Incapacitated (distinct from Critical); server sends posture lying
      const data = {
        old_dp: 5,
        new_dp: 0,
        max_dp: 100,
        posture: 'lying',
      };
      const timestamp = '2024-01-01T12:00:00Z';

      const result = buildHealthStatusFromEvent(null, data, timestamp);

      expect(result.status.tier).toBe('incapacitated');
      expect(result.status.current).toBe(0);
      expect(result.status.posture).toBe('lying');
    });
  });

  describe('buildHealthChangeMessage', () => {
    it('should build message for damage', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          reason: 'damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {};

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('Health loses 15');
      expect(message).toContain('(damage)');
      expect(message).toContain('→ 85/100');
      expect(message).toContain('(Vigorous)');
    });

    it('should build message for healing', () => {
      // Arrange
      const status: HealthStatus = {
        current: 95,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: 10,
          reason: 'healing',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = 10;
      const data = {};

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('Health recovers 10');
      expect(message).toContain('(healing)');
      expect(message).toContain('→ 95/100');
    });

    it('should include source name when provided', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          reason: 'damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {
        source_name: 'Goblin',
      };

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('from Goblin');
    });

    it('should include source when source_name not available', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          reason: 'damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {
        source: 'Fire Trap',
      };

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('from Fire Trap');
    });

    it('should include source_id as fallback', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          reason: 'damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {
        source_id: 'npc_123',
      };

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('from npc_123');
    });

    it('should humanize reason with underscores', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          reason: 'combat_damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {};

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('(combat damage)');
      expect(message).not.toContain('_');
    });

    it('should handle missing reason gracefully', () => {
      // Arrange
      const status: HealthStatus = {
        current: 85,
        max: 100,
        tier: 'vigorous',
        lastChange: {
          delta: -15,
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -15;
      const data = {};

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('Health loses 15');
      expect(message).toContain('→ 85/100'); // Still contains tier in parentheses
      // The message format always includes tier in parentheses at the end
    });

    it('should handle different health tiers', () => {
      // Arrange
      const status: HealthStatus = {
        current: 25,
        max: 100,
        tier: 'critical',
        lastChange: {
          delta: -10,
          reason: 'damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -10;
      const data = {};

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toContain('(Critical)');
    });

    it('should format complete message with all parts', () => {
      // Arrange
      const status: HealthStatus = {
        current: 75,
        max: 100,
        tier: 'wounded',
        lastChange: {
          delta: -25,
          reason: 'poison_damage',
          timestamp: '2024-01-01T12:00:00Z',
        },
      };
      const delta = -25;
      const data = {
        source_name: 'Poison Dart',
      };

      // Act
      const message = buildHealthChangeMessage(status, delta, data);

      // Assert
      expect(message).toBe('Health loses 25 (poison damage) from Poison Dart → 75/100 (Wounded)');
    });
  });

  describe('HEALTH_LOG_TAGS', () => {
    it('should be defined', () => {
      // Assert
      expect(HEALTH_LOG_TAGS).toBeDefined();
      expect(Array.isArray(HEALTH_LOG_TAGS)).toBe(true);
    });

    it('should contain health tag', () => {
      // Assert
      expect(HEALTH_LOG_TAGS).toContain('health');
    });
  });
});
