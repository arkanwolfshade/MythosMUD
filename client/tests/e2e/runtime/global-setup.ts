/// <reference types="node" />

/**
 * Global Setup for E2E Runtime Tests
 *
 * This file runs before all tests to:
 * - Seed E2E users and default characters via scripts/seed_e2e_users.py:
 *   ArkanWolfshade/Cthulhu1 (admin), Ithaqua/Cthulhu1, TestAdmin/Cthulhu1 (superuser, no default char)
 * - Verify server is running
 * - Verify client is accessible
 */

import { chromium, type FullConfig } from '@playwright/test';
import { spawnSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..', '..', '..', '..');

/** E2E server and client base URLs (HTTPS only for secure request checks). */
const E2E_SERVER_URL = 'https://localhost:54731';
const E2E_CLIENT_URL = 'https://localhost:5173';

const E2E_ENV_DEFAULTS: Record<string, string> = {
  DATABASE_URL: 'postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e',
  POSTGRES_SEARCH_PATH: 'mythos_e2e',
};

/** Parse .env file content and return only DATABASE_URL and POSTGRES_SEARCH_PATH. */
function parseE2eEnvContent(content: string): Record<string, string> {
  const env: Record<string, string> = {};
  for (const line of content.split('\n')) {
    const m = line.match(/^([^#][^=]+)=(.*)$/);
    if (m) {
      const key = m[1].trim();
      const value = m[2].trim();
      if (key === 'DATABASE_URL' || key === 'POSTGRES_SEARCH_PATH') env[key] = value;
    }
  }
  return env;
}

/** Load DATABASE_URL and POSTGRES_SEARCH_PATH from .env.e2e_test so seed uses same schema as E2E server. */
function loadE2eEnv(): Record<string, string> {
  const envPath = path.join(projectRoot, '.env.e2e_test');
  if (!fs.existsSync(envPath)) return { ...E2E_ENV_DEFAULTS };
  const content = fs.readFileSync(envPath, 'utf-8');
  const env = parseE2eEnvContent(content);
  return {
    DATABASE_URL: env.DATABASE_URL ?? E2E_ENV_DEFAULTS.DATABASE_URL,
    POSTGRES_SEARCH_PATH: env.POSTGRES_SEARCH_PATH ?? E2E_ENV_DEFAULTS.POSTGRES_SEARCH_PATH,
  };
}

function runE2eSeed(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const seedResult = spawnSync('uv', ['run', 'python', 'scripts/seed_e2e_users.py'], {
    cwd: projectRoot,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
  });
  if (seedResult.status !== 0) {
    console.warn('seed_e2e_users.py failed:', seedResult.stderr || seedResult.stdout);
    console.warn('E2E logins (ArkanWolfshade, Ithaqua, TestAdmin) may fail with 401 Invalid credentials.');
  }
}

async function verifyServerAccessible(): Promise<void> {
  try {
    const response = await fetch(`${E2E_SERVER_URL}/v1/monitoring/health`, {
      signal: AbortSignal.timeout(5000),
    });
    if (!response.ok) console.warn(`Server health check failed: ${response.status}`);
  } catch {
    console.warn(`Server not accessible at ${E2E_SERVER_URL}. Make sure the server is running.`);
    console.warn('Tests may fail if server is not running.');
  }
}

async function verifyClientAccessible(): Promise<void> {
  try {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(E2E_CLIENT_URL, { waitUntil: 'load', timeout: 10000 }).catch(() => {
      console.warn(`Client not accessible at ${E2E_CLIENT_URL}. Make sure the client is running.`);
    });
    await browser.close();
  } catch {
    console.warn(`Client not accessible at ${E2E_CLIENT_URL}. Make sure the client is running.`);
    console.warn('Tests may fail if client is not running.');
  }
}

async function globalSetup(_config: FullConfig): Promise<void> {
  console.log('Starting global setup for E2E runtime tests...');
  runE2eSeed();
  await verifyServerAccessible();
  await verifyClientAccessible();
  console.log('Global setup complete.');
}

export default globalSetup;
