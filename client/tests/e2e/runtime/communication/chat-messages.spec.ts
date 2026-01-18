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
  getPlayerMessages,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

test.describe('Chat Messages Between Players', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);

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

  test('Ithaqua should see AW chat message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Ensure both players are unmuted (may have been done in beforeAll, but ensure clean state)
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await ithaquaContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // AW sends chat message
    await executeCommand(awContext.page, 'say Hello Ithaqua');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say: Hello Ithaqua');

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Hello Ithaqua/i, 15000);

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.toLowerCase().includes('arkanwolfshade says: hello ithaqua'));
    expect(seesMessage).toBe(true);
  });

  test('AW should see Ithaqua chat message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Ensure both players are unmuted (may have been done in beforeAll, but ensure clean state)
    try {
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await awContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Ithaqua sends chat message
    await executeCommand(ithaquaContext.page, 'say Hello ArkanWolfshade');

    // Wait for confirmation on Ithaqua's side
    await waitForMessage(ithaquaContext.page, 'You say: Hello ArkanWolfshade');

    // Wait for message to appear on AW's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(awContext, /Ithaqua says: Hello ArkanWolfshade/i, 15000);

    // Verify AW sees the message
    const awMessages = await getPlayerMessages(awContext);
    const seesMessage = awMessages.some(msg => msg.toLowerCase().includes('ithaqua says: hello arkanwolfshade'));
    expect(seesMessage).toBe(true);
  });

  test('chat messages should be properly formatted', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Ensure Ithaqua can see AW's messages (may have been done in beforeAll, but ensure clean state)
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await ithaquaContext.page.waitForTimeout(1000);
    } catch {
      // Ignore if already unmuted or command fails
    }

    // AW sends formatted message
    await executeCommand(awContext.page, 'say Testing message formatting');

    // Wait for confirmation on AW's side
    await waitForMessage(awContext.page, 'You say: Testing message formatting');

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Testing message formatting/i, 15000);

    // Verify Ithaqua sees properly formatted message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesFormattedMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade says: testing message formatting')
    );
    expect(seesFormattedMessage).toBe(true);
  });
});
