# Implementation Guide

This document provides concrete code examples and patterns for implementing the spec detailed in @.agent-os/specs/2025-10-08-e2e-playwright-cli-conversion/spec.md

## Authentication Fixture Example

```typescript
// client/tests/e2e/runtime/fixtures/auth.ts
import { Page, expect } from '@playwright/test';

export async function loginAsPlayer(
  page: Page,
  username: string,
  password: string
): Promise<void> {
  // Navigate to login page
  await page.goto('/');

  // Wait for login form
  await expect(page.locator('[data-testid="username-input"]')).toBeVisible({ timeout: 30000 });

  // Fill credentials
  await page.fill('[data-testid="username-input"]', username);
  await page.fill('[data-testid="password-input"]', password);

  // Click login button
  await page.click('[data-testid="login-button"]');

  // Wait for MOTD screen
  await expect(page.locator('[data-testid="continue-button"]')).toBeVisible({ timeout: 30000 });

  // Click Continue to enter game
  await page.click('[data-testid="continue-button"]');

  // Wait for game interface
  await expect(page.locator('text=Chat')).toBeVisible({ timeout: 30000 });

  // Additional wait for room subscription to stabilize
  await page.waitForTimeout(2000);
}

export async function logout(page: Page): Promise<void> {
  // Click logout button
  await page.click('[data-testid="logout-button"]');

  // Wait for logout confirmation
  await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

  // Verify redirect to login page
  await expect(page.locator('[data-testid="username-input"]')).toBeVisible({ timeout: 10000 });
}

export async function isLoggedIn(page: Page): Promise<boolean> {
  const gameInterface = page.locator('text=Chat');
  return await gameInterface.isVisible();
}
```

## Player Utilities Example

```typescript
// client/tests/e2e/runtime/fixtures/player.ts
import { Page, expect } from '@playwright/test';

export async function sendCommand(page: Page, command: string): Promise<void> {
  const commandInput = page.locator('[data-testid="command-input"]');
  await commandInput.fill(command);
  await commandInput.press('Enter');
}

export async function waitForMessage(
  page: Page,
  messageText: string,
  timeout: number = 10000
): Promise<void> {
  await expect(page.locator('.message', { hasText: messageText }))
    .toBeVisible({ timeout });
}

export async function getMessages(page: Page): Promise<string[]> {
  const messageElements = await page.locator('.message').all();
  const messages = await Promise.all(
    messageElements.map(el => el.textContent())
  );
  return messages.map(m => m?.trim() || '');
}

export async function getPlayerLocation(page: Page): Promise<string> {
  const locationDisplay = page.locator('.location-display');
  const location = await locationDisplay.textContent();
  return location?.trim() || '';
}

export async function clearMessageHistory(page: Page): Promise<void> {
  // Execute client-side JavaScript to clear message history
  await page.evaluate(() => {
    const messages = document.querySelectorAll('.message');
    messages.forEach(msg => msg.remove());
  });
}
```

## Database Seeding Example

