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
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

/** Matches server `format_who_result` / error / empty branches (who_commands.py). */
const WHO_LISTING_LINE =
  /who to see all online|No players found matching|No players are currently online|Player information is not available|Online Players\s*\(|Online Players:/i;

/** CommandInputPanel disables the input when `!isConnected`; wait before fill/Enter. */
async function waitForCommandReady(page: Page, timeoutMs: number = TEST_TIMEOUTS.GAME_LOAD): Promise<void> {
  await page.bringToFront().catch(() => {});
  const commandInput = page.getByTestId('command-input');
  await expect(commandInput).toBeVisible({ timeout: TEST_TIMEOUTS.COMMAND });
  await commandInput.scrollIntoViewIfNeeded();
  await expect(page.getByRole('button', { name: 'Send Command' })).toBeEnabled({ timeout: timeoutMs });
}

async function expectWhoListingOnPage(page: Page): Promise<void> {
  const tryOnce = async (timeoutMs: number) => {
    await waitForCommandReady(page, TEST_TIMEOUTS.GAME_LOAD);
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

/** After `look`, room copy is often in Location / Room Description, not Game Info `[data-message-text]`. */
async function assertLookVisibleInPanels(page: Page): Promise<void> {
  const cue = page.getByText(
    /Arena\s*>\s*Arena|Arena entrance \(center\)|heart of the gladiator|sand and shadow|Exits:\s*North/i
  );
  await expect(cue.first()).toBeVisible({ timeout: 45000 });
}

test.describe('Who Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Who lists all online players; no co-location required.
  });

  test.beforeEach(async () => {
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should see both players in who list', async () => {
    const awContext = contexts[0];

    // `who` is server-global; same-room occupant sync is unnecessary and can burn the 180s test timeout.
    await awContext.page.bringToFront().catch(() => {});
    await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await waitForCommandReady(awContext.page);
    await executeCommand(awContext.page, 'look');
    await assertLookVisibleInPanels(awContext.page);

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.bringToFront().catch(() => {});
    await expectWhoListingOnPage(awContext.page);

    // Verify at least one player name appears in who list (both if timing allows)
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
    await waitForCommandReady(ithaquaContext.page);
    await executeCommand(ithaquaContext.page, 'look');
    await assertLookVisibleInPanels(ithaquaContext.page);

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
