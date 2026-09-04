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
import {
  ensurePlayableConnection,
  executeCommand,
  getMessages,
  getPageSessionCredentials,
  waitForMessage,
} from '../fixtures/auth';
import type { PlayerContext } from '../fixtures/multiplayer';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';
import {
  despawnSanitariumCultists,
  ensureNotInCombat,
  ensurePlayableAlive,
  ensureStanding,
  listSanitariumCultistIds,
} from '../fixtures/player';

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
  await page
    .waitForFunction(
      () => {
        const text = document.body?.innerText ?? '';
        return !/\(warded\)/i.test(text) && !/still warded by protective energies/i.test(text);
      },
      { timeout: timeoutMs }
    )
    .catch(() => {});
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

async function isInDeathVoid(page: PlayerContext['page']): Promise<boolean> {
  return page.evaluate(() => /Death\s*>\s*Void/i.test(document.body?.innerText ?? '')).catch(() => false);
}

async function tryStartCombat(page: PlayerContext['page'], target: string): Promise<boolean> {
  let live = page;
  const session = getPageSessionCredentials(live);
  if (session) {
    live = await ensurePlayableConnection(live, {
      username: session.username,
      password: session.password,
      timeoutMs: 30000,
    });
  }
  await live.bringToFront().catch(() => {});
  await executeCommand(live, `attack ${target}`);
  await new Promise(r => setTimeout(r, 2500));

  if (await isWardBlockingCombat(live)) {
    await new Promise(r => setTimeout(r, 5000));
    return false;
  }

  const inCombat = await isInCombatStatus(live);
  const messages = await getMessages(live);
  if (inCombat || hasCombatMessage(messages)) {
    return true;
  }

  await new Promise(r => setTimeout(r, 3000));
  return false;
}

