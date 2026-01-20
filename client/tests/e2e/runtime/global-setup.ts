/**
 * Global Setup for E2E Runtime Tests
 *
 * This file runs before all tests to:
 * - Verify test database exists
 * - Seed test players if needed
 * - Verify server is running
 *
 * Note: Database seeding is handled by the server's test database setup.
 * This file primarily verifies prerequisites are met.
 */

import { chromium, type FullConfig } from '@playwright/test';

async function globalSetup(_config: FullConfig): Promise<void> {
  console.log('Starting global setup for E2E runtime tests...');

  // Verify server is accessible
  const serverUrl = 'http://localhost:54731';
  try {
    const response = await fetch(`${serverUrl}/health`, { signal: AbortSignal.timeout(5000) });
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
