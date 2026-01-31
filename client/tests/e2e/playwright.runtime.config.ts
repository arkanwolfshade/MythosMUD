import { defineConfig, devices } from '@playwright/test';

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
  /* Run tests serially to avoid race conditions with shared player accounts */
  fullyParallel: false,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* CRITICAL: E2E tests must run serially to avoid race conditions */
  workers: 1,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: 'html',
  /* Global setup and teardown */
  globalSetup: './runtime/global-setup.ts',
  globalTeardown: './runtime/global-teardown.ts',
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('/')`. */
    baseURL: 'http://localhost:5173',
    /* Default timeout for each action (30 seconds) */
    actionTimeout: 30000,
    /* Default timeout for navigation */
    navigationTimeout: 30000,
    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',
    /* Screenshot on failure */
    screenshot: 'only-on-failure',
    /* Video on failure */
    video: 'retain-on-failure',
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
  /* Configure projects for major browsers */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  /* Run your local dev server before starting the tests (disabled in CI) */
  webServer: process.env.CI
    ? undefined
    : {
        command: 'npm run dev',
        url: 'http://localhost:5173',
        reuseExistingServer: !process.env.CI,
        timeout: 120000,
      },
});
