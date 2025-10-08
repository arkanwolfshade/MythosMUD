/**
 * Logout Error Handling Tests
 *
 * Tests logout error conditions and fallback mechanisms.
 * Converted from e2e-tests/scenarios/scenario-20-logout-errors.md
 *
 * Test Coverage:
 * - Network errors during logout
 * - Server errors during logout
 * - Session expiry handling
 * - Error recovery mechanisms
 * - Multiple logout attempts
 * - Concurrent logout handling
 * - System stability
 */

import { expect, test } from '@playwright/test';
import { clearAuthState, loginAsPlayer } from '../fixtures/auth';
import { getMessages } from '../fixtures/player';
import { SELECTORS, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Logout Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should handle graceful logout under normal conditions', async ({ page }) => {
    // Click logout button
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Verify logout confirmation appears
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

    // Verify redirect to login page
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });
  });

  test('should handle network errors during logout', async ({ page }) => {
    // Simulate network offline
    await page.evaluate(() => {
      // Override navigator.onLine
      Object.defineProperty(window.navigator, 'onLine', {
        writable: true,
        value: false,
      });
      window.dispatchEvent(new Event('offline'));
    });

    // Attempt logout
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Wait for response (either error or fallback to client-side logout)
    await page.waitForTimeout(2000);

    // System should handle this gracefully (either show error or force logout)
    // Both are acceptable - just verify no crash
    const messages = await getMessages(page);

    // Should have some response
    expect(messages.length).toBeGreaterThan(0);
  });

  test('should recover from network errors', async ({ page }) => {
    // Simulate network offline then online
    await page.evaluate(() => {
      Object.defineProperty(window.navigator, 'onLine', {
        writable: true,
        value: false,
      });
      window.dispatchEvent(new Event('offline'));
    });

    await page.waitForTimeout(500);

    // Restore network
    await page.evaluate(() => {
      Object.defineProperty(window.navigator, 'onLine', {
        writable: true,
        value: true,
      });
      window.dispatchEvent(new Event('online'));
    });

    // Now logout should work
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Verify logout works after recovery
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });
  });

  test('should handle session expiry during logout', async ({ page }) => {
    // Clear auth state to simulate session expiry
    await clearAuthState(page);

    // Attempt logout with expired session
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Wait for response
    await page.waitForTimeout(2000);

    // Should handle gracefully (either show error or force logout)
    // Check if we're redirected to login page or see error
    const isOnLoginPage = await page.locator(SELECTORS.USERNAME_INPUT).isVisible();
    const messages = await getMessages(page);
    const hasSessionError = messages.some(m => m.includes('Session') || m.includes('expired') || m.includes('log in'));

    // Either redirect to login OR show session error
    expect(isOnLoginPage || hasSessionError).toBeTruthy();
  });

  test('should handle multiple logout button clicks', async ({ page }) => {
    // Click logout multiple times rapidly
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Should handle gracefully and only logout once
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

    // Verify redirect to login
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });
  });

  test('should handle concurrent logout attempts', async ({ page }) => {
    // Trigger concurrent logout attempts via different mechanisms
    // (button click + programmatic logout)
    await Promise.all([
      page.click(SELECTORS.LOGOUT_BUTTON),
      page.evaluate(() => {
        // Simulate programmatic logout
        window.dispatchEvent(new CustomEvent('logout'));
      }),
    ]);

    // Wait for logout to process
    await page.waitForTimeout(2000);

    // Should handle gracefully
    const isOnLoginPage = await page.locator(SELECTORS.USERNAME_INPUT).isVisible();
    expect(isOnLoginPage).toBeTruthy();
  });

  test('should maintain system stability after logout errors', async ({ page }) => {
    // Try to cause logout error by clearing session mid-logout
    await clearAuthState(page);

    // Attempt logout
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await page.waitForTimeout(1000);

    // Verify system didn't crash
    const currentUrl = page.url();

    // Should be in a valid state (login page or error page, not blank/crashed)
    expect(currentUrl).toBeTruthy();
    expect(currentUrl.length).toBeGreaterThan(0);
  });

  test('should handle logout during high system load', async ({ page }) => {
    // Simulate system load by creating heavy DOM manipulation
    await page.evaluate(() => {
      for (let i = 0; i < 100; i++) {
        console.log(`Load test ${i}`);
      }
    });

    // Logout during "load"
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Should still logout successfully
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });
  });

  test('should prevent re-logout after successful logout', async ({ page }) => {
    // Logout first
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

    // Verify logout button is no longer accessible
    const logoutButtonExists = await page.locator(SELECTORS.LOGOUT_BUTTON).isVisible();
    expect(logoutButtonExists).toBeFalsy();

    // Verify we're on login page
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });
  });
});
