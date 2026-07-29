/**
 * Scenario 1: Basic Connection/Disconnection Flow
 *
 * Tests basic multiplayer connection and disconnection messaging between two players.
 * Verifies that players can connect to the game, see each other's connection/disconnection
 * events, and that the messaging system works correctly.
 *
 * player_entered_game / player_left_game are room-scoped: AW must share Ithaqua's room
 * (and stay foregrounded in Firefox) to see Game Info lines.
 */

import { expect, test, type Page } from '@playwright/test';
import { ensurePlayableConnection, executeCommandTrusted, loginPlayer, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  getPlayerMessages,
  prepareReceiverForInboundMessages,
  resetE2ePlayerRoomsInDatabase,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

/** Force server-side leave (player_left_game). UI Exit uses /rest and can be cancelled by NPCs. */
async function forceLogoutPlayer(page: Page): Promise<void> {
  await page.bringToFront().catch(() => {});
  await executeCommandTrusted(page, 'logout');
}

test.describe('Basic Connection/Disconnection Flow', () => {
  test('AW should see Ithaqua entered message when Ithaqua connects', async ({ browser }) => {
    test.setTimeout(300_000);
    // Co-locate first so AW is a room subscriber; then force a fresh enter via logout/login.
    // Cold solo-then-join can miss room subscription targets under Firefox serial load.
    resetE2ePlayerRoomsInDatabase();
    const contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    try {
      await waitForAllPlayersInGame(contexts, 60000);
      await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

      const awContext = contexts[0];
      const ithaquaContext = contexts[1];

      await prepareReceiverForInboundMessages(awContext, 20000);
      await awContext.page.bringToFront().catch(() => {});

      await Promise.all([
        waitForMessage(awContext.page, /Ithaqua has left the game/i, 60000),
        forceLogoutPlayer(ithaquaContext.page),
      ]);
      // /logout force-disconnects server-side but does not always restore login UI; navigate explicitly.
      await ithaquaContext.page.goto('/', { waitUntil: 'domcontentloaded' });
      await ithaquaContext.page.getByTestId('username-input').waitFor({ state: 'visible', timeout: 45000 });

      await prepareReceiverForInboundMessages(awContext, 20000);
      await awContext.page.bringToFront().catch(() => {});

      await Promise.all([
        waitForMessage(awContext.page, /Ithaqua has entered the game/i, 90000),
        (async () => {
          await loginPlayer(ithaquaContext.page, ithaquaContext.player.username, ithaquaContext.player.password);
          await ensurePlayerInGame(ithaquaContext, 45000);
          await ensurePlayableConnection(ithaquaContext.page, {
            username: ithaquaContext.player.username,
            password: ithaquaContext.player.password,
            timeoutMs: 30000,
          });
        })(),
      ]);

      const awMessages = await getPlayerMessages(awContext);
      expect(awMessages.some(msg => msg.includes('Ithaqua has entered the game'))).toBe(true);

      const ithaquaMessages = await getPlayerMessages(ithaquaContext);
      const unwantedMessages = ithaquaMessages.filter(
        msg =>
          msg.includes('enters the room') ||
          msg.includes('leaves the room') ||
          msg.includes('entered the game') ||
          msg.includes('left the game')
      );
      expect(unwantedMessages).toHaveLength(0);
    } finally {
      await cleanupMultiPlayerContexts(contexts).catch(() => {});
    }
  });

  test('AW should see Ithaqua left message when Ithaqua disconnects', async ({ browser }) => {
    test.setTimeout(300_000);
    resetE2ePlayerRoomsInDatabase();
    const contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    try {
      await waitForAllPlayersInGame(contexts, 60000);
      await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

      const awContext = contexts[0];
      const ithaquaContext = contexts[1];

      await ensurePlayerInGame(awContext, 45000);
      await ensurePlayableConnection(awContext.page, {
        username: awContext.player.username,
        password: awContext.player.password,
        timeoutMs: 30000,
      });
      await prepareReceiverForInboundMessages(awContext, 30000);
      await awContext.page.bringToFront().catch(() => {});
      await expect(awContext.page.getByText('Connected', { exact: true }).first()).toBeVisible({ timeout: 15000 });

      // /logout force-disconnects server-side so player_left_game reaches room peers.
      await Promise.all([
        waitForMessage(awContext.page, /Ithaqua has left the game/i, 60000),
        (async () => {
          await ithaquaContext.page.bringToFront().catch(() => {});
          await executeCommandTrusted(ithaquaContext.page, 'logout');
        })(),
      ]);

      const awMessages = await getPlayerMessages(awContext);
      expect(awMessages.some(msg => msg.includes('Ithaqua has left the game'))).toBe(true);
    } finally {
      await cleanupMultiPlayerContexts(contexts).catch(() => {});
    }
  });
});
