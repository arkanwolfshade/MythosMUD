/**
 * Scenario 5: Chat Messages Between Players
 *
 * Tests chat message broadcasting between players in the same room.
 * Verifies that players can send and receive chat messages, that messages
 * are properly formatted, and that the chat system works correctly for
 * multiplayer communication.
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

test.describe('Chat Messages Between Players', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // Room-based /say requires both players in the same room. Co-locate by having AW (admin) teleport
    // Ithaqua to his location; "go north" only works when both already share a room.
    const [awContext, ithaquaContext] = contexts;
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'teleport Ithaqua');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);

    // Unmute both players to ensure clean state (mute state may persist from previous scenarios)
    // Mute filtering happens on the receiving end, so both players need to unmute each other
    try {
      // Ithaqua unmutes AW (so Ithaqua can see AW's messages)
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));

      // AW unmutes Ithaqua (so AW can see Ithaqua's messages)
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await new Promise(r => setTimeout(r, 1000));

      // Small additional wait to ensure mute state is cleared
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

  test('Ithaqua should see AW chat message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    // Ensure Ithaqua has unmuted AW so the server delivers AW's say to Ithaqua (mute filter is per-receiver).
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        8000
      );
    } catch {
      // Ignore if already unmuted or command fails
    }
    // Allow server mute state to be applied before we send the say (avoids filtered delivery).
    await new Promise(r => setTimeout(r, 2500));

    // Re-ensure receiver (Ithaqua) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 10000);
    await new Promise(r => setTimeout(r, 2000));

    // AW sends chat message
    await executeCommand(awContext.page, 'say Hello Ithaqua');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say: Hello Ithaqua');

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Hello Ithaqua/i, 30000);

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.toLowerCase().includes('arkanwolfshade says: hello ithaqua'));
    expect(seesMessage).toBe(true);
  });

  test('AW should see Ithaqua chat message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await waitForMessage(awContext.page, /You have unmuted Ithaqua|Failed to unmute Ithaqua/i, 8000);
      await new Promise(r => setTimeout(r, 1500));
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Re-ensure receiver (AW) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(awContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 10000);
    await new Promise(r => setTimeout(r, 2000));

    // Ithaqua sends chat message
    await executeCommand(ithaquaContext.page, 'say Hello ArkanWolfshade');

    // Wait for confirmation on Ithaqua's side
    await waitForMessage(ithaquaContext.page, 'You say: Hello ArkanWolfshade');

    // Wait for message to appear on AW's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(awContext, /Ithaqua says: Hello ArkanWolfshade/i, 30000);

    // Verify AW sees the message
    const awMessages = await getPlayerMessages(awContext);
    const seesMessage = awMessages.some(msg => msg.toLowerCase().includes('ithaqua says: hello arkanwolfshade'));
    expect(seesMessage).toBe(true);
  });

  test('chat messages should be properly formatted', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        8000
      );
      await new Promise(r => setTimeout(r, 1500));
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Re-ensure receiver (Ithaqua) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 10000);
    await new Promise(r => setTimeout(r, 2000));

    // AW sends formatted message
    await executeCommand(awContext.page, 'say Testing message formatting');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say: Testing message formatting');

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Testing message formatting/i, 30000);

    // Verify Ithaqua sees properly formatted message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesFormattedMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade says: testing message formatting')
    );
    expect(seesFormattedMessage).toBe(true);
  });
});
