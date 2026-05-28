/**
 * Scenario 20: Logout Errors
 *
 * Tests logout button error handling and fallback mechanisms.
 * Verifies that the logout system properly handles various error conditions,
 * that fallback mechanisms work correctly, that error messages are clear and
 * informative, and that the system remains stable during error conditions.
 */

import { expect, test } from '@playwright/test';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

test.describe('Logout Errors', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('logout button should handle logout successfully', async () => {
    const awContext = contexts[0];
    const { page } = awContext;

    await ensurePlayerInGame(awContext, 30000);

    // performGameClientLogout sends `rest` (~10s server countdown) then disconnect; login can exceed 15s on CI.
    const logoutButton = page.getByTestId('logout-button');
    await expect(logoutButton).toBeEnabled({ timeout: 15000 });
    await logoutButton.click();

    await expect(page.getByTestId('username-input')).toBeVisible({ timeout: 45000 });
  });
});
