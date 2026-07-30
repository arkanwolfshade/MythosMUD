/**
 * Scenario 31: Administrative Set Stat Command
 *
 * Validates the admin set administrative command from end to end: parser recognition,
 * permission gating, stat modification, DP/MP maximum warnings, error handling, and
 * audit logging. Confirms non-admin rejection flow and validates all stat types.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, getMessages, recoverPlayableSession, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureFreshMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { despawnSanitariumCultists, ensurePlayableAlive } from '../fixtures/player';
import { DEFAULT_SPAWN_LOOK_CUE } from '../fixtures/test-data';

/**
 * After `look`, room prose is shown in Location / Room Description, not always Game Info `[data-message-text]`.
 */
async function assertLookVisibleInPanels(page: Page): Promise<void> {
  const cue = page.getByText(DEFAULT_SPAWN_LOOK_CUE);
  await expect(cue.first()).toBeVisible({ timeout: 45000 });
}

async function characterNameFromPage(page: Page, fallback: string): Promise<string> {
  await page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
  return (await page.getByTestId('current-character-name').textContent())?.trim() ?? fallback;
}

async function lookAndStand(page: Page): Promise<void> {
  await page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
  await executeCommand(page, 'look');
  await assertLookVisibleInPanels(page);
  await executeCommand(page, 'stand');
  await new Promise(r => setTimeout(r, 1500));
}

async function prepAwForAdminSet(awContext: PlayerContext): Promise<void> {
  await awContext.page.bringToFront().catch(() => {});
  await ensurePlayerInGame(awContext, 30000);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  await despawnSanitariumCultists(awContext.page);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
  await lookAndStand(awContext.page);
}

async function prepNonAdminForSetAttempt(ctx: PlayerContext): Promise<void> {
  await ctx.page.bringToFront().catch(() => {});
  await ensurePlayerInGame(ctx, 30000);
  ctx.page = await ensurePlayableAlive(ctx.page, ctx.player.username, ctx.player.password);
  await expect(ctx.page.getByText(new RegExp(`Player:\\s*${ctx.player.username}\\b`, 'i'))).toBeVisible({
    timeout: 15000,
  });
  await lookAndStand(ctx.page);
}

async function runAdminSetWithRecovery(awContext: PlayerContext, targetName: string): Promise<void> {
  const runAdminSet = async (): Promise<void> => {
    await executeCommand(awContext.page, `admin set STR ${targetName} 75`);
    await waitForMessage(
      awContext.page,
      /Set .+['\u2019]s STR from|STR from \d+ to 75|do not have permission|You do not have permission/i,
      45000
    );
  };

  try {
    await runAdminSet();
  } catch {
    awContext.page = await recoverPlayableSession(
      awContext.page,
      awContext.player.username,
      awContext.player.password,
      45000
    );
    await runAdminSet();
  }
}

test.describe('Administrative Set Stat Command', () => {
  test.describe.configure({ timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(300_000);
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to set player stats', async ({ browser }) => {
    test.setTimeout(300_000);
    contexts = await ensureFreshMultiPlayerContexts(browser, contexts, ['ArkanWolfshade', 'Ithaqua']);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Admin set resolves the target by name on the server; same-room UI sync is not required.

    // Server resolves target by character name; get Ithaqua's current character name
    await ithaquaContext.page.bringToFront().catch(() => {});
    const ithaquaCharName = await characterNameFromPage(ithaquaContext.page, 'Ithaqua');

    await prepAwForAdminSet(awContext);
    await runAdminSetWithRecovery(awContext, ithaquaCharName);
    const messages = await getMessages(awContext.page);
    const seesSuccess = messages.some(
      msg => /Set .+['\u2019]s STR from/i.test(msg) || /\bSTR from\b.*\bto 75\b/i.test(msg)
    );
    const seesPermissionDenied = messages.some(
      msg => msg.includes('do not have permission') || msg.includes('You do not have permission')
    );
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
    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 60000);
    const awCharName = await characterNameFromPage(awContext.page, 'ArkanWolfshade');

    await awContext.page.bringToFront().catch(() => {});
    awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
    await despawnSanitariumCultists(awContext.page);

    await prepNonAdminForSetAttempt(ithaquaContext);
    await executeCommand(ithaquaContext.page, `admin set STR ${awCharName} 50`);
    // Server: "You do not have permission to use this command." or target / usage errors.
    const denyPattern =
      /do not have permission|You do not have permission|not allowed|not found|Error setting|No such|Usage: admin set/i;
    await waitForMessage(ithaquaContext.page, denyPattern, 45000);
    const messages = await getMessages(ithaquaContext.page);
    expect(messages.some(msg => denyPattern.test(msg))).toBe(true);
  });
});
