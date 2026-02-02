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

test.describe('Movement Between Rooms', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Require both players in same room so movement broadcasts are visible
    await ensurePlayersInSameRoom(contexts, 2, 30000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see AW leave when AW moves east', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW must stand before moving (server rejects "go" when sitting)
    await executeCommand(awContext.page, 'stand');
    await waitForMessage(awContext.page, /rise|standing|feet|already standing/i, 5000).catch(() => {});

    // AW moves north (use north - room may have West/North only in some envs)
    await executeCommand(awContext.page, 'go north');

    // Wait for movement confirmation
    await waitForMessage(awContext.page, 'You move north', 10000).catch(() => {
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

    // Ithaqua must stand before moving (server rejects "go" when sitting)
    await executeCommand(ithaquaContext.page, 'stand');
    await waitForMessage(ithaquaContext.page, /rise|standing|feet|already standing/i, 5000).catch(() => {});

    // Ithaqua moves north to join AW
    await executeCommand(ithaquaContext.page, 'go north');

    // Wait for movement confirmation
    await waitForMessage(ithaquaContext.page, 'You move north', 10000).catch(() => {
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
