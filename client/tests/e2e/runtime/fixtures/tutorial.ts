/**
 * First Exposure fixtures for the E2ETutorial character.
 *
 * Finishing the tutorial is one-way, so every tutorial test starts from a reset:
 * `scripts/e2e_reset_players.py --tutorial` saves E2ETutorial in the Main Foyer with the pending-instance
 * marker, one Sling in its inventory, full DP, lucidity 100, corruption 0 and no quest rows, and empties the
 * lost-and-found chest and E2ETutorial's bank deposit box (what an instance leaves behind lands in the box).
 * Logging in then goes through the server's tutorial connect path, which builds a brand new instance.
 */

import { spawnSync } from 'child_process';
import { join } from 'path';

import type { Page } from '@playwright/test';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import { executeCommand, loginPlayer, logoutPlayer, waitForMessage, waitForPlayableSession } from './auth';
import type { PlayerContext } from './multiplayer-contexts';

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

export interface E2ePlayerState {
  current_room_id: string;
  respawn_room_id: string | null;
  tutorial_instance_id: string | null;
  /** Names of the stacks in the character's bank deposit box (empty when they have none). */
  bank_items: string[];
  current_dp: number | null;
  corruption: number | null;
  /** Lucidity (LCD); null when the character has no lucidity record yet. */
  current_lcd: number | null;
  /** Names of the stacks in the character's inventory. */
  inventory_items: string[];
  /** Quest id -> instance state (`active` / `completed`). */
  quests: Record<string, string>;
  /** True while a debrief (delirium or sanitarium respawn) is waiting for Dr. Morgan. */
  debrief_pending: boolean;
}

function runE2eScript(script: string, args: string[]): string {
  const result = spawnSync('uv', ['run', '--no-sync', 'python', join(E2E_PROJECT_ROOT, 'scripts', script), ...args], {
    cwd: E2E_PROJECT_ROOT,
    // shell:false so timeout is honored on Windows (shell:true has hung the Playwright worker).
    shell: false,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: { ...process.env, ...loadE2eEnv() },
    timeout: 20000,
  });
  if (result.status !== 0) {
    throw new Error(`${script} ${args.join(' ')} failed (exit ${result.status}): ${result.stderr?.slice(0, 500)}`);
  }
  return result.stdout;
}

/** Put E2ETutorial back at the very start of First Exposure (only while it is logged out). */
export function resetTutorialCharacterInDatabase(): void {
  runE2eScript('e2e_reset_players.py', ['--tutorial']);
}

/** Server-authoritative room/respawn/instance fields for one character, straight from Postgres. */
export function readE2ePlayerState(characterName: string): E2ePlayerState {
  return JSON.parse(runE2eScript('e2e_player_state.py', [characterName])) as E2ePlayerState;
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
    resetTutorialCharacterInDatabase();
  }
  if (placeAt) {
    runE2eScript('e2e_place_player.py', [TUTORIAL_USERNAME, placeAt]);
  }
  await loginPlayer(tutorial.page, tutorial.player.username, tutorial.player.password);
  await waitForPlayableSession(tutorial.page, 30000);
}

/** Start a test with E2ETutorial in a brand new tutorial, standing in Independence Square holding its Sling. */
export async function startFreshTutorial(tutorial: PlayerContext): Promise<void> {
  await relogTutorialCharacter(tutorial, true);
  await executeCommand(tutorial.page, 'look');
  await waitForMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE, 20000);
}
