/**
 * Character display name validation (ADR-021).
 * Keep in sync with server/validators/security_validator.py.
 */

export const PLAYER_NAME_MIN_LENGTH = 3;
export const PLAYER_NAME_MAX_LENGTH = 20;

/** Must start with a letter; only letters, digits, underscore, hyphen. */
export const PLAYER_NAME_PATTERN = /^[a-zA-Z][a-zA-Z0-9_-]*$/;

export const PLAYER_NAME_RULES_HINT =
  '3-20 characters. Start with a letter. Letters, numbers, underscores, and hyphens only. No spaces.';

export interface PlayerNameValidationResult {
  valid: boolean;
  error?: string;
}

export function validatePlayerName(trimmedName: string): PlayerNameValidationResult {
  if (!trimmedName) {
    return { valid: false, error: 'Please enter a character name' };
  }

  if (trimmedName.length < PLAYER_NAME_MIN_LENGTH) {
    return {
      valid: false,
      error: `Player name must be at least ${PLAYER_NAME_MIN_LENGTH} characters long`,
    };
  }

  if (trimmedName.length > PLAYER_NAME_MAX_LENGTH) {
    return {
      valid: false,
      error: `Player name must be ${PLAYER_NAME_MAX_LENGTH} characters or less`,
    };
  }

  if (!PLAYER_NAME_PATTERN.test(trimmedName)) {
    return {
      valid: false,
      error: 'Player name must start with a letter and contain only letters, numbers, underscores, and hyphens',
    };
  }

  return { valid: true };
}
