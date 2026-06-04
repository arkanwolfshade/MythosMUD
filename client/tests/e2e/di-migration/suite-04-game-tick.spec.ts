/**
 * Suite 4: Game Tick and Background Task Tests (DI migration validation).
 */

/* eslint-disable playwright/no-standalone-expect -- authenticatedTest is test.extend(); expects run inside its callbacks */

import { expect, test } from '@playwright/test';

import { authenticatedTest } from './fixtures/authenticated';
import { executeCommand } from './fixtures/commands';
import { safeWait, waitForGameTick } from './fixtures/wait';

test.describe('Suite 4: Game Tick and Background Task Tests', () => {
  authenticatedTest.afterEach(async () => {
    // Keep session for next test
  });

  authenticatedTest('Game Tick Processing Test', async ({ page }) => {
    await waitForGameTick(page);

    await executeCommand(page, 'status');
    await safeWait(page, 2000);

    const statusOutput = page.locator(
      '[data-message-text*="Name:"], [data-message-text*="Location:"], [data-message-text*="Health:"]'
    );
    await expect(statusOutput.first()).toBeVisible({ timeout: 5000 });
  });

  authenticatedTest('Background Task Service Access Test', async ({ page }) => {
    await waitForGameTick(page);
    await waitForGameTick(page);

    await executeCommand(page, 'time');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });
});
