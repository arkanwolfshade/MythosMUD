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
import { ensureStanding } from '../fixtures/player';

function hasCombatMessage(messages: string[]): boolean {
  return messages.some(msg => {
    const lower = msg.toLowerCase();
    return (
      lower.includes('attack') ||
      lower.includes('auto_attack') ||
      lower.includes('slain') ||
      lower.includes('has been slain') ||
      lower.includes('you attack') ||
      lower.includes(' damage') ||
      lower.includes('dealt ') ||
      lower.includes('fighting')
    );
  });
}

const COMBAT_MESSAGE_PATTERN =
  /attack|attacks|auto_attack|slain|has been slain|you attack| damage|Dealt \d+ damage|fighting/i;

/** Entry ward (~10s) must clear before attack; occupant label can lag until ticks run. */
async function waitForEntryWardCleared(page: PlayerContext['page'], timeoutMs: number): Promise<void> {
  await expect
    .poll(
      async () => {
        const text = await page.evaluate(() => document.body?.innerText ?? '');
        return !/\(warded\)/i.test(text) && !/still warded by protective energies/i.test(text);
      },
      { timeout: timeoutMs, message: 'entry ward cleared' }
    )
    .toBe(true);
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

async function isWardBlockingCombat(page: PlayerContext['page']): Promise<boolean> {
  return page
    .getByText(/still warded by protective energies|cannot engage in combat yet/i)
    .isVisible()
    .catch(() => false);
}

async function isInCombatStatus(page: PlayerContext['page']): Promise<boolean> {
  return page
    .evaluate(
      () =>
        (document.body?.innerText ?? '').includes('In Combat:') &&
        /In Combat:\s*Yes/i.test(document.body?.innerText ?? '')
    )
    .catch(() => false);
}

async function tryStartCombat(page: PlayerContext['page'], targetName: string): Promise<boolean> {
  await executeCommand(page, `attack ${targetName}`);
  await new Promise(r => setTimeout(r, 2500));

  if (await isWardBlockingCombat(page)) {
    await new Promise(r => setTimeout(r, 5000));
    return false;
  }

  const inCombat = await isInCombatStatus(page);
  const messages = await getMessages(page);
  if (inCombat || hasCombatMessage(messages)) {
    return true;
  }

  await new Promise(r => setTimeout(r, 3000));
  return false;
}

async function retryUntilCombatStarted(
  page: PlayerContext['page'],
  targetName: string,
  maxAttempts = 18
): Promise<boolean> {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    if (await tryStartCombat(page, targetName)) {
      return true;
    }
  }
  return false;
}

async function waitForCombatRoundMessage(page: PlayerContext['page']): Promise<void> {
  await expect
    .poll(async () => hasCombatMessage(await getMessages(page)), {
      timeout: 90000,
      message: 'combat round message in Game Info',
    })
    .toBe(true);
}

async function spawnCombatTargetNpc(page: PlayerContext['page']): Promise<void> {
  await ensureStanding(page, 8000);
  await executeCommand(page, 'npc spawn 54');
  await waitForMessage(page, /NPC spawned successfully|spawned successfully/i, 20000);
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
    test.setTimeout(240_000);
    const awContext = contexts[0];
    const { page } = awContext;

    await page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    // beforeAll login applies entry_ward (~10s); do not relogin here — that re-applies ward and can drop to login UI.
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: 15000 });
    await waitForEntryWardCleared(page, 60000);

    // Wait for room state so Location/Exits are loaded (avoids "Unknown" and "You can't go that way").
    await page
      .getByText(/Exits:/)
      .first()
      .waitFor({ state: 'visible', timeout: 15000 });

    // DEFAULT_RESPAWN_ROOM is the limbo arena grid; room_links do not reach earth_arkhamcity_sanitarium_room_foyer_001,
    // so walk south/west/north never shows "Main Foyer" where the world's Dr. Francis Morgan template lives.
    // Spawn his definition (id 54 in mythos_e2e DML) into the current cell for a stable combat target.
    await spawnCombatTargetNpc(page);

    // Login grace / entry_ward blocks combat briefly after entering the realm; retry until In Combat or attack line.
    expect(await retryUntilCombatStarted(page, 'Dr. Francis Morgan')).toBe(true);

    expect(await assertStillConnected(page)).toBe(true);

    // Combat round events can take several ticks; poll Game Info instead of a single locator wait.
    await waitForCombatRoundMessage(page);

    const messages = await getMessages(page);
    expect(hasCombatMessage(messages)).toBe(true);

    const combatMessageLocator = page
      .locator('[data-message-text]')
      .filter({ hasText: COMBAT_MESSAGE_PATTERN })
      .first();
    await expect(combatMessageLocator).toBeVisible({ timeout: 5000 });

    expect(await assertStillConnected(page)).toBe(true);
  });
});
