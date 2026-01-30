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

test.describe('Local Channel Isolation', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // CRITICAL: Ensure both players are in the same room initially
    await ensurePlayersInSameRoom(contexts, 2, 30000);
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

    await executeCommand(awContext.page, 'stand');
    await waitForMessage(awContext.page, /rise|standing|feet|already standing/i, 5000).catch(() => {});

    await executeCommand(awContext.page, 'go north');
    await waitForMessage(awContext.page, 'You move north', 10000).catch(() => {
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
      msg.includes('ArkanWolfshade (local): Testing different sub-zone isolation')
    );
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW returns to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(awContext.page, 'go south');
    await waitForMessage(awContext.page, 'You move south', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });
    await awContext.page.waitForTimeout(2000);

    // AW sends local message after returning
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
