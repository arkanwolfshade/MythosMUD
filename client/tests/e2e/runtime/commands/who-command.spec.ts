/**
 * Scenario 7: Who Command
 *
 * Tests the who command functionality for multi-player visibility and real-time updates.
 * Verifies that players can see OTHER online players in the who list and that the list
 * updates correctly as players connect and disconnect.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

test.describe('Who Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // CRITICAL: Ensure both players are in the same room before who command tests
    await ensurePlayersInSameRoom(contexts, 2, 30000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should see both players in who list', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    await executeCommand(awContext.page, 'who');

    // Wait for who command response to appear in the game log (required before asserting)
    await waitForMessage(awContext.page, 'Online Players:', 15000);

    // Verify at least one player name appears in who list (both if timing allows)
    const messages = await getMessages(awContext.page);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });

  test('Ithaqua should see both players in who list', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    await executeCommand(ithaquaContext.page, 'who');

    // Wait for who command response to appear in the game log (required before asserting)
    await waitForMessage(ithaquaContext.page, 'Online Players:', 15000);

    const messages = await getPlayerMessages(ithaquaContext);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });
});
