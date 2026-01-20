/**
 * Scenario 2: Clean Game State on Connection
 *
 * Tests that players don't see stale/previous game state information when connecting.
 * Verifies that each new connection starts with a clean slate and doesn't inherit
 * messages or state from previous sessions.
 */

import { expect, test } from '@playwright/test';
import { createMultiPlayerContexts, cleanupMultiPlayerContexts, getPlayerMessages } from '../fixtures/multiplayer';
import { getMessages } from '../fixtures/auth';

test.describe('Clean Game State on Connection', () => {
  test('AW should see no previous game state on fresh connection', async ({ browser }) => {
    // Create context for AW (fresh session)
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];

    // Wait for AW to be fully in the game
    await awContext.page.waitForTimeout(5000);

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
    // Create context for AW first
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];

    // Wait for AW to be in the game
    await awContext.page.waitForTimeout(5000);

    // Create context for Ithaqua (fresh session)
    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];

    // Wait for Ithaqua to be fully in the game
    await ithaquaContext.page.waitForTimeout(5000);

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
    // Create context for AW first
    const awContexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    const awContext = awContexts[0];

    // Wait for AW to be in the game
    await awContext.page.waitForTimeout(5000);

    // AW sends a message
    await awContext.page.locator('[data-testid="command-input"]').fill('say Hello before Ithaqua connects');
    await awContext.page.locator('[data-testid="command-input"]').press('Enter');
    await awContext.page.waitForTimeout(2000);

    // Create context for Ithaqua (after AW's message)
    const ithaquaContexts = await createMultiPlayerContexts(browser, ['Ithaqua']);
    const ithaquaContext = ithaquaContexts[0];

    // Wait for Ithaqua to be fully in the game
    await ithaquaContext.page.waitForTimeout(5000);

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
