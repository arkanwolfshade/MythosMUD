/**
 * Scenario 9: Local Channel Isolation
 *
 * Tests local channel isolation between different sub-zones.
 * Verifies that local channel messages are properly isolated to their
 * respective sub-zones, that players in different sub-zones cannot see
 * each other's local messages, and that the sub-zone routing system
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

test.describe('Local Channel Isolation', () => {
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

  test('Ithaqua should see local message when both players in same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    await executeCommand(awContext.page, 'local Testing same sub-zone communication');
    await waitForMessage(awContext.page, 'You say locally: Testing same sub-zone communication');

    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade (local): Testing same sub-zone communication',
      35000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing same sub-zone communication')
    );
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message when AW is in different sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Main Foyer has no north exit; use east to move AW to Eastern Hallway (different room)
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You move east|Eastern Hallway/i, 10000).catch(() => {
      // If movement fails, test cannot verify isolation
    });
    await new Promise(r => setTimeout(r, 2000));

    // AW sends local message from different room (Eastern Hallway); Ithaqua stays in Main Foyer
    await executeCommand(awContext.page, 'local Testing different sub-zone isolation');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Testing different sub-zone isolation');

    // Wait a bit for message routing
    await new Promise(r => setTimeout(r, 3000));

    // Verify Ithaqua does NOT see the message (different rooms = different local scope)
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing different sub-zone isolation')
    );
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW returns to same sub-zone', async () => {
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
    await executeCommand(awContext.page, 'local Testing same sub-zone after return');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Testing same sub-zone after return');

    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade (local): Testing same sub-zone after return',
      30000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing same sub-zone after return')
    );
    expect(seesMessage).toBe(true);
  });
});
