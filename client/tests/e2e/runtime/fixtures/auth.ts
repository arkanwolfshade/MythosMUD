/**
 * Authentication Fixtures
 *
 * Helper functions for player authentication in E2E tests.
 */

import './multiplayer-browser-window.d.ts';

import { expect, type BrowserContext, type Page } from '@playwright/test';
import { CharacterSelectionPage, LoginPage, MotdPage } from '../pages';
import { TEST_TIMEOUTS } from './test-data';

/** Last login credentials per page — used by executeCommand recovery in multiplayer tests. */
const pageSessionCredentials = new WeakMap<Page, { username: string; password: string }>();

/** Live page per username — survives Firefox page death when we reopen on the same context. */
const livePagesByUsername = new Map<string, Page>();

export function rememberPageSession(page: Page, username: string, password: string): void {
  pageSessionCredentials.set(page, { username, password });
  livePagesByUsername.set(username, page);
}

export function getPageSessionCredentials(page: Page): { username: string; password: string } | undefined {
  return pageSessionCredentials.get(page);
}

export function getLivePageForUsername(username: string): Page | undefined {
  const page = livePagesByUsername.get(username);
  if (page && !page.isClosed()) {
    return page;
  }
  return undefined;
}

/**
 * If `page` is closed, open a new page on the same browser context and re-login.
 * Updates live-page tracking so later executeCommand calls use the new page.
 */
export async function reopenClosedPage(
  page: Page,
  username: string,
  password: string,
  timeoutMs: number = 45000
): Promise<Page> {
  if (!page.isClosed()) {
    rememberPageSession(page, username, password);
    return page;
  }
  let context: BrowserContext;
  try {
    context = page.context();
  } catch {
    throw new Error(`Cannot recover playable session for ${username}: browser page is closed`);
  }
  const browser = context.browser();
  if (browser === null) {
    throw new Error(`Cannot recover playable session for ${username}: browser context is closed`);
  }
  let next: Page;
  try {
    next = await context.newPage();
  } catch {
    // Context died with the page (common under Firefox serial load); mint a fresh context.
    if (!browser.isConnected()) {
      throw new Error(`Cannot recover playable session for ${username}: browser has been closed`);
    }
    context = await browser.newContext();
    next = await context.newPage();
  }
  rememberPageSession(next, username, password);
  await loginPlayer(next, username, password);
  await waitForPlayableSession(next, timeoutMs);
  return next;
}

function isPageUsable(page: Page): boolean {
  return !page.isClosed();
}

