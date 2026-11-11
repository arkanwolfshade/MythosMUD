/// <reference types="node" />

/**
 * Client for the e2e server's test-only endpoints (`/v1/admin/test/...`, server/api/admin/e2e_test_support.py).
 *
 * They replace the scripts that used to write Postgres behind the server's back (reset, place, read state). Every
 * change goes through the server's player registry, and the state read is the registry's own view of a character.
 * The endpoints are admin-only and exist only on the e2e server, so this signs in as the seeded admin,
 * ArkanWolfshade, once per worker and reuses the token (the login endpoint is rate-limited).
 */

import { E2E_SERVER_URL } from '../../../../src/test/e2e-bootstrap';
import { TEST_PLAYERS } from './test-data';

const REQUEST_TIMEOUT_MS = 20000;

export interface E2ePlayerState {
  current_room_id: string;
  respawn_room_id: string | null;
  tutorial_instance_id: string | null;
  /** Names of the stacks in the character's bank deposit box (empty when they have none). */
  bank_items: string[];
  current_dp: number | null;
  corruption: number | null;
  magic_points: number | null;
  max_magic_points: number | null;
  intelligence: number | null;
  /** Lucidity (LCD). */
  current_lcd: number;
  /** Names of the stacks in the character's inventory. */
  inventory_items: string[];
  /** Quest id -> instance state (`active` / `completed` / `abandoned`). */
  quests: Record<string, string>;
  /** True while a debrief (delirium or sanitarium respawn) is waiting for Dr. Morgan. */
  debrief_pending: boolean;
}

let adminToken: Promise<string> | null = null;

async function loginAsAdmin(): Promise<string> {
  const admin = TEST_PLAYERS.find(player => player.isAdmin);
  if (!admin) throw new Error('No admin among TEST_PLAYERS');
  const response = await fetch(`${E2E_SERVER_URL}/v1/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: admin.username, password: admin.password }),
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  });
  if (!response.ok) {
    throw new Error(`${admin.username} login for the test endpoints failed (HTTP ${response.status})`);
  }
  const body = (await response.json()) as { access_token?: string };
  if (!body.access_token) throw new Error('Admin login returned no access_token');
  return body.access_token;
}

async function send(method: 'GET' | 'POST', path: string, body?: object): Promise<Response> {
  adminToken ??= loginAsAdmin();
  const token = await adminToken;
  return fetch(`${E2E_SERVER_URL}/v1/admin/test${path}`, {
    method,
    headers: { Authorization: `Bearer ${token}`, ...(body ? { 'Content-Type': 'application/json' } : {}) },
    body: body ? JSON.stringify(body) : undefined,
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  });
}

/** One call; a 401 means the token is stale (the server restarted), so sign in again and retry once. */
async function call(method: 'GET' | 'POST', path: string, body?: object): Promise<Response> {
  let response: Response;
  try {
    response = await send(method, path, body);
    if (response.status === 401) {
      adminToken = null;
      response = await send(method, path, body);
    }
  } catch (error) {
    adminToken = null; // a failed login must not stick
    throw error;
  }
  if (!response.ok) {
    const detail = (await response.text().catch(() => '')).slice(0, 500);
    throw new Error(`${method} /v1/admin/test${path} failed (HTTP ${response.status}): ${detail}`);
  }
  return response;
}

/** Put ArkanWolfshade and Ithaqua back in the default room, standing, at 50 DP. */
export async function resetSharedE2ePlayers(): Promise<void> {
  await call('POST', '/players/reset');
}

/** Put a character back at the very start of First Exposure; empties the lost-and-found chest and their deposit box. */
export async function resetE2eTutorialCharacter(name: string): Promise<void> {
  await call('POST', `/players/${encodeURIComponent(name)}/reset-tutorial`);
}

/** Move a character to a room, out of the tutorial (only while they are logged out). */
export async function placeE2ePlayer(name: string, roomId: string): Promise<void> {
  await call('POST', `/players/${encodeURIComponent(name)}/place`, { room_id: roomId });
}

/** One character's state as the server's player registry holds it. */
export async function fetchE2ePlayerState(name: string): Promise<E2ePlayerState> {
  const response = await call('GET', `/players/${encodeURIComponent(name)}/state`);
  return (await response.json()) as E2ePlayerState;
}
