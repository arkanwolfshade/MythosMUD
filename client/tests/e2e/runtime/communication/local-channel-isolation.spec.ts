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
import {
  createMultiPlayerContexts,
  cleanupMultiPlayerContexts,
  waitForCrossPlayerMessage,
  getPlayerMessages,
} from '../fixtures/multiplayer';
import { executeCommand, waitForMessage } from '../fixtures/auth';

test.describe('Local Channel Isolation', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see local message when both players in same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW sends local message (both in same sub-zone)
    await executeCommand(awContext.page, 'local Testing same sub-zone communication');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Testing same sub-zone communication');

    // Verify Ithaqua sees the message
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade says locally: Testing same sub-zone communication');
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade says locally: Testing same sub-zone communication')
    );
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message when AW is in different sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW moves to different sub-zone
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, 'You move east', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });
    await awContext.page.waitForTimeout(2000);

    // AW sends local message from different sub-zone
    await executeCommand(awContext.page, 'local Testing different sub-zone isolation');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Testing different sub-zone isolation');

    // Wait a bit for message routing
    await ithaquaContext.page.waitForTimeout(3000);

    // Verify Ithaqua does NOT see the message (different sub-zones)
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade says locally: Testing different sub-zone isolation')
    );
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW returns to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW moves back to same sub-zone as Ithaqua
    await executeCommand(awContext.page, 'go west');
    await waitForMessage(awContext.page, 'You move west', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });
    await awContext.page.waitForTimeout(2000);

    // AW sends local message after returning
    await executeCommand(awContext.page, 'local Testing same sub-zone after return');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You say locally: Testing same sub-zone after return');

    // Verify Ithaqua sees the message (same sub-zone again)
    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade says locally: Testing same sub-zone after return',
      10000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade says locally: Testing same sub-zone after return')
    );
    expect(seesMessage).toBe(true);
  });
});
