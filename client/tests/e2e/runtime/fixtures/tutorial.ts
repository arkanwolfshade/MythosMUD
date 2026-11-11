/**
 * First Exposure fixtures for the E2ETutorial character.
 *
 * Finishing the tutorial is one-way, so every tutorial test starts from a reset:
 * the server's test endpoint (fixtures/e2e-test-api.ts) saves E2ETutorial in the Main Foyer with the
 * pending-instance marker, one Sling in its inventory, full DP, lucidity 100, corruption 0 and no quest rows,
 * and empties the lost-and-found chest and E2ETutorial's bank deposit box (what an instance leaves behind lands
 * in the box). Logging in then goes through the server's tutorial connect path, which builds a brand new instance.
 */

import { expect, type Page } from '@playwright/test';
import { executeCommand, loginPlayer, logoutPlayer, waitForMessage, waitForPlayableSession } from './auth';
import { fetchE2ePlayerState, placeE2ePlayer, resetE2eTutorialCharacter, type E2ePlayerState } from './e2e-test-api';
import type { PlayerContext } from './multiplayer-contexts';

export type { E2ePlayerState };

export const TUTORIAL_USERNAME = 'E2ETutorial';

/**
 * `look` in Independence Square, the tutorial's first room (any instance of it). The room name is only
 * in the Location header; the look message carries the description.
 */
export const TUTORIAL_SQUARE_LOOK_CUE = /last of the light lies along the roofs of Arkham/i;

/** `look` in the Recovery Ward, where a tutorial delirium wakes the player. */
export const RECOVERY_WARD_LOOK_CUE = /eight iron cots/i;

/** The Recovery Ward's stable id (server/constants/spawn_defaults.RECOVERY_WARD_ROOM_ID). */
export const RECOVERY_WARD_ROOM_ID = 'earth_arkhamcity_sanitarium_room_recovery_ward_001';

/** The room id of a First Exposure template room as it appears in an instance: `instance_<uuid>_<stable id>`. */
export function tutorialRoomPattern(name: string): RegExp {
  return new RegExp(`^instance_.+_earth_arkhamcity_first_exposure_room_${name}_001$`);
}

/** What `look` says about a floor with nothing on it. */
export const EMPTY_FLOOR_CUE = /The floor bears no abandoned curios/i;

/** Arkham Savings & Trust: the bank room (db/migrations/20261007120000_bank_deposit_boxes.sql). */
export const BANK_ROOM_ID = 'earth_arkhamcity_downtown_room_arkham_savings_001';

/** `look` in the bank (the room name is only in the Location header; the description carries this). */
export const BANK_LOOK_CUE = /hushed banking hall/i;

/** Put E2ETutorial back at the very start of First Exposure (only while it is logged out). */
export async function resetTutorialCharacterInDatabase(): Promise<void> {
  await resetE2eTutorialCharacter(TUTORIAL_USERNAME);
}

/** Server-authoritative state of one character (room, DP, inventory, quests, ...), from the server's player registry. */
export async function readE2ePlayerState(characterName: string): Promise<E2ePlayerState> {
  return fetchE2ePlayerState(characterName);
}

async function clearStoredSession(page: Page): Promise<void> {
  // Clear the persisted token so loginPlayer gets the login form instead of a session restore.
  await page
    .evaluate(() => {
      localStorage.clear();
      sessionStorage.clear();
    })
    .catch(() => {});
}

/**
 * Log E2ETutorial out (a real departure: its instance is flushed) and back in (a fresh instance).
 * With `placeAt` it logs back in standing in that room instead, out of the tutorial (e.g. at the bank):
 * the move, which also clears the tutorial marker, is written between logout and login, because the
 * server keeps a logged-in player's room in memory and would overwrite it.
 */
export async function relogTutorialCharacter(
  tutorial: PlayerContext,
  resetFirst: boolean,
  placeAt?: string
): Promise<void> {
  await logoutPlayer(tutorial.page, 25000, { spaFallback: true }).catch(() => {});
  await clearStoredSession(tutorial.page);
  if (resetFirst) {
    // Logging out first also stops the logout's own save from overwriting the reset.
    await resetTutorialCharacterInDatabase();
  }
  if (placeAt) {
    await placeE2ePlayer(TUTORIAL_USERNAME, placeAt);
  }
  await loginPlayer(tutorial.page, tutorial.player.username, tutorial.player.password);
  await waitForPlayableSession(tutorial.page, 30000);
}

/** Walk one step and wait until the server has the player in the expected room. */
export async function walk(player: PlayerContext, direction: string, room: RegExp): Promise<void> {
  await executeCommand(player.page, `go ${direction}`);
  await expect
    .poll(async () => (await readE2ePlayerState(player.player.username)).current_room_id, {
      timeout: 20000,
      message: `after "go ${direction}"`,
    })
    .toMatch(room);
}

/** Say a command and wait for a line of the reply. */
export async function say(player: PlayerContext, command: string, reply: RegExp, timeout = 20000): Promise<void> {
  await executeCommand(player.page, command);
  await waitForMessage(player.page, reply, timeout);
}

/** Start a test with E2ETutorial in a brand new tutorial, standing in Independence Square holding its Sling. */
export async function startFreshTutorial(tutorial: PlayerContext): Promise<void> {
  await relogTutorialCharacter(tutorial, true);
  await executeCommand(tutorial.page, 'look');
  await waitForMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE, 20000);
}
