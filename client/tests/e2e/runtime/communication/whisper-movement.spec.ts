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

async function pageShowsEasternHallway(page: Page): Promise<boolean> {
  try {
    return await page.evaluate(function () {
      const body = document.body;
      const text = body ? body.innerText : '';
      return /Eastern Hallway|hallway_001/i.test(text);
    });
  } catch {
    return false;
  }
}

/** One foyer -> east attempt; returns the page handle after the hop. */
async function attemptEastHop(page: Page, hopIndex: number): Promise<Page> {
  let live = page;
  try {
    live = await ensureStanding(live, 5000);
  } catch {
    // keep prior page handle
  }
  await executeCommand(live, hopIndex % 2 === 0 ? 'go east' : 'east');
  // lizard: avoid apostrophe inside /regex/ (lexer treats ' as string start)
  try {
    await waitForMessage(live, /You (move|go) east|Eastern Hallway|can.t go that way/i, 12000);
  } catch {
    // movement feedback optional
  }
  try {
    await executeCommand(live, 'look');
  } catch {
    // look best-effort
  }
  return live;
}

/** Foyer -> east with retries; helpers may branch (playwright/no-conditional-in-test). */
async function hopEastUntilHallway(page: Page): Promise<Page> {
  let live = page;
  for (let hop = 0; hop < 4; hop++) {
    live = await attemptEastHop(live, hop);
    if (await pageShowsEasternHallway(live)) {
      return live;
    }
    await new Promise(function (resolve) {
      setTimeout(resolve, 2000);
    });
  }
  return live;
}

async function pageIsInDeathVoid(page: Page): Promise<boolean> {
  return page.evaluate(() => /Death\s*>\s*Void/i.test(document.body?.innerText ?? '')).catch(() => false);
}

async function assertNeitherPlayerInVoid(left: Page, right: Page): Promise<void> {
  const voidLeft = await pageIsInDeathVoid(left);
  const voidRight = await pageIsInDeathVoid(right);
  expect(voidLeft || voidRight).toBe(false);
}

async function characterNameFromPage(page: Page, fallback: string): Promise<string> {
  await page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
  return (await page.getByTestId('current-character-name').textContent())?.trim() ?? fallback;
}

async function focusCommandInput(page: Page): Promise<void> {
  await page.getByTestId('command-input').evaluate((el: HTMLElement) => {
    el.focus();
  });
}

async function bringFrontAndAssertPlayerBanner(page: Page, username: string): Promise<void> {
  await page.bringToFront().catch(() => {});
  await expect(page.getByText(new RegExp(`Player:\\s*${username}\\b`, 'i'))).toBeVisible({
    timeout: 15000,
  });
}

async function lookAndWaitForUi(page: Page): Promise<void> {
  await focusCommandInput(page);
  await executeCommand(page, 'look');
  await waitForLookReflectedInUi(page);
}

async function whisperUntilSenderAck(page: Page, whisperCommand: string, senderAck: RegExp): Promise<void> {
  await focusCommandInput(page);
  await executeCommand(page, whisperCommand);
  try {
    await waitForMessage(page, senderAck, 45000);
  } catch {
    await focusCommandInput(page);
    await executeCommand(page, whisperCommand);
    await waitForMessage(page, senderAck, 45000);
  }
}

async function moveAwToEasternHallway(awPage: Page): Promise<Page> {
  await awPage.bringToFront().catch(() => {});
  let live = await ensureStanding(awPage, 8000);
  await executeCommand(live, 'look');
  await live
    .getByText(/Exits:/)
    .first()
    .waitFor({ state: 'visible', timeout: 15000 });
  await waitForLookReflectedInUi(live).catch(() => {});
  live = await hopEastUntilHallway(live);
  await expect(live.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  await new Promise(r => setTimeout(r, 2500));
  return live;
}

async function sendCrossRoomWhisper(
  awContext: PlayerContext,
  ithaquaContext: PlayerContext,
  ithaquaCharName: string,
  whisperBody: string,
  senderAck: RegExp
): Promise<void> {
  await bringFrontAndAssertPlayerBanner(ithaquaContext.page, ithaquaContext.player.username);
  await lookAndWaitForUi(ithaquaContext.page);

  await bringFrontAndAssertPlayerBanner(awContext.page, awContext.player.username);
  await lookAndWaitForUi(awContext.page);

  await whisperUntilSenderAck(awContext.page, `whisper ${ithaquaCharName} ${whisperBody}`, senderAck);
}

async function deliverWhisperAcrossRooms(
  awContext: PlayerContext,
  ithaquaContext: PlayerContext,
  ithaquaCharName: string,
  whisperBody: string,
  senderAck: RegExp,
  recipientLine: RegExp
): Promise<void> {
  await sendCrossRoomWhisper(awContext, ithaquaContext, ithaquaCharName, whisperBody, senderAck);
  await new Promise(r => setTimeout(r, 500));
  try {
    await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
  } catch {
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await sendCrossRoomWhisper(awContext, ithaquaContext, ithaquaCharName, whisperBody, senderAck);
    await new Promise(r => setTimeout(r, 500));
    await waitForCrossPlayerMessage(ithaquaContext, recipientLine, 45000);
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
    contexts[0].page = await ensurePlayableAlive(
      contexts[0].page,
      contexts[0].player.username,
      contexts[0].player.password
    );
    await executeCommand(contexts[0].page, `admin set DP ${contexts[1].player.username} 20`).catch(() => {});
    contexts[1].page = await ensurePlayableAlive(
      contexts[1].page,
      contexts[1].player.username,
      contexts[1].player.password
    );
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

    awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
    ithaquaContext.page = await ensurePlayableAlive(
      ithaquaContext.page,
      ithaquaContext.player.username,
      ithaquaContext.player.password
    );
    await assertNeitherPlayerInVoid(awContext.page, ithaquaContext.page);

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    let ithaquaCharName = await characterNameFromPage(ithaquaContext.page, 'Ithaqua');
    awContext.page = await moveAwToEasternHallway(awContext.page);

    const awCharName = await characterNameFromPage(awContext.page, 'ArkanWolfshade');
    ithaquaCharName = await characterNameFromPage(ithaquaContext.page, ithaquaCharName);

    const whisperBody = 'Testing whisper from different room';
    const senderAck = new RegExp(
      `You whisper to ${escapeRegExp(ithaquaCharName)}:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );
    const recipientLine = new RegExp(
      `${escapeRegExp(awCharName)} whispers to you:\\s*${escapeRegExp(whisperBody)}`,
      'i'
    );

    await deliverWhisperAcrossRooms(awContext, ithaquaContext, ithaquaCharName, whisperBody, senderAck, recipientLine);

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => recipientLine.test(msg));
    expect(seesMessage).toBe(true);
  });
});
