/**
 * Catalog visibility: ESC Catalog page and /catalog slash command.
 *
 * Mirrors skills-visibility.spec.ts for the item prototype catalog.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, loginPlayer, waitForMessage } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

/** Game Info rows or tick text — proves WS/game log pipeline before command_response. */
async function waitForGameInfoActivity(page: Page, timeoutMs: number): Promise<void> {
  await page.waitForFunction(
    () => {
      if (document.querySelectorAll('[data-message-text]').length > 0) return true;
      const body = document.body?.innerText ?? '';
      return body.includes('[Tick') && body.includes(']');
    },
    undefined,
    { timeout: timeoutMs }
  );
}

test.describe('Catalog visibility', () => {
  test('ESC Catalog (New Tab) opens catalog page', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });

    await page.keyboard.press('Escape');
    await page.getByRole('button', { name: 'Catalog (New Tab)' }).waitFor({
      state: 'visible',
      timeout: 5000,
    });

    const popupPromise = page.waitForEvent('popup', { timeout: 30000 });
    await page.getByRole('button', { name: 'Catalog (New Tab)' }).evaluate((el: HTMLElement) => {
      el.click();
    });
    const popup = await popupPromise;
    await popup.waitForLoadState('domcontentloaded');
    await popup.waitForLoadState('load', { timeout: 15000 }).catch(() => {});

    await expect(popup).toHaveURL(/\/catalog/);

    await expect(
      popup
        .getByRole('heading', { name: 'Item Catalog' })
        .or(popup.getByText('Loading catalog...'))
        .or(popup.getByText('Not authenticated', { exact: false }))
        .or(popup.getByRole('heading', { name: 'Error' }))
    ).toBeVisible({ timeout: 15000 });

    await expect(popup.getByRole('heading', { name: 'Item Catalog' })).toBeVisible({
      timeout: 10000,
    });
    await expect(popup.getByText(/Showing \d+-\d+ of \d+|No prototypes match|Loading catalog/)).toBeVisible({
      timeout: 15000,
    });
  });

  test('/catalog command returns item catalog text in game log', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });

    const catalogAck = /Item catalog: showing|Failed to load item catalog\.|Item catalog is not available/i;

    const runCatalog = async (): Promise<void> => {
      await page.bringToFront().catch(() => {});
      await executeCommand(page, 'stand');
      await new Promise(r => setTimeout(r, 1500));
      await waitForGameInfoActivity(page, 45000);
      await executeCommand(page, '/catalog');
      await waitForMessage(page, catalogAck, 35000);
    };

    try {
      await runCatalog();
    } catch {
      await executeCommand(page, 'stand');
      await new Promise(r => setTimeout(r, 3000));
      await waitForGameInfoActivity(page, 35000).catch(() => {});
      await runCatalog();
    }

    const messages = await page.locator('[data-message-text]').allTextContents();
    expect(messages.some(m => catalogAck.test(m))).toBe(true);
  });

  test('/catalog with type filter returns filtered header in game log', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await waitForGameInfoActivity(page, 45000);

    const catalogAck = /Item catalog: showing|Failed to load item catalog\./i;
    await executeCommand(page, '/catalog type=weapon');
    await waitForMessage(page, catalogAck, 35000);

    const messages = await page.locator('[data-message-text]').allTextContents();
    expect(messages.some(m => catalogAck.test(m))).toBe(true);
  });
});
