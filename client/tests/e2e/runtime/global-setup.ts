/// <reference types="node" />

/**
 * Global Setup for E2E Runtime Tests
 *
 * This file runs before all tests to:
 * - Ensure mythos_e2e has profession reference data (scripts/ensure_e2e_database.ps1)
 * - Seed E2E users and default characters via scripts/seed_e2e_users.py
 * - Verify users exist in mythos_e2e (scripts/verify_e2e_users_seeded.py)
 * - Verify server health, username login (/v1/auth/login), and profession catalog
 * - Verify client is accessible
 *
 * Any failure throws after writing logs/e2e_test/bootstrap-errors.log (non-zero Playwright exit).
 */

import type { FullConfig } from '@playwright/test';
import { spawnSync } from 'child_process';

import {
  countProfessionsPayload,
  E2E_CLIENT_URL,
  E2E_PROJECT_ROOT,
  E2E_SERVER_URL,
  failBootstrap,
  formatLoginFailure,
  loadE2eEnv,
  spawnOutputDetail,
} from '../../../src/test/e2e-bootstrap';

const E2E_TEST_USERNAME = 'Ithaqua';
const E2E_TEST_PASSWORD = 'Cthulhu1';

function runEnsureE2eDatabase(): void {
  const ensureScript = `${E2E_PROJECT_ROOT}/scripts/ensure_e2e_database.ps1`;
  const ensureResult = spawnSync('pwsh', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', ensureScript], {
    cwd: E2E_PROJECT_ROOT,
    stdio: 'pipe',
    encoding: 'utf-8',
  });
  if (ensureResult.status !== 0) {
    failBootstrap('ensure_e2e_database', `ensure_e2e_database.ps1 failed (exit ${ensureResult.status}).`, [
      spawnOutputDetail(ensureResult.stdout, ensureResult.stderr),
      'Run: make ensure-e2e-database from repo root.',
    ]);
  }
}

function runE2ePlayerRoomReset(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const resetResult = spawnSync('uv', ['run', 'python', 'scripts/e2e_reset_players.py'], {
    cwd: E2E_PROJECT_ROOT,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
  });
  if (resetResult.status !== 0) {
    failBootstrap('e2e_reset_players', `e2e_reset_players.py failed (exit ${resetResult.status}).`, [
      spawnOutputDetail(resetResult.stdout, resetResult.stderr),
    ]);
  }
}

function runE2eSeed(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const seedResult = spawnSync('uv', ['run', 'python', 'scripts/seed_e2e_users.py'], {
    cwd: E2E_PROJECT_ROOT,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
  });
  if (seedResult.status !== 0) {
    failBootstrap('seed_e2e_users', `seed_e2e_users.py failed (exit ${seedResult.status}).`, [
      spawnOutputDetail(seedResult.stdout, seedResult.stderr),
      'E2E logins (ArkanWolfshade, Ithaqua) will not work until seed succeeds.',
    ]);
  }
}

function verifyE2eUsersInDatabase(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const verifyResult = spawnSync('uv', ['run', 'python', 'scripts/verify_e2e_users_seeded.py'], {
    cwd: E2E_PROJECT_ROOT,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
  });
  if (verifyResult.status !== 0) {
    failBootstrap('verify_e2e_users', `verify_e2e_users_seeded.py failed (exit ${verifyResult.status}).`, [
      spawnOutputDetail(verifyResult.stdout, verifyResult.stderr),
    ]);
  }
}

async function fetchResponseBodyText(response: Response): Promise<string> {
  try {
    return (await response.text()).trim();
  } catch {
    return '(could not read response body)';
  }
}

/**
 * When the E2E server is running, verify health, username login, and GET /v1/professions catalog.
 *
 * Uses POST /v1/auth/login (JSON), matching the production client. FastAPI Users'
 * /v1/auth/jwt/login expects email in the OAuth2 username field, not MythosMUD usernames.
 */
async function verifyServerBootstrap(): Promise<void> {
  const env = loadE2eEnv();
  let health: Response;
  try {
    health = await fetch(`${E2E_SERVER_URL}/v1/monitoring/health`, {
      signal: AbortSignal.timeout(5000),
    });
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    failBootstrap('server_health', `No E2E server at ${E2E_SERVER_URL} (${msg}).`, [
      'Start the E2E stack from this worktree (e2e.bat or scripts/start_e2e_test.ps1).',
      'Only one server may use port 54768.',
    ]);
  }

  if (!health.ok) {
    failBootstrap('server_health', `GET /v1/monitoring/health returned HTTP ${health.status}.`, [
      await fetchResponseBodyText(health),
    ]);
  }

  const loginEndpoint = `${E2E_SERVER_URL}/v1/auth/login`;
  const loginResp = await fetch(loginEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: E2E_TEST_USERNAME, password: E2E_TEST_PASSWORD }),
    signal: AbortSignal.timeout(15000),
  });

  if (!loginResp.ok) {
    const bodyText = await fetchResponseBodyText(loginResp);
    failBootstrap(
      'auth_login',
      `${E2E_TEST_USERNAME} login rejected by E2E server (HTTP ${loginResp.status}).`,
      formatLoginFailure(loginResp.status, bodyText, loginEndpoint, env)
    );
  }

  const loginJson = (await loginResp.json()) as { access_token?: string };
  const token = loginJson.access_token;
  if (!token) {
    failBootstrap('auth_login', 'Login returned 200 but no access_token in JSON body.', [
      JSON.stringify(loginJson).slice(0, 500),
    ]);
  }

  const profResp = await fetch(`${E2E_SERVER_URL}/v1/professions/`, {
    headers: { Authorization: `Bearer ${token}` },
    signal: AbortSignal.timeout(15000),
  });
  if (!profResp.ok) {
    failBootstrap('professions_catalog', `GET /v1/professions/ failed with HTTP ${profResp.status}.`, [
      await fetchResponseBodyText(profResp),
    ]);
  }

  const raw: unknown = await profResp.json();
  const count = countProfessionsPayload(raw);
  if (count === 0) {
    failBootstrap('professions_catalog', `E2E server returned an empty profession catalog at ${E2E_SERVER_URL}.`, [
      'Run make ensure-e2e-database (or e2e.bat), then restart the E2E server on port 54768.',
    ]);
  }
  console.log(`E2E bootstrap OK: ${E2E_TEST_USERNAME} login and ${count} professions at ${E2E_SERVER_URL}`);
}

async function verifyClientAccessible(): Promise<void> {
  let response: Response;
  try {
    response = await fetch(E2E_CLIENT_URL, { signal: AbortSignal.timeout(10000) });
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    failBootstrap('client', `Client not reachable at ${E2E_CLIENT_URL} (${msg}).`, [
      'Start the Vite client on port 5173 (e2e.bat starts server and client).',
    ]);
  }

  if (!response.ok) {
    failBootstrap('client', `GET ${E2E_CLIENT_URL} returned HTTP ${response.status}.`, [
      'Start the Vite client on port 5173 (e2e.bat starts server and client).',
    ]);
  }
}

async function globalSetup(_config: FullConfig): Promise<void> {
  console.log('Starting global setup for E2E runtime tests...');
  runEnsureE2eDatabase();
  runE2eSeed();
  runE2ePlayerRoomReset();
  verifyE2eUsersInDatabase();
  await verifyServerBootstrap();
  await verifyClientAccessible();
  console.log('Global setup complete.');
}

export default globalSetup;
