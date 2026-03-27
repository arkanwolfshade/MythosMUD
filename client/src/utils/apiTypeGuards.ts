/**
 * Runtime type validation utilities for API responses.
 *
 * Provides type guard functions to validate API response data at runtime,
 * ensuring type safety when parsing JSON responses from the server.
 *
 * Following TypeScript best practices: use `unknown` for untyped data,
 * then narrow with type guards before use.
 */

import type { Profession } from '../components/ProfessionCard.tsx';
import type { CharacterInfo, LoginResponse } from '../types/auth.js';

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
 * Note: Server Stats model does NOT include 'wisdom' - it was removed/never existed.
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
    charisma: number;
    luck: number;
  };
  stat_summary: {
    total: number;
    average: number;
    highest: number;
    lowest: number;
  };
  profession_id?: number | null;
  meets_requirements?: boolean | null;
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
 * ASCII map API response (map viewer and minimap endpoints).
 */
export interface AsciiMapApiResponse {
  map_html?: string;
  viewport?: { x?: number; y?: number };
}

function hasValidOptionalString(value: unknown): boolean {
  return value === undefined || typeof value === 'string';
}

function hasValidOptionalNumber(value: unknown): boolean {
  return value === undefined || typeof value === 'number';
}

function isValidAsciiViewport(value: unknown): boolean {
  if (value === undefined) {
    return true;
  }
  if (!isObject(value)) {
    return false;
  }
  return hasValidOptionalNumber(value.x) && hasValidOptionalNumber(value.y);
}

/**
 * Type guard: Check if value is an AsciiMapApiResponse.
 */
export function isAsciiMapApiResponse(value: unknown): value is AsciiMapApiResponse {
  if (!isObject(value)) {
    return false;
  }

  return hasValidOptionalString(value.map_html) && isValidAsciiViewport(value.viewport);
}

/**
 * Rooms list API response (GET /api/rooms/list).
 */
export interface RoomsListApiResponse {
  rooms?: unknown[];
  total?: number;
}

/**
 * Type guard: Check if value is a RoomsListApiResponse.
 */
export function isRoomsListApiResponse(value: unknown): value is RoomsListApiResponse {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  if (o.rooms !== undefined && !Array.isArray(o.rooms)) {
    return false;
  }
  if (o.total !== undefined && typeof o.total !== 'number') {
    return false;
  }
  return true;
}

/**
 * API error body with optional detail message.
 */
export interface ApiErrorWithDetail {
  detail?: string;
}

/**
 * Type guard: Check if value is an ApiErrorWithDetail (for error response bodies).
 */
export function isApiErrorWithDetail(value: unknown): value is ApiErrorWithDetail {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  if (o.detail !== undefined && typeof o.detail !== 'string') {
    return false;
  }
  return true;
}

/**
 * Respawn API success response (POST /api/players/respawn or respawn-delirium).
 */
export interface RespawnApiResponse {
  room?: unknown;
  player?: unknown;
  message?: string;
}

/**
 * Type guard: Check if value is a RespawnApiResponse.
 */
export function isRespawnApiResponse(value: unknown): value is RespawnApiResponse {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  if (o.message !== undefined && typeof o.message !== 'string') {
    return false;
  }
  return true;
}

/**
 * Open container API response (container + mutation_token).
 */
export interface OpenContainerApiResponse {
  container?: unknown;
  mutation_token?: string;
}

/**
 * Type guard: Check if value is an OpenContainerApiResponse.
 */