async function retryUntilCombatStarted(
  page: PlayerContext['page'],
  creds: { username: string; password: string },
  getTarget: () => Promise<string>,
  maxAttempts = 18
): Promise<boolean> {
  let live = page;
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    if (await isInDeathVoid(live)) {
      live = await ensurePlayableAlive(live, creds.username, creds.password);
      await despawnSanitariumCultists(live);
      await spawnCombatTargetNpc(live, creds);
    }

    const messages = await getMessages(live);
    if (messages.some(m => /Multiple targets match/i.test(m))) {
      await despawnSanitariumCultists(live);
      await spawnCombatTargetNpc(live, creds);
    }

    const target = await getTarget();
    if (await tryStartCombat(live, target)) {
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

/** Aggressive mob — quest_giver Morgan is not a reliable combat target. */
const SPAWN_NPC_ID = 58;
const SPAWN_NPC_NAME = 'Cultist of the Yellow Sign';

async function assertNpcSpawnVisible(page: PlayerContext['page'], npcName: string): Promise<void> {
  const escapedNpcName = npcName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const occupantCue = page.getByText(new RegExp(escapedNpcName, 'i'));
  const bodyHasNpc = page.evaluate(
    (name: string) => (document.body?.innerText ?? '').toLowerCase().includes(name.toLowerCase()),
    npcName
  );
  const messageCue = page.locator('[data-message-text]').filter({ hasText: new RegExp(escapedNpcName, 'i') });
  await expect
    .poll(
      async () =>
        (await occupantCue
          .first()
          .isVisible()
          .catch(() => false)) ||
        (await bodyHasNpc) ||
        (await messageCue
          .first()
          .isVisible()
          .catch(() => false)),
      { timeout: 30000, message: `spawn visible: ${npcName}` }
    )
    .toBe(true);
}

/** Despawn extras; keep the first instance as the unique attack target. */
async function keepFirstCultistInstanceId(page: PlayerContext['page'], ids: string[]): Promise<string | null> {
  for (const extra of ids.slice(1)) {
    await executeCommand(page, `npc despawn ${extra}`).catch(() => {});
  }
  const remaining = await listSanitariumCultistIds(page);
  return remaining.length >= 1 ? remaining[0] : null;
}

/** After a visible spawn, resolve a unique cultist id (or name on last attempt). */
async function resolveSpawnedCultistTarget(
  page: PlayerContext['page'],
  isLastAttempt: boolean
): Promise<string | null> {
  await assertNpcSpawnVisible(page, SPAWN_NPC_NAME);
  await waitForMessage(page, /NPC spawned successfully|spawned successfully/i, 20000).catch(() => {});
  const ids = await listSanitariumCultistIds(page);
  if (ids.length === 1) {
    return ids[0];
  }
  if (ids.length > 1) {
    return keepFirstCultistInstanceId(page, ids);
  }
  // Zone list empty but spawn UI visible — use spawn name as last resort.
  return isLastAttempt ? SPAWN_NPC_NAME : null;
}

/** Spawn a single cultist; return its unique instance id for unambiguous attack. */
async function spawnCombatTargetNpc(
  page: PlayerContext['page'],
  creds: { username: string; password: string }
): Promise<string> {
  let live = await ensurePlayableConnection(page, { ...creds, timeoutMs: 45000 });
  await live
    .locator('[data-message-text]')
    .first()
    .waitFor({ state: 'visible', timeout: 20000 })
    .catch(() => {});
  await executeCommand(live, 'look');
  await waitForMessage(live, /Main Foyer|Sanitarium|marble|Exits/i, 20000).catch(() => {});
  live = await ensureStanding(live, 15000);
  for (let attempt = 0; attempt < 3; attempt++) {
    live = await ensurePlayableConnection(live, { ...creds, timeoutMs: 45000 });
    await despawnSanitariumCultists(live);
    await executeCommand(live, `npc spawn ${SPAWN_NPC_ID}`);
    try {
      const target = await resolveSpawnedCultistTarget(live, attempt === 2);
      if (target) {
        return target;
      }
    } catch (err) {
      if (attempt === 2) {
        throw err;
      }
      await executeCommand(live, 'look');
      await new Promise(r => setTimeout(r, 2000));
    }
  }
  throw new Error('spawnCombatTargetNpc: could not obtain a unique cultist instance id');
}

test.describe('Combat messages in Game Info', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(120_000);
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
  });

  test.afterAll(async () => {
    test.setTimeout(60_000);
    await cleanupMultiPlayerContexts(contexts);
  });

  test('first combat: combat round messages appear in Game Info and connection stays Connected', async () => {
    test.setTimeout(240_000);
    const awContext = contexts[0];

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
    await despawnSanitariumCultists(awContext.page);
    awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
    await awContext.page.getByTestId('command-input').waitFor({ state: 'visible', timeout: 15000 });
    await waitForEntryWardCleared(awContext.page, 60000);

    // Wait for room state so Location/Exits are loaded (avoids "Unknown" and "You can't go that way").
    await awContext.page
      .getByText(/Exits:/)
      .first()
      .waitFor({ state: 'visible', timeout: 15000 });

    const creds = {
      username: awContext.player.username,
      password: awContext.player.password,
    };

    // Spawn one aggressive mob; attack by instance id to avoid "Multiple targets match".
    let combatTargetId = await spawnCombatTargetNpc(awContext.page, creds);

    awContext.page = await ensurePlayableConnection(awContext.page, { ...creds, timeoutMs: 45000 });
    awContext.page = await ensureStanding(awContext.page, 15000);
    await waitForEntryWardCleared(awContext.page, 60000);

    // Login grace / entry_ward blocks combat briefly after entering the realm; retry until In Combat or attack line.
    expect(
      await retryUntilCombatStarted(awContext.page, creds, async () => {
        const ids = await listSanitariumCultistIds(awContext.page);
        if (ids.length === 1) {
          combatTargetId = ids[0];
          return combatTargetId;
        }
        combatTargetId = await spawnCombatTargetNpc(awContext.page, creds);
        return combatTargetId;
      })
    ).toBe(true);

    expect(await assertStillConnected(awContext.page)).toBe(true);

    // Combat round events can take several ticks; poll Game Info instead of a single locator wait.
    await waitForCombatRoundMessage(awContext.page);

    const messages = await getMessages(awContext.page);
    expect(hasCombatMessage(messages)).toBe(true);

    const combatMessageLocator = awContext.page
      .locator('[data-message-text]')
      .filter({ hasText: COMBAT_MESSAGE_PATTERN })
      .first();
    await expect(combatMessageLocator).toBeVisible({ timeout: 5000 });

    expect(await assertStillConnected(awContext.page)).toBe(true);

    // Flee, despawn hostiles, heal — foyer must be safe for later admin/connection specs.
    await ensureNotInCombat(awContext.page);
    await despawnSanitariumCultists(awContext.page);
    awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  });
});
