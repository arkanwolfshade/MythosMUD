/**
 * Issue #610: new game session vs grace reconnect.
 *
 * A second browser context for the same player sends a new session_id on WS
 * establish. Prior sockets must close; occupancy/who must reach the live tab.
 * Firefox runtime project (playwright.runtime.config.ts).
 *
 * Existing occupancy coverage: who-command, chat-messages, local-channel-integration.
 * This spec is the replacement path those suites do not exercise (same account, two tabs).
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForPlayableSession } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

const WHO_LISTING_LINE =
  /who to see all online|No players found matching|No players are currently online|Player information is not available|Online Players\s*\(|Online Players:/i;

test.describe('New game session replacement (#610)', () => {
  test.describe.configure({ timeout: 300_000 });

  test('second AW tab is playable and Ithaqua who still sees AW', async ({ browser }) => {
    const firstPair = await createMultiPlayerContexts(browser, ['Ithaqua', 'ArkanWolfshade']);
    await waitForAllPlayersInGame(firstPair, 60000);

    const replacement = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const ithaqua = firstPair[0];
    const awLive = replacement[0];

    try {
      // Replacement login kicks the first AW socket; that tab may show login/linkdead.
      // waitForAllPlayersInGame does not re-enter. ensurePlayerInGame does.
      await ensurePlayerInGame(awLive, 60000);
      await ensurePlayerInGame(ithaqua, 45000);
      await waitForPlayableSession(awLive.page, 30000);

      await awLive.page.bringToFront().catch(() => {});
      await executeCommand(awLive.page, 'who');
      await expect
        .poll(
          async () => {
            const texts = await getPlayerMessages(awLive);
            const hasListing = texts.some(t => WHO_LISTING_LINE.test(t));
            const seesIthaqua = texts.some(t => t.includes('Ithaqua'));
            return hasListing && seesIthaqua;
          },
          { timeout: 45000, message: 'Replacement AW tab did not see Ithaqua in who' }
        )
        .toBe(true);

      await ithaqua.page.bringToFront().catch(() => {});
      await executeCommand(ithaqua.page, 'who');
      await expect
        .poll(
          async () => {
            const texts = await getPlayerMessages(ithaqua);
            const hasListing = texts.some(t => WHO_LISTING_LINE.test(t));
            const seesAw = texts.some(t => t.includes('ArkanWolfshade'));
            return hasListing && seesAw;
          },
          { timeout: 45000, message: 'Ithaqua did not see AW after session replacement' }
        )
        .toBe(true);
    } finally {
      await cleanupMultiPlayerContexts(replacement).catch(() => {});
      await cleanupMultiPlayerContexts(firstPair).catch(() => {});
    }
  });
});