/** Prefer the live reopened page for this username when the caller's page handle is stale. */
function resolveActivePage(page: Page): Page {
  const session = getPageSessionCredentials(page);
  if (session) {
    const live = getLivePageForUsername(session.username);
    if (live) {
      return live;
    }
  }
  return page;
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

/** Grace-period disconnect copy shown in Game Info when the server blocks commands. */
const GRACE_PERIOD_MESSAGE = 'You are disconnected and cannot perform actions';

/** Rest disconnect countdown — session is about to drop; do not wait for presence/chat. */
const REST_DISCONNECT_POLLUTION_RE = /You will disconnect in \d+ seconds|You have rested and disconnected/i;

/**
 * Fail fast when the page shows a mid-rest disconnect countdown (poisons enter/chat waits).
 * Attempt a direct `stand` first; do not relogin here (that cascades under Firefox serial load).
 */
export async function assertNoRestDisconnectPollution(page: Page): Promise<void> {
  if (!isPageUsable(page)) {
    throw new Error('Cannot check rest pollution: browser page is closed');
  }
  const isPolluted = async (): Promise<boolean> =>
    page.evaluate(reSource => {
      const re = new RegExp(reSource, 'i');
      return re.test(document.body?.innerText ?? '');
    }, REST_DISCONNECT_POLLUTION_RE.source);

  if (!(await isPolluted())) {
    return;
  }

  const input = page.getByTestId('command-input');
  if (await input.isVisible({ timeout: 2000 }).catch(() => false)) {
    await input.fill('stand');
    await input.press('Enter');
    await new Promise(r => setTimeout(r, 800));
  }

  if (await isPolluted()) {
    throw new Error(
      'Rest disconnect countdown/pollution detected in Game Info; aborting presence/chat wait. ' +
        'Reconnect should cancel rest; if this persists, cancel rest before multiplayer waits.'
    );
  }
}

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
  await expect(page.getByTestId('command-input')).toBeVisible({ timeout: Math.min(timeoutMs, 15000) });

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
    const commandInput = page.getByTestId('command-input');
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

async function reopenIfClosed(page: Page, options: EnsurePlayableConnectionOptions | undefined): Promise<Page> {
  if (isPageUsable(page)) {
    return page;
  }
  if (!options?.username || !options?.password) {
    throw new Error('Cannot ensure playable connection: browser page is closed');
  }
  return reopenClosedPage(page, options.username, options.password, options.timeoutMs ?? 45000);
}

function resolveEnsuredPage(activePage: Page, username: string | undefined): Page {
  // Caller may still hold a closed Page handle; return the live tab after recovery.
  if (username) {
    return getLivePageForUsername(username) ?? resolveActivePage(activePage);
  }
  return resolveActivePage(activePage);
}

/**
 * Gate before command execution: header Connected, no grace-period copy, command input enabled.
 * Send Command stays disabled until the input has text; do not probe readiness with that button.
 */
export async function ensurePlayableConnection(page: Page, options?: EnsurePlayableConnectionOptions): Promise<Page> {
  const activePage = await reopenIfClosed(resolveActivePage(page), options);
  const timeoutMs = options?.timeoutMs ?? 45000;
  await activePage.bringToFront().catch(() => {});

  if (!(await assertCommandChannelReady(activePage, timeoutMs))) {
    await reconnectPlayableSession(activePage, options, timeoutMs);
  }

  return resolveEnsuredPage(activePage, options?.username);
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
  let activePage = page;
  if (!isPageUsable(activePage)) {
    activePage = await reopenClosedPage(activePage, username, password, timeoutMs);
    if (await assertCommandChannelReady(activePage, RECOVER_COMMAND_READY_MS)) {
      return;
    }
  }

  await activePage.bringToFront().catch(() => {});

  if (await isUsernameLoginVisible(activePage)) {
    await restorePlayableAfterLogin(activePage, username, password, timeoutMs);
    return;
  }

  if (await assertCommandChannelReady(activePage, RECOVER_COMMAND_READY_MS)) {
    return;
  }

  if (await tryInPlacePlayableRecovery(activePage, timeoutMs)) {
    return;
  }

  if (await isUsernameLoginVisible(activePage)) {
    await restorePlayableAfterLogin(activePage, username, password, timeoutMs);
    return;
  }

  await recoverPlayableViaSpaNavigation(activePage, username, password, timeoutMs);
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

async function assertNotStuckOnLogin(page: Page): Promise<void> {
  const onLogin = await page
    .getByTestId('username-input')
    .isVisible()
    .catch(() => false);
  if (onLogin) {
    throw new Error(
      'Cannot execute command: Still on login screen. Login may have failed or not completed. URL: ' + page.url()
    );
  }
}

/** Prefer tracked live tab; reopen when the caller's Page handle is closed. */
async function resolveExecuteCommandPage(page: Page): Promise<Page> {
  const session = getPageSessionCredentials(page);
  if (!session) {
    return page;
  }
  const tracked = getLivePageForUsername(session.username);
  if (tracked) {
    return tracked;
  }
  if (page.isClosed()) {
    return reopenClosedPage(page, session.username, session.password, TEST_TIMEOUTS.GAME_LOAD);
  }
  return page;
}

/**
 * Submit a command when the session is already verified playable (no recovery loop).
 * Use after ensurePlayableConnection to avoid logout/relogin during multiplayer co-locate.
 */
export async function executeCommandTrusted(page: Page, command: string): Promise<void> {
  const activePage = resolveActivePage(page);
  await assertNotStuckOnLogin(activePage);
  await executeCommandWithoutRecovery(activePage, command);
}

export async function executeCommandWithoutRecovery(page: Page, command: string): Promise<void> {
  const commandInput = page.getByTestId('command-input');
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await commandInput.evaluate((el: HTMLElement) => {
    el.focus();
  });
  await commandInput.clear();
  await commandInput.fill(command);
  await expect(commandInput).toHaveValue(command, { timeout: 5000 });
  const sendCommand = page.getByRole('button', { name: 'Send Command' });
  await expect(sendCommand).toBeEnabled({ timeout: TEST_TIMEOUTS.GAME_LOAD });
  await commandInput.press('Enter');
  await expect(commandInput).toBeVisible({ timeout: 3000 });
}

/**
 * Execute a command via the command input field.
 *
 * @param page - Playwright page instance
 * @param command - Command to execute
 * @returns Promise that resolves when command is sent
 */
export async function executeCommand(page: Page, command: string): Promise<void> {
  const session = getPageSessionCredentials(page);
  const activePage = await resolveExecuteCommandPage(page);
  await assertNotStuckOnLogin(activePage);

  const creds = getPageSessionCredentials(activePage) ?? session;
  // ensurePlayableConnection may reopen after page death; use its returned live Page.
  const live = await ensurePlayableConnection(activePage, {
    ...creds,
    timeoutMs: TEST_TIMEOUTS.GAME_LOAD,
  });
  await executeCommandWithoutRecovery(live, command);
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
  const activePage = resolveActivePage(page);
  const messageLocator = activePage.locator('[data-message-text]');
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
  const activePage = resolveActivePage(page);
  return activePage.evaluate(() => {
    const messages = Array.from(document.querySelectorAll('[data-message-text]'));
    return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });
}
