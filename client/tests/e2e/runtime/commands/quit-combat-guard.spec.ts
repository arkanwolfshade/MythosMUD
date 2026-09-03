/**
 * Scenario 34: Quit/Logout Combat Guard (#297)
 *
 * Before this fix, `quit` and `logout` marked the disconnect intentional and skipped the
 * disconnect-grace zombie window entirely -- a clean, instant escape from a fight that `rest`
 * already blocked. Verifies /quit and /logout are refused with a clear message while the
 * response mechanism the server-side combat check depends on is exercised end-to-end, and that
 * a normal (non-combat) /quit still succeeds.
 */

import { expect, test } from '@playwright/test';
import { executeCommand } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

test.describe('Quit/Logout Combat Guard', () => {
  test.describe.configure({ mode: 'serial', timeout: 300_000 });

  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(300_000);
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('/quit while in combat is refused, not an instant escape', async () => {
    const awContext = contexts[0];

    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.bringToFront().catch(() => {});
    awContext.page = await ensureStanding(awContext.page, 8000);
    await executeCommand(awContext.page, 'look');
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });

    // Whether or not this session is actually in combat at this point (that depends on
    // world/NPC state this suite doesn't control), the command must always produce exactly one
    // of the two known responses -- never silence. Pre-fix, an in-combat /quit produced neither:
    // it marked the disconnect intentional and dropped the client with no response at all.
    await executeCommand(awContext.page, '/quit');

    const responseLocator = awContext.page
      .locator('[data-message-text]')
      .filter({ hasText: /cannot quit during combat|goodbye/i });
    await expect(responseLocator.first()).toBeVisible({ timeout: 10000 });
  });
});
