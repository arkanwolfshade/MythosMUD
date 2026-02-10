/**
 * Authentication Fixtures
 *
 * Helper functions for player authentication in E2E tests.
 */

import { expect, type Page } from '@playwright/test';
import { TEST_TIMEOUTS } from './test-data';

const BASE_URL = 'http://localhost:5173';

/**
 * Login a player and navigate through the full authentication flow.
 * Handles:
 * - Login form
 * - Character selection (if multiple characters exist)
 * - MOTD screen
 * - Game interface loading
 *
 * @param page - Playwright page instance
 * @param username - Username to login with
 * @param password - Password to login with
 */
export async function loginPlayer(page: Page, username: string, password: string): Promise<void> {
  // Navigate to base URL
  await page.goto(BASE_URL, { waitUntil: 'load' });

  // Wait for login form
  const usernameInput = page.locator('input[placeholder*="username" i], input[name*="username" i]');
  await expect(usernameInput).toBeVisible({ timeout: TEST_TIMEOUTS.LOGIN });

  // Fill login form
  await usernameInput.fill(username);
  await page.fill('input[type="password"]', password);

  // Click login button
  await page.click('button:has-text("Enter"), button:has-text("Login"), button[type="submit"]');
  await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

  // Wait for loading to complete
  try {
    await page.waitForFunction(
      () => {
        const loadingElements = Array.from(document.querySelectorAll('*')).filter(
          el => el.textContent?.trim() === 'Loading...' || el.textContent?.includes('Loading...')
        );
        return loadingElements.length === 0;
      },
      { timeout: TEST_TIMEOUTS.LOGIN }
    );
  } catch {
    // Loading might not appear, continue anyway
  }

  // Wait for either character selection or game interface
  await page.waitForFunction(
    () => {
      const hasCharacterSelection = document.querySelector('.character-selection') !== null;
      const hasGameClient = document.querySelector('.game-client') !== null;
      const hasCommandInput = document.querySelector('.command-input') !== null;
      const hasTextareaCommand = document.querySelector('textarea[placeholder*="command" i]') !== null;
      const hasMOTDButton = document.querySelector('[data-testid="motd-enter-realm"]') !== null;
      const hasCharacterHeading = Array.from(document.querySelectorAll('h1, h2, h3')).some(el =>
        el.textContent?.includes('Select Your Character')
      );
      return (
        hasCharacterSelection ||
        hasGameClient ||
        hasCommandInput ||
        hasTextareaCommand ||
        hasMOTDButton ||
        hasCharacterHeading
      );
    },
    { timeout: TEST_TIMEOUTS.LOGIN }
  );

  // Handle character selection if present
  const characterSelectionHeading = page.locator('h1, h2, h3').filter({ hasText: /Select Your Character/i });
  const isCharacterSelectionVisible = await characterSelectionHeading.isVisible({ timeout: 2000 }).catch(() => false);
  if (isCharacterSelectionVisible) {
    const selectCharacterButton = page.locator('button:has-text("Select Character")').first();
    if (await selectCharacterButton.isVisible({ timeout: 3000 }).catch(() => false)) {
      await selectCharacterButton.click();
      await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});
      await new Promise(r => setTimeout(r, 1000)); // Wait for character selection to process
    } else {
      // Fallback: try clicking first character card or button
      const firstCharacter = page.locator('.character-card, [data-character-id], button:has-text("Select")').first();
      if (await firstCharacter.isVisible({ timeout: 3000 }).catch(() => false)) {
        await firstCharacter.click();
        await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});
        await new Promise(r => setTimeout(r, 1000)); // Wait for character selection to process
      }
    }
    // After character selection, wait for MOTD screen to appear (it appears after character selection in App.tsx)
    try {
      await Promise.race([
        page.waitForSelector('[data-testid="motd-enter-realm"]', { state: 'visible', timeout: 10000 }),
        page.getByRole('button', { name: /Enter the Realm/i }).waitFor({ state: 'visible', timeout: 10000 }),
        page.waitForFunction(
          () => {
            const bodyText = document.body?.textContent || '';
            return bodyText.includes('Welcome to the Dreamlands');
          },
          { timeout: 10000 }
        ),
      ]);
      await page.waitForTimeout(500); // Small delay to ensure MOTD is fully rendered
    } catch {
      // MOTD might not appear immediately, continue anyway
    }
  }

  // Handle MOTD/welcome screen if present
  // Use DOM-based detection (not visibility checks) since MOTD might be present but not "visible" to Playwright
  // Check page content directly in DOM (more reliable than visibility checks)
  const motdCheck = await page
    .evaluate(() => {
      const bodyText = document.body?.textContent || '';
      const hasWelcomeText = bodyText.includes('Welcome to the Dreamlands');
      const hasMotdContent = document.querySelector('.motd-content') !== null;
      const hasMotdButton = document.querySelector('[data-testid="motd-enter-realm"]') !== null;

      // Find button by text content in DOM
      const buttons = Array.from(document.querySelectorAll('button'));
      const enterRealmButton = buttons.find(btn => btn.textContent?.includes('Enter the Realm'));

      return {
        hasWelcomeText,
        hasMotdContent,
        hasMotdButton,
        hasEnterRealmButton: enterRealmButton !== null,
        buttonFound: enterRealmButton !== null,
      };
    })
    .catch(() => ({
      hasWelcomeText: false,
      hasMotdContent: false,
      hasMotdButton: false,
      hasEnterRealmButton: false,
      buttonFound: false,
    }));

  const isMOTDScreen =
    motdCheck.hasWelcomeText || motdCheck.hasMotdContent || motdCheck.hasMotdButton || motdCheck.hasEnterRealmButton;

  if (isMOTDScreen) {
    // Click MOTD button - use direct DOM click since visibility checks are unreliable
    // Try multiple click strategies in order of preference
    let clicked = false;

    // Strategy 1: Try by test ID selector (if button exists in DOM)
    if (motdCheck.hasMotdButton && !clicked) {
      try {
        await page.click('[data-testid="motd-enter-realm"]', { timeout: 3000 });
        clicked = true;
      } catch {
        // Continue to next strategy
      }
    }

    // Strategy 2: Try by role/text (Playwright's getByRole)
    if (!clicked) {
      try {
        await page.getByRole('button', { name: /Enter the Realm/i }).click({ timeout: 3000 });
        clicked = true;
      } catch {
        // Continue to next strategy
      }
    }

    // Strategy 3: Direct DOM click (most reliable - works even if Playwright thinks button isn't visible)
    if (!clicked) {
      await page.evaluate(() => {
        // Try by test ID first
        const testIdButton = document.querySelector('[data-testid="motd-enter-realm"]') as HTMLElement;
        if (testIdButton) {
          testIdButton.click();
          return;
        }

        // Fallback: find by text content
        const buttons = Array.from(document.querySelectorAll('button'));
        const enterButton = buttons.find(btn => btn.textContent?.includes('Enter the Realm'));
        if (enterButton) {
          (enterButton as HTMLElement).click();
        }
      });
    }

    // Wait for game interface to load
    await page.waitForTimeout(2000);
    try {
      await Promise.race([
        page.getByText('Game Info', { exact: false }).waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
        page.waitForSelector('.message-item', { state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
        page.waitForSelector('[data-message-text]', { state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
      ]).catch(() => {});
    } catch {
      // Continue anyway
    }
  }

  // Final wait: Verify command input is visible (confirms we're in the game)
  // This is a best-effort check - if it fails, we still proceed
  try {
    await page.waitForFunction(
      () => {
        const inputByPlaceholder = document.querySelector(
          'input[placeholder*="command" i], textarea[placeholder*="command" i]'
        );
        const inputByTestId = document.querySelector('[data-testid="command-input"]');
        const input = inputByPlaceholder || inputByTestId;
        return input !== null && (input as HTMLElement).offsetParent !== null;
      },
      { timeout: TEST_TIMEOUTS.GAME_LOAD }
    );
  } catch {
    // Command input might not be immediately visible - this is okay, tests will handle it
    // Wait a bit more for the page to stabilize (only if page is still open)
    try {
      await page.waitForTimeout(2000);
    } catch {
      // Page might be closed, ignore
    }
  }

  // #region agent log
  const hasCmdInput = await page
    .evaluate(() => {
      const input =
        document.querySelector('input[placeholder*="command" i], textarea[placeholder*="command" i]') ||
        document.querySelector('[data-testid="command-input"]');
      return input !== null && (input as HTMLElement).offsetParent !== null;
    })
    .catch(() => false);
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'auth.ts:loginPlayer:exit',
      message: 'loginPlayer finished',
      data: { username, hasCommandInput: hasCmdInput },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'A',
    }),
  }).catch(() => {});
  // #endregion
}

