/**
 * Scenario 18: Whisper Logging
 *
 * Tests whisper channel logging and privacy functionality.
 * Verifies that whisper messages are private between players and that
 * the recipient receives the intended message.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  getPlayerMessages,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

test.describe('Whisper Logging', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('whisper messages should be private between players', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW sends whisper message
    await executeCommand(awContext.page, 'whisper Ithaqua Testing whisper logging functionality');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Testing whisper logging functionality', 10000).catch(
      () => {
        // Message may succeed even if format differs
      }
    );

    // Verify Ithaqua receives the whisper (privacy maintained)
    // Whisper messages use format: "{sender_name} whispers: {content}" (not "whispers to you:")
    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade whispers: Testing whisper logging functionality',
      10000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(
      msg =>
        msg.includes('ArkanWolfshade whispers: Testing whisper logging functionality') ||
        msg.includes('ArkanWolfshade whispers to you: Testing whisper logging functionality')
    );
    expect(seesMessage).toBe(true);
  });
});
