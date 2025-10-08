import { defineConfig, devices } from '@playwright/test';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Playwright configuration for runtime E2E tests
 *
 * These tests are automated and run against a running development server.
 * They do NOT require Playwright MCP or AI Agent coordination.
 *
 * Test Categories:
 * - Error Handling: Single-player error condition testing
 * - Accessibility: WCAG compliance and keyboard navigation
 * - Integration: System integration point verification
 * - Admin: Admin-only functionality testing
 *
 * @see https://playwright.dev/docs/test-configuration
 */
export default defineConfig({
  // Test directory for runtime E2E tests
  testDir: './runtime',

  // Maximum time one test can run (30 seconds)
  timeout: 30 * 1000,

  // Test expectations timeout (10 seconds)
  expect: {
    timeout: 10 * 1000,
  },

  // Run tests in parallel for faster execution
  fullyParallel: true,

  // Fail the build on CI if test.only is accidentally left in
  forbidOnly: !!process.env.CI,

  // Retry once on CI to handle transient failures
  retries: process.env.CI ? 1 : 0,

  // Use single worker on CI to avoid resource contention
  workers: process.env.CI ? 1 : undefined,

  // Reporter configuration
  reporter: [['html', { outputFolder: 'playwright-report/runtime' }], ['list'], process.env.CI ? ['github'] : ['line']],

  // Shared settings for all tests
  use: {
    // Base URL for navigation
    baseURL: 'http://localhost:5173',

    // Collect trace on first retry for debugging
    trace: 'on-first-retry',

    // Screenshot only on failure
    screenshot: 'only-on-failure',

    // Video on failure for debugging
    video: 'retain-on-failure',

    // Browser viewport
    viewport: { width: 1280, height: 720 },

    // Action timeout (10 seconds)
    actionTimeout: 10 * 1000,

    // Navigation timeout (30 seconds)
    navigationTimeout: 30 * 1000,
  },

  // Configure projects for different browsers
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    // Uncomment for cross-browser testing in future
    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },
    // {
    //   name: 'webkit',
    //   use: { ...devices['Desktop Safari'] },
    // },
  ],

  // Development server configuration
  // Only auto-start server for local development (not in CI)
  webServer: process.env.CI
    ? undefined
    : {
        command: 'npm run dev',
        url: 'http://localhost:5173',
        reuseExistingServer: true, // Reuse if already running
        timeout: 120 * 1000, // 2 minutes to start
        stdout: 'ignore',
        stderr: 'pipe',
      },

  // Global setup and teardown for database seeding
  globalSetup: join(__dirname, 'runtime', 'global-setup.ts'),
  globalTeardown: join(__dirname, 'runtime', 'global-teardown.ts'),

  // Output directories
  outputDir: 'test-results/runtime/',
});
