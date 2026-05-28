/**
 * Scenario 6: Admin Teleportation
 *
 * Tests admin teleportation functionality and privilege handling.
 * Verifies that admin players can teleport other players to different rooms,
 * that non-admin players cannot use teleportation commands, and that
 * teleportation messages are properly broadcast to all relevant players.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';

/**
 * After `look`, room prose is in Location / Room Description, not always Game Info `[data-message-text]`.
 */
async function assertLookVisibleInPanels(page: Page): Promise<void> {
  const cue = page.getByText(
    /Arena\s*>\s*Arena|Arena entrance \(center\)|heart of the gladiator|sand and shadow|Exits:\s*North/i
  );
  await expect(cue.first()).toBeVisible({ timeout: 45000 });
}

test.describe('Admin Teleportation', () => {
  // ensureMultiplayerCoLocated can take several 45s co-locate waits across retries; default 180s is too tight.
  test.describe.configure({ timeout: 300_000 });

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

    await ensureMultiplayerCoLocated(contexts, { coLocateTimeoutMs: 45000 });

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Server resolves teleport target by character name (connection manager). Use Ithaqua's
    // current character name so the server finds her as online.
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const ithaquaCharacterName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() || 'Ithaqua';

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await assertLookVisibleInPanels(awContext.page);

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, `teleport ${ithaquaCharacterName} south`);

    // teleport_helpers: "You teleport {target} to the {dir}." (optional period); or permission denial.
    const escapedTarget = ithaquaCharacterName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    await waitForMessage(
      awContext.page,
      new RegExp(
        `You teleport ${escapedTarget} to the south\\.?|You teleport .+ to the south\\.?|You do not have permission|do not have permission`,
        'i'
      ),
      45000
    );
    const awMessages = await getPlayerMessages(awContext);
    const seesPermissionDenied = awMessages.some(msg => /do not have permission/i.test(msg));
    expect(
      seesPermissionDenied,
      "Teleport returned 'You do not have permission'. Ensure ArkanWolfshade's character has is_admin set in the test database."
    ).toBe(false);

    // Receiver must be focused for Game Info delivery; prior tests can leave second browser linkdead.
    await ithaquaContext.page.bringToFront().catch(() => {});
    // Verify Ithaqua sees teleportation message (teleport_helpers: "You are teleported to the {dir} by {name}.")
    await waitForCrossPlayerMessage(ithaquaContext, /You are teleported to the south by .+\.?/, 45000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesTeleportMessage = ithaquaMessages.some(msg => /teleported.*south/.test(msg));
    expect(seesTeleportMessage).toBe(true);
  });

  test('Ithaqua should not be able to teleport AW', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { coLocateTimeoutMs: 45000 });
    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Target by character name so server finds AW and returns permission denied (not "not found")
    await awContext.page.bringToFront().catch(() => {});
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 30000);
    await expect(
      ithaquaContext.page.getByText(new RegExp(`Player:\\s*${ithaquaContext.player.username}\\b`, 'i'))
    ).toBeVisible({ timeout: 15000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(ithaquaContext.page, 'look');
    await assertLookVisibleInPanels(ithaquaContext.page);

    await executeCommand(ithaquaContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(ithaquaContext.page, `teleport ${awCharName} west`);

    // Server (admin_teleport_commands): "You do not have permission to use teleport commands."
    await waitForMessage(
      ithaquaContext.page,
      /do not have permission|You do not have permission|not allowed|not found|teleport commands|no such/i,
      45000
    );

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesError = ithaquaMessages.some(msg =>
      /permission|not allowed|not found|teleport commands|no such/i.test(msg)
    );
    expect(seesError).toBe(true);
  });
});
