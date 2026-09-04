/**
 * Suite 1: Core Service Functionality Tests (DI migration validation).
 */

/* eslint-disable playwright/no-standalone-expect -- authenticatedTest is test.extend(); expects run inside its callbacks */

import { expect, test } from '@playwright/test';

import { authenticatedTest } from './fixtures/authenticated';
import { executeCommand } from './fixtures/commands';
import { expectStatusCommandOutput } from './fixtures/status-output';
import { safeWait } from './fixtures/wait';

test.describe('Suite 1: Core Service Functionality Tests', () => {
  authenticatedTest.afterEach(async () => {
    // Keep session for next test; do not logout
  });

  authenticatedTest('Container Initialization Test', async ({ page }) => {
    const commandInput = page.getByTestId('command-input');
    await expect(commandInput).toBeVisible({ timeout: 10000 });

    const lookResult = await executeCommand(page, 'look');
    expect(lookResult.sent).toBe(true);
    await safeWait(page, 2000);

    const statusResult = await executeCommand(page, 'status');
    expect(statusResult.sent).toBe(true);
    await safeWait(page, 2000);

    const sayResult = await executeCommand(page, 'say Testing container initialization');
    expect(sayResult.sent).toBe(true);
    await safeWait(page, 2000);

    const timeResult = await executeCommand(page, 'time');
    expect(timeResult.sent).toBe(true);
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 10000 });

    const anyResponseReceived =
      lookResult.responseReceived ||
      statusResult.responseReceived ||
      sayResult.responseReceived ||
      timeResult.responseReceived;
    expect(anyResponseReceived).toBe(true);
  });

  authenticatedTest('Combat Services Test', async ({ page }) => {
    test.setTimeout(60000);

    const commandInput = page.getByTestId('command-input');
    await expect(commandInput).toBeVisible({ timeout: 10000 });

    const commandResult = await executeCommand(page, 'status');
    expect(commandResult.sent).toBe(true);
    await safeWait(page, 5000);
    await expectStatusCommandOutput(page, commandResult);
  });

  authenticatedTest('Magic Services Test', async ({ page }) => {
    await executeCommand(page, 'meditate');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });

    await executeCommand(page, 'pray');
    await safeWait(page, 2000);
  });

  authenticatedTest('Chat Service Test', async ({ page }) => {
    await executeCommand(page, 'say Hello, testing chat service');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });

    await executeCommand(page, 'local Testing local channel');
    await safeWait(page, 2000);
  });

  authenticatedTest('Other Services Test', async ({ page }) => {
    await executeCommand(page, 'time');
    await safeWait(page, 2000);

    const gameLogMessages = page.locator('[data-message-text]');
    await expect(gameLogMessages.first()).toBeVisible({ timeout: 5000 });
  });
});
