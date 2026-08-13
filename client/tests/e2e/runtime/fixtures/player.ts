/**
 * Player Utilities
 *
 * Helper functions for player management in E2E tests.
 */

import { expect, type Page } from '@playwright/test';
import { locationIndicatesDeathVoid, requiredAliveButDeadMessage } from '../../../../src/utils/deathVoidLocation';
import {
  clickWithoutStability,
  ensurePlayableConnection,
  executeCommand,
  getCommandPanelInput,
  getMessages,
  getPageSessionCredentials,
  loginPlayer,
  waitForPlayableSession,
} from './auth';
import { resetE2ePlayerRoomsInDatabase } from './multiplayer';
import { DEFAULT_SPAWN_LOOK_CUE } from './test-data';

/** Zone key for earth_arkhamcity_sanitarium_room_foyer_001 (npc zone command). */
const SANITARIUM_ZONE_KEY = 'arkhamcity/sanitarium';

export async function dismissDeathInterstitial(page: Page): Promise<void> {
  const respawnBtn = page.getByRole('button', {
    name: /Rejoin the earthly plane|Returning to the mortal realm/i,
  });
  if (await respawnBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
    await clickWithoutStability(respawnBtn);
    await getCommandPanelInput(page)
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

export async function isInDeathVoid(page: Page): Promise<boolean> {
  const bodyText = await page.evaluate(() => document.body?.innerText ?? '').catch(() => '');
  return locationIndicatesDeathVoid(bodyText);
}

/** True when Location is Death > Void or the death interstitial is showing. */
export async function isPlayerDead(page: Page): Promise<boolean> {
  if (await isInDeathVoid(page)) {
    return true;
  }
  const respawnBtn = page.getByRole('button', {
    name: /Rejoin the earthly plane|Returning to the mortal realm/i,
  });
  return respawnBtn.isVisible({ timeout: 500 }).catch(() => false);
}

/**
 * Fail if this player must be alive for the current step.
 * Do not heal here: a corpse means this test or the previous test's cleanup is wrong.
 */
export async function assertPlayerAlive(page: Page, username: string): Promise<void> {
  if (await isPlayerDead(page)) {
    throw new Error(requiredAliveButDeadMessage(username));
  }
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
      ids.add(match[0]);
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
export async function ensurePlayableAlive(page: Page, username: string, password: string): Promise<void> {
  await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
  await dismissDeathInterstitial(page);
  await ensureNotInCombat(page, 4);
  await executeCommand(page, `admin set DP ${username} 20`).catch(() => {});
  await dismissDeathInterstitial(page);
  await ensureStanding(page, 8000).catch(() => {});

  // Void blocks most commands. Full DP in limbo skips the death interstitial, so SPA re-login alone
  // reloads persisted limbo — drop client, heal DB rows, then re-enter.
  let recoveredFromVoid = false;
  if (await isInDeathVoid(page)) {
    recoveredFromVoid = true;
    await dismissDeathInterstitial(page);
    await executeCommand(page, `admin set DP ${username} 20`).catch(() => {});
    await dismissDeathInterstitial(page);
  }
  if (await isInDeathVoid(page)) {
    recoveredFromVoid = true;
    // Fast path: do not wait on Exit-the-Realm (void / ward often blocks it for tens of seconds).
    await page.goto('/', { waitUntil: 'domcontentloaded' });
    // Workers=1 default: safe to reset both E2E player rows mid-spec.
    resetE2ePlayerRoomsInDatabase();
    await loginPlayer(page, username, password);
    await waitForPlayableSession(page, 30000);
    await dismissDeathInterstitial(page);
    await executeCommand(page, `admin set DP ${username} 20`).catch(() => {});
    await dismissDeathInterstitial(page);
    await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
    await executeCommand(page, 'look').catch(() => {});
    await ensureStanding(page, 8000).catch(() => {});
  }

  if (await isInDeathVoid(page)) {
    throw new Error(`ensurePlayableAlive: still in Death > Void for ${username}`);
  }

  // After void recovery, spawn should be foyer; require it so movement/combat specs do not proceed blind.
  if (recoveredFromVoid) {
    await executeCommand(page, 'look').catch(() => {});
    await expect(page.getByText(DEFAULT_SPAWN_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  }
}

/**
 * Ensure the player is standing before movement.
 * Server rejects "go" when sitting. Assert Character Info posture (not Game Info leftovers).
 *
 * @param page - Playwright page instance
 * @param timeoutMs - Max wait for Character Info posture to read standing (default: 8000)
 */
export async function ensureStanding(page: Page, timeoutMs: number = 8000): Promise<void> {
  const session = getPageSessionCredentials(page);
  if (session) {
    await ensurePlayableConnection(page, {
      username: session.username,
      password: session.password,
      timeoutMs: Math.max(timeoutMs, 20000),
    });
  } else {
    const onLogin = await page
      .getByTestId('username-input')
      .isVisible({ timeout: 1000 })
      .catch(() => false);
    if (onLogin) {
      throw new Error('Cannot ensure standing: on login screen with no saved session credentials');
    }
  }

  const posture = page.getByTestId('player-posture');
  const current = (await posture.textContent({ timeout: 2000 }).catch(() => ''))?.trim() ?? '';
  if (/^standing$/i.test(current)) {
    return;
  }

  await page.bringToFront().catch(() => {});
  await executeCommand(page, 'stand');
  try {
    await expect(posture).toHaveText(/^standing$/i, { timeout: timeoutMs });
  } catch (err) {
    const onLogin = await page
      .getByTestId('username-input')
      .isVisible({ timeout: 1000 })
      .catch(() => false);
    const creds = getPageSessionCredentials(page);
    if (onLogin && creds) {
      await ensurePlayableConnection(page, {
        username: creds.username,
        password: creds.password,
        timeoutMs: Math.max(timeoutMs, 20000),
      });
      await executeCommand(page, 'stand');
      await expect(page.getByTestId('player-posture')).toHaveText(/^standing$/i, { timeout: timeoutMs });
      return;
    }
    throw err;
  }
}

/**
 * Reset a player's position to their starting room.
 * Note: This requires admin privileges or a test helper endpoint.
 *
 * @param page - Playwright page instance
 * @param targetPlayer - Username of player to reset (defaults to current player)
 */
export async function resetPlayerPosition(page: Page, targetPlayer?: string): Promise<void> {
  if (targetPlayer) {
    // teleport only accepts an optional Direction — pull target to admin's room via goto + teleport
    await executeCommand(page, `goto ${targetPlayer}`);
    await executeCommand(page, `teleport ${targetPlayer}`);
  } else {
    await ensureStanding(page, 5000);
    await executeCommand(page, 'go north');
    await page
      .locator('[data-message-text]')
      .first()
      .waitFor({ state: 'attached', timeout: 5000 })
      .catch(() => {});
    await ensureStanding(page, 5000);
    await executeCommand(page, 'go south');
    await page
      .locator('[data-message-text]')
      .first()
      .waitFor({ state: 'attached', timeout: 5000 })
      .catch(() => {});
  }
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
