/**
 * Runtime type validation utilities for API responses.
 *
 * Provides type guard functions to validate API response data at runtime,
 * ensuring type safety when parsing JSON responses from the server.
 *
 * Following TypeScript best practices: use `unknown` for untyped data,
 * then narrow with type guards before use.
 */

import type { CharacterInfo, LoginResponse } from '../types/auth';
import type { Profession } from '../components/ProfessionCard';

/**
 * Server response character type (server may return 'id' or 'player_id').
 */
export interface ServerCharacterResponse {
  id?: string;
  player_id?: string;
  name: string;
  profession_id: number;
  profession_name?: string;
  level: number;
  created_at: string;
  last_active: string;
}

/**
 * Stats roll response from the server.
 */
export interface StatsRollResponse {
  stats: {
    strength: number;
    dexterity: number;
    constitution: number;
    size: number;
    intelligence: number;
    power: number;
    education: number;
    wisdom: number;
    charisma: number;
    luck: number;
  };
  stat_summary: {
    total: number;
    average: number;
    highest: number;
    lowest: number;
  };
  profession_id: number;
  meets_requirements: boolean;
  method_used: string;
}

/**
 * Refresh token response from the server.
 */
export interface RefreshTokenResponse {
  access_token: string;
  expires_in: number;
  refresh_token?: string;
}

/**
 * Type guard: Check if value is a string.
 */
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

/**
 * Type guard: Check if value is a number.
 */
function isNumber(value: unknown): value is number {
  return typeof value === 'number' && !isNaN(value);
}

/**
 * Type guard: Check if value is an object (not null, not array).
 */
function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

/**
 * Type guard: Check if value is an array.
 */
function isArray(value: unknown): value is unknown[] {
  return Array.isArray(value);
}

/**
 * Type guard: Check if value is a CharacterInfo object.
 */
function isCharacterInfo(value: unknown): value is CharacterInfo {
  if (!isObject(value)) {
    return false;
  }

  return (
    isString(value.player_id) &&
    isString(value.name) &&
    isNumber(value.profession_id) &&
    isNumber(value.level) &&
    isString(value.created_at) &&
    isString(value.last_active) &&
    (value.profession_name === undefined || isString(value.profession_name))
  );
}

/**
 * Type guard: Check if value is a ServerCharacterResponse object.
 * Server may return either 'id' or 'player_id' field.
 */
export function isServerCharacterResponse(value: unknown): value is ServerCharacterResponse {
  if (!isObject(value)) {
    return false;
  }

  // Must have either id or player_id
  const hasId = value.id === undefined || isString(value.id);
  const hasPlayerId = value.player_id === undefined || isString(value.player_id);
  if (!hasId && !hasPlayerId) {
    return false;
  }

  return (
    isString(value.name) &&
    isNumber(value.profession_id) &&
    isNumber(value.level) &&
    isString(value.created_at) &&
    isString(value.last_active) &&
    (value.profession_name === undefined || isString(value.profession_name))
  );
}

/**
 * Type guard: Check if value is an array of CharacterInfo.
 */
export function isCharacterInfoArray(value: unknown): value is CharacterInfo[] {
  if (!isArray(value)) {
    return false;
  }

  return value.every(item => isCharacterInfo(item));
}

/**
 * Type guard: Check if value is an array of ServerCharacterResponse.
 */
export function isServerCharacterResponseArray(value: unknown): value is ServerCharacterResponse[] {
  if (!isArray(value)) {
    return false;
  }

  return value.every(item => isServerCharacterResponse(item));
}

/**
 * Type guard: Check if value is a LoginResponse.
 */
export function isLoginResponse(value: unknown): value is LoginResponse {
  if (!isObject(value)) {
    return false;
  }

  return (
    isString(value.access_token) &&
    isString(value.token_type) &&
    isString(value.user_id) &&
    isArray(value.characters) &&
    value.characters.every((char: unknown) => isCharacterInfo(char))
  );
}

/**
 * Type guard: Check if value is a Profession object.
 */
