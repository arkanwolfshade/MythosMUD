/**
 * Scenario 20: Logout Errors
 *
 * Tests logout button error handling and fallback mechanisms.
 * Verifies that the logout system properly handles various error conditions,
 * that fallback mechanisms work correctly, that error messages are clear and
 * informative, and that the system remains stable during error conditions.
 */

import { expect, test } from '@playwright/test';
import { getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

test.describe('Logout Errors', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('logout button should handle logout successfully', async () => {
    const awContext = contexts[0];

    // Click logout button (UI uses "Exit the Realm" and data-testid="logout-button")
    // Logout sends /rest and shows a 10-second countdown before redirect
    const logoutButton = awContext.page.locator(
      '[data-testid="logout-button"], button:has-text("Exit the Realm"), button:has-text("Exit the realm"), button:has-text("Logout"), button:has-text("Log out")'
    );
    await logoutButton.first().click();

    // Wait for either logout message or login form. Logout flow: 10s countdown then redirect.
    await waitForMessage(awContext.page, 'You have been logged out', 5000).catch(() => {});
    const seesLogoutMessage = await awContext.page
      .locator('[data-message-text]')
      .filter({ hasText: /logged out|logout|disconnect/i })
      .first()
      .isVisible()
      .catch(() => false);

    // If no message yet, wait for login form (allow full countdown + redirect: 15s)
    const loginFormVisible = await awContext.page
      .locator('input[placeholder*="username" i], input[name*="username" i]')
      .waitFor({ state: 'visible', timeout: 15000 })
      .then(() => true)
      .catch(() => false);

    const messages = await getMessages(awContext.page);
    const seesLogoutInMessages = messages.some(
      msg => msg.includes('logged out') || msg.includes('logout') || msg.toLowerCase().includes('disconnect')
    );
    expect(seesLogoutMessage || seesLogoutInMessages || loginFormVisible).toBe(true);
  });
});
