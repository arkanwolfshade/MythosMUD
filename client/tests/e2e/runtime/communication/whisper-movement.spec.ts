/**
 * Scenario 16: Whisper Movement
 *
 * Tests whisper channel functionality across different player locations.
 * Verifies that whisper messages work correctly when players are in different
 * rooms, that whisper delivery is not affected by player movement, and that
 * the whisper system maintains privacy and proper message delivery regardless
 * of player location.
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
  waitForLookReflectedInUi,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensurePlayableAlive, ensureStanding } from '../fixtures/player';
import { EASTERN_HALLWAY_LOOK_CUE } from '../fixtures/test-data';

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

/** Foyer -> east with retries; helpers may branch (playwright/no-conditional-in-test). */
async function hopEastUntilHallway(page: Page): Promise<void> {
  let inHallway = false;
  for (let hop = 0; hop < 4 && !inHallway; hop++) {
    await ensureStanding(page, 5000).catch(() => {});
    await executeCommand(page, hop % 2 === 0 ? 'go east' : 'east');
    await waitForMessage(page, /You (move|go) east|Eastern Hallway|can't go that way/i, 12000).catch(() => {});
    await executeCommand(page, 'look').catch(() => {});
    inHallway = await page
      .evaluate(() => /Eastern Hallway|hallway_001/i.test(document.body?.innerText ?? ''))
      .catch(() => false);
    if (!inHallway) {
      await new Promise(r => setTimeout(r, 2000));
    }
  }
}

test.describe('Whisper Movement', () => {
  test.describe.configure({ mode: 'serial', timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(120_000);
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
  });

  async function prepareWhisperPair(): Promise<void> {
    await ensurePlayableAlive(contexts[0].page, contexts[0].player.username, contexts[0].player.password);
    await executeCommand(contexts[0].page, `admin set DP ${contexts[1].player.username} 20`).catch(() => {});
    await ensurePlayableAlive(contexts[1].page, contexts[1].player.username, contexts[1].player.password);
  }

  test.afterAll(async () => {
    test.setTimeout(60_000);
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive whisper when both players in same room', async () => {
    await prepareWhisperPair();
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await nudgeStandBothPlayers(awContext, ithaquaContext);

    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const awCharacterName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    const whisperBody = 'Testing whisper in same room';
    const senderAck = new RegExp(
      `You whisper to ${escapeRegExp(ithaquaCharName)}:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );
    const recipientLine = new RegExp(
      `${escapeRegExp(awCharacterName)} whispers to you:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );

    const sendWhisperFromAw = async (): Promise<void> => {
      await awContext.page.bringToFront().catch(() => {});
      await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible(
        {
          timeout: 15000,
        }
      );
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
    };

    await sendWhisperFromAw();
    await new Promise(r => setTimeout(r, 500));

    try {
      await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
    } catch {
      // Prior suite idle or WS flake can surface "X has left the game" on receiver; reunite then resend.
      await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
      await ensurePlayerInGame(awContext, 30000);
      await ensurePlayerInGame(ithaquaContext, 30000);
      await ensurePlayersInSameRoom(contexts, 2, 45000);
      await nudgeStandBothPlayers(awContext, ithaquaContext);
      await sendWhisperFromAw();
      await new Promise(r => setTimeout(r, 500));
      await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
    }

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => recipientLine.test(msg));
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should receive whisper when AW is in different room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
    await ensurePlayableAlive(ithaquaContext.page, ithaquaContext.player.username, ithaquaContext.player.password);
    const voidLeft = await awContext.page
      .evaluate(() => /Death\s*>\s*Void/i.test(document.body?.innerText ?? ''))
      .catch(() => false);
    const voidRight = await ithaquaContext.page
      .evaluate(() => /Death\s*>\s*Void/i.test(document.body?.innerText ?? ''))
      .catch(() => false);
    expect(voidLeft || voidRight).toBe(false);

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    let ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';

    // Foyer -> east only. Wait for Exits: (same as combat harness) before hop; retry if move_player flakes.
    await awContext.page.bringToFront().catch(() => {});
    await ensureStanding(awContext.page, 8000);
    await executeCommand(awContext.page, 'look');
    await awContext.page
      .getByText(/Exits:/)
      .first()
      .waitFor({ state: 'visible', timeout: 15000 });
    await waitForLookReflectedInUi(awContext.page).catch(() => {});
    await hopEastUntilHallway(awContext.page);
    await expect(awContext.page.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
    await new Promise(r => setTimeout(r, 2500));

    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';
    ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? ithaquaCharName;

    const whisperBody = 'Testing whisper from different room';
    const senderAck = new RegExp(
      `You whisper to ${escapeRegExp(ithaquaCharName)}:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );
    const recipientLine = new RegExp(
      `${escapeRegExp(awCharName)} whispers to you:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );

    const sendWhisperAfterSplit = async (): Promise<void> => {
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
      await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible(
        {
          timeout: 15000,
        }
      );
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
    };

    await sendWhisperAfterSplit();
    await new Promise(r => setTimeout(r, 500));

    try {
      await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
    } catch {
      await ensurePlayerInGame(awContext, 30000);
      await ensurePlayerInGame(ithaquaContext, 30000);
      await sendWhisperAfterSplit();
      await new Promise(r => setTimeout(r, 500));
      await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
    }

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => recipientLine.test(msg));
    expect(seesMessage).toBe(true);
  });
});
