/**
 * Scenario 9: Local Channel Isolation
 *
 * Tests local channel isolation between different sub-zones.
 * Verifies that local channel messages are properly isolated to their
 * respective sub-zones, that players in different sub-zones cannot see
 * each other's local messages, and that the sub-zone routing system
 * works correctly for local communication.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';
import { EASTERN_HALLWAY_LOOK_CUE } from '../fixtures/test-data';

async function returnAwToFoyerIfInHallway(aw: PlayerContext, contexts: PlayerContext[]): Promise<void> {
  const awAlreadyHallway = await aw.page
    .evaluate(() => /Eastern Hallway/i.test(document.body?.innerText ?? ''))
    .catch(() => false);
  if (!awAlreadyHallway) {
    return;
  }
  await executeCommand(aw.page, 'go west');
  await waitForMessage(aw.page, /You (move|go) west|Main Foyer/i, 15000).catch(() => {});
  await new Promise(r => setTimeout(r, 1000));
  await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 30000 });
}

/** `look` may land in Location/Room panels or Game Info — accept Eastern Hallway cues. */
async function waitForLookReflected(page: Page): Promise<void> {
  await page.waitForFunction(
    () => {
      const body = document.body?.innerText ?? '';
      if (/Eastern Hallway|hallway, branching|first section of the eastern hallway/i.test(body)) {
        return true;
      }
      return Array.from(document.querySelectorAll('[data-message-text]')).some(el => {
        const v = (el.getAttribute('data-message-text') || '').trim();
        return /Eastern Hallway|hallway, branching|You see/i.test(v);
      });
    },
    undefined,
    { timeout: 45000 }
  );
}

/** Bilateral game UI + look before teleport/occupant sync (linkdead / stale Occupants (1)). */
async function primeBothForCoLocate(contexts: PlayerContext[]): Promise<void> {
  if (contexts.length < 2) return;
  await Promise.all([ensurePlayerInGame(contexts[0], 30000), ensurePlayerInGame(contexts[1], 30000)]);
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await ctx.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(ctx.page, 'look');
    await waitForLookReflected(ctx.page).catch(() => {});
  }
}

/** Park Ithaqua in Main Foyer so AW's east hop creates a real local-scope split. */
async function ensureIthaquaInFoyer(ithaqua: PlayerContext): Promise<void> {
  await ithaqua.page.bringToFront().catch(() => {});
  await ensureStanding(ithaqua.page, 5000).catch(() => {});
  await executeCommand(ithaqua.page, 'look').catch(() => {});
  const inHallway = await ithaqua.page
    .evaluate(() => /Eastern Hallway/i.test(document.body?.innerText ?? ''))
    .catch(() => false);
  if (inHallway) {
    await executeCommand(ithaqua.page, 'go west').catch(() => {});
    await waitForMessage(ithaqua.page, /You (move|go) west|Main Foyer/i, 15000).catch(() => {});
  }
  await executeCommand(ithaqua.page, 'look').catch(() => {});
  await expect(ithaqua.page.getByText(/Main Foyer/i).first()).toBeVisible({ timeout: 20000 });
}

