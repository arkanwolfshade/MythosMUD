/**
 * Authentication Fixtures
 *
 * Helper functions for player authentication in E2E tests.
 */

import './multiplayer-browser-window.d.ts';

import { expect, type Page } from '@playwright/test';
import { CharacterSelectionPage, LoginPage, MotdPage } from '../pages';
import { toMessageMatchPattern } from './message-match';
import { TEST_TIMEOUTS } from './test-data';

/** Last login credentials per page — used by executeCommand recovery in multiplayer tests. */
const pageSessionCredentials = new WeakMap<Page, { username: string; password: string }>();

export function rememberPageSession(page: Page, username: string, password: string): void {
  pageSessionCredentials.set(page, { username, password });
}

export function getPageSessionCredentials(page: Page): { username: string; password: string } | undefined {
  return pageSessionCredentials.get(page);
}

function isPageUsable(page: Page): boolean {
  return !page.isClosed();
}

/** Commands panel input only — never a chat-history compose field. */
export function getCommandPanelInput(page: Page) {
  return page.getByTestId('command-input-panel').getByTestId('command-input');
}

/**
 * Login a player and navigate through the full authentication flow.
 * Uses LoginPage, CharacterSelectionPage, and MotdPage for stable locators and actions.
 *
 * @param page - Playwright page instance
 * @param username - Username to login with
 * @param password - Password to login with
 */
export async function loginPlayer(page: Page, username: string, password: string): Promise<void> {
  rememberPageSession(page, username, password);
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
      undefined,
      { timeout: TEST_TIMEOUTS.LOGIN }
    );
  } catch {
    // Loading might not appear
  }

  const postLoginUi = page
    .locator('.character-selection-screen')
    .or(page.getByTestId('command-input-panel'))
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

  await expect(getCommandPanelInput(page)).toBeVisible({ timeout: TEST_TIMEOUTS.GAME_LOAD });
}

/** Grace-period disconnect copy shown in Game Info when the server blocks commands. */
const GRACE_PERIOD_MESSAGE = 'You are disconnected and cannot perform actions';

export interface LogoutPlayerOptions {
  /**
   * When true, SPA-navigate to login if intentional logout never reaches username-input.
   * Creates Occupants linkdead ghosts — use only for context cleanup, not leave-message asserts.
   */
  spaFallback?: boolean;
}

/**
 * Intentionally exit the game via Exit the Realm so the server records a clean logout
 * instead of starting a linkdead grace period when the browser context closes.
 */
export async function logoutPlayer(
  page: Page,
  timeoutMs: number = 90000,
  options?: LogoutPlayerOptions
): Promise<void> {
  await page.bringToFront().catch(() => {});

  if (await isUsernameLoginVisible(page, 2000)) {
    return;
  }

  const spaFallback = options?.spaFallback === true;

  // Prefer intentional Exit-the-Realm / logout so the server emits left_game (not linkdead grace).
  const logoutButton = page.getByTestId('logout-button');
  const inGame = await logoutButton.isVisible({ timeout: 3000 }).catch(() => false);
  if (inGame) {
    const logoutEnabled = await logoutButton.isEnabled({ timeout: 3000 }).catch(() => false);
    if (logoutEnabled) {
      await clickWithoutStability(logoutButton);
    } else {
      // Disabled (ward/combat): intentional logout command; DOM click bypasses disabled if still present.
      await executeCommandWithoutRecovery(page, 'logout').catch(() => {});
      await logoutButton
        .evaluate((el: HTMLElement) => {
          el.click();
        })
        .catch(() => {});
    }
  } else {
    await executeCommandWithoutRecovery(page, 'logout').catch(() => {});
  }

  const loginInput = page.getByTestId('username-input');
  if (spaFallback) {
    const softMs = Math.min(timeoutMs, 15000);
    const reachedLogin = await loginInput.isVisible({ timeout: softMs }).catch(() => false);
    if (!reachedLogin) {
      await page.goto('/', { waitUntil: 'domcontentloaded' });
    }
    await expect(loginInput).toBeVisible({ timeout: Math.max(timeoutMs - softMs, 10000) });
    return;
  }

  await expect(loginInput).toBeVisible({ timeout: timeoutMs });
}

/**
 * Wait until the client can accept commands (no disconnect banner, WS connected).
 * Send Command enablement is enforced separately in executeCommand.
 */
export async function waitForPlayableSession(page: Page, timeoutMs: number = 30000): Promise<void> {
  await expect(getCommandPanelInput(page)).toBeVisible({ timeout: Math.min(timeoutMs, 15000) });

  await page
    .waitForFunction((msg: string) => !(document.body?.innerText ?? '').includes(msg), GRACE_PERIOD_MESSAGE, {
      timeout: timeoutMs,
    })
    .catch(() => {});

  await page.waitForFunction(
    () =>
      typeof window.__mythosE2eHasConnectedStatus === 'function'
        ? window.__mythosE2eHasConnectedStatus() === true
        : document.body?.innerText?.includes('Connected') === true,
    undefined,
    { timeout: timeoutMs }
  );
}

