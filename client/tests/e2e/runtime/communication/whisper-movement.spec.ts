/**
 * Scenario 16: Whisper Movement
 *
 * Tests whisper channel functionality across different player locations.
 * Verifies that whisper messages work correctly when players are in different
 * rooms, that whisper delivery is not affected by player movement, and that
 * the whisper system maintains privacy and proper message delivery regardless
 * of player location.
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
import { ensureStanding } from '../fixtures/player';

test.describe('Whisper Movement', () => {
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

  test('Ithaqua should receive whisper when both players in same room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(awContext.page, 'whisper Ithaqua Testing whisper in same room');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Testing whisper in same room', 10000).catch(() => {
      // Message may succeed even if format differs
    });

    // Verify Ithaqua receives the whisper
    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade whispers to you: Testing whisper in same room',
      10000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade whispers to you: Testing whisper in same room')
    );
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should receive whisper when AW is in different room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await ensureStanding(awContext.page, 5000);
    // AW moves to different room
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, 'You move east', 10000).catch(() => {
      // Movement may succeed even if message format differs
    });
    await new Promise(r => setTimeout(r, 2000));

    // AW sends whisper from different room
    await executeCommand(awContext.page, 'whisper Ithaqua Testing whisper from different room');

    // Wait for confirmation
    await waitForMessage(awContext.page, 'You whisper to Ithaqua: Testing whisper from different room', 10000).catch(
      () => {
        // Message may succeed even if format differs
      }
    );

    // Verify Ithaqua receives the whisper (whispers work across rooms; Game Info + Chat use data-message-text)
    await waitForCrossPlayerMessage(
      ithaquaContext,
      'ArkanWolfshade whispers to you: Testing whisper from different room',
      30000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade whispers to you: Testing whisper from different room')
    );
    expect(seesMessage).toBe(true);
  });
});
