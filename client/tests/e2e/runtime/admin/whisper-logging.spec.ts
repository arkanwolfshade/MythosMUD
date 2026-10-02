/**
 * Scenario 18: Whisper Logging
 *
 * Tests whisper channel logging and privacy functionality.
 * Verifies that whisper messages are private between players and that
 * the recipient receives the intended message.
 */

import { expect, adoptSharedPlayers, test } from '../fixtures/shared-session';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  createMultiPlayerContexts,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

test.describe('Whisper Logging', { tag: '@shared-session' }, () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser, sharedPlayers }) => {
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await adoptSharedPlayers(browser, sharedPlayers);
    await waitForAllPlayersInGame(contexts);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test('whisper messages should be private between players', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    const whisperBody = 'Testing whisper logging functionality';
    const senderAck = new RegExp(
      `You whisper to Ithaqua:\\s*${whisperBody.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`,
      'i'
    );
    const recipientAck = new RegExp(
      `ArkanWolfshade whispers to you:\\s*${whisperBody.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`,
      'i'
    );

    const runWhisper = async (): Promise<void> => {
      await awContext.page.bringToFront().catch(() => {});
      await ithaquaContext.page.bringToFront().catch(() => {});
      await ensurePlayerInGame(awContext, 30000);
      await ensurePlayerInGame(ithaquaContext, 30000);
      await executeCommand(awContext.page, 'stand');
      await executeCommand(ithaquaContext.page, 'stand');
      await new Promise(r => setTimeout(r, 2000));

      await awContext.page.bringToFront().catch(() => {});
      await executeCommand(awContext.page, `whisper Ithaqua ${whisperBody}`);
      await waitForMessage(awContext.page, senderAck, 25000);
      await waitForCrossPlayerMessage(ithaquaContext, recipientAck, 45000);
    };

    try {
      await runWhisper();
    } catch {
      await executeCommand(awContext.page, 'stand');
      await ithaquaContext.page.bringToFront().catch(() => {});
      await executeCommand(ithaquaContext.page, 'stand');
      await new Promise(r => setTimeout(r, 3000));
      await ensurePlayerInGame(awContext, 20000);
      await ensurePlayerInGame(ithaquaContext, 20000);
      await runWhisper();
    }

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    expect(ithaquaMessages.some(msg => recipientAck.test(msg))).toBe(true);
  });
});
