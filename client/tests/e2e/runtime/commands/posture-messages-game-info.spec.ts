/**
 * Issue #395: Posture change lines appear in Game Info (holistic contract).
 *
 * Covers server-initiated posture (admin set DP) for self and room observers,
 * plus voluntary /sit third-person room broadcast.
 */

import { expect, test } from '@playwright/test';
import { executeCommand } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureFreshMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureMultiplayerCoLocated } from '../fixtures/multiplayer-colocated';
import { despawnSanitariumCultists, ensurePlayableAlive } from '../fixtures/player';

const LYING_SELF = /You stretch out and lie down/i;
const SITTING_SELF = /You settle into a seated position/i;
const SITTING_ROOM = /settles into a seated position/i;
const LYING_ROOM = /stretches out and lies prone upon the floor/i;
const ADMIN_DP_SET = /Set .+['\u2019]s DP from|DP from \d+ to 0/i;

async function characterNameFromPage(ctx: PlayerContext): Promise<string> {
  await ctx.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
  return (await ctx.page.getByTestId('current-character-name').textContent())?.trim() ?? ctx.player.username;
}

async function prepCoLocatedContexts(
  browser: Parameters<typeof createMultiPlayerContexts>[0],
  contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>
): Promise<[PlayerContext, PlayerContext]> {
  const fresh = await ensureFreshMultiPlayerContexts(browser, contexts, ['ArkanWolfshade', 'Ithaqua']);
  await waitForAllPlayersInGame(fresh);
  await ensureMultiplayerCoLocated(fresh, { timeoutMs: 90000, coLocateTimeoutMs: 60000 });
  const aw = fresh[0];
  const target = fresh[1];
  for (const ctx of [aw, target]) {
    await ctx.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ctx, 30000);
    ctx.page = await ensurePlayableAlive(ctx.page, ctx.player.username, ctx.player.password);
    await despawnSanitariumCultists(ctx.page);
    ctx.page = await ensurePlayableAlive(ctx.page, ctx.player.username, ctx.player.password);
    await executeCommand(ctx.page, 'stand');
    await executeCommand(ctx.page, 'look');
  }
  return [aw, target];
}

test.describe('Posture messages in Game Info (#395)', () => {
  test.describe.configure({ timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('target sees lying line when admin sets DP to 0 (server-initiated self)', async ({ browser }) => {
    test.setTimeout(300_000);
    const [aw, target] = await prepCoLocatedContexts(browser, contexts);
    const targetCharName = await characterNameFromPage(target);

    await aw.page.bringToFront();
    await executeCommand(aw.page, `admin set DP ${targetCharName} 0`);
    await expect(aw.page.locator('[data-message-text]').filter({ hasText: ADMIN_DP_SET }).first()).toBeVisible({
      timeout: 45000,
    });

    await target.page.bringToFront();
    await expect(target.page.locator('[data-message-text]').filter({ hasText: LYING_SELF }).first()).toBeVisible({
      timeout: 45000,
    });

    await executeCommand(aw.page, `admin set DP ${targetCharName} 20`);
  });

  test('observer sees third-person sit line when co-player uses /sit', async ({ browser }) => {
    test.setTimeout(300_000);
    const [aw, target] = await prepCoLocatedContexts(browser, contexts);

    await target.page.bringToFront();
    await executeCommand(target.page, 'sit');
    await expect(target.page.locator('[data-message-text]').filter({ hasText: SITTING_SELF }).first()).toBeVisible({
      timeout: 30000,
    });

    await aw.page.bringToFront();
    await expect(aw.page.locator('[data-message-text]').filter({ hasText: SITTING_ROOM }).first()).toBeVisible({
      timeout: 45000,
    });

    await target.page.bringToFront();
    await executeCommand(target.page, 'stand');
  });

  test('observer sees third-person lying line when admin sets co-player DP to 0', async ({ browser }) => {
    test.setTimeout(300_000);
    const [aw, target] = await prepCoLocatedContexts(browser, contexts);
    const targetCharName = await characterNameFromPage(target);

    await aw.page.bringToFront();
    await executeCommand(aw.page, `admin set DP ${targetCharName} 0`);
    await expect(aw.page.locator('[data-message-text]').filter({ hasText: LYING_ROOM }).first()).toBeVisible({
      timeout: 45000,
    });

    await executeCommand(aw.page, `admin set DP ${targetCharName} 20`);
  });
});
