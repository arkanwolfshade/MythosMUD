/**
 * Scenario 13: Whisper Basic
 *
 * Tests basic whisper channel functionality for private messaging between players.
 * Verifies that players can send and receive whisper messages, that messages
 * are properly delivered to the intended recipient, and that the whisper system
 * works correctly for private multiplayer communication.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

test.describe('Whisper Basic', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive AW whisper message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(awContext.page, 'whisper Ithaqua Hello, this is a private message');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Hello, this is a private message');

    // Verify Ithaqua receives the whisper (match by content; sender display name is character name, not account)
    const whisperToReceiver = /whispers to you: Hello, this is a private message/;
    await waitForCrossPlayerMessage(ithaquaContext, whisperToReceiver);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesWhisper = ithaquaMessages.some(msg => whisperToReceiver.test(msg));
    expect(seesWhisper).toBe(true);
  });

  test('AW should receive Ithaqua whisper reply', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Server resolves whisper target by character name, not account username. Use AW's
    // current character name so the whisper is delivered to the correct client.
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharacterName = await awContext.page.getByTestId('current-character-name').textContent();
    const targetName = (awCharacterName ?? '').trim() || 'ArkanWolfshade';

    await executeCommand(ithaquaContext.page, `whisper ${targetName} Hello back to you`);

    // Wait for confirmation (echo uses resolved target name)
    await waitForMessage(ithaquaContext.page, new RegExp(`You whisper to ${targetName}: Hello back to you`));

    // Verify AW receives the whisper (match by content; sender display name is character name, not account)
    const whisperToAw = /whispers to you: Hello back to you/;
    await waitForCrossPlayerMessage(awContext, whisperToAw);
    const awMessages = await getPlayerMessages(awContext);
    const seesWhisper = awMessages.some(msg => whisperToAw.test(msg));
    expect(seesWhisper).toBe(true);
  });
});
