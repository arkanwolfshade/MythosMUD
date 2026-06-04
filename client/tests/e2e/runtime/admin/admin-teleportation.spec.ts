/**
 * Scenario 6: Admin Teleportation
 *
 * Tests admin teleportation functionality and privilege handling.
 * Verifies that admin players can teleport other players to different rooms,
 * that non-admin players cannot use teleportation commands, and that
 * teleportation messages are properly broadcast to all relevant players.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, recoverPlayableSession, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
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
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to teleport Ithaqua', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

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

    const escapedTarget = ithaquaCharacterName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const teleportAck = new RegExp(
      `You teleport ${escapedTarget} to the south\\.?|You teleport .+ to the south\\.?|You do not have permission|do not have permission`,
      'i'
    );

    const runTeleport = async (): Promise<void> => {
      await executeCommand(awContext.page, `teleport ${ithaquaCharacterName} south`);
      await waitForMessage(awContext.page, teleportAck, 45000);
    };

    try {
      await runTeleport();
    } catch {
      await recoverPlayableSession(awContext.page, awContext.player.username, awContext.player.password, 45000);
      await runTeleport();
    }

    const awMessages = await getPlayerMessages(awContext);
    const seesPermissionDenied = awMessages.some(msg => /do not have permission/i.test(msg));
    expect(
      seesPermissionDenied,
      "Teleport returned 'You do not have permission'. Ensure ArkanWolfshade's character has is_admin set in the test database."
    ).toBe(false);

    await ithaquaContext.page.bringToFront().catch(() => {});
    await waitForCrossPlayerMessage(ithaquaContext, /You are teleported to the south by .+\.?/, 45000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    expect(ithaquaMessages.some(msg => /teleported.*south/.test(msg))).toBe(true);
  });

  test('Ithaqua should not be able to teleport AW', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

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
    await waitForMessage(
      ithaquaContext.page,
      /do not have permission|You do not have permission|not allowed|not found|teleport commands|no such/i,
      45000
    );

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    expect(ithaquaMessages.some(msg => /permission|not allowed|not found|teleport commands|no such/i.test(msg))).toBe(
      true
    );
  });
});