export function isOpenContainerApiResponse(value: unknown): value is OpenContainerApiResponse {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  if (o.mutation_token !== undefined && typeof o.mutation_token !== 'string') {
    return false;
  }
  return true;
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
function isArray(value: unknown): boolean {
  return Array.isArray(value);
}

/**
 * Type guard: Check if value is a CharacterInfo object.
 */
function isCharacterInfoCoreFields(value: Record<string, unknown>) {
  const requiredStringFields = ['player_id', 'name', 'created_at', 'last_active'] as const;
  const requiredNumberFields = ['profession_id', 'level'] as const;

  return (
    requiredStringFields.every(field => isString(value[field])) &&
    requiredNumberFields.every(field => isNumber(value[field]))
  );
}

function isCharacterInfoProfessionNameValid(value: Record<string, unknown>) {
  const professionName = value.profession_name;
  return professionName === undefined || professionName === null || isString(professionName);
}

function isCharacterInfoObject(value: unknown): value is Record<string, unknown> {
  return isObject(value);
}

const isCharacterInfo = (value: unknown): value is CharacterInfo => {
  if (!isCharacterInfoObject(value)) {
    return false;
  }
  return isCharacterInfoCoreFields(value) && isCharacterInfoProfessionNameValid(value);
};

/**
 * Type guard: Check if value is a ServerCharacterResponse object.
 * Server may return either 'id' or 'player_id' field.
 */
function hasServerCharacterIdentifierFields(value: Record<string, unknown>): boolean {
  const hasValidIdField = hasOptionalString(value.id);
  const hasValidPlayerIdField = hasOptionalString(value.player_id);
  return hasValidIdField && hasValidPlayerIdField && hasAtLeastOneIdentifier(value);
}

function hasOptionalString(value: unknown): boolean {
  return value === undefined || isString(value);
}

function hasAtLeastOneIdentifier(value: Record<string, unknown>): boolean {
  return value.id !== undefined || value.player_id !== undefined;
}

function hasServerCharacterCoreFields(value: Record<string, unknown>): boolean {
  const requiredStringFields = ['name', 'created_at', 'last_active'] as const;
  const requiredNumberFields = ['profession_id', 'level'] as const;

  return (
    requiredStringFields.every(field => isString(value[field])) &&
    requiredNumberFields.every(field => isNumber(value[field])) &&
    hasOptionalString(value.profession_name)
  );
}

export function isServerCharacterResponse(value: unknown): value is ServerCharacterResponse {
  if (!isObject(value)) {
    return false;
  }
  if (!hasServerCharacterIdentifierFields(value)) {
    return false;
  }
  return hasServerCharacterCoreFields(value);
}

/**
 * Type guard: Check if value is an array of CharacterInfo.
 */
export function isCharacterInfoArray(value: unknown): value is CharacterInfo[] {
  if (!isArray(value)) {
    return false;
  }

  const arr = value as unknown[];
  return arr.every(item => isCharacterInfo(item));
}

/**
 * Type guard: Check if value is an array of ServerCharacterResponse.
 */
export function isServerCharacterResponseArray(value: unknown): value is ServerCharacterResponse[] {
  if (!isArray(value)) {
    return false;
  }

  const arr = value as unknown[];
  return arr.every(item => isServerCharacterResponse(item));
}

/**
 * Type guard: Check if value is a LoginResponse.
 */
export function isLoginResponse(value: unknown): value is LoginResponse {
  if (!isObject(value)) {
    return false;
  }

  if (!isString(value.access_token)) return false;
  if (!isString(value.token_type)) return false;
  if (!isString(value.user_id)) return false;
  if (!isArray(value.characters)) return false;

  const characters = value.characters as unknown[];
  if (!characters.every((char: unknown) => isCharacterInfo(char))) return false;

  return value.refresh_token === undefined || isString(value.refresh_token);
}

/**
 * Type guard: Check if value is a StatRequirement object.
 */
function isStatRequirement(value: unknown): value is { stat: string; minimum: number } {
  if (!isObject(value)) {
    return false;
  }
  return isString(value.stat) && isNumber(value.minimum);
}

/**
 * Type guard: Check if value is a MechanicalEffect object.
 */
function isMechanicalEffect(
  value: unknown
): value is { effect_type: string; value: number | string; description?: string | null } {
  if (!isObject(value)) {
    return false;
  }

  if (!isString(value.effect_type)) {
    return false;
  }

  const hasValidEffectValue = isNumber(value.value) || isString(value.value);
  if (!hasValidEffectValue) {
    return false;
  }

  const description = value.description;
  return description === undefined || description === null || isString(description);
}

/**
 * Type guard: Check if value is a Profession object.
 */
function hasValidProfessionStatRequirements(value: Record<string, unknown>) {
  if (!isArray(value.stat_requirements)) return false;
  const statRequirements = value.stat_requirements as unknown[];
  return statRequirements.every((item: unknown) => isStatRequirement(item));
}

function hasValidProfessionMechanicalEffects(value: Record<string, unknown>) {
  if (!isArray(value.mechanical_effects)) return false;
  const mechanicalEffects = value.mechanical_effects as unknown[];
  return mechanicalEffects.every((item: unknown) => isMechanicalEffect(item));
}

function isProfessionFlavorTextValid(value: Record<string, unknown>) {
  return value.flavor_text === null || isString(value.flavor_text);
}

function isProfessionCoreFields(value: Record<string, unknown>) {
  return (
    isNumber(value.id) &&
    isString(value.name) &&
    isString(value.description) &&
    isProfessionFlavorTextValid(value) &&
    typeof value.is_available === 'boolean'
  );
}

function isProfession(value: unknown): value is Profession {
  if (!isObject(value)) return false;
  if (!hasValidProfessionStatRequirements(value)) return false;
  if (!hasValidProfessionMechanicalEffects(value)) return false;
  return isProfessionCoreFields(value);
}

/**
 * Type guard: Check if value is an array of Profession.
 */
export function isProfessionArray(value: unknown): value is Profession[] {
  if (!isArray(value)) {
    return false;
  }

  const arr = value as unknown[];
  return arr.every(item => isProfession(item));
}

const REQUIRED_STATS_FIELDS = [
  'strength',
  'dexterity',
  'constitution',
  'size',
  'intelligence',
  'power',
  'education',
  'charisma',
  'luck',
] as const;

function hasValidStatsObject(value: unknown): value is Record<string, unknown> {
  if (!isObject(value)) {
    return false;
  }
  return REQUIRED_STATS_FIELDS.every(stat => isNumber(value[stat]));
}

function hasValidStatSummary(value: unknown): value is Record<string, unknown> {
  if (!isObject(value)) {
    return false;
  }
  return isNumber(value.total) && isNumber(value.average) && isNumber(value.highest) && isNumber(value.lowest);
}

function hasValidOptionalRollFields(value: Record<string, unknown>): boolean {
  if (value.profession_id !== undefined && value.profession_id !== null && !isNumber(value.profession_id)) {
    return false;
  }
  if (
    value.meets_requirements !== undefined &&
    value.meets_requirements !== null &&
    typeof value.meets_requirements !== 'boolean'
  ) {
    return false;
  }
  return isString(value.method_used);
}

/**
 * Type guard: Check if value is a StatsRollResponse.
 */
export function isStatsRollResponse(value: unknown): value is StatsRollResponse {
  if (!isObject(value)) {
    return false;
  }

  if (!hasValidStatsObject(value.stats)) {
    return false;
  }

  if (!hasValidStatSummary(value.stat_summary)) {
    return false;
  }

  return hasValidOptionalRollFields(value);
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