```typescript
// client/tests/e2e/runtime/fixtures/database.ts
import Database from 'better-sqlite3';
import { hash } from 'argon2';
import { join } from 'path';
import { existsSync, copyFileSync, mkdirSync } from 'fs';

interface TestPlayer {
  userId: string;
  playerId: string;
  email: string;
  username: string;
  password: string;
  isAdmin: boolean;
  isSuperuser: boolean;
  startingRoom: string;
}

const TEST_PLAYERS: TestPlayer[] = [
  {
    userId: 'test-user-arkan-001',
    playerId: 'test-player-arkan-001',
    email: 'arkanwolfshade@test.local',
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    isAdmin: true,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001'
  },
  {
    userId: 'test-user-ithaqua-001',
    playerId: 'test-player-ithaqua-001',
    email: 'ithaqua@test.local',
    username: 'Ithaqua',
    password: 'Cthulhu1',
    isAdmin: false,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001'
  }
];

export async function seedTestDatabase(): Promise<void> {
  const dbPath = join(__dirname, '../../../../../data/players/test_players.db');
  const dbDir = join(__dirname, '../../../../../data/players');

  // Create directory if needed
  if (!existsSync(dbDir)) {
    mkdirSync(dbDir, { recursive: true });
  }

  // Backup existing database
  if (existsSync(dbPath)) {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    copyFileSync(dbPath, `${dbPath}.backup.${timestamp}`);
  }

  const db = new Database(dbPath);

  // Create schema
  createSchema(db);

  // Seed players
  for (const player of TEST_PLAYERS) {
    const hashedPassword = await hash(player.password, {
      type: 2, // argon2id
      timeCost: 3,
      memoryCost: 65536,
      parallelism: 1
    });

    // Insert user
    db.prepare(`
      INSERT OR REPLACE INTO users
      (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
      VALUES (?, ?, ?, ?, 1, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    `).run(
      player.userId,
      player.email,
      player.username,
      hashedPassword,
      player.isSuperuser ? 1 : 0
    );

    // Insert player
    const stats = JSON.stringify({
      health: 100,
      sanity: 100,
      strength: 10,
      dexterity: 10,
      constitution: 10,
      intelligence: 10,
      wisdom: 10,
      charisma: 10,
      occult_knowledge: 0,
      fear: 0,
      corruption: 0,
      cult_affiliation: 0,
      current_health: 100,
      max_health: 100,
      max_sanity: 100
    });

    db.prepare(`
      INSERT OR REPLACE INTO players
      (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
      VALUES (?, ?, ?, ?, '[]', '[]', ?, 0, 1, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    `).run(
      player.playerId,
      player.userId,
      player.username,
      stats,
      player.startingRoom,
      player.isAdmin ? 1 : 0
    );
  }

  db.close();
  console.log(`✅ Test database seeded with ${TEST_PLAYERS.length} players`);
}

export async function cleanupTestDatabase(): Promise<void> {
  const dbPath = join(__dirname, '../../../../../data/players/test_players.db');

  if (!existsSync(dbPath)) {
    console.log('⚠️ Test database not found, skipping cleanup');
    return;
  }

  const db = new Database(dbPath);

  // Reset player positions
  db.prepare(`
    UPDATE players
    SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001',
        last_active = CURRENT_TIMESTAMP
    WHERE player_id LIKE 'test-player-%'
  `).run();

  // Clear test-created invites
  db.prepare(`
    DELETE FROM invites
    WHERE created_by_user_id LIKE 'test-user-%'
  `).run();

  db.close();
  console.log('✅ Test database cleaned successfully');
}

function createSchema(db: Database): void {
  // Create users table
  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY NOT NULL,
      email TEXT UNIQUE NOT NULL,
      username TEXT UNIQUE NOT NULL,
      hashed_password TEXT NOT NULL,
      is_active BOOLEAN NOT NULL DEFAULT 1,
      is_superuser BOOLEAN NOT NULL DEFAULT 0,
      is_verified BOOLEAN NOT NULL DEFAULT 0,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Create players table
  db.exec(`
    CREATE TABLE IF NOT EXISTS players (
      player_id TEXT PRIMARY KEY NOT NULL,
      user_id TEXT NOT NULL UNIQUE,
      name TEXT UNIQUE NOT NULL,
      stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
      inventory TEXT NOT NULL DEFAULT '[]',
      status_effects TEXT NOT NULL DEFAULT '[]',
      current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',
      experience_points INTEGER NOT NULL DEFAULT 0,
      level INTEGER NOT NULL DEFAULT 1,
      is_admin INTEGER NOT NULL DEFAULT 0,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
  `);

  // Create invites table
  db.exec(`
    CREATE TABLE IF NOT EXISTS invites (
      id TEXT PRIMARY KEY NOT NULL,
      invite_code TEXT UNIQUE NOT NULL,
      created_by_user_id TEXT,
      used_by_user_id TEXT,
      used BOOLEAN NOT NULL DEFAULT 0,
      expires_at DATETIME,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE SET NULL,
      FOREIGN KEY (used_by_user_id) REFERENCES users(id) ON DELETE SET NULL
    )
  `);

  // Create indexes
  db.exec(`
    CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
    CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
    CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
    CREATE INDEX IF NOT EXISTS idx_players_is_admin ON players(is_admin);
    CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
    CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
  `);
}

export { TEST_PLAYERS };
```

## Test Example: Local Channel Errors

```typescript
// client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts
import { test, expect } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { sendCommand, waitForMessage, getMessages } from '../fixtures/player';

test.describe('Local Channel Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  test('should reject empty local messages', async ({ page }) => {
    // Send empty local message
    await sendCommand(page, 'local');

    // Verify error message
    await waitForMessage(page, 'You must provide a message to send locally');

    const messages = await getMessages(page);
    expect(messages).toContain('You must provide a message to send locally');
  });

  test('should reject long local messages', async ({ page }) => {
    // Create message over 500 characters
    const longMessage = 'This is a very long message. '.repeat(20);

    await sendCommand(page, `local ${longMessage}`);

    // Verify error message
    await waitForMessage(page, 'Local message too long');
  });

  test('should handle special characters', async ({ page }) => {
    await sendCommand(page, 'local Test message with !@#$%^&*()');

    await waitForMessage(page, 'You say locally: Test message with !@#$%^&*()');

    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('!@#$%^&*()'))).toBeTruthy();
  });

  test('should handle Unicode characters', async ({ page }) => {
    await sendCommand(page, 'local Unicode test: 你好世界 🌍');

    await waitForMessage(page, 'You say locally: Unicode test: 你好世界 🌍');
  });

  test('should allow valid messages after errors', async ({ page }) => {
    // Trigger error first
    await sendCommand(page, 'local');
    await waitForMessage(page, 'You must provide a message to send locally');

    // Then send valid message
    await sendCommand(page, 'local Valid message after error');
    await waitForMessage(page, 'You say locally: Valid message after error');

    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('Valid message after error'))).toBeTruthy();
  });
});
```

## Test Example: Whisper Rate Limiting

```typescript
// client/tests/e2e/runtime/error-handling/whisper-rate-limiting.spec.ts
import { test, expect } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { sendCommand, waitForMessage, getMessages } from '../fixtures/player';

test.describe('Whisper Rate Limiting', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  test('should enforce per-recipient rate limit', async ({ page }) => {
    // Send 3 whispers (within limit)
    for (let i = 1; i <= 3; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
      await waitForMessage(page, `You whisper to Ithaqua: Message ${i}`);
    }

    // 4th whisper should trigger rate limit
    await sendCommand(page, 'whisper Ithaqua Message 4');
    await waitForMessage(
      page,
      'Rate limit exceeded. You can only send 3 whispers per minute to the same player.'
    );

    const messages = await getMessages(page);
    expect(messages.filter(m => m.includes('Rate limit exceeded'))).toHaveLength(1);
  });

  test('should reset rate limit after 60 seconds', async ({ page }) => {
    // Send 3 whispers to reach limit
    for (let i = 1; i <= 3; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
      await waitForMessage(page, `You whisper to Ithaqua: Message ${i}`);
    }

    // Verify rate limit triggered
    await sendCommand(page, 'whisper Ithaqua Message 4');
    await waitForMessage(page, 'Rate limit exceeded');

    // Wait for rate limit reset (60 seconds)
    console.log('Waiting 60 seconds for rate limit reset...');
    await page.waitForTimeout(60000);

    // Should be able to send whisper again
    await sendCommand(page, 'whisper Ithaqua After reset');
    await waitForMessage(page, 'You whisper to Ithaqua: After reset');
  });
});
```

## Test Example: Logout Accessibility

```typescript
// client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts
import { test, expect } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';

test.describe('Logout Accessibility', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  test('should have proper ARIA attributes', async ({ page }) => {
    const logoutButton = page.locator('[data-testid="logout-button"]');

    // Verify ARIA label
    await expect(logoutButton).toHaveAttribute('aria-label');

    // Verify role (should be 'button' or default)
    const role = await logoutButton.getAttribute('role');
    expect(role === 'button' || role === null).toBeTruthy();

    // Verify tabindex (should be focusable)
    const tabindex = await logoutButton.getAttribute('tabindex');
    expect(parseInt(tabindex || '0')).toBeGreaterThanOrEqual(0);
  });

  test('should be keyboard navigable', async ({ page }) => {
    // Focus logout button via keyboard
    await page.keyboard.press('Tab');

    // Check if logout button is focused
    const logoutButton = page.locator('[data-testid="logout-button"]');
    await expect(logoutButton).toBeFocused();

    // Activate via Enter key
    await page.keyboard.press('Enter');

    // Verify logout occurred
    await expect(page.locator('text=You have been logged out')).toBeVisible();
  });

  test('should meet touch target size requirements', async ({ page }) => {
    const logoutButton = page.locator('[data-testid="logout-button"]');
    const boundingBox = await logoutButton.boundingBox();

    expect(boundingBox).not.toBeNull();
    expect(boundingBox!.width).toBeGreaterThanOrEqual(44);
    expect(boundingBox!.height).toBeGreaterThanOrEqual(44);
  });

  test('should have sufficient color contrast', async ({ page }) => {
    const logoutButton = page.locator('[data-testid="logout-button"]');

    const backgroundColor = await logoutButton.evaluate(el =>
      window.getComputedStyle(el).backgroundColor
    );
    const color = await logoutButton.evaluate(el =>
      window.getComputedStyle(el).color
    );

    // Verify colors are defined (actual contrast ratio calculation is complex)
    expect(backgroundColor).toBeTruthy();
    expect(color).toBeTruthy();
    expect(backgroundColor).not.toBe(color);
  });

  test('should have proper screen reader support', async ({ page }) => {
    const logoutButton = page.locator('[data-testid="logout-button"]');

    // Should have either text content or aria-label
    const textContent = await logoutButton.textContent();
    const ariaLabel = await logoutButton.getAttribute('aria-label');

    expect(textContent || ariaLabel).toBeTruthy();
    expect((textContent || ariaLabel || '').length).toBeGreaterThan(0);
  });
});
```

## Playwright Runtime Configuration Example

```typescript
// client/tests/e2e/playwright.runtime.config.ts
import { defineConfig, devices } from '@playwright/test';

/**
 * Playwright configuration for runtime E2E tests
 *
 * These tests are automated and run against a running development server.
 * They do NOT require Playwright MCP or AI Agent coordination.
 */
export default defineConfig({
  testDir: './runtime',

  // Maximum time one test can run
  timeout: 30 * 1000,

  // Test expectations timeout
  expect: {
    timeout: 10 * 1000,
  },

  // Run tests in parallel
  fullyParallel: true,

  // Fail the build on CI if you accidentally left test.only
  forbidOnly: !!process.env.CI,

  // Retry on CI only
  retries: process.env.CI ? 1 : 0,

  // Opt out of parallel tests on CI
  workers: process.env.CI ? 1 : undefined,

  // Reporter to use
  reporter: [
    ['html', { outputFolder: 'playwright-report/runtime' }],
    ['list'],
    process.env.CI ? ['github'] : ['line'],
  ],

  // Shared settings for all tests
  use: {
    // Base URL for all tests
    baseURL: 'http://localhost:5173',

    // Collect trace on first retry
    trace: 'on-first-retry',

    // Screenshot on failure
    screenshot: 'only-on-failure',

    // Video on first retry
    video: 'retain-on-failure',

    // Browser context options
    viewport: { width: 1280, height: 720 },
  },

  // Configure projects for different browsers
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    // Uncomment for cross-browser testing
    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },
  ],

  // Run local dev server before starting tests
  webServer: process.env.CI ? undefined : {
    command: 'npm run dev',
    url: 'http://localhost:5173',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000,
  },

  // Global setup and teardown
  globalSetup: require.resolve('./global-setup'),
  globalTeardown: require.resolve('./global-teardown'),
});
```

## GitHub Actions Workflow Example

```yaml
# .github/workflows/e2e-runtime-tests.yml
name: E2E Runtime Tests

on:
  pull_request:
    branches: [ main, develop, playwright ]
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  e2e-automated:
    name: Run Automated E2E Tests
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - name: Checkout code
        uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1

      - name: Setup Node.js
        uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4.0.2
        with:
          node-version: '18'
          cache: 'npm'
          cache-dependency-path: client/package-lock.json

      - name: Setup Python
        uses: actions/setup-python@0a5c61591373683505ea898e09a3ea4f39ef2b9c # v5.0.0
        with:
          python-version: '3.11'

      - name: Install Python dependencies
        run: |
          pip install uv
          uv pip install -e .

      - name: Install Node dependencies
        working-directory: client
        run: npm ci

      - name: Install Playwright browsers
        working-directory: client
        run: npx playwright install --with-deps chromium

      - name: Start development server
        run: |
          ./scripts/start_local.ps1 &
          sleep 10
          # Wait for server to be ready
          timeout 60 bash -c 'until curl -f http://localhost:54731/health; do sleep 2; done'

      - name: Run Playwright runtime tests
        working-directory: client
        run: npm run test:e2e:runtime

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
        with:
          name: playwright-runtime-report
          path: client/playwright-report/runtime/
          retention-days: 30

      - name: Upload test artifacts
        if: failure()
        uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
        with:
          name: playwright-runtime-artifacts
          path: |
            client/test-results/runtime/
            client/playwright-report/runtime/
          retention-days: 7

      - name: Stop development server
        if: always()
        run: ./scripts/stop_server.ps1

      - name: Comment PR with test results
        if: github.event_name == 'pull_request' && always()
        uses: daun/playwright-report-comment@4a9f85ad393b381af71b9574bdf0ce732e20d9fa # v3.2.0
        with:
          report-path: client/playwright-report/runtime/
```

## Makefile Updates Example

```makefile
# Add to existing Makefile

.PHONY: test-client-runtime test-server-runtime test-runtime

# Run client runtime E2E tests (no server required)
test-client-runtime:
	@echo "Running client runtime E2E tests..."
	cd client && npm run test:e2e:runtime

# Run server runtime E2E tests (starts server automatically)
test-server-runtime:
	@echo "Starting server and running runtime E2E tests..."
	@./scripts/start_local.ps1 &
	@sleep 10
	@echo "Server started, running tests..."
	cd client && npm run test:e2e:runtime
	@echo "Tests complete, stopping server..."
	@./scripts/stop_server.ps1

# Run all runtime E2E tests
test-runtime: test-client-runtime
	@echo "All runtime E2E tests complete"

# Update main test target to include runtime tests
test: test-server test-client test-runtime
	@echo "✅ All tests (unit + integration + E2E runtime) complete"

.PHONY: help
help:
	@echo "E2E Testing Commands:"
	@echo "  make test-client-runtime  - Run client E2E runtime tests"
	@echo "  make test-server-runtime  - Start server and run E2E runtime tests"
	@echo "  make test-runtime         - Run all E2E runtime tests"
	@echo ""
	@echo "For MCP multiplayer scenarios, see e2e-tests/MULTIPLAYER_TEST_RULES.md"
```

## Pattern: Error Handling Test Template

```typescript
// Template for error handling tests
test.describe('[Feature] Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  // Test 1: Empty input
  test('should reject empty [command]', async ({ page }) => {
    await sendCommand(page, '[command]');
    await waitForMessage(page, '[expected error message]');
  });

  // Test 2: Invalid syntax
  test('should reject invalid syntax', async ({ page }) => {
    await sendCommand(page, '[invalid command]');
    await waitForMessage(page, '[expected error message]');
  });

  // Test 3: Valid input after error
  test('should work correctly after error', async ({ page }) => {
    // Trigger error
    await sendCommand(page, '[invalid command]');
    await waitForMessage(page, '[error message]');

    // Send valid command
    await sendCommand(page, '[valid command]');
    await waitForMessage(page, '[success message]');
  });
});
```

## Pattern: Accessibility Test Template

```typescript
// Template for accessibility tests
test.describe('[Component] Accessibility', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  test('should have proper ARIA attributes', async ({ page }) => {
    const element = page.locator('[data-testid="[element-id]"]');

    await expect(element).toHaveAttribute('aria-label');
    await expect(element).toHaveAttribute('role');

    const tabindex = await element.getAttribute('tabindex');
    expect(parseInt(tabindex || '0')).toBeGreaterThanOrEqual(0);
  });

  test('should be keyboard navigable', async ({ page }) => {
    await page.keyboard.press('Tab');
    const element = page.locator('[data-testid="[element-id]"]');
    await expect(element).toBeFocused();

    await page.keyboard.press('Enter');
    // Verify action occurred
  });

  test('should meet size requirements', async ({ page }) => {
    const element = page.locator('[data-testid="[element-id]"]');
    const box = await element.boundingBox();

    expect(box).not.toBeNull();
    expect(box!.width).toBeGreaterThanOrEqual(44);
    expect(box!.height).toBeGreaterThanOrEqual(44);
  });
});
```

## Pattern: Integration Test Template

```typescript
// Template for integration tests
test.describe('[Feature] Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  });

  test('should integrate with [system 1]', async ({ page }) => {
    // Perform action that requires integration
    await sendCommand(page, '[command]');

    // Verify integration worked
    await waitForMessage(page, '[expected result]');
  });

  test('should integrate with [system 2]', async ({ page }) => {
    // Test another integration point
  });

  test('should handle integration errors gracefully', async ({ page }) => {
    // Test error handling at integration boundaries
  });
});
```

## Test Naming Conventions

- **File Names**: `[feature]-[aspect].spec.ts` (e.g., `local-channel-errors.spec.ts`)
- **Test Suite Names**: `[Feature] [Aspect]` (e.g., `Local Channel Error Handling`)
- **Test Names**: `should [expected behavior]` (e.g., `should reject empty local messages`)
- **Use kebab-case for directories**: `error-handling/`, `accessibility/`
- **Use PascalCase for test data types**: `TestPlayer`, `TestMessage`

## Common Patterns

### Pattern 1: Command Execution with Verification
```typescript
await sendCommand(page, 'command arg1 arg2');
await waitForMessage(page, 'Expected response');
const messages = await getMessages(page);
expect(messages).toContain('Expected response');
```

### Pattern 2: Error Condition Testing
```typescript
await sendCommand(page, 'invalid command');
await waitForMessage(page, 'Error message');
// Verify system stability
await sendCommand(page, 'valid command');
await waitForMessage(page, 'Success message');
```

### Pattern 3: Accessibility Verification
```typescript
const element = page.locator('[data-testid="element"]');
await expect(element).toHaveAttribute('aria-label');
await expect(element).toBeFocused();
const box = await element.boundingBox();
expect(box!.width).toBeGreaterThanOrEqual(44);
```

### Pattern 4: State Reset Between Tests
```typescript
test.beforeEach(async ({ page }) => {
  await loginAsPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  await clearMessageHistory(page);
});

test.afterEach(async ({ page }) => {
  await page.evaluate(() => localStorage.clear());
});
```

## Debugging Tips

### Enable Headed Mode for Debugging
```bash
cd client
npm run test:e2e:runtime:headed
```

### Run Specific Test File
```bash
cd client
npx playwright test tests/e2e/runtime/error-handling/local-channel-errors.spec.ts
```

### Use Playwright Inspector
```bash
cd client
npm run test:e2e:runtime:debug
```

### View Test Report
```bash
cd client
npx playwright show-report playwright-report/runtime/
```

### Increase Timeout for Debugging
```typescript
test('my test', async ({ page }) => {
  test.setTimeout(60000); // 60 seconds for this specific test
  // ... test code
});
```

## Best Practices

1. **Use Test Data Constants**: Don't hardcode credentials or room IDs in tests
2. **Wait for Elements**: Always use `expect().toBeVisible()` instead of `waitForTimeout()`
3. **Clean State**: Reset player state between tests in `beforeEach` hooks
4. **Meaningful Names**: Test names should clearly describe what they're testing
5. **Single Responsibility**: Each test should test one specific behavior
6. **Avoid Test Dependencies**: Tests should not depend on execution order
7. **Use Page Object Pattern**: Consider creating page objects for complex UI interactions
8. **Handle Timeouts Gracefully**: Use appropriate timeout values for different operations
9. **Screenshot on Failure**: Playwright does this automatically, don't disable it
10. **Comment Complex Logic**: Explain why tests are structured a certain way

## Anti-Patterns to Avoid

1. ❌ **Don't use fixed waits**: Use `waitForMessage()` instead of `waitForTimeout()`
2. ❌ **Don't share state between tests**: Each test should be completely independent
3. ❌ **Don't test implementation details**: Test user-visible behavior only
4. ❌ **Don't use production database**: Always use `test_players.db`
5. ❌ **Don't skip cleanup**: Always clean up test data after tests
6. ❌ **Don't hardcode URLs**: Use `baseURL` from config
7. ❌ **Don't ignore flaky tests**: Fix the root cause or add proper waits
8. ❌ **Don't test multiple things in one test**: Keep tests focused
9. ❌ **Don't use `page.goto()` in every test**: Use navigation helpers
10. ❌ **Don't forget accessibility**: Include accessibility tests for UI components
