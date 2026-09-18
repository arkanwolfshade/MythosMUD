/**
 * Follow commands and functionality (#864).
 *
 * Tests /follow (player request/accept/decline, NPC immediate attach), /following, and
 * /unfollow end-to-end: command parsing, server round-trip, follow_request/follow_state
 * WebSocket events, the accept/decline modal, and the header's "Following: <name>" indicator.
 * Mirrors ../party/party-commands.spec.ts, follow's closest analogue (request/accept flow,
 * same InviteModal component), plus a single-player NPC case party has no equivalent of.
 */

import { expect, test, type Page } from '@playwright/test';
import { clickWithoutStability, executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';

/** Dr. Francis Morgan: non-aggressive quest_giver spawned in the admin's current room (sanitarium foyer). */
const NPC_SPAWN_ID = 54;
const NPC_ASK_ALIAS = 'morgan';
const NPC_NAME = 'Dr. Francis Morgan';

/** Command responses may not reach `[data-message-text]` while this banner is present. */
async function waitForDisconnectBannerClear(page: Page): Promise<void> {
  await page
    .waitForFunction(
      () => !(document.body?.innerText ?? '').includes('You are disconnected and cannot perform actions'),
      undefined,
      { timeout: 20000 }
    )
    .catch(() => {});
}

async function primeBothForCoLocate(contexts: PlayerContext[]): Promise<void> {
  if (contexts.length < 2) return;
  await Promise.all([ensurePlayerInGame(contexts[0], 30000), ensurePlayerInGame(contexts[1], 30000)]);
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await ctx.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(ctx.page, 'look');
    await waitForLookReflectedInUi(ctx.page).catch(() => {});
  }
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/**
 * The header's "Following: <name>" indicator, scoped to the fixed header bar and away from
 * `[data-message-text]` chat history, which can contain the same substring (e.g. the `following`
 * command's own "You are following: X (npc)" reply) and persists across tests in this file.
 */
function followingIndicator(page: Page, name?: string) {
  const header = page.locator('.fixed.top-0.left-0.right-0.z-50');
  return header.getByText(name ? new RegExp(`Following:\\s*${escapeRegExp(name)}`, 'i') : /Following:/i);
}

/** Find and despawn any live Morgan instance via `npc zone`, so repeated runs start from zero. */
async function despawnMorganInstances(page: Page): Promise<void> {
  await executeCommand(page, 'npc zone arkhamcity/sanitarium');
  await waitForMessage(page, /NPC Zone Statistics/i, 15000).catch(() => {});
  const messages = await getMessages(page);
  const latest = [...messages].reverse().find(m => /NPC Zone Statistics/i.test(m));
  if (!latest) return;
  const ids = new Set<string>();
  for (const match of Array.from(latest.matchAll(/dr\._francis_morgan_[a-z0-9_]+/gi))) {
    ids.add(match[0].replace(/npc$/i, ''));
  }
  for (const id of ids) {
    await executeCommand(page, `npc despawn ${id}`).catch(() => {});
  }
}

test.describe('Follow Commands', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('following with no active follow shows helpful message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];
    // Single-player assertion: do not call ensureMultiplayerCoLocated here (see party-commands.spec.ts).
    await Promise.all([ensurePlayerInGame(awContext, 30000), ensurePlayerInGame(ithaquaContext, 30000)]);

    await awContext.page.bringToFront().catch(() => {});
    await waitForDisconnectBannerClear(awContext.page);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1000));

    await executeCommand(awContext.page, 'following');
    await waitForMessage(awContext.page, /not following anyone/i, 20000);
    const messages = await getMessages(awContext.page);
    expect(messages.some(m => /not following anyone/i.test(m))).toBe(true);
    expect(messages.some(m => /no one is following you/i.test(m))).toBe(true);
  });

  test('following an NPC attaches immediately, no accept step', async () => {
    const awContext = contexts[0];
    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1000));

    await despawnMorganInstances(awContext.page);

    await executeCommand(awContext.page, `npc spawn ${NPC_SPAWN_ID}`);
    await waitForMessage(awContext.page, /NPC spawned successfully|spawned successfully/i, 20000);

    await executeCommand(awContext.page, `follow ${NPC_ASK_ALIAS}`);
    await waitForMessage(awContext.page, new RegExp(`You are now following ${NPC_NAME}`, 'i'), 20000);

    await expect(followingIndicator(awContext.page, NPC_NAME)).toBeVisible({ timeout: 10000 });

    await executeCommand(awContext.page, 'following');
    await waitForMessage(awContext.page, new RegExp(`You are following: ${NPC_NAME} \\(npc\\)`, 'i'), 20000);

    await executeCommand(awContext.page, 'unfollow');
    await waitForMessage(awContext.page, /no longer following anyone/i, 20000);

    await despawnMorganInstances(awContext.page);
  });

  test('AW can request to follow Ithaqua, Ithaqua accepts, AW unfollows', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // beforeAll co-location can decay; bilateral look refreshes room_state before teleport/sync storm.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'follow Ithaqua');
    await waitForMessage(awContext.page, /Follow request sent|Waiting for them to accept/i, 45000);

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ithaquaContext.page.getByText(/wants to follow you/i).waitFor({ state: 'visible', timeout: 30000 });
    await clickWithoutStability(ithaquaContext.page.getByRole('button', { name: /Accept/i }));
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.bringToFront().catch(() => {});
    await waitForMessage(awContext.page, /You are now following Ithaqua/i, 20000);
    await expect(followingIndicator(awContext.page, 'Ithaqua')).toBeVisible({ timeout: 10000 });

    await executeCommand(awContext.page, 'unfollow');
    await waitForMessage(awContext.page, /no longer following anyone/i, 20000);
    await expect(followingIndicator(awContext.page, 'Ithaqua')).toHaveCount(0);

    // #864 Part 1: the followee is now also notified so both clients reflect the ended relationship.
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade is no longer following you/i, 30000);
  });

  test("Ithaqua can decline AW's follow request", async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'follow Ithaqua');
    await waitForMessage(awContext.page, /Follow request sent|Waiting for them to accept/i, 45000);

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ithaquaContext.page.getByText(/wants to follow you/i).waitFor({ state: 'visible', timeout: 30000 });
    await clickWithoutStability(ithaquaContext.page.getByRole('button', { name: /Decline/i }));
    await waitForMessage(ithaquaContext.page, /You declined the follow request/i, 20000);

    await awContext.page.bringToFront().catch(() => {});
    await waitForMessage(awContext.page, /Your follow request was declined/i, 30000);
    await expect(followingIndicator(awContext.page)).toHaveCount(0);
  });
});
