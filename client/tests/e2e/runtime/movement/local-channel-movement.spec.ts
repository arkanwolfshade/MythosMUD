/**
 * Scenario 10: Local Channel Movement
 *
 * Tests local channel message routing based on player movement.
 * Verifies that local channel messages are properly routed when players
 * move between sub-zones, that message delivery is updated in real-time
 * based on player location, and that the movement-based routing system
 * works correctly for local communication.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

test.describe('Local Channel Movement', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Local channel requires both players in same room. Force co-location: stand then move both north.
    const [awContext, ithaquaContext] = contexts;
    await ensureStanding(awContext.page, 10000);
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 2000));
    await ensureStanding(ithaquaContext.page, 10000);
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see local message before AW moves', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(awContext.page, 'local Before movement test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Before movement test');

    // Verify Ithaqua sees the message
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade (local): Before movement test');
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): Before movement test'));
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message after AW moves to different sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Main Foyer has no north exit; use east to move AW to Eastern Hallway (different room)
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You move east|Eastern Hallway/i, 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    await new Promise(r => setTimeout(r, 2000));

    // AW sends local message from different room (Eastern Hallway); Ithaqua stays in Main Foyer
    await executeCommand(awContext.page, 'local After movement test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: After movement test');

    await new Promise(r => setTimeout(r, 3000));

    // Verify Ithaqua does NOT see the message (different rooms = different local scope)
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): After movement test'));
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW moves back to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // AW is in Eastern Hallway from previous test; go west to return to Main Foyer (same room as Ithaqua)
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go west');
    await waitForMessage(awContext.page, /You move west|Main Foyer/i, 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    await new Promise(r => setTimeout(r, 2000));

    // Re-ensure both in same room and receiver still in game before send (avoids timeout when second player left)
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);
    await new Promise(r => setTimeout(r, 2000));

    // AW sends local message after returning to Main Foyer
    await executeCommand(awContext.page, 'local After returning test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: After returning test');

    // Verify Ithaqua sees the message (they're in same sub-zone again)
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade (local): After returning test', 25000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): After returning test'));
    expect(seesMessage).toBe(true);
  });
});
