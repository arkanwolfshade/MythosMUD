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

/** `look` may land in Location/Room panels or Game Info — accept either before asserting /local echo. */
async function waitForLookReflected(page: Page): Promise<void> {
  await page.waitForFunction(
    () => {
      const body = document.body?.innerText ?? '';
      if (
        /Arena\s*>|Arena entrance|heart of the gladiator|sand and shadow|Exits:\s*North|Exits: North, South/i.test(body)
      ) {
        return true;
      }
      return Array.from(document.querySelectorAll('[data-message-text]')).some(el => {
        const v = (el.getAttribute('data-message-text') || '').trim();
        return /Arena|gladiator|heart of the|exits|sand|You see/i.test(v);
      });
    },
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

test.describe('Local Channel Isolation', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // Same-room /local needs a shared cell; dual "go north" leaves each client at Occupants (1) on different cells.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });

    const [awContext, ithaquaContext] = contexts;
    // Unmute both so local messages are delivered (mute state may persist from previous scenarios)
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await new Promise(r => setTimeout(r, 1000));
    } catch {
      // Ignore unmute errors - players may not be muted
    }
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see local message when both players in same sub-zone', async () => {
    test.setTimeout(300_000);
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

    // Prior test can leave linkdead / empty log; restore WS health before movement + local send.
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1000));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Use east to move AW to a different room (layout varies; movement message is best-effort).
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You move east|Eastern Hallway|Arena/i, 15000).catch(() => {
      // If movement message format differs, isolation check still uses getPlayerMessages below.
    });
    await new Promise(r => setTimeout(r, 2000));

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1000));

    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    // After movement + stand, re-prime log delivery (same pattern as chat-messages).
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    try {
      await waitForLookReflected(awContext.page);
    } catch {
      // Fall through to unconditional room-line assertion below.
    }
    await expect(awContext.page.getByText(/Arena entrance|heart of the gladiator|Exits:/i).first()).toBeVisible({
      timeout: 20000,
    });

    // AW sends local message from different room; Ithaqua stays put.
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'local Testing different sub-zone isolation');

    await waitForMessage(awContext.page, /You say locally:.*Testing different sub-zone isolation/i, 45000);

    // Wait a bit for message routing
    await new Promise(r => setTimeout(r, 3000));

    // Verify Ithaqua does NOT see the message (different rooms = different local scope)
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
