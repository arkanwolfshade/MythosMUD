/**
 * Scenario 13: Whisper Basic
 *
 * Tests basic whisper channel functionality for private messaging between players.
 * Verifies that players can send and receive whisper messages, that messages
 * are properly delivered to the intended recipient, and that the whisper system
 * works correctly for private multiplayer communication.
 */

import { expect, test } from '@playwright/test';
import {
  createMultiPlayerContexts,
  cleanupMultiPlayerContexts,
  waitForCrossPlayerMessage,
  getPlayerMessages,
} from '../fixtures/multiplayer';
import { executeCommand, waitForMessage } from '../fixtures/auth';

test.describe('Whisper Basic', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive AW whisper message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW sends whisper to Ithaqua
    await executeCommand(awContext.page, 'whisper Ithaqua Hello, this is a private message');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Hello, this is a private message');

    // Verify Ithaqua receives the whisper
    await waitForCrossPlayerMessage(ithaquaContext, 'ArkanWolfshade whispers to you: Hello, this is a private message');
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesWhisper = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade whispers to you: Hello, this is a private message')
    );
    expect(seesWhisper).toBe(true);
  });

  test('AW should receive Ithaqua whisper reply', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Ithaqua replies with whisper
    await executeCommand(ithaquaContext.page, 'whisper ArkanWolfshade Hello back to you');

    // Wait for confirmation
    await waitForMessage(ithaquaContext.page, 'You whisper to ArkanWolfshade: Hello back to you');

    // Verify AW receives the whisper
    await waitForCrossPlayerMessage(awContext, 'Ithaqua whispers to you: Hello back to you');
    const awMessages = await awContext.page.evaluate(() => {
      const messages = Array.from(document.querySelectorAll('[data-message-text]'));
      return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
    });
    const seesWhisper = awMessages.some(msg => msg.includes('Ithaqua whispers to you: Hello back to you'));
    expect(seesWhisper).toBe(true);
  });
});
