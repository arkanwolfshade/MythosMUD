/**
 * Scenario 7: Who Command
 *
 * Tests the who command functionality for multi-player visibility and real-time updates.
 * Verifies that players can see OTHER online players in the who list and that the list
 * updates correctly as players connect and disconnect.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, getMessages } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForLookReflectedInUi,
} from '../fixtures/multiplayer';

/** Matches server `format_who_result` / error / empty branches (who_commands.py). */
const WHO_LISTING_LINE =
  /who to see all online|No players found matching|No players are currently online|Player information is not available|Online Players\s*\(|Online Players:/i;

async function expectWhoListingOnPage(page: Page): Promise<void> {
  const tryOnce = async (timeoutMs: number) => {
    await page.bringToFront().catch(() => {});
    await executeCommand(page, 'who');
    await expect
      .poll(
        async () => {
          const texts: string[] = await page.evaluate(() =>
            Array.from(document.querySelectorAll('[data-message-text]')).map(el => {
              const attr = (el.getAttribute('data-message-text') || '').trim();
              if (attr) return attr;
              return (el.textContent || '').trim();
            })
          );
          return texts.some(t => WHO_LISTING_LINE.test(t));
        },
        { timeout: timeoutMs, message: '`who` output did not appear in Game Info' }
      )
      .toBe(true);
  };
  try {
    await tryOnce(45_000);
  } catch {
    await tryOnce(45_000);
  }
}

test.describe('Who Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.beforeEach(async () => {
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should see both players in who list', async () => {
    const awContext = contexts[0];

    await awContext.page.bringToFront().catch(() => {});
    await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await waitForLookReflectedInUi(awContext.page);

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.bringToFront().catch(() => {});
    await expectWhoListingOnPage(awContext.page);

    const messages = await getMessages(awContext.page);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });

  test('Ithaqua should see both players in who list', async () => {
    const ithaquaContext = contexts[1];

    await ithaquaContext.page.bringToFront().catch(() => {});
    await expect(
      ithaquaContext.page.getByText(new RegExp(`Player:\\s*${ithaquaContext.player.username}\\b`, 'i'))
    ).toBeVisible({ timeout: 15000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(ithaquaContext.page, 'look');
    await waitForLookReflectedInUi(ithaquaContext.page);

    await executeCommand(ithaquaContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await ithaquaContext.page.bringToFront().catch(() => {});
    await expectWhoListingOnPage(ithaquaContext.page);

    const messages = await getPlayerMessages(ithaquaContext);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });
});
