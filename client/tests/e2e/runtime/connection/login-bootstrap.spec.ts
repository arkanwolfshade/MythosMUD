/**
 * Smoke tests for loginPlayer bootstrap (Firefox runtime E2E).
 */

import { expect, test } from '@playwright/test';

import { loginPlayer } from '../fixtures/auth';
import { TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Login bootstrap', () => {
  for (const player of TEST_PLAYERS) {
    test(`${player.username} reaches command input via loginPlayer`, async ({ page }) => {
      await loginPlayer(page, player.username, player.password);
      await expect(page.getByTestId('command-input')).toBeVisible({ timeout: 30000 });
    });
  }
});
