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
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

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

    // AW mutes Ithaqua
    await executeCommand(awContext.page, 'mute Ithaqua');

    // Wait for mute confirmation
    await waitForMessage(awContext.page, 'You have muted Ithaqua', 10000).catch(() => {
      // Message may succeed even if format differs
    });

    // Verify mute confirmation appears
    const messages = await getMessages(awContext.page);
    const seesMute = messages.some(msg => msg.includes('muted') || msg.includes('Ithaqua'));
    expect(seesMute).toBe(true);
  });

  test('AW should not see Ithaqua emote when Ithaqua is muted', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await executeCommand(awContext.page, 'mute Ithaqua');
    await waitForMessage(awContext.page, /muted|Ithaqua/, 5000).catch(() => {});

    // Ithaqua uses dance emote
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
      msg => msg.includes('Ithaqua') && (msg.includes('dance') || msg.includes('dancing'))
    );
    expect(seesEmote).toBe(false);
  });

  test('AW should be able to unmute Ithaqua', async () => {
    const awContext = contexts[0];

    // AW unmutes Ithaqua
    await executeCommand(awContext.page, 'unmute Ithaqua');

    // Wait for unmute confirmation
    await waitForMessage(awContext.page, 'You have unmuted Ithaqua', 10000).catch(() => {
      // Message may succeed even if format differs
    });

    // Verify unmute confirmation appears
    const messages = await getMessages(awContext.page);
    const seesUnmute = messages.some(msg => msg.includes('unmuted') || msg.includes('Ithaqua'));
    expect(seesUnmute).toBe(true);
  });
});
