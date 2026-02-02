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
import { ensureStanding } from '../fixtures/player';

test.describe('Local Channel Integration', () => {
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

    // Unmute both players to ensure clean state
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await new Promise(r => setTimeout(r, 1000));
      await new Promise(r => setTimeout(r, 1000));
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
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Re-ensure receiver (Ithaqua) is in game and same room; brief stability wait so receiver is not
    // gone when sender sends
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 10000);
    await new Promise(r => setTimeout(r, 2000));

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
