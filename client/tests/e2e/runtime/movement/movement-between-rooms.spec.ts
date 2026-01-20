/**
 * Scenario 3: Movement Between Rooms
 *
 * Tests multiplayer visibility when players move between different rooms.
 * Verifies that movement messages are properly broadcast to other players
 * in the same room, and that players can see each other's room transitions.
 */

import { expect, test } from '@playwright/test';
import {
  createMultiPlayerContexts,
  cleanupMultiPlayerContexts,
  waitForCrossPlayerMessage,
  getPlayerMessages,
} from '../fixtures/multiplayer';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';

test.describe('Movement Between Rooms', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see AW leave when AW moves east', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW moves east
    await executeCommand(awContext.page, 'go east');

    // Wait for movement confirmation
    await waitForMessage(awContext.page, 'You move east', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Verify Ithaqua sees AW leave
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade leaves the room', 10000);
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

    // Ithaqua moves east to join AW
    await executeCommand(ithaquaContext.page, 'go east');

    // Wait for movement confirmation
    await waitForMessage(ithaquaContext.page, 'You move east', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Verify AW sees Ithaqua enter
    await waitForCrossPlayerMessage(awContext, 'Ithaqua enters the room', 10000);
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
