/* global process -- Node when Playwright loads this config (satisfies ESLint no-undef in tools without flat-config globals). */
import { setDefaultResultOrder } from 'node:dns';

import { defineConfig, devices } from '@playwright/test';

/**
 * Node 17+ often resolves `localhost` to `::1` first; Playwright's browser CDP socket can then
 * hit `connect EACCES ::1:<port>` on Windows. Prefer IPv4 before any connections run.
 */
setDefaultResultOrder('ipv4first');

/**
 * @see https://playwright.dev/docs/test-configuration
 */
/** Prefer IPv4 loopback: on Windows, `localhost` can resolve to ::1 and Playwright/Node may hit EACCES. */
const DEV_ORIGIN = 'http://127.0.0.1:5173';

export default defineConfig({
  testDir: './tests',
  /* Only run .spec.ts files, ignore .test.tsx files */
  testMatch: '**/*.spec.ts',
  /* Run tests in files in parallel */
  fullyParallel: false,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* CRITICAL: E2E tests must run serially to avoid race conditions with shared player accounts */
  workers: 1,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: [['html'], ['list']],
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('/')`. */
    baseURL: DEV_ORIGIN,

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',
    /* Screenshot on failure for CI debugging */
    screenshot: 'only-on-failure',
    /* Video on first retry for CI debugging */
    video: 'on-first-retry',

    /* Run in headless mode in CI, headed mode locally for debugging */
    headless: process.env.CI === 'true',
  },

  /* Configure projects for major browsers */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },

    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },

    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    /* Test against mobile viewports. */
    // {
    //   name: 'Mobile Chrome',
    //   use: { ...devices['Pixel 5'] },
    // },
    // {
    //   name: 'Mobile Safari',
    //   use: { ...devices['iPhone 12'] },
    // },

    /* Test against branded browsers. */
    // {
    //   name: 'Microsoft Edge',
    //   use: { ...devices['Desktop Edge'], channel: 'msedge' },
    // },
    // {
    //   name: 'Google Chrome',
    //   use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    // },
  ],

  /* Run your local dev server before starting the tests */
  webServer: {
    /* Bind dev server to IPv4 loopback so `url` matches and nothing relies on ::1. */
    command: 'npm run dev -- --host 127.0.0.1',
    url: DEV_ORIGIN,
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
    stdout: 'pipe',
    stderr: 'pipe',
  },
});
