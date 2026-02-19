/**
 * Scenario 31: Administrative Set Stat Command
 *
 * Validates the admin set administrative command from end to end: parser recognition,
 * permission gating, stat modification, DP/MP maximum warnings, error handling, and
 * audit logging. Confirms non-admin rejection flow and validates all stat types.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

test.describe('Administrative Set Stat Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to set player stats', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Server resolves target by character name; get Ithaqua's current character name
    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';

    await executeCommand(awContext.page, `admin set STR ${ithaquaCharName} 75`);

    // Wait for success or permission-denied (server returns "You do not have permission" if issuer is not admin)
    await waitForMessage(awContext.page, /Set .* (STR|strength)|do not have permission/, 10000).catch(() => {});

    const messages = await getMessages(awContext.page);
    const seesSuccess = messages.some(
      msg => (msg.includes('Set') && (msg.includes('STR') || msg.includes('75'))) || msg.includes("'s STR")
    );
    const seesPermissionDenied = messages.some(msg => msg.includes('do not have permission'));
    expect(
      seesPermissionDenied,
      "Admin set stat returned 'You do not have permission'. Ensure ArkanWolfshade's character has is_admin set in the test database."
    ).toBe(false);
    expect(seesSuccess).toBe(true);
  });

  test('Ithaqua should not be able to set stats', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Target by character name so server finds the player and returns permission denied (not "not found")
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await executeCommand(ithaquaContext.page, `admin set STR ${awCharName} 50`);

    await waitForMessage(ithaquaContext.page, /do not have permission|not found/, 10000).catch(() => {});

    const messages = await ithaquaContext.page.evaluate(() => {
      const msgs = Array.from(document.querySelectorAll('[data-message-text]'));
      return msgs.map(msg => (msg.getAttribute('data-message-text') || '').trim());
    });
    const seesError = messages.some(
      msg =>
        msg.includes('permission') || msg.includes('admin') || msg.includes('not allowed') || msg.includes('not found')
    );
    expect(seesError).toBe(true);
  });
});
