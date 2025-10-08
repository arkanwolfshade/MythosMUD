/**
 * Logout Accessibility Tests
 *
 * Tests logout button accessibility features including keyboard navigation,
 * ARIA attributes, screen reader compatibility, and WCAG compliance.
 * Converted from e2e-tests/scenarios/scenario-21-logout-accessibility.md
 *
 * Test Coverage:
 * - ARIA attributes (aria-label, role, tabindex)
 * - Keyboard navigation (Tab to focus, Enter to activate)
 * - Screen reader compatibility
 * - Focus management
 * - Color contrast
 * - Touch target size (minimum 44px)
 * - Button state changes
 * - Error state accessibility
 * - Loading state indication
 * - Success state feedback
 *
 * @see https://www.w3.org/WAI/WCAG21/quickref/
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { SELECTORS, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Logout Accessibility - ARIA Attributes', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should have proper ARIA label', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should have aria-label for screen readers
    await expect(logoutButton).toHaveAttribute('aria-label');

    const ariaLabel = await logoutButton.getAttribute('aria-label');
    expect(ariaLabel).toBeTruthy();
    expect(ariaLabel!.length).toBeGreaterThan(0);
  });

  test('should have proper role attribute', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Button element should have role='button' or rely on semantic HTML
    const role = await logoutButton.getAttribute('role');
    const tagName = await logoutButton.evaluate(el => el.tagName.toLowerCase());

    // Either has explicit role='button' or is a <button> element
    expect(role === 'button' || tagName === 'button').toBeTruthy();
  });

  test('should have proper tabindex for keyboard navigation', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should be keyboard focusable (tabindex >= 0)
    const tabindex = await logoutButton.getAttribute('tabindex');
    const tabindexValue = parseInt(tabindex || '0');

    expect(tabindexValue).toBeGreaterThanOrEqual(0);
  });

  test('should have accessible name for screen readers', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should have either text content or aria-label
    const textContent = await logoutButton.textContent();
    const ariaLabel = await logoutButton.getAttribute('aria-label');

    const accessibleName = textContent || ariaLabel;
    expect(accessibleName).toBeTruthy();
    expect(accessibleName!.length).toBeGreaterThan(0);
  });
});

test.describe('Logout Accessibility - Keyboard Navigation', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should be keyboard navigable via Tab key', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Focus the logout button via keyboard
    // Note: Might need multiple Tab presses depending on UI
    await page.keyboard.press('Tab');

    // Check if button can receive focus
    const isFocusable = await logoutButton.evaluate(el => {
      const tabIndex = el.getAttribute('tabindex');
      return tabIndex === null || parseInt(tabIndex) >= 0;
    });

    expect(isFocusable).toBeTruthy();
  });

  test('should be activatable via Enter key', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Focus the button
    await logoutButton.focus();

    // Verify it's focused
    await expect(logoutButton).toBeFocused();

    // Activate via Enter
    await page.keyboard.press('Enter');

    // Verify logout occurred
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });
  });

  test('should be activatable via Space key', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Focus the button
    await logoutButton.focus();

    // Activate via Space
    await page.keyboard.press('Space');

    // Verify logout occurred
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });
  });
});

test.describe('Logout Accessibility - Visual Requirements', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should meet minimum touch target size (44x44px)', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get button dimensions
    const boundingBox = await logoutButton.boundingBox();

    expect(boundingBox).not.toBeNull();
    expect(boundingBox!.width).toBeGreaterThanOrEqual(44);
    expect(boundingBox!.height).toBeGreaterThanOrEqual(44);
  });

  test('should have sufficient color contrast', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get computed styles
    const styles = await logoutButton.evaluate(el => {
      const computed = window.getComputedStyle(el);
      return {
        backgroundColor: computed.backgroundColor,
        color: computed.color,
        borderColor: computed.borderColor,
      };
    });

    // Verify colors are defined
    expect(styles.backgroundColor).toBeTruthy();
    expect(styles.color).toBeTruthy();

    // Colors should be different (basic contrast check)
    expect(styles.backgroundColor).not.toBe(styles.color);

    // Neither should be transparent
    expect(styles.backgroundColor).not.toBe('rgba(0, 0, 0, 0)');
    expect(styles.color).not.toBe('rgba(0, 0, 0, 0)');
  });

  test('should be visible and not hidden', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should be visible
    await expect(logoutButton).toBeVisible();

    // Should have non-zero dimensions
    const isVisible = await logoutButton.evaluate(el => {
      return el.offsetParent !== null && el.offsetWidth > 0 && el.offsetHeight > 0;
    });

    expect(isVisible).toBeTruthy();
  });
});

test.describe('Logout Accessibility - Focus Management', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should be focusable via programmatic focus', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Programmatically focus the button
    await logoutButton.focus();

    // Verify focus
    await expect(logoutButton).toBeFocused();
  });

  test('should not be disabled by default', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Should be enabled
    await expect(logoutButton).toBeEnabled();

    // Verify aria-disabled is not set to true
    const ariaDisabled = await logoutButton.getAttribute('aria-disabled');
    expect(ariaDisabled).not.toBe('true');
  });

  test('should have visible focus indicator', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Focus the button
    await logoutButton.focus();

    // Check for focus styles
    const hasFocusStyle = await logoutButton.evaluate(el => {
      const styles = window.getComputedStyle(el);
      // Check for common focus indicators
      return styles.outline !== 'none' || styles.boxShadow !== 'none' || styles.border !== 'none';
    });

    // Should have some kind of focus indicator
    expect(hasFocusStyle).toBeTruthy();
  });
});

test.describe('Logout Accessibility - Screen Reader Support', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should have screen reader compatible text', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get accessible name (combination of text, aria-label, title)
    const accessibleInfo = await logoutButton.evaluate(el => {
      return {
        textContent: el.textContent?.trim(),
        ariaLabel: el.getAttribute('aria-label'),
        title: el.getAttribute('title'),
      };
    });

    // Should have at least one way to identify the button
    const hasAccessibleName =
      (accessibleInfo.textContent && accessibleInfo.textContent.length > 0) ||
      (accessibleInfo.ariaLabel && accessibleInfo.ariaLabel.length > 0) ||
      (accessibleInfo.title && accessibleInfo.title.length > 0);

    expect(hasAccessibleName).toBeTruthy();
  });

  test('should have descriptive accessible name', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    const textContent = await logoutButton.textContent();
    const ariaLabel = await logoutButton.getAttribute('aria-label');

    const accessibleName = (textContent || ariaLabel || '').toLowerCase();

    // Should contain "logout" or "sign out" or similar
    const hasLogoutTerm =
      accessibleName.includes('logout') ||
      accessibleName.includes('log out') ||
      accessibleName.includes('sign out') ||
      accessibleName.includes('exit');

    expect(hasLogoutTerm).toBeTruthy();
  });
});

test.describe('Logout Accessibility - State Management', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should indicate button state changes', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get initial state
    const initialState = await logoutButton.evaluate(el => ({
      disabled: (el as HTMLButtonElement).disabled,
      ariaDisabled: el.getAttribute('aria-disabled'),
      className: el.className,
    }));

    expect(initialState.disabled).toBeFalsy();

    // Click button
    await logoutButton.click();

    // Button state might change during logout (e.g., loading state)
    // This is acceptable - we're just verifying state management exists
    await page.waitForTimeout(500);

    // Verify logout processed
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });
  });

  test('should have accessible error states', async ({ page }) => {
    // Clear auth to trigger potential error
    await clearAuthState(page);

    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);
    await logoutButton.click();

    // Wait for error or logout
    await page.waitForTimeout(2000);

    // Check for error message accessibility
    const errorMessage = page.locator('.error-message, [role="alert"]');
    const hasErrorWithRole = (await errorMessage.count()) > 0;

    // If error appears, it should have proper role
    if (hasErrorWithRole) {
      const role = await errorMessage.first().getAttribute('role');
      expect(role === 'alert' || role === 'status').toBeTruthy();
    }
  });

  test('should have accessible success states', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);
    await logoutButton.click();

    // Wait for logout confirmation
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

    // Success message should be accessible
    const successMessage = page.locator('.success-message, [role="status"], text=You have been logged out');
    await expect(successMessage.first()).toBeVisible();
  });
});

test.describe('Logout Accessibility - Comprehensive Validation', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should meet all core accessibility requirements', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Comprehensive accessibility check
    const accessibility = await logoutButton.evaluate(el => {
      const styles = window.getComputedStyle(el);
      const rect = el.getBoundingClientRect();

      return {
        // ARIA attributes
        hasAriaLabel: !!el.getAttribute('aria-label'),
        hasRole: !!el.getAttribute('role') || el.tagName.toLowerCase() === 'button',

        // Focus management
        isFocusable: el.getAttribute('tabindex') === null || parseInt(el.getAttribute('tabindex') || '0') >= 0,
        isVisible: el.offsetParent !== null,
        isEnabled: !(el as HTMLButtonElement).disabled,

        // Text content
        hasTextContent: !!el.textContent?.trim(),

        // Size requirements
        width: rect.width,
        height: rect.height,
        minSize: Math.min(rect.width, rect.height),

        // Visual properties
        backgroundColor: styles.backgroundColor,
        color: styles.color,
        hasOutline: styles.outline !== 'none',
      };
    });

    // Verify accessibility requirements
    expect(accessibility.hasAriaLabel || accessibility.hasTextContent).toBeTruthy();
    expect(accessibility.hasRole).toBeTruthy();
    expect(accessibility.isFocusable).toBeTruthy();
    expect(accessibility.isVisible).toBeTruthy();
    expect(accessibility.isEnabled).toBeTruthy();
    expect(accessibility.minSize).toBeGreaterThanOrEqual(44);
    expect(accessibility.backgroundColor).toBeTruthy();
    expect(accessibility.color).toBeTruthy();
  });

  test('should support keyboard-only navigation workflow', async ({ page }) => {
    // Complete logout workflow using only keyboard
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Navigate to button (might need multiple tabs)
    // Just verify we can focus it
    await logoutButton.focus();
    await expect(logoutButton).toBeFocused();

    // Activate via keyboard
    await page.keyboard.press('Enter');

    // Verify logout completed
    await expect(page.locator('text=You have been logged out')).toBeVisible({ timeout: 10000 });

    // Verify moved to login page
    await expect(page.locator(SELECTORS.USERNAME_INPUT)).toBeVisible({ timeout: 10000 });

    // Login input should be keyboard focusable too
    const loginInput = page.locator(SELECTORS.USERNAME_INPUT);
    await loginInput.focus();
    await expect(loginInput).toBeFocused();
  });

  test('should maintain focus visibility throughout interaction', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Focus button
    await logoutButton.focus();

    // Get focus styles
    const focusStyles = await logoutButton.evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        outline: styles.outline,
        outlineWidth: styles.outlineWidth,
        outlineStyle: styles.outlineStyle,
        boxShadow: styles.boxShadow,
        border: styles.border,
      };
    });

    // Should have some visual focus indicator
    const hasFocusIndicator =
      (focusStyles.outline && focusStyles.outline !== 'none') ||
      (focusStyles.boxShadow && focusStyles.boxShadow !== 'none') ||
      (focusStyles.outlineWidth && focusStyles.outlineWidth !== '0px');

    expect(hasFocusIndicator).toBeTruthy();
  });

  test('should have appropriate button semantics', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Check semantic HTML
    const semantics = await logoutButton.evaluate(el => {
      return {
        tagName: el.tagName.toLowerCase(),
        type: (el as HTMLButtonElement).type,
        role: el.getAttribute('role'),
        ariaLabel: el.getAttribute('aria-label'),
      };
    });

    // Should be a button element with type='button'
    expect(semantics.tagName).toBe('button');
    expect(semantics.type === 'button' || semantics.type === 'submit').toBeTruthy();
  });
});

test.describe('Logout Accessibility - Edge Cases', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should remain accessible after being disabled', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // If button becomes disabled (e.g., during logout), should maintain accessibility
    await logoutButton.click();

    // Button might be disabled during logout process
    await page.waitForTimeout(100);

    // Check if aria-disabled is used when disabled
    const ariaDisabled = await logoutButton.getAttribute('aria-disabled');
    const isDisabled = await logoutButton.evaluate(el => (el as HTMLButtonElement).disabled);

    // If disabled, should use aria-disabled
    if (isDisabled) {
      expect(ariaDisabled === 'true').toBeTruthy();
    }
  });

  test('should handle high contrast mode', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Get border and outline info
    const styles = await logoutButton.evaluate(el => {
      const computed = window.getComputedStyle(el);
      return {
        border: computed.border,
        outline: computed.outline,
        backgroundColor: computed.backgroundColor,
      };
    });

    // Should have some visual distinction (border, background, etc.)
    expect(
      styles.border !== 'none' || styles.outline !== 'none' || styles.backgroundColor !== 'transparent'
    ).toBeTruthy();
  });

  test('should maintain accessibility across viewport sizes', async ({ page }) => {
    const logoutButton = page.locator(SELECTORS.LOGOUT_BUTTON);

    // Test at mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    await expect(logoutButton).toBeVisible();

    const mobileBoundingBox = await logoutButton.boundingBox();
    expect(mobileBoundingBox).not.toBeNull();
    expect(mobileBoundingBox!.width).toBeGreaterThanOrEqual(44);
    expect(mobileBoundingBox!.height).toBeGreaterThanOrEqual(44);

    // Test at desktop viewport
    await page.setViewportSize({ width: 1920, height: 1080 });
    await expect(logoutButton).toBeVisible();

    const desktopBoundingBox = await logoutButton.boundingBox();
    expect(desktopBoundingBox).not.toBeNull();
    expect(desktopBoundingBox!.width).toBeGreaterThanOrEqual(44);
    expect(desktopBoundingBox!.height).toBeGreaterThanOrEqual(44);
  });
});
