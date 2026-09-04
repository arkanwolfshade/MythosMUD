import { setDefaultResultOrder } from 'node:dns';
import process from 'node:process';

import { defineConfig, devices } from '@playwright/test';

setDefaultResultOrder('ipv4first');

/** Prefer IPv4 loopback: avoids ::1 EACCES on some Windows setups when using `localhost`. */
const DEV_ORIGIN = 'http://127.0.0.1:5173';

/** Parallel runtime suite (opt-in): workers>1, fullyParallel. Requires server already running at DEV_ORIGIN. */
const RUNTIME_PARALLEL = process.env.E2E_RUNTIME_PARALLEL === '1' || process.env.E2E_RUNTIME_PARALLEL === 'true';
const PARALLEL_WORKERS = Math.min(
  Math.max(1, parseInt(process.env.E2E_WORKERS || process.env.WORKERS || '2', 10) || 2),
  4
);

/**
 * Playwright Runtime Configuration for E2E Tests
 *
 * This configuration is used for runtime E2E tests that require:
 * - Multi-context support for multiplayer scenarios
 * - Test database isolation
 * - Proper timeout configuration
 * - Server and client running on specific ports
 *
 * @see https://playwright.dev/docs/test-configuration
 */
export default defineConfig({
  testDir: './runtime',
  /* Only run .spec.ts files */
  testMatch: '**/*.spec.ts',
  /* Serial by default (shared accounts). Opt-in: E2E_RUNTIME_PARALLEL=1 */
  fullyParallel: RUNTIME_PARALLEL,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  workers: RUNTIME_PARALLEL ? PARALLEL_WORKERS : 1,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: [['html'], ['list']],
  /* Global setup and teardown */
  globalSetup: './runtime/global-setup.ts',
  globalTeardown: './runtime/global-teardown.ts',
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('/')`. */
    baseURL: DEV_ORIGIN,
    /* Run headed locally (do not use headless); headless only in CI. */
    headless: process.env.CI === 'true',
    /* Default timeout for each action (30 seconds) */
    actionTimeout: 30000,
    /* Default timeout for navigation */
    navigationTimeout: 30000,
    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',
    /* Screenshot on failure */
    screenshot: 'only-on-failure',
    /* Video on first retry for CI debugging (aligns with Playwright best practices) */
    video: 'on-first-retry',
  },
  /* Timeout for each test and beforeAll hooks.
   * Multiplayer setup (createContexts + waitForAllPlayersInGame + ensurePlayersInSameRoom)
   * can take 90-120s when server is cold. 3 min prevents premature teardown (CLOSE 1001).
   */
  timeout: 180000,
  /* Expect timeout (30 seconds) */
  expect: {
    timeout: 30000,
  },
  /* Runtime E2E project: bundled Firefox (no system Chrome required).
   * Install browsers once per machine: `cd client && npx playwright install firefox`
   */
  projects: [
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
  ],
  /* Local dev: start Vite when not in parallel mode (parallel expects server already up) */
  webServer:
    process.env.CI || RUNTIME_PARALLEL
      ? undefined
      : {
          command: 'npm run dev -- --host 127.0.0.1',
          url: DEV_ORIGIN,
          reuseExistingServer: !process.env.CI,
          timeout: 120000,
        },
});
