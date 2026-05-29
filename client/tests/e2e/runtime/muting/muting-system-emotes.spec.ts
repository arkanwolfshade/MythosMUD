/**
 * Scenario 4: Muting System and Emotes
 *
 * Tests the muting system and emote functionality across game sessions.
 * Verifies that players can mute and unmute other players, and that muted
 * players' emotes are properly blocked while other communication remains unaffected.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  type PlayerContext,
} from '../fixtures/multiplayer';

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/** Best-effort: command_response does not land on `[data-message-text]` while disconnect banner is up. */
async function waitForDisconnectBannerClear(page: PlayerContext['page']): Promise<void> {
  await page
    .waitForFunction(
      () => !(document.body?.innerText ?? '').includes('You are disconnected and cannot perform actions'),
      { timeout: 20000 }
    )
    .catch(() => {});
}

async function getIthaquaMuteTargetName(ithaquaContext: PlayerContext): Promise<string> {
  await ithaquaContext.page
    .getByTestId('current-character-name')
    .waitFor({ state: 'visible', timeout: 15000 })
    .catch(() => {});
  const raw = await ithaquaContext.page.getByTestId('current-character-name').textContent();
  return (raw ?? '').trim() || 'Ithaqua';
}

test.describe('Muting System and Emotes', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to mute Ithaqua', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await Promise.all([ensurePlayerInGame(awContext, 30000), ensurePlayerInGame(ithaquaContext, 30000)]);

    await awContext.page.bringToFront().catch(() => {});
    await waitForDisconnectBannerClear(awContext.page);
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|Exits:|already standing|rise to your feet/i, 20000).catch(() => {});

    const targetName = await getIthaquaMuteTargetName(ithaquaContext);
    const muteAck = new RegExp(`You have muted\\s+${escapeRegExp(targetName)}\\b`, 'i');

    await awContext.page.bringToFront().catch(() => {});
    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, `mute ${targetName}`);
    await waitForMessage(awContext.page, muteAck, 45000);
    const muteMessages = await getMessages(awContext.page);
    expect(muteMessages.some(msg => muteAck.test(msg))).toBe(true);
  });

  test('AW should not see Ithaqua emote when Ithaqua is muted', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await Promise.all([ensurePlayerInGame(awContext, 30000), ensurePlayerInGame(ithaquaContext, 30000)]);

    await awContext.page.bringToFront().catch(() => {});
    await waitForDisconnectBannerClear(awContext.page);
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|Exits:|already standing/i, 20000).catch(() => {});

    const targetName = await getIthaquaMuteTargetName(ithaquaContext);
    const muteAck = new RegExp(`You have muted\\s+${escapeRegExp(targetName)}\\b`, 'i');

    await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
      el.focus();
    });
    await executeCommand(awContext.page, `mute ${targetName}`);
    await waitForMessage(awContext.page, muteAck, 45000);

    // Ithaqua uses dance emote
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 30000);
    await executeCommand(ithaquaContext.page, 'dance');

    // Wait for Ithaqua's own confirmation
    await waitForMessage(ithaquaContext.page, 'You dance', 10000).catch(() => {
      // Message may succeed even if format differs
    });

    try {
      await expect(awContext.page.locator('[data-message-text]').first()).toBeVisible({ timeout: 5000 });
    } catch {
      // Message may or may not appear
    }

    // Verify AW does NOT see Ithaqua's emote
    const awMessages = await getMessages(awContext.page);
    const seesEmote = awMessages.some(
      msg => msg.includes(targetName) && (msg.includes('dance') || msg.includes('dancing'))
    );
    expect(seesEmote).toBe(false);
  });

  test('AW should be able to unmute Ithaqua', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    const targetName = await getIthaquaMuteTargetName(ithaquaContext);
    const unmuteAck = new RegExp(`You have unmuted\\s+${escapeRegExp(targetName)}\\b`, 'i');

    const attemptUnmute = async (): Promise<void> => {
      await awContext.page.bringToFront().catch(() => {});
      await Promise.all([ensurePlayerInGame(awContext, 30000), ensurePlayerInGame(ithaquaContext, 20000)]);
      await waitForDisconnectBannerClear(awContext.page);
      await executeCommand(awContext.page, 'stand');
      await new Promise(r => setTimeout(r, 1500));
      await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
        el.focus();
      });
      await executeCommand(awContext.page, 'look');
      await waitForMessage(awContext.page, /Arena|Exits:|already standing/i, 20000).catch(() => {});
      await awContext.page.getByTestId('command-input').evaluate((el: HTMLElement) => {
        el.focus();
      });
      await executeCommand(awContext.page, `unmute ${targetName}`);
      await waitForMessage(awContext.page, unmuteAck, 45000);
    };

    try {
      await attemptUnmute();
    } catch {
      await executeCommand(awContext.page, 'stand');
      await ithaquaContext.page.bringToFront().catch(() => {});
      await executeCommand(ithaquaContext.page, 'stand');
      await new Promise(r => setTimeout(r, 3000));
      await ensurePlayerInGame(awContext, 20000);
      await ensurePlayerInGame(ithaquaContext, 20000);
      await attemptUnmute();
    }
    const postUnmuteMessages = await getMessages(awContext.page);
    expect(postUnmuteMessages.some(msg => unmuteAck.test(msg))).toBe(true);
  });
});
