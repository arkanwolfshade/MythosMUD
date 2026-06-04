/**
 * Scenario 8: Local Channel Basic
 *
 * Tests basic local channel communication functionality.
 * Verifies that players can send and receive local channel messages,
 * that messages are properly broadcast to players in the same sub-zone,
 * and that the local channel system works correctly for basic multiplayer communication.
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
  prepareReceiverForInboundMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

/**
 * Occupants can show (linkdead) while the header still says Connected; command_response may not
 * land on [data-message-text] until both sessions recover. Same pattern as chat-messages.spec.ts.
 */
async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

/** Warm both sessions with `look` before teleport co-locate (chat-messages / multiplayer recovery pattern). */
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

/** Server: `You have unmuted {name}.` or `Failed to unmute {name}.` — wait for Game Info pipeline, not Chat-only. */
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

test.describe('Local Channel Basic', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    await ensureE2eRuntimeReady(contexts, 60000);

    // Same-room /local needs a shared cell. Dual "go north" does not guarantee the same grid cell; use
    // teleport + retries like other runtime multiplayer specs (avoids beforeAll stuck at Occupants (1)).
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });

    const [awContext, ithaquaContext] = contexts;
    // Unmute both players to ensure clean state (mute state may persist from previous scenarios)
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

  test('Ithaqua should see AW local channel message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    // Ensure receiver (Ithaqua) is not muting sender (AW) so local message is delivered.
    await executeUnmuteAndWaitForAck(awContext, ithaquaContext, 'ArkanWolfshade');
    await new Promise(r => setTimeout(r, 500));

    // AW sends local channel message
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'local Hello everyone in the sanitarium');

    await prepareReceiverForInboundMessages(ithaquaContext, 20000);

    await Promise.all([
      waitForMessage(awContext.page, 'You say locally: Hello everyone in the sanitarium', 45000),
      waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade \(local\): Hello everyone in the sanitarium/i, 45000),
    ]);

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade (local): hello everyone in the sanitarium')
    );
    expect(seesMessage).toBe(true);
  });

  test('AW should see Ithaqua local channel reply', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    // Prior test can leave linkdead; prime Game Info like chat-messages "AW should see Ithaqua".
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    // Receiver (AW) unmutes sender (Ithaqua); need command_response on AW after occupant recovery.
    await executeUnmuteAndWaitForAck(ithaquaContext, awContext, 'Ithaqua');
    await new Promise(r => setTimeout(r, 500));

    await ensurePlayerInGame(awContext, 20000);
    await ensurePlayerInGame(ithaquaContext, 20000);
    // Unmute / stand can desync occupant labels while header still says Connected; bilateral look heals Step 1.
    await awContext.page.bringToFront().catch(() => {});
    await ensureStanding(awContext.page, 8000);
    await executeCommand(awContext.page, 'look');
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensureStanding(ithaquaContext.page, 8000);
    await executeCommand(ithaquaContext.page, 'look');
    await new Promise(r => setTimeout(r, 2500));
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await new Promise(r => setTimeout(r, 2000));

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    await prepareReceiverForInboundMessages(awContext, 20000);
    await new Promise(r => setTimeout(r, 1500));

    // Ithaqua sends local reply (sender must be focused on some hosts)
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 30000);

    await executeCommand(ithaquaContext.page, 'local Greetings ArkanWolfshade');

    await prepareReceiverForInboundMessages(awContext, 20000);

    await Promise.all([
      waitForMessage(ithaquaContext.page, 'You say locally: Greetings ArkanWolfshade'),
      waitForCrossPlayerMessage(awContext, /Ithaqua \(local\): Greetings ArkanWolfshade/i, 45000),
    ]);

    // Verify AW sees the reply
    const awMessages = await getPlayerMessages(awContext);
    const seesMessage = awMessages.some(msg => msg.toLowerCase().includes('ithaqua (local): greetings arkanwolfshade'));
    expect(seesMessage).toBe(true);
  });
});
