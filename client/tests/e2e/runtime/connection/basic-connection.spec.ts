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

import { expect, test } from '@playwright/test';
import { ensurePlayableConnection, executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';
import { DEFAULT_RESPAWN_ROOM } from '../fixtures/test-data';

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

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, `teleport ArkanWolfshade ${DEFAULT_RESPAWN_ROOM}`);
    await waitForMessage(awContext.page, /Arena|grid position|exits/i, 20000).catch(() => {});

    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];
    await ensurePlayerInGame(ithaquaContext, 45000);

    await awContext.page.bringToFront().catch(() => {});
    await waitForMessage(awContext.page, /Ithaqua has entered the game/i, 45000);

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
    await ensurePlayerInGame(contexts[0], 15000);
    await ensurePlayerInGame(contexts[1], 15000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await awContext.page.bringToFront().catch(() => {});
    await ithaquaContext.context.close();

    await waitForMessage(awContext.page, /Ithaqua has left the game/i, 15000);

    const awMessages = await getPlayerMessages(awContext);
    expect(awMessages.some(msg => msg.includes('Ithaqua has left the game'))).toBe(true);

    await cleanupMultiPlayerContexts([awContext]);
  });
});
