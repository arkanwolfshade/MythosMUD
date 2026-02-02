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

test.describe('Local Channel Movement', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Require both players in same room so local broadcasts are visible
    await ensurePlayersInSameRoom(contexts, 2, 30000);
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

    await executeCommand(awContext.page, 'stand');
    await waitForMessage(awContext.page, /rise|standing|feet|already standing/i, 5000).catch(() => {});

    // AW moves to different sub-zone (north - room may have West/North only in some envs)
    await executeCommand(awContext.page, 'go north');
    await waitForMessage(awContext.page, 'You move north', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Wait for movement to complete
    await awContext.page.waitForTimeout(2000);

    // AW sends local message after movement
    await executeCommand(awContext.page, 'local After movement test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: After movement test');

    // Wait a bit for message routing
    await ithaquaContext.page.waitForTimeout(3000);

    // Verify Ithaqua does NOT see the message (they're in different sub-zones)
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): After movement test'));
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW moves back to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(awContext.page, 'go south');
    await waitForMessage(awContext.page, 'You move south', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Wait for movement to complete
    await awContext.page.waitForTimeout(2000);

    // AW sends local message after returning
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