test.describe('Local Channel Isolation', () => {
  test.describe.configure({ mode: 'serial', timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  // Keep beforeAll light — heavy co-locate belongs in tests (default hook timeout is 30s).
  test.beforeAll(async ({ browser }) => {
    test.setTimeout(120_000);
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
  });

  test.afterAll(async () => {
    test.setTimeout(60_000);
    await cleanupMultiPlayerContexts(contexts);
  });

  async function prepareLocalIsolationPair(): Promise<void> {
    const [awContext, ithaquaContext] = contexts;
    // Match whisper prepare: co-locate only. Avoid sync DB reset + SPA re-login (blocks the worker / poisons pair).
    await ensureStanding(awContext.page, 8000).catch(() => {});
    await ensureStanding(ithaquaContext.page, 8000).catch(() => {});
    await executeCommand(awContext.page, `admin set DP ${awContext.player.username} 20`).catch(() => {});
    await executeCommand(awContext.page, `admin set DP ${ithaquaContext.player.username} 20`).catch(() => {});
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade').catch(() => {});
    await executeCommand(awContext.page, 'unmute Ithaqua').catch(() => {});
  }

  test('Ithaqua should see local message when both players in same sub-zone', async () => {
    test.setTimeout(300_000);
    await prepareLocalIsolationPair();
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    // Ensure receiver (Ithaqua) is not muting sender (AW); match chat-messages (no mandatory ".").
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        20000
      );
    } catch {
      // Already unmuted or command_response did not land while linkdead; proceed.
    }
    await new Promise(r => setTimeout(r, 500));

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForLookReflected(awContext.page);
    await new Promise(r => setTimeout(r, 1000));

    await executeCommand(awContext.page, 'local Testing same sub-zone communication');
    await waitForMessage(awContext.page, /You say locally:.*Testing same sub-zone communication/i, 45000);

    await waitForCrossPlayerMessage(
      ithaquaContext,
      /ArkanWolfshade \(local\): Testing same sub-zone communication/i,
      45000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing same sub-zone communication')
    );
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message when AW is in different sub-zone', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Prior test can leave hallway; reunite in foyer then split (avoid ensurePlayableAlive pair poison).
    await returnAwToFoyerIfInHallway(awContext, contexts);
    await ensureIthaquaInFoyer(ithaquaContext).catch(() => {});
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1000));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Persist can leave AW in hallway; return to foyer so east is a real room change.
    await ensureStanding(awContext.page, 5000);
    await returnAwToFoyerIfInHallway(awContext, contexts);

    // Keep Ithaqua in foyer; only AW walks east (co-locate can leave both mid-hallway).
    await ensureIthaquaInFoyer(ithaquaContext);

    // Foyer east -> Eastern Hallway (server copy is "You go east.", not "You move east").
    await awContext.page.bringToFront().catch(() => {});
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You (move|go) east|Eastern Hallway/i, 20000).catch(() => {});
    await new Promise(r => setTimeout(r, 2000));

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1000));

    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    try {
      await waitForLookReflected(awContext.page);
    } catch {
      // Fall through to hallway assertion below.
    }
    // Hard proof of room split — bare Exits: matches foyer too and caused false isolation failures.
    await expect(awContext.page.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
    await ensureIthaquaInFoyer(ithaquaContext);

    // AW sends local message from different room; Ithaqua stays put.
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'local Testing different sub-zone isolation');

    await waitForMessage(awContext.page, /You say locally:.*Testing different sub-zone isolation/i, 45000);

    await new Promise(r => setTimeout(r, 3000));

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing different sub-zone isolation')
    );
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW returns to same sub-zone', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Prior tests can leave Ithaqua out of the world or linkdead; restore before movement/unmute.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Try to move AW back toward Ithaqua (layout varies: Arena vs foyer/hallway names).
    await ensureStanding(awContext.page, 5000);
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'go west');
    await waitForMessage(awContext.page, /You move west|Main Foyer|Arena/i, 15000).catch(() => {});
    await new Promise(r => setTimeout(r, 2000));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    // go west is best-effort; Ithaqua can remain at Occupants (1) with linkdead until teleport reunites.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await new Promise(r => setTimeout(r, 2000));

    await ithaquaContext.page.bringToFront().catch(() => {});

    // Ensure receiver (Ithaqua) is not muting AW; match chat-messages unmute pattern.
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        20000
      );
    } catch {
      // Already unmuted or no log line; proceed.
    }
    await new Promise(r => setTimeout(r, 500));

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForLookReflected(awContext.page);
    await new Promise(r => setTimeout(r, 1000));

    await executeCommand(awContext.page, 'local Testing same sub-zone after return');

    await waitForMessage(awContext.page, /You say locally:.*Testing same sub-zone after return/i, 45000);

    await waitForCrossPlayerMessage(
      ithaquaContext,
      /ArkanWolfshade \(local\): Testing same sub-zone after return/i,
      45000
    );
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.includes('ArkanWolfshade (local): Testing same sub-zone after return')
    );
    expect(seesMessage).toBe(true);
  });
});
