/**
 * Authentication Helpers for Runtime E2E Tests
 *
 * Provides functions for logging in and out of the game,
 * handling the full authentication flow including MOTD screen.
 */

import { Page, expect } from '@playwright/test';
import { SELECTORS, TIMEOUTS } from './test-data';

/**
 * Log in as a test player
 *
 * Handles the complete login flow:
 * 1. Navigate to login page
 * 2. Fill username and password
 * 3. Click login button
 * 4. Wait for MOTD screen
 * 5. Click Continue button
 * 6. Wait for game interface to load
 * 7. Wait for room subscription to stabilize
 *
 * @param page - Playwright page object
 * @param username - Player username
 * @param password - Player password
 */
export async function loginAsPlayer(page: Page, username: string, password: string): Promise<void> {
  // Navigate to login page
  await page.goto('/');

  // Wait for login form to be visible
  await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: TIMEOUTS.PAGE_LOAD });

  // Fill credentials
  await page.fill(SELECTORS.USERNAME_INPUT, username);
  await page.fill(SELECTORS.PASSWORD_INPUT, password);

  // Click login button
  await page.click(SELECTORS.LOGIN_BUTTON);

  // Wait for MOTD screen to appear
  await expect(page.locator(SELECTORS.CONTINUE_BUTTON)).toBeVisible({ timeout: TIMEOUTS.MOTD_SCREEN });

  // Click Continue button to enter game
  await page.click(SELECTORS.CONTINUE_BUTTON);

  // Wait for game interface to load (Chat panel is good indicator)
  await expect(page.locator('text=Chat')).toBeVisible({ timeout: TIMEOUTS.GAME_LOAD });

  // Additional wait for room subscription to stabilize
  // This prevents timing issues with message broadcasting
  await page.waitForTimeout(TIMEOUTS.ROOM_SUBSCRIPTION);
}

/**
 * Log out of the game
 *
 * Clicks logout button and verifies logout confirmation and redirect.
 *
 * @param page - Playwright page object
 */
export async function logout(page: Page): Promise<void> {
  // Click logout button
  await page.click(SELECTORS.LOGOUT_BUTTON);

  // Wait for logout confirmation message
  await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: TIMEOUTS.LOGOUT });

  // Verify redirect to login page
  await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: TIMEOUTS.PAGE_LOAD });
}

/**
 * Check if player is currently logged in
 *
 * @param page - Playwright page object
 * @returns true if player is logged in, false otherwise
 */
export async function isLoggedIn(page: Page): Promise<boolean> {
  try {
    const gameInterface = page.locator('text=Chat');
    return await gameInterface.isVisible({ timeout: 1000 });
  } catch {
    return false;
  }
}

/**
 * Wait for login form to be visible
 *
 * Used to verify logout or check if user is on login page.
 *
 * @param page - Playwright page object
 */
export async function waitForLoginForm(page: Page): Promise<void> {
  await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: TIMEOUTS.PAGE_LOAD });
}

/**
 * Login with error handling
 *
 * Attempts login and returns whether it was successful.
 * Useful for testing invalid credentials or error conditions.
 *
 * @param page - Playwright page object
 * @param username - Player username
 * @param password - Player password
 * @returns true if login succeeded, false if error occurred
 */
export async function attemptLogin(page: Page, username: string, password: string): Promise<boolean> {
  try {
    await loginAsPlayer(page, username, password);
    return true;
  } catch (error) {
    console.log('Login attempt failed:', error);
    return false;
  }
}

/**
 * Clear all authentication state
 *
 * Removes tokens, session data, and cached credentials.
 * Useful for testing session expiry or clean state scenarios.
 *
 * @param page - Playwright page object
 */
export async function clearAuthState(page: Page): Promise<void> {
  await page.evaluate(() => {
    localStorage.clear();
    sessionStorage.clear();

    // Clear any auth cookies
    document.cookie.split(';').forEach(cookie => {
      const name = cookie.split('=')[0].trim();
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    });
  });
}
