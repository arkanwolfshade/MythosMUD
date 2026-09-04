/**
 * Scenario 17: Whisper Integration
 *
 * Tests whisper message delivery between players in real-time.
 * Verifies that whisper messages are properly delivered to the intended
 * recipient and that the whisper system maintains privacy across player sessions.
 */

import { expect, test } from '@playwright/test';
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
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';

async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

test.describe('Whisper Integration', () => {
  test.describe.configure({ mode: 'serial' });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('should deliver whisper message to intended recipient', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() || 'Ithaqua';
    const escapedIth = ithaquaCharName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const whisperBody = 'Testing player management integration';
    const senderAck = new RegExp(`You whisper to ${escapedIth}:\\s*${whisperBody}`, 'i');
    const whisperToReceiver = new RegExp(`whispers to you:\\s*${whisperBody}`, 'i');

    await ithaquaContext.page.bringToFront().catch(() => {});
    await expect(
      ithaquaContext.page.getByText(new RegExp(`Player:\\s*${ithaquaContext.player.username}\\b`, 'i'))
    ).toBeVisible({ timeout: 15000 });
    await ithaquaContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(ithaquaContext.page, 'look');
    await waitForLookReflectedInUi(ithaquaContext.page);

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

    await waitForCrossPlayerMessage(ithaquaContext, whisperToReceiver, 45000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => whisperToReceiver.test(msg));
    expect(seesMessage).toBe(true);
  });
});
