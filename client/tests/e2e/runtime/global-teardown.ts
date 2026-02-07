/**
 * Global Teardown for E2E Runtime Tests
 *
 * This file runs after all tests to:
 * - Reset test players (ArkanWolfshade, Ithaqua) to starting room and current_dp
 * - Log test completion
 */
/// <reference types="node" />

import { spawnSync } from 'child_process';
import * as path from 'path';
import { fileURLToPath } from 'url';
import { type FullConfig } from '@playwright/test';

// In ESM, we need to synthesize __dirname from import.meta.url
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** Project root (one level up from client/). */
const projectRoot = path.resolve(__dirname, '..', '..', '..', '..');

async function globalTeardown(_config: FullConfig): Promise<void> {
  console.log('Starting global teardown for E2E runtime tests...');

  const scriptPath = path.join(projectRoot, 'scripts', 'e2e_reset_players.py');
  const result = spawnSync('uv', ['run', 'python', scriptPath], {
    cwd: projectRoot,
    shell: true,
    stdio: 'inherit',
  });

  if (result.status !== 0) {
    console.warn('e2e_reset_players.py exited with code', result.status, '- test players may not have been reset.');
  }

  console.log('Global teardown complete.');
}

export default globalTeardown;
