/**
 * Global Teardown for E2E Runtime Tests
 *
 * This file runs after all tests to:
 * - Reset test players (ArkanWolfshade, Ithaqua) to starting room and current_dp, through the server's test endpoint
 * - Fail the run if the server's errors.log or DLQ is non-empty (#1053)
 * - Log test completion
 */
/// <reference types="node" />

import { type FullConfig } from '@playwright/test';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

import { resetSharedE2ePlayers } from './fixtures/e2e-test-api';

// In ESM, we need to synthesize __dirname from import.meta.url
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** Project root (one level up from client/). */
const projectRoot = path.resolve(__dirname, '..', '..', '..', '..');

async function globalTeardown(_config: FullConfig): Promise<void> {
  console.log('Starting global teardown for E2E runtime tests...');

  try {
    await resetSharedE2ePlayers();
  } catch (error) {
    console.warn('Resetting the test players failed - they may not have been reset:', error);
  }

  assertServerLogsClean();

  console.log('Global teardown complete.');
}

/**
 * Fail the run when the E2E server logged errors or dead-lettered a message (#1053).
 *
 * e2e.bat wipes logs/ before the stack starts, so anything here came from this run. Unlike a failed spec, a
 * server-side error never reached the browser, so without this check it passes silently.
 */
function assertServerLogsClean(): void {
  const logDir = path.join(projectRoot, 'logs', 'e2e_test');
  const errorsLog = path.join(logDir, 'errors.log');
  const dlqDir = path.join(logDir, 'dlq');

  const problems: string[] = [];
  if (fs.existsSync(errorsLog) && fs.statSync(errorsLog).size > 0) {
    problems.push(`${errorsLog} is not empty (${fs.statSync(errorsLog).size} bytes)`);
  }
  const dlqFiles = fs.existsSync(dlqDir) ? fs.readdirSync(dlqDir).filter(f => f.endsWith('.json')) : [];
  if (dlqFiles.length > 0) {
    problems.push(`${dlqDir} holds ${dlqFiles.length} dead-lettered message(s)`);
  }
  if (problems.length > 0) {
    throw new Error(`E2E server logged errors during the run:\n  - ${problems.join('\n  - ')}`);
  }
}

export default globalTeardown;
