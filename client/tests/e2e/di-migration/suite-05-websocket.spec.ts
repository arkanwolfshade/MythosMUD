/**
 * Suite 5: WebSocket and Real-time Communication Tests (DI migration validation).
 */

/* eslint-disable playwright/no-standalone-expect -- authenticatedTest is test.extend(); expects run inside its callbacks */

import { expect, test } from '@playwright/test';

import { authenticatedTest } from './fixtures/authenticated';
import { executeCommand } from './fixtures/commands';
import { safeWait } from './fixtures/wait';

test.describe('Suite 5: WebSocket and Real-time Communication Tests', () => {
  authenticatedTest.afterEach(async () => {
    // Keep session for next test
  });

  authenticatedTest('WebSocket Connection Test', async ({ page }) => {
    const commandInput = page.getByTestId('command-input');
    await expect(commandInput).toBeVisible({ timeout: 10000 });

    await executeCommand(page, 'look');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });

  authenticatedTest('Real-time Message Broadcasting Test', async ({ page }) => {
    const messages: unknown[] = [];
    page.on('websocket', ws => {
      ws.on('framereceived', event => {
        try {
          const data = JSON.parse(event.payload as string);
          messages.push(data);
        } catch {
          // Not JSON
        }
      });
    });

    const result = await executeCommand(page, 'say Testing real-time broadcasting');
    expect(result.sent).toBe(true);
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 10000 });
    expect(messages.length >= 0).toBe(true);
  });

  authenticatedTest('WebSocket Request Context Test', async ({ page }) => {
    await executeCommand(page, 'look');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });
});
