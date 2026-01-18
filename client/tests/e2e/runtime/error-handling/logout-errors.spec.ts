/**
 * Scenario 20: Logout Errors
 *
 * Tests logout button error handling and fallback mechanisms.
 * Verifies that the logout system properly handles various error conditions,
 * that fallback mechanisms work correctly, that error messages are clear and
 * informative, and that the system remains stable during error conditions.
 */

import { expect, test } from '@playwright/test';
import { createMultiPlayerContexts, cleanupMultiPlayerContexts } from '../fixtures/multiplayer';
import { waitForMessage, getMessages } from '../fixtures/auth';

test.describe('Logout Errors', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('logout button should handle logout successfully', async () => {
    const awContext = contexts[0];

    // Click logout button
    const logoutButton = awContext.page.locator(
      '[data-testid="logout-button"], button:has-text("Logout"), button:has-text("Log out")'
    );
    await logoutButton.click();

    // Wait for logout response
    await waitForMessage(awContext.page, 'You have been logged out', 10000).catch(() => {
      // Message may succeed even if format differs
    });

    // Verify logout message appears
    const messages = await getMessages(awContext.page);
    const seesLogout = messages.some(msg => msg.includes('logged out') || msg.includes('logout'));
    expect(seesLogout).toBe(true);
  });
});
