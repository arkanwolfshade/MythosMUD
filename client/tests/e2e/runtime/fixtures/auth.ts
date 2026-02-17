/**
 * Authentication Fixtures
 *
 * Helper functions for player authentication in E2E tests.
 */

import { expect, type Page } from '@playwright/test';
import { CharacterSelectionPage, LoginPage, MotdPage } from '../pages';
import { TEST_TIMEOUTS } from './test-data';

/**
 * Login a player and navigate through the full authentication flow.
 * Uses LoginPage, CharacterSelectionPage, and MotdPage for stable locators and actions.
 *
 * @param page - Playwright page instance
 * @param username - Username to login with
 * @param password - Password to login with
 */
export async function loginPlayer(page: Page, username: string, password: string): Promise<void> {
  const loginPage = new LoginPage(page);
  const characterSelection = new CharacterSelectionPage(page);
  const motdPage = new MotdPage(page);

  await loginPage.navigate();
  await loginPage.login(username, password);
  await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

  try {
    await page.waitForFunction(
      () => {
        const loading = Array.from(document.querySelectorAll('*')).filter(
          el => el.textContent?.trim() === 'Loading...' || el.textContent?.includes('Loading...')
        );
        return loading.length === 0;
      },
      { timeout: TEST_TIMEOUTS.LOGIN }
    );
  } catch {
    // Loading might not appear
  }

  await page.waitForFunction(
    () => {
      return (
        document.querySelector('.character-selection') !== null ||
        document.querySelector('[data-testid="command-input"]') !== null ||
        document.querySelector('[data-testid="motd-enter-realm"]') !== null ||
        Array.from(document.querySelectorAll('h1, h2, h3')).some(el =>
          el.textContent?.includes('Select Your Character')
        )
      );
    },
    { timeout: TEST_TIMEOUTS.LOGIN }
  );

  if (await characterSelection.isVisible()) {
    await characterSelection.selectFirstCharacter();
    await page
      .getByTestId('motd-enter-realm')
      .waitFor({ state: 'visible', timeout: 10000 })
      .catch(() => {});
  }

  const motdCheck = await page
    .evaluate(() => {
      const bodyText = document.body?.textContent || '';
      const hasButton = document.querySelector('[data-testid="motd-enter-realm"]') !== null;
      const hasWelcome = bodyText.includes('Welcome to the Dreamlands');
      return hasButton || hasWelcome;
    })
    .catch(() => false);

  if (motdCheck) {
    await motdPage.enterRealm();
    await motdPage.waitForGameReady(TEST_TIMEOUTS.GAME_LOAD);
  }

  try {
    await page.waitForFunction(
      () => {
        const input = document.querySelector('[data-testid="command-input"]');
        return input !== null && (input as HTMLElement).offsetParent !== null;
      },
      { timeout: TEST_TIMEOUTS.GAME_LOAD }
    );
  } catch {
    await page
      .getByTestId('command-input')
      .waitFor({ state: 'visible', timeout: 5000 })
      .catch(() => {});
  }
}

/**
 * Execute a command via the command input field.
 *
 * @param page - Playwright page instance
 * @param command - Command to execute
 * @returns Promise that resolves when command is sent
 */
export async function executeCommand(page: Page, command: string): Promise<void> {
  // First, verify we're not still on the login screen (check for login form by test id)
  const isOnLoginScreen = await page
    .getByTestId('username-input')
    .isVisible()
    .catch(() => false);

  if (isOnLoginScreen) {
    throw new Error(
      'Cannot execute command: Still on login screen. Login may have failed or not completed. ' + 'URL: ' + page.url()
    );
  }

  const commandInput = page.getByTestId('command-input');
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await commandInput.clear();
  await commandInput.fill(command);
  // Wait for input to reflect full command (avoids submitting before React state updates)
  await expect(commandInput).toHaveValue(command, { timeout: 5000 });
  await commandInput.press('Enter');
  // Wait for command to be processed (game log or next prompt)
  await expect(commandInput).toBeVisible({ timeout: 3000 });
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
