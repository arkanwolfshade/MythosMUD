import { describe, it, expect } from 'vitest';
import {
  buildLucidityStatus,
  buildLucidityChangeMessage,
  createHallucinationEntry,
  createRescueState,
} from '../lucidityEventUtils';

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

  it('creates hallucination entry with defaults', () => {
    const entry = createHallucinationEntry({}, '2025-11-13T12:00:00Z');
    expect(entry.id).toBeTruthy();
    expect(entry.title).toBeTruthy();
    expect(entry.timestamp).toBe('2025-11-13T12:00:00Z');
  });

  it('normalizes rescue state data', () => {
    const state = createRescueState(
      {
        status: 'channeling',
        progress: 27,
        rescuer_name: 'Ada',
        eta_seconds: 12,
      },
      '2025-11-13T12:00:00Z'
    );

    expect(state.status).toBe('channeling');
    expect(state.progress).toBe(27);
    expect(state.rescuerName).toBe('Ada');
    expect(state.etaSeconds).toBe(12);
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

  it('should generate hallucination id when id is not provided', () => {
    // Arrange - Test line 88: createHallucinationId when id is not provided
    const entry1 = createHallucinationEntry({}, '2025-11-13T12:00:00Z');
    const entry2 = createHallucinationEntry({}, '2025-11-13T12:00:00Z');

    // Assert - should generate unique IDs when id is not provided
    expect(entry1.id).toBeTruthy();
    expect(entry2.id).toBeTruthy();
    expect(entry1.id).not.toBe(entry2.id); // Should be unique
    expect(entry1.id).toMatch(/2025-11-13T12:00:00Z-/); // Should include timestamp
  });

  it('should use provided id when creating hallucination entry', () => {
    // Arrange
    const entry = createHallucinationEntry({ id: 'custom-id-123' }, '2025-11-13T12:00:00Z');

    // Assert - should use provided id
    expect(entry.id).toBe('custom-id-123');
  });

  it('should generate id when provided id is empty string', () => {
    // Arrange - Test line 88: createHallucinationId when id is empty
    const entry = createHallucinationEntry({ id: '' }, '2025-11-13T12:00:00Z');

    // Assert - should generate id when provided id is empty
    expect(entry.id).toBeTruthy();
    expect(entry.id).not.toBe('');
    expect(entry.id).toMatch(/2025-11-13T12:00:00Z-/); // Should include timestamp
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

  it('should create hallucination entry with title from message when title not provided', () => {
    // Arrange - Test lines 97-98: message fallback branch
    const entry = createHallucinationEntry({ message: 'A strange vision appears' }, '2025-11-13T12:00:00Z');

    // Assert - should use message as title
    expect(entry.title).toBe('A strange vision appears');
  });

  it('should create hallucination entry with description', () => {
    // Arrange - Test line 102: description branch
    const entry = createHallucinationEntry(
      { title: 'Vision', description: 'A detailed description' },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should include description
    expect(entry.description).toBe('A detailed description');
  });

  it('should create hallucination entry with category', () => {
    // Arrange - Test line 109: category branch
    const entry = createHallucinationEntry({ title: 'Vision', category: 'visual' }, '2025-11-13T12:00:00Z');

    // Assert - should include category
    expect(entry.category).toBe('visual');
  });

  it('should create hallucination entry without category when not provided', () => {
    // Arrange - Test line 109: category undefined branch
    const entry = createHallucinationEntry({ title: 'Vision' }, '2025-11-13T12:00:00Z');

    // Assert - should not include category
    expect(entry.category).toBeUndefined();
  });

  it('should create hallucination entry without description when empty', () => {
    // Arrange - Test line 102: description undefined branch
    const entry = createHallucinationEntry({ title: 'Vision', description: '' }, '2025-11-13T12:00:00Z');

    // Assert - should not include empty description
    expect(entry.description).toBeUndefined();
  });

  it('should normalize severity to valid values', () => {
    // Arrange - Test lines 105-107: severity normalization
    const entry = createHallucinationEntry({ title: 'Vision', severity: 'INVALID' }, '2025-11-13T12:00:00Z');

    // Assert - should default to 'minor' for invalid severity
    expect(entry.severity).toBe('minor');
  });

  it('should create rescue state with valid status', () => {
    // Arrange - Test lines 123-126: status validation
    const state = createRescueState({ status: 'catatonic' }, '2025-11-13T12:00:00Z');

    // Assert - should use valid status
    expect(state.status).toBe('catatonic');
  });

  it('should use fallback status when status is invalid', () => {
    // Arrange - Test lines 123-126: status fallback branch
    const state = createRescueState({ status: 'invalid_status' }, '2025-11-13T12:00:00Z');

    // Assert - should default to 'idle'
    expect(state.status).toBe('idle');
  });

  it('should use fallback status when status is not a string', () => {
    // Arrange - Test line 122: statusRaw when status is not a string
    const state = createRescueState({ status: 123 }, '2025-11-13T12:00:00Z');

    // Assert - should default to 'idle' when status is not a string
    expect(state.status).toBe('idle');
  });

  it('should use fallback status when status is null', () => {
    // Arrange - Test line 122: statusRaw when status is null
    const state = createRescueState({ status: null }, '2025-11-13T12:00:00Z');

    // Assert - should default to 'idle' when status is null
    expect(state.status).toBe('idle');
  });

  it('should use etaSeconds when eta_seconds is not provided', () => {
    // Arrange - Test line 131: etaSeconds fallback branch (eta_seconds ?? etaSeconds)
    const state = createRescueState({ status: 'channeling', etaSeconds: 30 }, '2025-11-13T12:00:00Z');

    // Assert - should use etaSeconds
    expect(state.etaSeconds).toBe(30);
  });

  it('should use etaSeconds when eta_seconds is null', () => {
    // Arrange - Test line 131: etaSeconds fallback when eta_seconds is null
    const state = createRescueState(
      { status: 'channeling', eta_seconds: null, etaSeconds: 45 },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should use etaSeconds when eta_seconds is null
    expect(state.etaSeconds).toBe(45);
  });

  it('should use etaSeconds when eta_seconds is undefined', () => {
    // Arrange - Test line 131: etaSeconds fallback when eta_seconds is undefined
    const state = createRescueState(
      { status: 'channeling', eta_seconds: undefined, etaSeconds: 60 },
      '2025-11-13T12:00:00Z'
    );

    // Assert - should use etaSeconds when eta_seconds is undefined
    expect(state.etaSeconds).toBe(60);
  });

  it('should clamp progress to 0-100 range', () => {
    // Arrange - Test line 138: progress clamping
    const state1 = createRescueState({ status: 'channeling', progress: 150 }, '2025-11-13T12:00:00Z');
    const state2 = createRescueState({ status: 'channeling', progress: -10 }, '2025-11-13T12:00:00Z');

    // Assert - should clamp to valid range
    expect(state1.progress).toBe(100);
    expect(state2.progress).toBe(0);
  });

  it('should set progress to 0 when input cannot be parsed', () => {
    // Arrange - Test line 138: progress handling
    // Note: progress fallback is always 0 (finite), so progress can never be undefined
    // When input can't be parsed, parseNumber returns fallback 0, which is finite
    const state = createRescueState({ status: 'channeling', progress: 'not-a-number' }, '2025-11-13T12:00:00Z');

    // Assert - parseNumber('not-a-number', 0) returns 0 (fallback), which is finite
    // So progress will be clamped to 0, not undefined
    expect(state.progress).toBe(0);
  });

  it('should set etaSeconds to undefined when not finite', () => {
    // Arrange - Test line 139: etaSeconds undefined branch
    // etaSeconds fallback is Number.NaN, which is not finite, so it can be undefined
    const state = createRescueState({ status: 'channeling', eta_seconds: 'not-a-number' }, '2025-11-13T12:00:00Z');

    // Assert - parseNumber('not-a-number', NaN) returns NaN (fallback), which is not finite
    // So etaSeconds will be undefined
    expect(state.etaSeconds).toBeUndefined();
  });

  it('should clamp etaSeconds to non-negative', () => {
    // Arrange - Test line 139: etaSeconds clamping
    const state = createRescueState({ status: 'channeling', eta_seconds: -5 }, '2025-11-13T12:00:00Z');

    // Assert - should clamp to 0
    expect(state.etaSeconds).toBe(0);
  });

  it('should set etaSeconds to undefined when not finite', () => {
    // Arrange - Test line 139: etaSeconds undefined branch
    const state = createRescueState({ status: 'channeling', eta_seconds: Number.NaN }, '2025-11-13T12:00:00Z');

    // Assert - should be undefined when not finite
    expect(state.etaSeconds).toBeUndefined();
  });

  it('should set targetName to undefined when not a string', () => {
    // Arrange - Test line 128: targetName undefined branch
    const state = createRescueState({ status: 'channeling', target_name: 123 }, '2025-11-13T12:00:00Z');

    // Assert - should be undefined when not a string
    expect(state.targetName).toBeUndefined();
  });

  it('should set rescuerName to undefined when not a string', () => {
    // Arrange - Test line 129: rescuerName undefined branch
    const state = createRescueState({ status: 'channeling', rescuer_name: null }, '2025-11-13T12:00:00Z');

    // Assert - should be undefined when not a string
    expect(state.rescuerName).toBeUndefined();
  });

  it('should set message to undefined when not a string', () => {
    // Arrange - Test line 132: message undefined branch
    const state = createRescueState({ status: 'channeling', message: 456 }, '2025-11-13T12:00:00Z');

    // Assert - should be undefined when not a string
    expect(state.message).toBeUndefined();
  });
});
