/**
 * Global Setup for E2E Runtime Tests
 *
 * This file runs before all tests to:
 * - Seed E2E auth users (ArkanWolfshade, Ithaqua, TestAdmin) if missing
 * - Verify server is running
 * - Verify client is accessible
 */

import { chromium, type FullConfig } from '@playwright/test';
import { spawnSync } from 'child_process';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..', '..', '..', '..');

async function globalSetup(_config: FullConfig): Promise<void> {
  console.log('Starting global setup for E2E runtime tests...');

  // Seed TestAdmin only (character-creation E2E). No-op if already present. Does not create ArkanWolfshade/Ithaqua.
  const seedResult = spawnSync('uv', ['run', 'python', 'scripts/seed_e2e_users.py'], {
    cwd: projectRoot,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
  });
  if (seedResult.status !== 0) {
    console.warn('seed_e2e_users.py failed:', seedResult.stderr || seedResult.stdout);
    console.warn('E2E tests that log in as TestAdmin may fail with 401 Invalid credentials.');
  }

  // Verify server is accessible (versioned API health endpoint)
  const serverUrl = 'http://localhost:54731';
  try {
    const response = await fetch(`${serverUrl}/v1/monitoring/health`, { signal: AbortSignal.timeout(5000) });
    if (!response.ok) {
      console.warn(`Server health check failed: ${response.status}`);
    }
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
  } catch (_error) {
    console.warn(`Server not accessible at ${serverUrl}. Make sure the server is running.`);
    console.warn('Tests may fail if server is not running.');
  }

  // Verify client is accessible
  const clientUrl = 'http://localhost:5173';
  try {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(clientUrl, { waitUntil: 'load', timeout: 10000 }).catch(() => {
      console.warn(`Client not accessible at ${clientUrl}. Make sure the client is running.`);
    });
    await browser.close();
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
  } catch (_error) {
    console.warn(`Client not accessible at ${clientUrl}. Make sure the client is running.`);
    console.warn('Tests may fail if client is not running.');
  }

  console.log('Global setup complete.');
}

export default globalSetup;
