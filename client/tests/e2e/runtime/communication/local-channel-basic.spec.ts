/**
 * Scenario 8: Local Channel Basic
 *
 * Tests basic local channel communication functionality.
 * Verifies that players can send and receive local channel messages,
 * that messages are properly broadcast to players in the same sub-zone,
 * and that the local channel system works correctly for basic multiplayer communication.
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

test.describe('Local Channel Basic', () => {
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

  test('Ithaqua should see AW local channel message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await ithaquaContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // AW sends local channel message
    await executeCommand(awContext.page, 'local Hello everyone in the sanitarium');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say locally: Hello everyone in the sanitarium');

    // Wait for message to appear on Ithaqua's side
    // Local channel format is: "{sender_name} (local): {content}"
    await waitForCrossPlayerMessage(
      ithaquaContext,
      /ArkanWolfshade \(local\): Hello everyone in the sanitarium/i,
      30000
    );

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade (local): hello everyone in the sanitarium')
    );
    expect(seesMessage).toBe(true);
  });

  test('AW should see Ithaqua local channel reply', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    try {
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await awContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Ithaqua sends local reply
    await executeCommand(ithaquaContext.page, 'local Greetings ArkanWolfshade');

    // Wait for confirmation on Ithaqua's side
    await waitForMessage(ithaquaContext.page, 'You say locally: Greetings ArkanWolfshade');

    // Wait for message to appear on AW's side
    // Local channel format is: "{sender_name} (local): {content}"
    await waitForCrossPlayerMessage(awContext, /Ithaqua \(local\): Greetings ArkanWolfshade/i, 30000);

    // Verify AW sees the reply
    const awMessages = await getPlayerMessages(awContext);
    const seesMessage = awMessages.some(msg => msg.toLowerCase().includes('ithaqua (local): greetings arkanwolfshade'));
    expect(seesMessage).toBe(true);
  });
});
