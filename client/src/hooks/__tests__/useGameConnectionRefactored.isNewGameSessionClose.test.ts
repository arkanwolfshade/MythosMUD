import { describe, expect, it } from 'vitest';
import { isNewGameSessionClose } from '../useGameConnectionRefactored';

describe('isNewGameSessionClose', () => {
  it('is true for the ADR-018 kick-prior-session close', () => {
    expect(isNewGameSessionClose({ code: 1000, reason: 'New game session established' })).toBe(true);
  });

  it('is false for other code-1000 closes (#297 regression: dead-connection cleanup must still retry)', () => {
    expect(isNewGameSessionClose({ code: 1000, reason: 'Connection cleaned up' })).toBe(false);
  });

  it('is false for an explicit client disconnect', () => {
    expect(isNewGameSessionClose({ code: 1000, reason: 'Client disconnect' })).toBe(false);
  });

  it('is false for a non-1000 close even with a matching reason string', () => {
    expect(isNewGameSessionClose({ code: 1006, reason: 'New game session established' })).toBe(false);
  });
});
