/**
 * Player Utilities
 *
 * Helper functions for player management in E2E tests.
 */

import { expect, type Page } from '@playwright/test';
import {
  clickWithoutStability,
  ensurePlayableConnection,
  executeCommand,
  getMessages,
  getPageSessionCredentials,
  loginPlayer,
  waitForMessage,
  waitForPlayableSession,
} from './auth';
import { resetE2ePlayerRoomsInDatabase } from './multiplayer';
import { DEFAULT_SPAWN_LOOK_CUE, EASTERN_HALLWAY_LOOK_CUE } from './test-data';

/** Zone key for earth_arkhamcity_sanitarium_room_foyer_001 (npc zone command). */
const SANITARIUM_ZONE_KEY = 'arkhamcity/sanitarium';

export async function dismissDeathInterstitial(page: Page): Promise<void> {
  const respawnBtn = page.getByRole('button', {
    name: /Rejoin the earthly plane|Returning to the mortal realm/i,
  });
  if (await respawnBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
    await clickWithoutStability(respawnBtn);
    await page
      .getByTestId('command-input')
      .waitFor({ state: 'visible', timeout: 30000 })
      .catch(() => {});
    await new Promise(r => setTimeout(r, 1500));
  }
}

async function isInCombatYes(page: Page): Promise<boolean> {
  return page.evaluate(() => /In Combat:\s*Yes/i.test(document.body?.innerText ?? '')).catch(() => false);
}

/** Flee until Character Info shows In Combat: No (or attempts exhausted). */
export async function ensureNotInCombat(page: Page, maxAttempts = 10): Promise<void> {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    if (!(await isInCombatYes(page))) {
      return;
    }
    await executeCommand(page, 'flee').catch(() => {});
    await new Promise(r => setTimeout(r, 1500));
    await dismissDeathInterstitial(page);
  }
}

const CULTIST_INSTANCE_ID_RE = /cultist_of_the_yellow_sign_[a-z0-9_]+/gi;

/** Normalize zone-list matches that glue a trailing "npc" label onto the instance id. */
function normalizeCultistInstanceId(raw: string): string {
  return raw.replace(/npc$/i, '');
}

async function isInDeathVoid(page: Page): Promise<boolean> {
  // Location / live room id only. Game Info can retain limbo_death_void / Death > Void dumps.
  return page
    .evaluate(() => {
      const t = document.body?.innerText ?? '';
      if (/earth_arkhamcity_sanitarium_room_/i.test(t)) {
        return false;
      }
      const loc = t.match(/Location\s*\n\s*([^\n]+)/i);
      if (loc?.[1]) {
        return /Death\s*>\s*Void/i.test(loc[1]);
      }
      return false;
    })
    .catch(() => false);
}

/** Collect Cultist of the Yellow Sign instance IDs from npc zone / look text. */
export async function listSanitariumCultistIds(page: Page): Promise<string[]> {
  await executeCommand(page, `npc zone ${SANITARIUM_ZONE_KEY}`);
  await new Promise(r => setTimeout(r, 1200));
  const messages = await getMessages(page);
  const bodyText = await page.evaluate(() => document.body?.innerText ?? '');
  const ids = new Set<string>();
  for (const text of [...messages, bodyText]) {
    for (const match of text.matchAll(CULTIST_INSTANCE_ID_RE)) {
      ids.add(normalizeCultistInstanceId(match[0]));
    }
  }
  return [...ids];
}

/**
 * Despawn Cultist of the Yellow Sign instances left in the sanitarium zone.
 * Requires admin. Uses `npc zone arkhamcity/sanitarium` for instance IDs.
 */
export async function despawnSanitariumCultists(page: Page): Promise<void> {
  const ids = await listSanitariumCultistIds(page);
  for (const id of ids) {
    await executeCommand(page, `npc despawn ${id}`).catch(() => {});
  }
}

/**
 * Clear death interstitial, combat, and low DP so later specs see foyer spawn state.
 * Admin DP set is best-effort (non-admins get a harmless failure).
 * Hard-fails if Location stays on Death > Void after recovery attempts.
 */
