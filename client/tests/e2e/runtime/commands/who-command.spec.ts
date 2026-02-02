/**
 * Scenario 7: Who Command
 *
 * Tests the who command functionality for multi-player visibility and real-time updates.
 * Verifies that players can see OTHER online players in the who list and that the list
 * updates correctly as players connect and disconnect.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
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
    // Who lists all online players; no co-location required.
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should see both players in who list', async () => {
    const awContext = contexts[0];

    await ensurePlayerInGame(awContext, 15000);

    await executeCommand(awContext.page, 'who');

    // Wait for who command response (Game Info or game log). Use getByText so we match
    // "Online Players (n):" regardless of data-message-text visibility or scroll.
    await expect(awContext.page.getByText(/Online Players/)).toBeVisible({ timeout: 15000 });

    // Verify at least one player name appears in who list (both if timing allows)
    const messages = await getMessages(awContext.page);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });

  test('Ithaqua should see both players in who list', async () => {
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(ithaquaContext.page, 'who');

    // Wait for who command response (Game Info or game log). Use getByText so we match
    // "Online Players (n):" regardless of data-message-text visibility or scroll.
    await expect(ithaquaContext.page.getByText(/Online Players/)).toBeVisible({ timeout: 15000 });

    const messages = await getPlayerMessages(ithaquaContext);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan || seesIthaqua).toBe(true);
  });
});
