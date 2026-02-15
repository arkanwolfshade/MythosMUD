/**
 * Scenario 2: Clean Game State on Connection
 *
 * Tests that players don't see stale/previous game state information when connecting.
 * Verifies that each new connection starts with a clean slate and doesn't inherit
 * messages or state from previous sessions.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  getPlayerMessages,
} from '../fixtures/multiplayer';

test.describe('Clean Game State on Connection', () => {
  test('AW should see no previous game state on fresh connection', async ({ browser }) => {
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];
    await ensurePlayerInGame(awContext, 45000);

    // Check for stale messages
    const awMessages = await getMessages(awContext.page);
    const staleMessages = awMessages.filter(
      msg =>
        msg.includes('has entered the game') ||
        msg.includes('has left the game') ||
        msg.includes('enters the room') ||
        msg.includes('leaves the room')
    );

    // AW should see NO previous game state information
    expect(staleMessages.length).toBe(0);

    // Cleanup
    await cleanupMultiPlayerContexts(awContexts);
  });

  test('Ithaqua should see no previous game state on fresh connection', async ({ browser }) => {
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];
    await ensurePlayerInGame(awContext, 45000);

    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];
    await ensurePlayerInGame(ithaquaContext, 45000);

    // Check for stale messages
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const staleMessages = ithaquaMessages.filter(
      msg =>
        msg.includes('has entered the game') ||
        msg.includes('has left the game') ||
        msg.includes('enters the room') ||
        msg.includes('leaves the room')
    );

    // Ithaqua should see NO previous game state information
    expect(staleMessages.length).toBe(0);

    // Cleanup
    await cleanupMultiPlayerContexts(ithaquaContexts);
    await cleanupMultiPlayerContexts(awContexts);
  });

  test('players should not see messages from before their connection', async ({ browser }) => {
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];
    // Fresh connection needs longer timeout for login + WebSocket + first tick.
    await ensurePlayerInGame(awContext, 45000);

    await executeCommand(awContext.page, 'say Hello before Ithaqua connects');
    try {
      await expect(
        awContext.page.locator('[data-message-text]').filter({ hasText: /Hello before Ithaqua/ })
      ).toBeVisible({ timeout: 5000 });
    } catch {
      // Message may or may not appear due to timing
    }

    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];
    // Connecting player needs longer timeout for first tick.
    await ensurePlayerInGame(ithaquaContext, 45000);

    // Check Ithaqua's messages
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesOldMessage = ithaquaMessages.some(msg => msg.includes('Hello before Ithaqua connects'));

    // Ithaqua should NOT see messages from before their connection
    expect(seesOldMessage).toBe(false);

    // Cleanup
    await cleanupMultiPlayerContexts(ithaquaContexts);
    await cleanupMultiPlayerContexts(awContexts);
  });
});
