import { describe, it, expect } from 'vitest';
import { buildLucidityStatus, buildLucidityChangeMessage } from '../lucidityEventUtils';

describe('lucidityEventUtils', () => {
  it('builds lucidity status with delta applied', () => {
    const { status, delta } = buildLucidityStatus(
      {
        current: 90,
        max: 100,
        tier: 'lucid',
        liabilities: [],
      },
      { delta: -10, tier: 'uneasy' },
      '2025-11-13T12:00:00Z'
    );

    expect(delta).toBe(-10);
    expect(status.current).toBe(80);
    expect(status.tier).toBe('uneasy');
    expect(status.lastChange?.delta).toBe(-10);
  });

  it('creates descriptive lucidity message', () => {
    const { status, delta } = buildLucidityStatus(
      null,
      { current_lcd: 65, delta: -5, tier: 'uneasy', reason: 'disturbing_encounter', source: 'Byakhee' },
      '2025-11-13T12:00:00Z'
    );
    const message = buildLucidityChangeMessage(status, delta, {
      reason: 'disturbing_encounter',
      source: 'Byakhee',
    });

    expect(message).toMatch(/lucidity loses 5/i);
    expect(message).toMatch(/Byakhee/i);
    expect(message).toMatch(/65\/100/i);
  });

  it('should return fallback when sanitizeTier receives non-string value', () => {
    // Arrange - Test line 7: sanitizeTier fallback branch
    // We can't directly test sanitizeTier as it's not exported, but we can test it through buildLucidityStatus
    const { status } = buildLucidityStatus(
      null,
      { tier: 123, current_lcd: 50 }, // tier is not a string
      '2025-11-13T12:00:00Z'
    );

    // Assert - should use fallback tier 'lucid' when tier is not a string
    expect(status.tier).toBe('lucid');
  });

  it('should parse number from string in parseNumber', () => {
    // Arrange - Test lines 20-22: parseNumber string parsing branch
    // We can't directly test parseNumber, but we can test it through buildLucidityStatus
    const { status } = buildLucidityStatus(
      null,
      { current_lcd: '75', max_lcd: '100' }, // numbers as strings
      '2025-11-13T12:00:00Z'
    );

    // Assert - should parse string numbers correctly
    expect(status.current).toBe(75);
    expect(status.max).toBe(100);
  });

  it('should return fallback when tier is not in valid tiers list', () => {
    // Arrange - Test line 12: sanitizeTier when tier is not in valid list
    const { status } = buildLucidityStatus(null, { tier: 'invalid_tier', current_lcd: 50 }, '2025-11-13T12:00:00Z');

    // Assert - should use fallback tier 'lucid' when tier is invalid
    expect(status.tier).toBe('lucid');
  });

  it('should handle parseNumber with non-finite parsed value', () => {
    // Arrange - Test lines 21-22: parseNumber when parsed value is not finite
    const { status } = buildLucidityStatus(
      null,
      { current_lcd: 'not-a-number', max_lcd: 'also-not-a-number' },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should use fallback values when parsing fails
    expect(status.current).toBe(0); // fallback for null previous
    expect(status.max).toBe(100); // DEFAULT_max_lcd
  });

  it('should calculate current from previous + delta when current_lcd not provided', () => {
    // Arrange - Test line 35: previous + delta calculation
    const { status } = buildLucidityStatus(
      { current: 80, max: 100, tier: 'lucid', liabilities: [] },
      { delta: -10 },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should calculate 80 + (-10) = 70
    expect(status.current).toBe(70);
  });

  it('should use previous.current when previous exists and current_lcd is null', () => {
    // Arrange - Test line 35: previous?.current branch when previous exists
    const { status } = buildLucidityStatus(
      { current: 90, max: 100, tier: 'lucid', liabilities: [] },
      { current_lcd: null, delta: 5 },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should calculate (90) + 5 = 95
    expect(status.current).toBe(95);
  });

  it('should use 0 when previous is null and current_lcd is null', () => {
    // Arrange - Test line 35: (previous?.current ?? 0) branch when previous is null
    const { status } = buildLucidityStatus(null, { current_lcd: null, delta: 10 }, '2025-11-13T12:00:00Z');

    // Assert - should calculate (0) + 10 = 10
    expect(status.current).toBe(10);
  });

  it('should use 0 + delta when current_lcd is null and no previous', () => {
    // Arrange - Test line 35: fall through to (previous?.current ?? 0) + delta when previous is null
    const { status } = buildLucidityStatus(null, { current_lcd: null, delta: 5 }, '2025-11-13T12:00:00Z');

    // Assert - should calculate (0) + 5 = 5
    expect(status.current).toBe(5);
  });

  it('should use 0 + delta when current_lcd is undefined and no previous', () => {
    // Arrange - Test line 35: fall through to (previous?.current ?? 0) + delta when previous is null
    const { status } = buildLucidityStatus(null, { current_lcd: undefined, delta: -3 }, '2025-11-13T12:00:00Z');

    // Assert - should calculate (0) + (-3) = -3, but parseNumber will handle it
    expect(status.current).toBe(-3);
  });

  it('should use current_lcd when it is 0 (falsy but not null/undefined)', () => {
    // Arrange - Test line 35: current_lcd ?? branch - 0 is falsy but ?? only triggers for null/undefined
    const { status } = buildLucidityStatus(null, { current_lcd: 0, max_lcd: 100 }, '2025-11-13T12:00:00Z');

    // Assert - ?? operator only triggers for null/undefined, so 0 should be used
    expect(status.current).toBe(0);
  });

  it('should use DEFAULT_max_lcd when max is 0 or negative', () => {
    // Arrange - Test line 47: max > 0 check
    const { status } = buildLucidityStatus(null, { current_lcd: 50, max_lcd: 0 }, '2025-11-13T12:00:00Z');

    // Assert - should use DEFAULT_max_lcd (100) when max is 0
    expect(status.max).toBe(100);
  });

  it('should handle liabilities from previous when not provided', () => {
    // Arrange - Test line 40: liabilities fallback branch
    const { status } = buildLucidityStatus(
      { current: 50, max: 100, tier: 'lucid', liabilities: ['old_liability'] },
      { delta: -5 },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should use previous liabilities
    expect(status.liabilities).toEqual(['old_liability']);
  });

  it('should filter out empty liability entries', () => {
    // Arrange - Test line 41: filter(Boolean) branch
    // Note: String(null) = 'null' and String(undefined) = 'undefined', which are truthy
    // So only empty strings are filtered out
    const { status } = buildLucidityStatus(
      null,
      { current_lcd: 50, liabilities: ['valid', '', 'also-valid'] },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should filter out empty strings only
    expect(status.liabilities).toEqual(['valid', 'also-valid']);
  });

  it('should build lucidity change message without reason or source', () => {
    // Arrange - Test lines 73-78: buildLucidityChangeMessage branches
    const { status, delta } = buildLucidityStatus(null, { current_lcd: 75, delta: -5 }, '2025-11-13T12:00:00Z');
    const message = buildLucidityChangeMessage(status, delta, {});

    // Assert - should not include reason or source (tier is always in parentheses at end)
    expect(message).toMatch(/lucidity loses 5/i);
    expect(message).not.toMatch(/\(disturbing|\(encounter/); // No reason in parentheses
    expect(message).not.toMatch(/due to/); // No source
    expect(message).toMatch(/\(Lucid\)/); // Tier is always in parentheses
  });

  it('should build lucidity change message with reason but no source', () => {
    // Arrange
    const { status, delta } = buildLucidityStatus(null, { current_lcd: 75, delta: -5 }, '2025-11-13T12:00:00Z');
    const message = buildLucidityChangeMessage(status, delta, { reason: 'disturbing_encounter' });

    // Assert - should include reason but not source
    expect(message).toMatch(/lucidity loses 5/i);
    expect(message).toMatch(/\(disturbing encounter\)/i); // Reason with underscores replaced
    expect(message).not.toMatch(/due to/); // No source
  });

  it('should build lucidity change message with source but no reason', () => {
    // Arrange
    const { status, delta } = buildLucidityStatus(null, { current_lcd: 75, delta: -5 }, '2025-11-13T12:00:00Z');
    const message = buildLucidityChangeMessage(status, delta, { source: 'Byakhee' });

    // Assert - should include source but not reason (tier is always in parentheses at end)
    expect(message).toMatch(/lucidity loses 5/i);
    expect(message).not.toMatch(/\(disturbing|\(encounter/); // No reason in parentheses
    expect(message).toMatch(/due to Byakhee/i); // Source
    expect(message).toMatch(/\(Lucid\)/); // Tier is always in parentheses
  });

  it('should handle positive delta in lucidity change message', () => {
    // Arrange - Test line 69: direction branch for positive delta
    const { status, delta } = buildLucidityStatus(null, { current_lcd: 75, delta: 5 }, '2025-11-13T12:00:00Z');
    const message = buildLucidityChangeMessage(status, delta, {});

    // Assert - should say "gains" for positive delta
    expect(message).toMatch(/lucidity gains 5/i);
  });
});
