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
import { executeCommand, getMessages } from '../fixtures/auth';
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

    // Dr. Francis Morgan is in Main Foyer. Ensure we are there (test order may leave us in Laundry etc.).
    const inFoyer = await page.evaluate(() => {
      const bodyText = document.body?.innerText ?? '';
      return bodyText.includes('Main Foyer');
    });
    if (!inFoyer) {
      // From Laundry: go south -> Eastern Hallway, go west -> Main Foyer. From Eastern Hallway: go west -> Main Foyer.
      const hasLaundry = await page.evaluate(() => document.body?.innerText?.includes('Laundry Room') ?? false);
      if (hasLaundry) {
        await executeCommand(page, 'go south');
        await page.waitForTimeout(1500);
      }
      await executeCommand(page, 'go west');
      await page.waitForTimeout(1500);
    }

    await executeCommand(page, 'attack Dr. Francis Morgan');

    await page.waitForTimeout(2000);

    const stillConnected = await assertStillConnected(page);
    expect(stillConnected).toBe(true);

    await page.waitForFunction(
      () => {
        const messages = Array.from(document.querySelectorAll('[data-message-text]'));
        const texts = messages.map(m => (m.getAttribute('data-message-text') || '').trim());
        return texts.some(msg => {
          const lower = msg.toLowerCase();
          return (
            lower.includes('attack') ||
            lower.includes('auto_attack') ||
            lower.includes('slain') ||
            lower.includes('has been slain') ||
            lower.includes('you attack')
          );
        });
      },
      { timeout: 45000 }
    );

    const messages = await getMessages(page);
    expect(hasCombatMessage(messages)).toBe(true);

    const connectedAfter = await assertStillConnected(page);
    expect(connectedAfter).toBe(true);
  });
});
