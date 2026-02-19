/**
 * Scenario 6: Admin Teleportation
 *
 * Tests admin teleportation functionality and privilege handling.
 * Verifies that admin players can teleport other players to different rooms,
 * that non-admin players cannot use teleportation commands, and that
 * teleportation messages are properly broadcast to all relevant players.
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

test.describe('Admin Teleportation', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to teleport Ithaqua', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Server resolves teleport target by character name (connection manager). Use Ithaqua's
    // current character name so the server finds her as online.
    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const ithaquaCharacterName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() || 'Ithaqua';

    await executeCommand(awContext.page, `teleport ${ithaquaCharacterName} south`);

    // Wait for either success or permission denied on AW's page (fail fast if not admin)
    await waitForMessage(
      awContext.page,
      new RegExp(`You teleport ${ithaquaCharacterName} to the south|You do not have permission`),
      10000
    ).catch(() => {});
    const awMessages = await getPlayerMessages(awContext);
    const seesPermissionDenied = awMessages.some(msg => msg.includes('You do not have permission'));
    expect(
      seesPermissionDenied,
      "Teleport returned 'You do not have permission'. Ensure ArkanWolfshade's character has is_admin set in the test database."
    ).toBe(false);

    // Verify Ithaqua sees teleportation message (server sends with trailing period; admin name is character name)
    await waitForCrossPlayerMessage(ithaquaContext, /You are teleported to the south by .+\.?/, 30000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesTeleportMessage = ithaquaMessages.some(msg => /teleported.*south/.test(msg));
    expect(seesTeleportMessage).toBe(true);
  });

  test('Ithaqua should not be able to teleport AW', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Target by character name so server finds AW and returns permission denied (not "not found")
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await executeCommand(ithaquaContext.page, `teleport ${awCharName} west`);

    await waitForMessage(ithaquaContext.page, /do not have permission|not found/, 10000).catch(() => {});

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesError = ithaquaMessages.some(
      msg => msg.includes('permission') || msg.includes('not allowed') || msg.includes('not found')
    );
    expect(seesError).toBe(true);
  });
});
