/**
 * One logged-in ArkanWolfshade + Ithaqua pair per Playwright worker, shared by every spec whose
 * top-level describe has `{ tag: '@shared-session' }` (a literal: playwright/valid-test-tags), instead of each spec file logging both players in (beforeAll) and out
 * (afterAll). That per-file login/logout was ~13 of ~39 minutes of the runtime suite.
 *
 * Opt in only specs that keep the session alive: no logout, /quit, /rest, deliberate disconnects,
 * context closes, or createMultiPlayerContexts outside beforeAll. Untagged specs run in the
 * `isolated` project (playwright.runtime.config.ts). A different project gets a different worker,
 * so the shared pair is logged out before any isolated spec logs the same accounts in. Playwright
 * also restarts the worker after a failed test, which rebuilds the pair from scratch.
 */

import { test as base, type Browser, type Page } from '@playwright/test';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureFreshMultiPlayerContexts,
  waitForAllPlayersInGame,
  type PlayerContext,
} from './multiplayer';
import { waitUntil } from './player';

const SHARED_PLAYERS = ['ArkanWolfshade', 'Ithaqua'];

export const test = base.extend<object, { sharedPlayers: PlayerContext[] }>({
  sharedPlayers: [
    async ({ browser }, use) => {
      const contexts = await createMultiPlayerContexts(browser, SHARED_PLAYERS);
      await waitForAllPlayersInGame(contexts, 60000);
      await use(contexts);
      await cleanupMultiPlayerContexts(contexts);
    },
    { scope: 'worker', timeout: 180_000 },
  ],
});

export { expect } from '@playwright/test';

/** Empty Game Info / Chat (one message store), as a fresh login would leave it. Best-effort: ticks keep arriving. */
async function clearMessageLog(page: Page): Promise<void> {
  await page
    .getByRole('button', { name: 'Clear Log' })
    .evaluate((el: HTMLElement) => {
      el.click();
    })
    .catch(() => {});
  const messages = page.locator('[data-message-text]');
  await waitUntil(async () => (await messages.count()) <= 1, 3000);
}

/**
 * beforeAll replacement for `createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua'])`:
 * recover the shared pair if a previous spec left it disconnected, and clear the message log so
 * this spec's message assertions cannot match an earlier spec's lines.
 */
export async function adoptSharedPlayers(browser: Browser, shared: PlayerContext[]): Promise<PlayerContext[]> {
  const contexts = await ensureFreshMultiPlayerContexts(browser, shared, SHARED_PLAYERS);
  for (const ctx of contexts) {
    await clearMessageLog(ctx.page);
  }
  return contexts;
}
