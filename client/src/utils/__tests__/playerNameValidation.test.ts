import { describe, expect, it } from 'vitest';
import { PLAYER_NAME_MAX_LENGTH, PLAYER_NAME_MIN_LENGTH, validatePlayerName } from '../playerNameValidation.js';

describe('validatePlayerName', () => {
  it('rejects empty name', () => {
    const result = validatePlayerName('');
    expect(result.valid).toBe(false);
    expect(result.error).toContain('enter a character name');
  });

  it('rejects spaced names', () => {
    const result = validatePlayerName('Arkan Lovecraft');
    expect(result.valid).toBe(false);
    expect(result.error).toMatch(/letter/);
  });

  it('rejects names shorter than min length', () => {
    const result = validatePlayerName('Ab');
    expect(result.valid).toBe(false);
    expect(result.error).toContain(String(PLAYER_NAME_MIN_LENGTH));
  });

  it('rejects names longer than max length', () => {
    const tooLong = `A${new Array(PLAYER_NAME_MAX_LENGTH + 1).join('b')}`;
    const result = validatePlayerName(tooLong);
    expect(result.valid).toBe(false);
    expect(result.error).toContain(String(PLAYER_NAME_MAX_LENGTH));
  });

  it('accepts valid names with hyphen and underscore', () => {
    expect(validatePlayerName('Test_Player-1').valid).toBe(true);
    expect(validatePlayerName('Abc').valid).toBe(true);
    expect(validatePlayerName(`A${new Array(PLAYER_NAME_MAX_LENGTH).join('b')}`).valid).toBe(true);
  });
});
