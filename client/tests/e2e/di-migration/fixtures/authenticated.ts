/* eslint-disable react-hooks/rules-of-hooks */

import { test, type Browser, type BrowserContext, type Page } from '@playwright/test';

import { loginPlayer } from '../../runtime/fixtures/auth';
import {
  ADMIN_STORAGE_PATH,
  ADMIN_USERNAME,
  AUTH_STORAGE_PATH,
  BASE_URL,
  TEST_PASSWORD,
  TEST_USERNAME,
} from '../constants';
import { safeWait } from './wait';

async function setupAuthStorage(
  context: BrowserContext,
  username: string,
  password: string,
  storagePath: string
): Promise<void> {
  const page = await context.newPage();
  page.setDefaultTimeout(60000);

  try {
    await loginPlayer(page, username, password);
    await safeWait(page, 1000);

    if (page.isClosed()) {
      throw new Error('Page was closed after login');
    }

    const commandInput = page.getByTestId('command-input');
    const isLoggedIn = await commandInput.isVisible({ timeout: 5000 }).catch(() => false);
    if (!isLoggedIn) {
      throw new Error('Login verification failed - command input not found');
    }

    await context.storageState({ path: storagePath });
  } catch (error) {
    const errorMsg = error instanceof Error ? error.message : String(error);
    // nosemgrep: javascript.lang.security.audit.unsafe-formatstring.unsafe-formatstring
    console.error(`Failed to setup auth storage for ${username}:`, errorMsg);
    throw error;
  } finally {
    if (!page.isClosed()) {
      await page.close();
    }
  }
}

type AuthenticatedPage = {
  page: Page;
  username: string;
};

async function openAuthenticatedPage(
  browser: Browser,
  username: string,
  password: string,
  storagePath: string,
  use: (page: Page) => Promise<void>
): Promise<void> {
  const authContext = await browser.newContext();
  try {
    await setupAuthStorage(authContext, username, password, storagePath);
  } finally {
    await authContext.close();
  }

  const context = await browser.newContext({ storageState: storagePath });
  const page = await context.newPage();
  await page.goto(BASE_URL, { waitUntil: 'load' });

  const isAtLoginScreen = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);

  if (isAtLoginScreen) {
    await loginPlayer(page, username, password);
    await context.storageState({ path: storagePath });
  } else {
    const commandInput = page.getByTestId('command-input');
    const isInGame = await commandInput.isVisible({ timeout: 10000 }).catch(() => false);

    if (!isInGame) {
      const motdButton = page.getByTestId('motd-enter-realm');
      const isAtMOTD = await motdButton.isVisible({ timeout: 5000 }).catch(() => false);

      if (isAtMOTD) {
        await motdButton.click();
        await commandInput.waitFor({ state: 'visible', timeout: 15000 });
      } else {
        await loginPlayer(page, username, password);
        await context.storageState({ path: storagePath });
      }
    }
  }

  await page
    .getByTestId('command-input')
    .waitFor({ state: 'visible', timeout: 15000 })
    .catch(() => {});
  await use(page);
  await context.close();
}

export const authenticatedTest = test.extend<AuthenticatedPage>({
  page: async ({ browser }, use) => {
    await openAuthenticatedPage(browser, TEST_USERNAME, TEST_PASSWORD, AUTH_STORAGE_PATH, use);
  },
  username: TEST_USERNAME,
});

export const adminTest = test.extend<AuthenticatedPage>({
  page: async ({ browser }, use) => {
    await openAuthenticatedPage(browser, ADMIN_USERNAME, TEST_PASSWORD, ADMIN_STORAGE_PATH, use);
  },
  username: ADMIN_USERNAME,
});
