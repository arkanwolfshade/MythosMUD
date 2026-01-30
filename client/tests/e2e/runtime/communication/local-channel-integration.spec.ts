/**
 * Scenario 12: Local Channel Integration
 *
 * Tests local channel message broadcasting and real-time delivery to multiple
 * players in the same sub-zone. Verifies that local messages are properly
 * broadcast to all players in the same sub-zone in real-time.
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

test.describe('Local Channel Integration', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // CRITICAL: Ensure both players are in the same room before local channel tests
    await ensurePlayersInSameRoom(contexts, 2, 30000);

    // Unmute both players to ensure clean state (mute state may persist from previous scenarios)
    // Mute filtering happens on the receiving end, so both players need to unmute each other
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    try {
      // Ithaqua unmutes AW (so Ithaqua can see AW's messages)
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await ithaquaContext.page.waitForTimeout(1000);

      // AW unmutes Ithaqua (so AW can see Ithaqua's messages)
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await awContext.page.waitForTimeout(1000);

      // Small additional wait to ensure mute state is cleared
      await awContext.page.waitForTimeout(1000);
    } catch {
      // Ignore unmute errors - players may not be muted to begin with
      // This is expected if mute state doesn't persist between test runs
    }
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('should broadcast local message to all players in same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await ithaquaContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // AW sends local message
    await executeCommand(awContext.page, 'local Testing player management integration');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say locally: Testing player management integration');

    // Wait for message to appear on Ithaqua's side
    // Local channel format is: "{sender_name} (local): {content}"
    await waitForCrossPlayerMessage(
      ithaquaContext,
      /ArkanWolfshade \(local\): Testing player management integration/i,
      30000
    );

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade (local): testing player management integration')
    );
    expect(seesMessage).toBe(true);
  });
});
