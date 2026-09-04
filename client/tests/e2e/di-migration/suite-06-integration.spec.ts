/**
 * Suite 6: Integration Tests (DI migration validation).
 */

/* eslint-disable playwright/no-standalone-expect -- authenticatedTest is test.extend(); expects run inside its callbacks */

import { expect, test } from '@playwright/test';

import { authenticatedTest } from './fixtures/authenticated';
import { executeCommand } from './fixtures/commands';
import { safeWait } from './fixtures/wait';

test.describe('Suite 6: Integration Tests', () => {
  authenticatedTest.afterEach(async () => {
    // Keep session for next test
  });

  authenticatedTest('Service Interaction Test', async ({ page }) => {
    await executeCommand(page, 'status');
    await safeWait(page, 2000);

    await executeCommand(page, 'say Testing service interaction');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });

  authenticatedTest('Multi-Service Workflow Test', async ({ page }) => {
    await executeCommand(page, 'look');
    await safeWait(page, 2000);

    await executeCommand(page, 'stand');
    await safeWait(page, 2000);
    await executeCommand(page, 'go north');
    await safeWait(page, 2000);

    await executeCommand(page, 'status');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });

  authenticatedTest('Backward Compatibility Test', async ({ page }) => {
    await executeCommand(page, 'look');
    await safeWait(page, 2000);

    await executeCommand(page, 'status');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });
});