export interface EnsurePlayableConnectionOptions {
  username?: string;
  password?: string;
  timeoutMs?: number;
}

export async function assertCommandChannelReady(page: Page, budgetMs: number): Promise<boolean> {
  try {
    await waitForPlayableSession(page, Math.min(budgetMs, 30000));
    const commandInput = getCommandPanelInput(page);
    await expect(commandInput).toBeVisible({ timeout: Math.min(budgetMs, 10000) });
    await expect(commandInput).toBeEnabled({ timeout: Math.min(budgetMs, 10000) });
    return true;
  } catch {
    return false;
  }
}

async function reconnectPlayableSession(
  page: Page,
  options: EnsurePlayableConnectionOptions | undefined,
  timeoutMs: number
): Promise<void> {
  if (options?.username && options?.password) {
    // Full reload drops the SPA session and returns to login; re-enter the game instead.
    await recoverPlayableSession(page, options.username, options.password, timeoutMs);
    return;
  }

  await refreshPlayableSession(page, timeoutMs);
  if (await assertCommandChannelReady(page, timeoutMs)) {
    return;
  }

  await waitForPlayableSession(page, timeoutMs);
}

/**
 * Gate before command execution: header Connected, no grace-period copy, command input enabled.
 * Send Command stays disabled until the input has text; do not probe readiness with that button.
 */
export async function ensurePlayableConnection(page: Page, options?: EnsurePlayableConnectionOptions): Promise<void> {
  if (!isPageUsable(page)) {
    throw new Error('Cannot ensure playable connection: browser page is closed');
  }

  const timeoutMs = options?.timeoutMs ?? 45000;
  await page.bringToFront().catch(() => {});

  if (await assertCommandChannelReady(page, timeoutMs)) {
    return;
  }

  await reconnectPlayableSession(page, options, timeoutMs);
}

const RECOVER_COMMAND_READY_MS = 8000;

async function isUsernameLoginVisible(page: Page, visibilityTimeoutMs = 2000): Promise<boolean> {
  return page
    .getByTestId('username-input')
    .isVisible({ timeout: visibilityTimeoutMs })
    .catch(() => false);
}

async function restorePlayableAfterLogin(
  page: Page,
  username: string,
  password: string,
  timeoutMs: number
): Promise<void> {
  await loginPlayer(page, username, password);
  await waitForPlayableSession(page, timeoutMs);
  await assertCommandChannelReady(page, timeoutMs);
}

/** Grace period / stand without reload; true when command channel is ready. */
async function tryInPlacePlayableRecovery(page: Page, timeoutMs: number): Promise<boolean> {
  await waitForPlayableSession(page, Math.min(timeoutMs, 25000)).catch(() => {});
  if (await assertCommandChannelReady(page, RECOVER_COMMAND_READY_MS)) {
    return true;
  }
  await executeCommandWithoutRecovery(page, 'stand').catch(() => {});
  return assertCommandChannelReady(page, RECOVER_COMMAND_READY_MS);
}

/** SPA navigation to login (avoid Exit the Realm — it poisons parallel player sessions). */
async function recoverPlayableViaSpaNavigation(
  page: Page,
  username: string,
  password: string,
  timeoutMs: number
): Promise<void> {
  await page.goto('/', { waitUntil: 'domcontentloaded' });
  if (await isUsernameLoginVisible(page, 10000)) {
    await loginPlayer(page, username, password);
  }
  await waitForPlayableSession(page, timeoutMs);
  await executeCommandWithoutRecovery(page, 'stand').catch(() => {});
  await assertCommandChannelReady(page, timeoutMs);
}

/**
 * Restore a playable session when linkdead/disconnect left Send Command disabled.
 * Re-logs in only when reload did not restore command input.
 */
export async function recoverPlayableSession(
  page: Page,
  username: string,
  password: string,
  timeoutMs: number = 45000
): Promise<void> {
  if (!isPageUsable(page)) {
    throw new Error('Cannot recover playable session: browser page is closed');
  }

  await page.bringToFront().catch(() => {});

  if (await isUsernameLoginVisible(page)) {
    await restorePlayableAfterLogin(page, username, password, timeoutMs);
    return;
  }

  if (await assertCommandChannelReady(page, RECOVER_COMMAND_READY_MS)) {
    return;
  }

  if (await tryInPlacePlayableRecovery(page, timeoutMs)) {
    return;
  }

  if (await isUsernameLoginVisible(page)) {
    await restorePlayableAfterLogin(page, username, password, timeoutMs);
    return;
  }

  await recoverPlayableViaSpaNavigation(page, username, password, timeoutMs);
}

