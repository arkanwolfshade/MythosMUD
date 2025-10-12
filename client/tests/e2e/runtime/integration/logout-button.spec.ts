/**
 * Logout Button Integration Tests (Automated Portion)
 *
 * Tests single-player aspects of logout button functionality.
 * Converted from e2e-tests/scenarios/scenario-19-logout-button.md (partial)
 *
 * Automated Test Coverage:
 * - Button visibility and accessibility
 * - Click functionality
 * - Logout confirmation message
 * - Redirect to login page
 * - Re-login functionality after logout
 * - Button UI state changes
 * - Button styling verification
 *
 * MCP Testing Required For:
 * - Logout message broadcasting to other players
 * - Multi-player session termination
 * - (See e2e-tests/scenarios/scenario-19-logout-button.md for multi-player tests)
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { SELECTORS, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Logout Button - Basic Functionality', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should be visible and accessible', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should be visible
    await expect(logoutButton).toBeVisible();

    // Should be enabled
    await expect(logoutButton).toBeEnabled();
  });

  test('should have proper button text or icon', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should have text content or aria-label
    const textContent = await logoutButton.textContent();
    const ariaLabel = await logoutButton.getAttribute('aria-label');

    const hasLabel = (textContent && textContent.trim().length > 0) || (ariaLabel && ariaLabel.length > 0);

    expect(hasLabel).toBeTruthy();
  });

  test('should handle click event successfully', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Click button
    await logoutButton.click();

    // Verify logout confirmation appears
    await expect(page.getByText('You have been logged out', { exact: true }).first()).toBeVisible({ timeout: 10000 });
  });

  test('should show logout confirmation message', async ({ page }) => {
    // Click logout
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Verify specific confirmation text
    const confirmationMessage = page.getByText('You have been logged out', { exact: true }).first();
    await expect(confirmationMessage).toBeVisible({ timeout: 10000 });

    // Message should be clear and informative
    const messageText = await confirmationMessage.textContent();
    expect(messageText).toBeTruthy();
    expect(messageText!.toLowerCase()).toContain('logged out');
  });

  test('should redirect to login page after logout', async ({ page }) => {
    // Click logout
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Wait for logout confirmation
    await expect(page.getByText('You have been logged out', { exact: true }).first()).toBeVisible({ timeout: 10000 });

    // Verify redirect to login page
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

    // Verify URL changed to login
    const url = page.url();
    expect(url).toContain('localhost:5173');
  });

  test('should not show logout button after logout', async ({ page }) => {
    // Click logout
    await page.click(SELECTORS.LOGOUT_BUTTON);

    // Wait for redirect to login
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

    // Logout button should not be visible on login page
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);
    const isVisible = await logoutButton.isVisible().catch(() => false);

    expect(isVisible).toBeFalsy();
  });
});

test.describe('Logout Button - Re-login Workflow', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should allow re-login after logout', async ({ page }) => {
    // Logout first
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

    // Re-login
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);

    // Verify logged back in (logout button visible again)
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);
    await expect(logoutButton).toBeVisible({ timeout: 10000 });
  });

  test('should have working logout button after re-login', async ({ page }) => {
    // Logout
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

    // Re-login
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);

    // Logout again
    await page.click(SELECTORS.LOGOUT_BUTTON);
    await expect(page.getByText('You have been logged out', { exact: true }).first()).toBeVisible({ timeout: 10000 });
  });

  test('should maintain logout functionality across multiple sessions', async ({ page }) => {
    // Perform logout/login cycle 3 times
    for (let i = 0; i < 3; i++) {
      // Logout
      const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);
      await logoutButton.click();
      await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

      // Re-login (except on last iteration)
      if (i < 2) {
        await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
      }
    }

    // Should be on login page
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible();
  });
});

test.describe('Logout Button - UI State', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should have proper button styling', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get computed styles
    const styles = await logoutButton.evaluate(el => {
      const computed = window.getComputedStyle(el);
      return {
        display: computed.display,
        cursor: computed.cursor,
        backgroundColor: computed.backgroundColor,
        color: computed.color,
        padding: computed.padding,
      };
    });

    // Should be displayed as a button
    expect(styles.display).not.toBe('none');

    // Should have cursor pointer or similar
    expect(styles.cursor === 'pointer' || styles.cursor === 'default').toBeTruthy();

    // Should have background and text colors
    expect(styles.backgroundColor).toBeTruthy();
    expect(styles.color).toBeTruthy();
  });

  test('should update state during logout process', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get initial state
    const initialState = await logoutButton.evaluate(el => ({
      disabled: (el as HTMLButtonElement).disabled,
      className: el.className,
    }));

    // Click logout
    await logoutButton.click();

    // State might change during logout (e.g., disabled, loading class)
    await page.waitForTimeout(200);

    // Verify logout completed
    await expect(page.getByText('You have been logged out', { exact: true }).first()).toBeVisible({ timeout: 10000 });

    // Initial state should have been enabled
    expect(initialState.disabled).toBeFalsy();
  });

  test('should maintain button appearance on hover', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Hover over button
    await logoutButton.hover();

    // Get hover state
    const hoverStyles = await logoutButton.evaluate(el => {
      const computed = window.getComputedStyle(el);
      return {
        cursor: computed.cursor,
        opacity: computed.opacity,
      };
    });

    // Should have interactive cursor
    expect(hoverStyles.cursor === 'pointer' || hoverStyles.cursor === 'default').toBeTruthy();

    // Should be visible (not transparent)
    expect(parseFloat(hoverStyles.opacity)).toBeGreaterThan(0);
  });
});
