/**
 * Scenario 12: Local Channel Integration
 *
 * Tests local channel message broadcasting and real-time delivery to multiple
 * players in the same sub-zone. Verifies that local messages are properly
 * broadcast to all players in the same sub-zone in real-time.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { ensureE2eRuntimeReady } from '../fixtures/e2e-runtime-ready';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';

async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

/** Warm both sessions before teleport co-locate (local-channel-basic / chat-messages pattern). */
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

/** Server ack in Game Info — same pattern as local-channel-basic (mute filter is per-receiver). */
async function executeUnmuteAndWaitForAck(
  aw: PlayerContext,
  receiver: PlayerContext,
  targetUsername: string
): Promise<void> {
  const ack = new RegExp(`You have unmuted ${targetUsername}|Failed to unmute ${targetUsername}`, 'i');
  const once = async (): Promise<void> => {
    await receiver.page.bringToFront().catch(() => {});
    await expect(receiver.page.getByText(new RegExp(`Player:\\s*${receiver.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await receiver.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await receiver.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(receiver.page, 'look');
    await waitForLookReflectedInUi(receiver.page);
    await receiver.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(receiver.page, `unmute ${targetUsername}`);
    await waitForMessage(receiver.page, ack, 45000);
  };
  try {
    await once();
  } catch {
    await nudgeStandBothPlayers(aw, receiver);
    await ensurePlayerInGame(aw, 20000);
    await ensurePlayerInGame(receiver, 20000);
    await once();
  }
}

test.describe('Local Channel Integration', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    // Ensure each player is fully in game (including tick) with full timeout before shared wait,
    // so the slower client has time to receive the first tick without hitting a 30s cap.
    await Promise.all([ensurePlayerInGame(contexts[0], 60000), ensurePlayerInGame(contexts[1], 60000)]);
    await waitForAllPlayersInGame(contexts, 60000);

    await ensureE2eRuntimeReady(contexts, 60000);

    // Same-room /local needs a shared cell. Dual "go north" races linkdead and split cells; use teleport retries.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });

    const [awContext, ithaquaContext] = contexts;
    // Unmute both players to ensure clean state
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await new Promise(r => setTimeout(r, 1000));
      await new Promise(r => setTimeout(r, 1000));
    } catch {
      // Ignore unmute errors - players may not be muted to begin with
      // This is expected if mute state doesn't persist between test runs
    }
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('should broadcast local message to all players in same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await nudgeStandBothPlayers(awContext, ithaquaContext);
    await executeUnmuteAndWaitForAck(awContext, ithaquaContext, 'ArkanWolfshade');
    await new Promise(r => setTimeout(r, 500));

    await ensurePlayerInGame(ithaquaContext, 20000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    // Sender focused: command_response lands on Game Info reliably on CI (local-channel-basic).
    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'local Testing player management integration');

    await waitForMessage(awContext.page, /You say locally:\s*Testing player management integration/i, 45000);

    await ensurePlayersInSameRoom(contexts, 2, 10000);

    await waitForCrossPlayerMessage(
      ithaquaContext,
      /ArkanWolfshade \(local\): Testing player management integration/i,
      45000
    );

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade (local): testing player management integration')
    );
    expect(seesMessage).toBe(true);
  });
});