/**
 * Reload the game tab when Send Command is disabled but the game UI is still mounted.
 * Prefer this over full relogin in multiplayer tests to avoid kicking the other browser session.
 */
export async function refreshPlayableSession(page: Page, timeoutMs: number = 45000): Promise<void> {
  if (!isPageUsable(page)) {
    return;
  }

  if (await assertCommandChannelReady(page, 5000)) {
    return;
  }

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (onLogin) {
    return;
  }

  if (!isPageUsable(page)) {
    return;
  }

  await page.reload({ waitUntil: 'domcontentloaded' });

  const onLoginAfterReload = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 5000 })
    .catch(() => false);
  if (onLoginAfterReload) {
    return;
  }

  await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, undefined, { timeout: timeoutMs });
  await waitForPlayableSession(page, timeoutMs);
}

/**
 * Focus the command input without Playwright click stability (Firefox eldritch-border animation).
 */
export async function focusCommandInput(page: Page): Promise<void> {
  const commandInput = getCommandPanelInput(page);
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
 * Submit a command when the session is already verified playable (no recovery loop).
 * Use after ensurePlayableConnection to avoid logout/relogin during multiplayer co-locate.
 */
export async function executeCommandTrusted(page: Page, command: string): Promise<void> {
  const isOnLoginScreen = await page
    .getByTestId('username-input')
    .isVisible()
    .catch(() => false);

  if (isOnLoginScreen) {
    throw new Error(
      'Cannot execute command: Still on login screen. Login may have failed or not completed. URL: ' + page.url()
    );
  }

  await executeCommandWithoutRecovery(page, command);
}

export async function executeCommandWithoutRecovery(page: Page, command: string): Promise<void> {
  const commandPanel = page.getByTestId('command-input-panel');
  const commandInput = commandPanel.getByTestId('command-input');
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await expect(page.getByTestId('chat-history-panel').getByTestId('command-input')).toHaveCount(0);
  await commandInput.evaluate((el: HTMLElement) => {
    el.focus();
  });
  await commandInput.clear();
  await commandInput.fill(command);
  await expect(commandInput).toHaveValue(command, { timeout: 5000 });
  const sendCommand = commandPanel.getByRole('button', { name: 'Send Command' });
  await expect(sendCommand).toBeEnabled({ timeout: TEST_TIMEOUTS.GAME_LOAD });
  await commandInput.press('Enter');
  await expect(commandInput).toBeVisible({ timeout: 3000 });
}

/**
 * Execute a command via the Commands panel input (not Chat History).
 *
 * @param page - Playwright page instance
 * @param command - Command to execute
 * @returns Promise that resolves when command is sent
 */
export async function executeCommand(page: Page, command: string): Promise<void> {
  if (!isPageUsable(page)) {
    throw new Error('Cannot execute command: browser page is closed');
  }

  const session = getPageSessionCredentials(page);
  // Always try recovery first when we have credentials (idle rest / Exit / focus loss lands on login).
  if (session) {
    await ensurePlayableConnection(page, {
      username: session.username,
      password: session.password,
      timeoutMs: TEST_TIMEOUTS.GAME_LOAD,
    });
  } else {
    const isOnLoginScreen = await page
      .getByTestId('username-input')
      .isVisible()
      .catch(() => false);
    if (isOnLoginScreen) {
      throw new Error(
        'Cannot execute command: Still on login screen with no saved session credentials. URL: ' + page.url()
      );
    }
    await ensurePlayableConnection(page, { timeoutMs: TEST_TIMEOUTS.GAME_LOAD });
  }
  await executeCommandWithoutRecovery(page, command);
}

/**
 * Wait for a message to appear in the game log.
 *
 * Strings are matched literally (see toMessageMatchPattern). Poll + bringToFront so Firefox
 * background tabs keep painting Game Info; recover if idle rest dumps the session to login.
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
  const { src, fl } = toMessageMatchPattern(expectedText);
  const session = getPageSessionCredentials(page);
  await expect
    .poll(
      async () => {
        await page.bringToFront().catch(() => {});
        if (await isUsernameLoginVisible(page, 500)) {
          if (session) {
            await ensurePlayableConnection(page, {
              username: session.username,
              password: session.password,
              timeoutMs: Math.min(timeout, 30000),
            });
          }
          return false;
        }
        return page.evaluate(
          ({ matchSrc, matchFl }: { matchSrc: string; matchFl: string }) => {
            try {
              const re = new RegExp(matchSrc, matchFl);
              const nodes = Array.from(document.querySelectorAll('[data-message-text]'));
              if (nodes.some(n => re.test((n.getAttribute('data-message-text') || n.textContent || '').trim()))) {
                return true;
              }
              return re.test(document.body?.innerText ?? '');
            } catch {
              return false;
            }
          },
          { matchSrc: src, matchFl: fl }
        );
      },
      { timeout, message: `waitForMessage ${src}` }
    )
    .toBe(true);
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
