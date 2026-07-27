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
import { clickWithoutStability, ensurePlayableConnection, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  getPlayerMessages,
  prepareReceiverForInboundMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

/** Intentional logout click without waiting for login UI (leave broadcast is the assertion). */
async function clickLogout(page: Page): Promise<void> {
  await page.bringToFront().catch(() => {});
  const logoutButton = page.getByTestId('logout-button');
  await expect(logoutButton).toBeVisible({ timeout: 15000 });
  await clickWithoutStability(logoutButton);
}

test.describe('Basic Connection/Disconnection Flow', () => {
  test('AW should see Ithaqua entered message when Ithaqua connects', async ({ browser }) => {
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];
    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayableConnection(awContext.page, {
      username: awContext.player.username,
      password: awContext.player.password,
      timeoutMs: 30000,
    });

    // Seeded players share DEFAULT_RESPAWN_ROOM; do not use `teleport name room_id` (invalid syntax).
    await prepareReceiverForInboundMessages(awContext, 20000);

    const enteredWait = waitForCrossPlayerMessage(awContext, /Ithaqua has entered the game/i, 60000);

    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];
    await ensurePlayerInGame(ithaquaContext, 45000);

    await enteredWait;

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

    await cleanupMultiPlayerContexts(ithaquaContexts);
    await cleanupMultiPlayerContexts(awContexts);
  });

  test('AW should see Ithaqua left message when Ithaqua disconnects', async ({ browser }) => {
    const contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Intentional logout (not context.close): linkdead grace is 30s and delays left_game.
    // Logout marks intentional_disconnects then force-disconnects; that path must emit left_game.
    await prepareReceiverForInboundMessages(awContext, 20000);

    await Promise.all([
      waitForMessage(awContext.page, /Ithaqua has left the game/i, 45000),
      clickLogout(ithaquaContext.page),
    ]);

    const awMessages = await getPlayerMessages(awContext);
    expect(awMessages.some(msg => msg.includes('Ithaqua has left the game'))).toBe(true);

    await cleanupMultiPlayerContexts([awContext]);
    await cleanupMultiPlayerContexts([ithaquaContext]).catch(() => {});
  });
});
