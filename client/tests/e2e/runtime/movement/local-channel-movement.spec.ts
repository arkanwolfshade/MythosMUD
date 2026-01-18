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
import {
  createMultiPlayerContexts,
  cleanupMultiPlayerContexts,
  waitForCrossPlayerMessage,
  getPlayerMessages,
} from '../fixtures/multiplayer';
import { executeCommand, waitForMessage } from '../fixtures/auth';

test.describe('Local Channel Movement', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see local message before AW moves', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW sends local message before movement
    await executeCommand(awContext.page, 'local Before movement test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Before movement test');

    // Verify Ithaqua sees the message
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade says locally: Before movement test');
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says locally: Before movement test'));
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message after AW moves to different sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW moves to different sub-zone
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, 'You move east', 10000).catch(() => {
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
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says locally: After movement test'));
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW moves back to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW moves back to same sub-zone as Ithaqua
    await executeCommand(awContext.page, 'go west');
    await waitForMessage(awContext.page, 'You move west', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });

    // Wait for movement to complete
    await awContext.page.waitForTimeout(2000);

    // AW sends local message after returning
    await executeCommand(awContext.page, 'local After returning test');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: After returning test');

    // Verify Ithaqua sees the message (they're in same sub-zone again)
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade says locally: After returning test', 10000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says locally: After returning test'));
    expect(seesMessage).toBe(true);
  });
});
