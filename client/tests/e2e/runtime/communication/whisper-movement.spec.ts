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
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

/** After `look`, room copy is in Location / Room Description, not Game Info `[data-message-text]`. */
async function assertLookVisibleInPanels(page: Page): Promise<void> {
  const cue = page.getByText(
    /Arena\s*>\s*Arena|Arena entrance \(center\)|Eastern|Hallway|Main Foyer|heart of the gladiator|sand and shadow|Exits:\s*(North|East|West|South)/i
  );
  await expect(cue.first()).toBeVisible({ timeout: 45000 });
}

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

test.describe('Whisper Movement', () => {
  test.describe.configure({ mode: 'serial' });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive whisper when both players in same room', async () => {
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
      await awContext.page.getByTestId('command-input').click();
      await executeCommand(awContext.page, 'look');
      await assertLookVisibleInPanels(awContext.page);
      await awContext.page.getByTestId('command-input').click();
      await executeCommand(awContext.page, `whisper ${ithaquaCharName} ${whisperBody}`);
      try {
        await waitForMessage(awContext.page, senderAck, 45000);
      } catch {
        await awContext.page.getByTestId('command-input').click();
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

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 45000, coLocateTimeoutMs: 45000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);

    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    let ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';
    await ensureStanding(awContext.page, 8000);
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, `teleport ${ithaquaCharName}`);
    await new Promise(r => setTimeout(r, 5000));
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await ensureStanding(awContext.page, 8000);
    await executeCommand(awContext.page, 'go south');
    await new Promise(r => setTimeout(r, 2000));
    await executeCommand(awContext.page, 'go west');
    await new Promise(r => setTimeout(r, 2000));
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 2000));
    await ensureStanding(ithaquaContext.page, 8000);
    await executeCommand(ithaquaContext.page, 'go south');
    await new Promise(r => setTimeout(r, 2000));
    await executeCommand(ithaquaContext.page, 'go west');
    await new Promise(r => setTimeout(r, 2000));
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 2500));
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await ensureStanding(awContext.page, 8000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You move east|You go east|Eastern|east/i, 20000);
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
      await ithaquaContext.page.getByTestId('command-input').click();
      await executeCommand(ithaquaContext.page, 'look');
      await assertLookVisibleInPanels(ithaquaContext.page);

      await awContext.page.bringToFront().catch(() => {});
      await expect(awContext.page.getByText(new RegExp(`Player:\\s*${awContext.player.username}\\b`, 'i'))).toBeVisible(
        {
          timeout: 15000,
        }
      );
      await awContext.page.getByTestId('command-input').click();
      await executeCommand(awContext.page, 'look');
      await assertLookVisibleInPanels(awContext.page);

      await awContext.page.getByTestId('command-input').click();
      await executeCommand(awContext.page, `whisper ${ithaquaCharName} ${whisperBody}`);
      try {
        await waitForMessage(awContext.page, senderAck, 45000);
      } catch {
        await awContext.page.getByTestId('command-input').click();
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
