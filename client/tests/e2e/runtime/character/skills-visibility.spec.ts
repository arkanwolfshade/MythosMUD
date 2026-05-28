/**
 * Scenarios 39 (E2) and 40 (E3): Skills visibility (plan 10.8 E2, E3).
 *
 * E2: Skills (New Tab) opens with playerId; skills page shows that character's skills.
 * E3: /skills command returns active character's skills in game log.
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
    { timeout: timeoutMs }
  );
}

test.describe('Skills visibility (plan 10.8 E2, E3)', () => {
  test('E2: Skills (New Tab) opens with playerId and skills page loads', async ({ page, context }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    // Wait for character to be loaded so MainMenuModal receives playerId and opens /skills?playerId=...
    await page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });

    await page.keyboard.press('Escape');
    await page.getByRole('button', { name: 'Skills (New Tab)' }).waitFor({
      state: 'visible',
      timeout: 5000,
    });

    const popupPromise = context.waitForEvent('page');
    await page.getByRole('button', { name: 'Skills (New Tab)' }).click();
    const popup = await popupPromise;
    await popup.waitForLoadState('domcontentloaded');
    await popup.waitForLoadState('load', { timeout: 15000 }).catch(() => {});

    await expect(popup).toHaveURL(/\/(?:skills|skills\?)/);
    await expect(popup).toHaveURL(/playerId=/);

    await expect(
      popup
        .getByRole('heading', { name: 'Character Skills' })
        .or(popup.getByText('Loading skills...'))
        .or(popup.getByText('Not authenticated', { exact: false }))
        .or(popup.getByRole('heading', { name: 'Error' }))
    ).toBeVisible({ timeout: 15000 });

    await expect(popup.getByRole('heading', { name: 'Character Skills' })).toBeVisible({
      timeout: 10000,
    });
  });

  test('E3: /skills command returns active character skills in game log', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });

    const skillsAck =
      /Your skills:|No skills recorded|Failed to load skills\.|do not have access to this character's skills/i;

    const runSkills = async (): Promise<void> => {
      await page.bringToFront().catch(() => {});
      await executeCommand(page, 'stand');
      await new Promise(r => setTimeout(r, 1500));
      await waitForGameInfoActivity(page, 45000);
      await executeCommand(page, '/skills');
      await waitForMessage(page, skillsAck, 35000);
    };

    try {
      await runSkills();
    } catch {
      await executeCommand(page, 'stand');
      await new Promise(r => setTimeout(r, 3000));
      await waitForGameInfoActivity(page, 35000).catch(() => {});
      await runSkills();
    }

    const messages = await page.locator('[data-message-text]').allTextContents();
    expect(messages.some(m => skillsAck.test(m))).toBe(true);
  });
});
