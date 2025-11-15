import { describe, it, expect } from 'vitest';
import {
  buildSanityStatus,
  buildSanityChangeMessage,
  createHallucinationEntry,
  createRescueState,
} from '../sanityEventUtils';

describe('sanityEventUtils', () => {
  it('builds sanity status with delta applied', () => {
    const { status, delta } = buildSanityStatus(
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

  it('creates descriptive sanity message', () => {
    const { status, delta } = buildSanityStatus(
      null,
      { current_san: 65, delta: -5, tier: 'uneasy', reason: 'disturbing_encounter', source: 'Byakhee' },
      '2025-11-13T12:00:00Z'
    );
    const message = buildSanityChangeMessage(status, delta, {
      reason: 'disturbing_encounter',
      source: 'Byakhee',
    });

    expect(message).toMatch(/Sanity loses 5/i);
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
});