function isProfession(value: unknown): value is Profession {
  if (!isObject(value)) {
    return false;
  }

  return (
    isNumber(value.id) &&
    isString(value.name) &&
    isString(value.description) &&
    isString(value.flavor_text) &&
    isObject(value.stat_requirements) &&
    Object.values(value.stat_requirements).every((v: unknown) => isNumber(v)) &&
    isObject(value.mechanical_effects) &&
    Object.values(value.mechanical_effects).every((v: unknown) => isNumber(v)) &&
    typeof value.is_available === 'boolean'
  );
}

/**
 * Type guard: Check if value is an array of Profession.
 */
export function isProfessionArray(value: unknown): value is Profession[] {
  if (!isArray(value)) {
    return false;
  }

  return value.every(item => isProfession(item));
}

/**
 * Type guard: Check if value is a StatsRollResponse.
 */
export function isStatsRollResponse(value: unknown): value is StatsRollResponse {
  if (!isObject(value)) {
    return false;
  }

  // Validate stats object
  if (!isObject(value.stats)) {
    return false;
  }

  const stats = value.stats as Record<string, unknown>;
  const requiredStats = [
    'strength',
    'dexterity',
    'constitution',
    'size',
    'intelligence',
    'power',
    'education',
    'wisdom',
    'charisma',
    'luck',
  ];
  if (!requiredStats.every(stat => isNumber(stats[stat]))) {
    return false;
  }

  // Validate stat_summary
  if (!isObject(value.stat_summary)) {
    return false;
  }

  const statSummary = value.stat_summary as Record<string, unknown>;
  if (
    !isNumber(statSummary.total) ||
    !isNumber(statSummary.average) ||
    !isNumber(statSummary.highest) ||
    !isNumber(statSummary.lowest)
  ) {
    return false;
  }

  return isNumber(value.profession_id) && typeof value.meets_requirements === 'boolean' && isString(value.method_used);
}

/**
 * Type guard: Check if value is a RefreshTokenResponse.
 */
export function isRefreshTokenResponse(value: unknown): value is RefreshTokenResponse {
  if (!isObject(value)) {
    return false;
  }

  return (
    isString(value.access_token) &&
    isNumber(value.expires_in) &&
    (value.refresh_token === undefined || isString(value.refresh_token))
  );
}

/**
 * Validate and assert that value is a CharacterInfo array, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated CharacterInfo array
 * @throws Error if validation fails
 */
export function assertCharacterInfoArray(value: unknown, errorMessage?: string): CharacterInfo[] {
  if (!isCharacterInfoArray(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected CharacterInfo[]');
  }
  return value;
}

/**
 * Validate and assert that value is a LoginResponse, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated LoginResponse
 * @throws Error if validation fails
 */
export function assertLoginResponse(value: unknown, errorMessage?: string): LoginResponse {
  if (!isLoginResponse(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected LoginResponse');
  }
  return value;
}

/**
 * Validate and assert that value is a Profession array, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated Profession array
 * @throws Error if validation fails
 */
export function assertProfessionArray(value: unknown, errorMessage?: string): Profession[] {
  if (!isProfessionArray(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected Profession[]');
  }
  return value;
}

/**
 * Validate and assert that value is a StatsRollResponse, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated StatsRollResponse
 * @throws Error if validation fails
 */
export function assertStatsRollResponse(value: unknown, errorMessage?: string): StatsRollResponse {
  if (!isStatsRollResponse(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected StatsRollResponse');
  }
  return value;
}

/**
 * Validate and assert that value is a RefreshTokenResponse, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated RefreshTokenResponse
 * @throws Error if validation fails
 */
export function assertRefreshTokenResponse(value: unknown, errorMessage?: string): RefreshTokenResponse {
  if (!isRefreshTokenResponse(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected RefreshTokenResponse');
  }
  return value;
}

/**
 * Validate and assert that value is a ServerCharacterResponse array, throwing if invalid.
 *
 * @param value - Value to validate
 * @param errorMessage - Custom error message (optional)
 * @returns Validated ServerCharacterResponse array
 * @throws Error if validation fails
 */
export function assertServerCharacterResponseArray(value: unknown, errorMessage?: string): ServerCharacterResponse[] {
  if (!isServerCharacterResponseArray(value)) {
    throw new Error(errorMessage || 'Invalid API response: expected ServerCharacterResponse[]');
  }
  return value;
}
