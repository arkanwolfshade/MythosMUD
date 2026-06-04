/**
 * Scenario 13: Whisper Basic
 *
 * Tests basic whisper channel functionality for private messaging between players.
 * Verifies that players can send and receive whisper messages, that messages
 * are properly delivered to the intended recipient, and that the whisper system
 * works correctly for private multiplayer communication.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { ensureE2eRuntimeReady } from '../fixtures/e2e-runtime-ready';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';

/** Both browsers healthy before whisper; room co-location is not required for /whisper delivery. */
async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

/** Whisper is not room-scoped; avoid ensureMultiplayerCoLocate Occupants(2) gates that burn multi-minute budgets. */
async function waitForPlayableUi(contexts: PlayerContext[]): Promise<void> {
  await Promise.all(
    contexts.map(({ page }) =>
      page
        .waitForFunction(
          () => !(document.body?.innerText ?? '').includes('You are disconnected and cannot perform actions'),
          { timeout: 20000 }
        )
        .catch(() => {})
    )
  );
}

test.describe('Whisper Basic', () => {
  test.describe.configure({ mode: 'serial' });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    await ensureE2eRuntimeReady(contexts, 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive AW whisper message', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await waitForPlayableUi(contexts);
    await nudgeStandBothPlayers(awContext, ithaquaContext);
    // Best-effort: linkdead clients may omit command_response on [data-message-text]; `look` below still primes UI.
    await awContext.page
      .locator('[data-message-text]')
      .first()
      .waitFor({ state: 'visible', timeout: 15000 })
      .catch(() => {});
    await new Promise(r => setTimeout(r, 1500));

    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() || 'Ithaqua';
    const escapedIth = ithaquaCharName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const whisperBody = 'Hello, this is a private message';
    const senderAck = new RegExp(`You whisper to ${escapedIth}:\\s*${whisperBody}`, 'i');

    await awContext.page.bringToFront().catch(() => {});
    await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForLookReflectedInUi(awContext.page);

    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, `whisper ${ithaquaCharName} ${whisperBody}`);

    try {
      await waitForMessage(awContext.page, senderAck, 45000);
    } catch {
      await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
        el.focus();
      });
      await executeCommand(awContext.page, `whisper ${ithaquaCharName} ${whisperBody}`);
      await waitForMessage(awContext.page, senderAck, 45000);
    }

    // Verify Ithaqua receives the whisper (match by content; sender display name is character name, not account)
    const whisperToReceiver = /whispers to you: Hello, this is a private message/;
    await waitForCrossPlayerMessage(ithaquaContext, whisperToReceiver, 45000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesWhisper = ithaquaMessages.some(msg => whisperToReceiver.test(msg));
    expect(seesWhisper).toBe(true);
  });

  test('AW should receive Ithaqua whisper reply', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await waitForPlayableUi(contexts);
    await nudgeStandBothPlayers(awContext, ithaquaContext);
    await ithaquaContext.page
      .locator('[data-message-text]')
      .first()
      .waitFor({ state: 'visible', timeout: 15000 })
      .catch(() => {});
    await new Promise(r => setTimeout(r, 1500));

    // Server resolves whisper target by character name, not account username. Use AW's
    // current character name so the whisper is delivered to the correct client.
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const awCharacterName = await awContext.page.getByTestId('current-character-name').textContent();
    const targetName = (awCharacterName ?? '').trim() || 'ArkanWolfshade';

    // Receiver test 1 can leave Ithaqua linkdead; prime both pipelines before sender whisper.
    await awContext.page.bringToFront().catch(() => {});
    await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible({
      timeout: 15000,
    });
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForLookReflectedInUi(awContext.page);
    await new Promise(r => setTimeout(r, 1500));

    await ithaquaContext.page.bringToFront().catch(() => {});
    await expect(
      ithaquaContext.page.getByText(new RegExp(`Player:\\s*${ithaquaContext.player.username}\\b`, 'i'))
    ).toBeVisible({ timeout: 15000 });
    await ithaquaContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(ithaquaContext.page, 'look');
    await waitForLookReflectedInUi(ithaquaContext.page);

    const replyBody = 'Hello back to you';
    const escapedTarget = targetName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const senderAck = new RegExp(`You whisper to ${escapedTarget}:\\s*${replyBody}`, 'i');

    await ithaquaContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(ithaquaContext.page, `whisper ${targetName} ${replyBody}`);

    try {
      await waitForMessage(ithaquaContext.page, senderAck, 45000);
    } catch {
      await nudgeStandBothPlayers(awContext, ithaquaContext);
      await ensurePlayerInGame(ithaquaContext, 30000);
      await ithaquaContext.page.bringToFront().catch(() => {});
      await ithaquaContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
        el.focus();
      });
      await executeCommand(ithaquaContext.page, 'look');
      await waitForLookReflectedInUi(ithaquaContext.page);
      await ithaquaContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
        el.focus();
      });
      await executeCommand(ithaquaContext.page, `whisper ${targetName} ${replyBody}`);
      await waitForMessage(ithaquaContext.page, senderAck, 45000);
    }

    // Verify AW receives the whisper (match by content; sender display name is character name, not account)
    const whisperToAw = /whispers to you: Hello back to you/;
    await waitForCrossPlayerMessage(awContext, whisperToAw, 45000);
    const awMessages = await getPlayerMessages(awContext);
    const seesWhisper = awMessages.some(msg => whisperToAw.test(msg));
    expect(seesWhisper).toBe(true);
  });
});
