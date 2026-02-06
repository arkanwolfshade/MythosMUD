/**
 * Scenario 3: Movement Between Rooms
 *
 * Tests multiplayer visibility when players move between different rooms.
 * Verifies that movement messages are properly broadcast to other players
 * in the same room, and that players can see each other's room transitions.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
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

test.describe('Movement Between Rooms', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Movement tests require both in the same room and that room must have an east exit
    // (so AW can "go east" and Ithaqua sees "ArkanWolfshade leaves the room"). Co-locate
    // via admin teleport, then move both to Main Foyer using path south -> west -> north
    // (works from Laundry Room or from Main Foyer; both end in Main Foyer which has east).
    const [awContext, ithaquaContext] = contexts;
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'teleport Ithaqua');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
    // Navigate both to Main Foyer (has east exit): south -> west -> north
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 1500));
    await ensureStanding(ithaquaContext.page, 5000);
    await executeCommand(ithaquaContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see AW leave when AW moves east', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Main Foyer has no north exit; use east to move AW to Eastern Hallway so Ithaqua sees "leaves the room"
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');

    await waitForMessage(awContext.page, /You move east|You go east|Eastern Hallway/i, 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Verify Ithaqua sees AW leave
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade leaves the room', 30000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesAWLeave = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade leaves the room'));
    expect(seesAWLeave).toBe(true);
  });

  test('AW should not see self-movement messages', async () => {
    const awContext = contexts[0];

    // Check for self-movement messages
    const awMessages = await getMessages(awContext.page);
    const selfMovementMessages = awMessages.filter(
      msg => msg.includes('ArkanWolfshade enters the room') || msg.includes('ArkanWolfshade leaves the room')
    );

    // AW should see NO self-movement messages
    expect(selfMovementMessages.length).toBe(0);
  });

  test('AW should see Ithaqua enter when Ithaqua moves to same room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Re-ensure both in game before move (avoids timeout when second player left)
    await ensurePlayerInGame(awContext, 10000);
    await ensurePlayerInGame(ithaquaContext, 10000);
    await new Promise(r => setTimeout(r, 2000));

    // AW is in Eastern Hallway from previous test; Ithaqua is in Main Foyer - Ithaqua goes east to join AW
    await ensureStanding(ithaquaContext.page, 5000);
    await executeCommand(ithaquaContext.page, 'go east');

    await waitForMessage(ithaquaContext.page, /You move east|You go east|Eastern Hallway/i, 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Verify AW sees Ithaqua enter
    await waitForCrossPlayerMessage(awContext, 'Ithaqua enters the room', 30000);
    const awMessages = await getMessages(awContext.page);
    const seesIthaquaEnter = awMessages.some(msg => msg.includes('Ithaqua enters the room'));
    expect(seesIthaquaEnter).toBe(true);
  });

  test('Ithaqua should not see self-movement messages', async () => {
    const ithaquaContext = contexts[1];

    // Check for self-movement messages
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const selfMovementMessages = ithaquaMessages.filter(
      msg => msg.includes('Ithaqua enters the room') || msg.includes('Ithaqua leaves the room')
    );

    // Ithaqua should see NO self-movement messages
    expect(selfMovementMessages.length).toBe(0);
  });
});