/**
 * Execute a command via the command input field.
 *
 * @param page - Playwright page instance
 * @param command - Command to execute
 * @returns Promise that resolves when command is sent
 */
export async function executeCommand(page: Page, command: string): Promise<void> {
  // First, verify we're not still on the login screen
  const isOnLoginScreen = await page.evaluate(() => {
    const hasLoginForm = document.querySelector('input[placeholder*="username" i], input[name*="username" i]') !== null;
    const hasLoginButton = Array.from(document.querySelectorAll('button')).some(
      btn => btn.textContent?.includes('Enter the Void') || btn.textContent?.includes('Login')
    );
    return hasLoginForm && hasLoginButton;
  });

  if (isOnLoginScreen) {
    throw new Error(
      'Cannot execute command: Still on login screen. Login may have failed or not completed. ' + 'URL: ' + page.url()
    );
  }

  // Wait for command input to be available (may not be immediately visible after login)
  await page.waitForFunction(
    () => {
      const inputByPlaceholder = document.querySelector(
        'input[placeholder*="command" i], textarea[placeholder*="command" i]'
      );
      const inputByTestId = document.querySelector('[data-testid="command-input"]');
      const input = inputByPlaceholder || inputByTestId;
      return input !== null && (input as HTMLElement).offsetParent !== null;
    },
    { timeout: TEST_TIMEOUTS.COMMAND }
  );

  const commandInput = page.locator(
    'input[placeholder*="command" i], textarea[placeholder*="command" i], [data-testid="command-input"]'
  );
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await commandInput.clear();
  await commandInput.fill(command);
  // Wait for input to reflect full command (avoids submitting before React state updates)
  await expect(commandInput).toHaveValue(command, { timeout: 5000 });
  await commandInput.press('Enter');
  // Small wait for command processing
  await page.waitForTimeout(1000);
}

/**
 * Wait for a message to appear in the game log.
 *
 * @param page - Playwright page instance
 * @param expectedText - Text to wait for (can be string or regex)
 * @param timeout - Timeout in milliseconds
 */
export async function waitForMessage(
  page: Page,
  expectedText: string | RegExp,
  timeout: number = TEST_TIMEOUTS.MESSAGE
): Promise<void> {
  const messageLocator = page.locator('[data-message-text]');
  if (typeof expectedText === 'string') {
    await expect(messageLocator.filter({ hasText: expectedText }).first()).toBeVisible({ timeout });
  } else {
    await expect(messageLocator.filter({ hasText: expectedText }).first()).toBeVisible({ timeout });
  }
}

/**
 * Get all messages from the game log.
 *
 * @param page - Playwright page instance
 * @returns Array of message texts
 */
export async function getMessages(page: Page): Promise<string[]> {
  return await page.evaluate(() => {
    const messages = Array.from(document.querySelectorAll('[data-message-text]'));
    return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });
}