export async function ensurePlayableAlive(page: Page, username: string, password: string): Promise<Page> {
  let live = await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
  await dismissDeathInterstitial(live);
  await ensureNotInCombat(live, 4);
  await executeCommand(live, `admin set DP ${username} 20`).catch(() => {});
  await dismissDeathInterstitial(live);
  live = await ensureStanding(live, 8000).catch(() => live);

  // Void blocks most commands. Full DP in limbo skips the death interstitial, so SPA re-login alone
  // reloads persisted limbo — drop client, heal DB rows, then re-enter.
  let recoveredFromVoid = false;
  if (await isInDeathVoid(live)) {
    recoveredFromVoid = true;
    await dismissDeathInterstitial(live);
    await executeCommand(live, `admin set DP ${username} 20`).catch(() => {});
    await dismissDeathInterstitial(live);
  }
  if (await isInDeathVoid(live)) {
    recoveredFromVoid = true;
    // Fast path: do not wait on Exit-the-Realm (void / ward often blocks it for tens of seconds).
    await live.goto('/', { waitUntil: 'domcontentloaded' });
    // Workers=1 default: safe to reset both E2E player rows mid-spec.
    resetE2ePlayerRoomsInDatabase();
    await loginPlayer(live, username, password);
    await waitForPlayableSession(live, 30000);
    await dismissDeathInterstitial(live);
    await executeCommand(live, `admin set DP ${username} 20`).catch(() => {});
    await dismissDeathInterstitial(live);
    live = await ensurePlayableConnection(live, { username, password, timeoutMs: 30000 });
    await executeCommand(live, 'look').catch(() => {});
    live = await ensureStanding(live, 8000).catch(() => live);
  }

  if (await isInDeathVoid(live)) {
    throw new Error(`ensurePlayableAlive: still in Death > Void for ${username}`);
  }

  // After void recovery, spawn should be foyer; require it so movement/combat specs do not proceed blind.
  if (recoveredFromVoid) {
    await executeCommand(live, 'look').catch(() => {});
    await expect(live.getByText(DEFAULT_SPAWN_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  }
  return live;
}

/**
 * Flee combat and stand so `go` is not rejected as "You can't go that way."
 * (MovementService blocks combat/posture with that generic message.)
 */
export async function prepareForDirectionalMove(page: Page): Promise<Page> {
  await ensureNotInCombat(page, 6);
  return ensureStanding(page, 10000);
}

/**
 * Foyer east -> Eastern Hallway. Retries after flee/stand; admin teleport east if combat still blocks go.
 */
export async function goEastFromFoyer(page: Page): Promise<Page> {
  let live = await prepareForDirectionalMove(page);
  await executeCommand(live, 'go east');
  try {
    await waitForMessage(live, /You (move|go) east|Eastern Hallway/i, 20000);
  } catch {
    live = await prepareForDirectionalMove(live);
    await ensureNotInCombat(live, 12);
    await executeCommand(live, 'go east');
    try {
      await waitForMessage(live, /You (move|go) east|Eastern Hallway/i, 25000);
    } catch {
      // move_player returns "You can't go that way." while in combat; admin teleport bypasses that gate.
      const session = getPageSessionCredentials(live);
      const who = session?.username ?? 'ArkanWolfshade';
      await executeCommand(live, `teleport ${who} east`);
      await waitForMessage(live, /teleport|Eastern Hallway|You (move|go) east/i, 25000);
    }
  }
  await executeCommand(live, 'look').catch(() => {});
  await expect(live.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  return live;
}

/**
 * Ensure the player is standing before movement.
 * Server rejects "go" when sitting; call this before any movement command.
 * Waits for either the posture UI "standing" or the game message (e.g. "You rise to your feet.")
 * so we pass as soon as the server confirms; the Character Info panel can update later.
 * Uses .first() on posture locator (strict mode) and Promise.race with game message.
 *
 * @param page - Playwright page instance
 * @param timeoutMs - Max wait for standing confirmation (default: 10000)
 */
export async function ensureStanding(page: Page, timeoutMs: number = 10000): Promise<Page> {
  let live = page;
  const onLogin = await live
    .getByTestId('username-input')
    .isVisible({ timeout: 1000 })
    .catch(() => false);
  if (onLogin) {
    const session = getPageSessionCredentials(live);
    if (session) {
      await loginPlayer(live, session.username, session.password);
      await waitForPlayableSession(live, Math.max(timeoutMs, 15000));
    } else {
      throw new Error('Cannot ensure standing: on login screen with no saved session credentials');
    }
  }

  const alreadyStanding = await live.evaluate(() => {
    const bodyText = document.body?.innerText ?? '';
    return (
      /Posture:\s*standing\b/i.test(bodyText) ||
      /Posture\s*\n\s*standing\b/i.test(bodyText) ||
      /You are already standing/i.test(bodyText)
    );
  });
  if (alreadyStanding) {
    return live;
  }

  const session = getPageSessionCredentials(live);
  if (session) {
    live = await ensurePlayableConnection(live, {
      username: session.username,
      password: session.password,
      timeoutMs: Math.max(timeoutMs, 20000),
    });
  }

  await live.bringToFront().catch(() => {});
  await executeCommand(live, 'stand');
  const halfMs = Math.max(Math.floor(timeoutMs / 2), 4000);
  const standingPredicate = () => {
    const t = document.body?.innerText ?? '';
    if (/You rise to your feet|You are already standing/i.test(t)) return true;
    if (/Posture:\s*standing\b/i.test(t)) return true;
    if (/Posture\s*\n\s*standing\b/i.test(t)) return true;
    return false;
  };
  try {
    await live.waitForFunction(standingPredicate, undefined, { timeout: halfMs });
    return live;
  } catch {
    // Re-issue stand once (sitting/prone lag or first command dropped under load).
    await executeCommand(live, 'stand');
    await live.waitForFunction(standingPredicate, undefined, {
      timeout: Math.max(timeoutMs - halfMs, 5000),
    });
    return live;
  }
}

/**
 * Reset a player's position to their starting room.
 * Note: This requires admin privileges or a test helper endpoint.
 *
 * @param page - Playwright page instance
 * @param targetPlayer - Username of player to reset (defaults to current player)
 */
export async function resetPlayerPosition(page: Page, targetPlayer?: string): Promise<Page> {
  if (targetPlayer) {
    // teleport only accepts an optional Direction — pull target to admin's room via goto + teleport
    await executeCommand(page, `goto ${targetPlayer}`);
    await executeCommand(page, `teleport ${targetPlayer}`);
    return page;
  }
  let live = await ensureStanding(page, 5000);
  await executeCommand(live, 'go north');
  await live
    .locator('[data-message-text]')
    .first()
    .waitFor({ state: 'attached', timeout: 5000 })
    .catch(() => {});
  live = await ensureStanding(live, 5000);
  await executeCommand(live, 'go south');
  await live
    .locator('[data-message-text]')
    .first()
    .waitFor({ state: 'attached', timeout: 5000 })
    .catch(() => {});
  return live;
}

/**
 * Get player's current room ID from the game state.
 *
 * @param page - Playwright page instance
 * @returns Room ID or null if not found
 */
export async function getPlayerRoom(page: Page): Promise<string | null> {
  await executeCommand(page, 'look');
  await page
    .locator('[data-message-text]')
    .first()
    .waitFor({ state: 'attached', timeout: 5000 })
    .catch(() => {});

  // Try to extract room ID from look output
  const messages = await page.evaluate(() => {
    const messages = Array.from(document.querySelectorAll('[data-message-text]'));
    return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });

  // Look for room ID in messages (this is a simplified version)
  // In a real implementation, you'd parse the look output more carefully
  for (const msg of messages) {
    if (msg.includes('earth_arkhamcity_sanitarium_room_')) {
      const match = msg.match(/earth_arkhamcity_sanitarium_room_\w+/);
      if (match) {
        return match[0];
      }
    }
  }

  return null;
}
