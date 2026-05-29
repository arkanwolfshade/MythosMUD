/**
 * Authentication Fixtures
 *
 * Helper functions for player authentication in E2E tests.
 */

import './multiplayer-browser-window.d.ts';

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

  const loginNetworkFailure = page.getByText(/NetworkError when attempting to fetch/i);
  if (await loginNetworkFailure.isVisible({ timeout: 8000 }).catch(() => false)) {
    throw new Error(
      'E2E login: NetworkError on login fetch — backend unreachable or wrong API URL. ' +
        'Run the FastAPI server on http://127.0.0.1:54768 and ensure Vite proxies /v1 (or env) for E2E.'
    );
  }

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

  const postLoginUi = page
    .locator('.character-selection-screen')
    .or(page.getByTestId('command-input'))
    .or(page.getByTestId('motd-enter-realm'));
  await expect(postLoginUi.first()).toBeVisible({ timeout: TEST_TIMEOUTS.LOGIN });

  if (await characterSelection.isVisible()) {
    await characterSelection.selectFirstCharacter();
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

  await expect(page.getByTestId('command-input')).toBeVisible({ timeout: TEST_TIMEOUTS.GAME_LOAD });
}

/**
 * Wait until the client can accept commands (no disconnect banner, WS connected).
 * Send Command enablement is enforced separately in executeCommand.
 */
export async function waitForPlayableSession(page: Page, timeoutMs: number = 30000): Promise<void> {
  await expect(page.getByTestId('command-input')).toBeVisible({ timeout: Math.min(timeoutMs, 15000) });

  await page
    .waitForFunction(
      () => !(document.body?.innerText ?? '').includes('You are disconnected and cannot perform actions'),
      { timeout: timeoutMs }
    )
    .catch(() => {});

  await page.waitForFunction(
    () =>
      typeof window.__mythosE2eHasConnectedStatus === 'function'
        ? window.__mythosE2eHasConnectedStatus() === true
        : document.body?.innerText?.includes('Connected') === true,
    { timeout: timeoutMs }
  );
}

/**
 * Restore a playable session when linkdead/disconnect left Send Command disabled.
 * Re-logs in only when the game UI is visible but commands are still blocked.
 */
export async function recoverPlayableSession(
  page: Page,
  username: string,
  password: string,
  timeoutMs: number = 45000
): Promise<void> {
  await page.bringToFront().catch(() => {});

  const sendDisabled = await page
    .getByRole('button', { name: 'Send Command' })
    .isDisabled()
    .catch(() => true);
  if (!sendDisabled) {
    try {
      await waitForPlayableSession(page, 8000);
      return;
    } catch {
      // Fall through to relogin when header says Connected but commands stay blocked.
    }
  }

  await loginPlayer(page, username, password);
  await waitForPlayableSession(page, timeoutMs);
  await executeCommand(page, 'stand').catch(() => {});
  await expect(page.getByRole('button', { name: 'Send Command' })).toBeEnabled({ timeout: timeoutMs });
}

/**
 * Reload the game tab when Send Command is disabled but the game UI is still mounted.
 * Prefer this over full relogin in multiplayer tests to avoid kicking the other browser session.
 */
export async function refreshPlayableSession(page: Page, timeoutMs: number = 45000): Promise<void> {
  const sendCommand = page.getByRole('button', { name: 'Send Command' });
  const sendDisabled = await sendCommand.isDisabled().catch(() => true);
  if (!sendDisabled) {
    try {
      await waitForPlayableSession(page, 5000);
      return;
    } catch {
      // Continue to reload when header says Connected but Send stayed disabled.
    }
  }

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (onLogin) {
    return;
  }

  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, { timeout: timeoutMs });
  await waitForPlayableSession(page, timeoutMs);
}

/**
 * Focus the command input without Playwright click stability (Firefox eldritch-border animation).
 */
export async function focusCommandInput(page: Page): Promise<void> {
  const commandInput = page.getByTestId('command-input');
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await commandInput.evaluate((el: HTMLElement) => {
    el.focus();
  });
}

/**
 * Click without Playwright actionability (Firefox eldritch-border animation never stabilizes).
 */
export async function clickWithoutStability(
  locator: ReturnType<Page['getByRole']> | ReturnType<Page['getByTestId']>
): Promise<void> {
  await locator.evaluate((el: HTMLElement) => {
    el.click();
  });
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
  await commandInput.evaluate((el: HTMLElement) => {
    el.focus();
  });
  await commandInput.clear();
  await commandInput.fill(command);
  // Wait for input to reflect full command (avoids submitting before React state updates)
  await expect(commandInput).toHaveValue(command, { timeout: 5000 });
  // CommandInputPanel drops submits when `!isConnected` (Send Command stays disabled). Wait for a
  // playable session so Enter actually dispatches — otherwise waitForMessage times out with no server echo.
  const sendCommand = page.getByRole('button', { name: 'Send Command' });
  await expect(sendCommand).toBeEnabled({ timeout: TEST_TIMEOUTS.GAME_LOAD });
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
