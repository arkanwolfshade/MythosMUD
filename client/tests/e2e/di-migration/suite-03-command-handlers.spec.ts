/**
 * Suite 3: Command Handler Validation Tests (DI migration validation).
 */

/* eslint-disable playwright/no-standalone-expect -- authenticatedTest is test.extend(); expects run inside its callbacks */

import { expect, test } from '@playwright/test';

import { adminTest, authenticatedTest } from './fixtures/authenticated';
import { executeCommand } from './fixtures/commands';
import { safeWait } from './fixtures/wait';

test.describe('Suite 3: Command Handler Validation Tests', () => {
  authenticatedTest.afterEach(async () => {
    // Keep session for next test
  });

  authenticatedTest('Status Command Test', async ({ page }) => {
    await executeCommand(page, 'status');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });

    await executeCommand(page, 'whoami');
    await safeWait(page, 2000);
  });

  authenticatedTest('Communication Commands Test', async ({ page }) => {
    await executeCommand(page, 'say Testing say command');
    await safeWait(page, 2000);

    await executeCommand(page, 'local Testing local channel');
    await safeWait(page, 2000);

    await executeCommand(page, 'whisper TestPlayer Hello');
    await safeWait(page, 2000);
  });

  authenticatedTest('Magic Commands Test', async ({ page }) => {
    await executeCommand(page, 'meditate');
    await safeWait(page, 2000);

    await executeCommand(page, 'pray');
    await safeWait(page, 2000);
  });

  authenticatedTest('Combat Commands Test', async ({ page }) => {
    await executeCommand(page, 'attack TestTarget');
    await safeWait(page, 2000);

    await executeCommand(page, 'status');
    await safeWait(page, 2000);
  });

  adminTest('NPC Admin Commands Test', async ({ page }) => {
    await executeCommand(page, 'npc spawn TestNPC');
    await safeWait(page, 2000);
  });

  adminTest('Shutdown Command Test', async ({ page }) => {
    await executeCommand(page, 'shutdown 60');
    await safeWait(page, 2000);

    await executeCommand(page, 'shutdown cancel');
    await safeWait(page, 2000);
  });
});
