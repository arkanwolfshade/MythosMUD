/**
 * Combat messages in Game Info (single player)
 *
 * Verifies that when the client is connected, combat round messages appear in the
 * Game Info panel and the connection status remains "Connected". Covers the flow
 * where combat events are published over WebSocket and projected into game messages.
 *
 * Related: investigations/sessions/2026-02-04_combat-second-npc-and-linkdead-findings.md
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import type { PlayerContext } from '../fixtures/multiplayer';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

function hasCombatMessage(messages: string[]): boolean {
  return messages.some(msg => {
    const lower = msg.toLowerCase();
    return (
      lower.includes('attack') ||
      lower.includes('auto_attack') ||
      lower.includes('slain') ||
      lower.includes('has been slain') ||
      lower.includes('you attack')
    );
  });
}

function assertStillConnected(page: PlayerContext['page']): Promise<boolean> {
  return page.evaluate(() => {
    // Mirror multiplayer fixtures: any element whose text is exactly "Connected"
    // or contains "Connected" without also containing "linkdead" counts as connected.
    const statusElements = Array.from(document.querySelectorAll('*'));
    return statusElements.some(el => {
      const text = el.textContent?.trim() ?? '';
      return text === 'Connected' || (text.includes('Connected') && !text.includes('linkdead'));
    });
  });
}

test.describe('Combat messages in Game Info', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('first combat: combat round messages appear in Game Info and connection stays Connected', async () => {
    const awContext = contexts[0];
    const { page } = awContext;

    await ensurePlayerInGame(awContext, 15000);

    // Dr. Francis Morgan is in Main Foyer. Navigate there and wait until location actually shows Main Foyer.
    const inFoyer = await page.evaluate(() => (document.body?.innerText ?? '').includes('Main Foyer'));
    /* eslint-disable playwright/no-conditional-in-test -- optional navigation when not already in Foyer */
    if (!inFoyer) {
      const hasLaundry = await page.evaluate(() => document.body?.innerText?.includes('Laundry Room') ?? false);
      if (hasLaundry) {
        await executeCommand(page, 'go south');
        await waitForMessage(page, /You go south|Eastern Hallway/i, 10000).catch(() => {});
      }
      await executeCommand(page, 'go west');
      await waitForMessage(page, /You go west|Main Foyer/i, 10000).catch(() => {});
    }
    /* eslint-enable playwright/no-conditional-in-test */
    await page.waitForFunction(() => (document.body?.innerText ?? '').includes('Main Foyer'), { timeout: 10000 });

    await executeCommand(page, 'attack Dr. Francis Morgan');

    const stillConnected = await assertStillConnected(page);
    expect(stillConnected).toBe(true);

    // Wait for a combat message in Game Info (locator is more reliable than waitForFunction)
    const combatMessageLocator = page
      .locator('[data-message-text]')
      .filter({
        hasText: /attack|auto_attack|slain|has been slain|you attack/i,
      })
      .first();
    await combatMessageLocator.waitFor({ state: 'visible', timeout: 45000 });

    const messages = await getMessages(page);
    expect(hasCombatMessage(messages)).toBe(true);

    const connectedAfter = await assertStillConnected(page);
    expect(connectedAfter).toBe(true);
  });
});
