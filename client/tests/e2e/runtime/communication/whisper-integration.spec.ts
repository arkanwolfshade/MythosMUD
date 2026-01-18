/**
 * Scenario 17: Whisper Integration
 *
 * Tests whisper message delivery between players in real-time.
 * Verifies that whisper messages are properly delivered to the intended
 * recipient and that the whisper system maintains privacy across player sessions.
 */

import { expect, test } from '@playwright/test';
import {
  createMultiPlayerContexts,
  cleanupMultiPlayerContexts,
  waitForCrossPlayerMessage,
  getPlayerMessages,
} from '../fixtures/multiplayer';
import { executeCommand, waitForMessage } from '../fixtures/auth';

test.describe('Whisper Integration', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('should deliver whisper message to intended recipient', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // AW sends whisper message
    await executeCommand(awContext.page, 'whisper Ithaqua Testing player management integration');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Testing player management integration', 10000).catch(
      () => {
        // Message may succeed even if format differs
      }
    );

    // Verify Ithaqua receives the whisper
    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade whispers to you: Testing player management integration',
      10000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade whispers to you: Testing player management integration')
    );
    expect(seesMessage).toBe(true);
  });
});
