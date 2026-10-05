/**
 * Tutorial-instance fixtures for the E2ETutorial character.
 *
 * Leaving the tutorial is one-way, so every tutorial test starts from a reset:
 * `scripts/e2e_reset_players.py --tutorial` saves E2ETutorial in the bedroom template with no
 * instance, one Sling in its inventory and no quest rows, and empties the lost-and-found chest.
 * Logging in then goes through the server's re-entry repair, which builds a brand new instance.
 */

import { spawnSync } from 'child_process';
import { join } from 'path';

import type { Page } from '@playwright/test';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import { executeCommand, loginPlayer, logoutPlayer, waitForMessage, waitForPlayableSession } from './auth';
import type { PlayerContext } from './multiplayer-contexts';

export const TUTORIAL_USERNAME = 'E2ETutorial';

/**
 * `look` in the tutorial bedroom (any instance of it). The room name ("Patient Bedroom") is only
 * in the Location header; the look message carries the description.
 */
export const TUTORIAL_BEDROOM_LOOK_CUE = /small, spartan room|narrow bed and a nightstand/i;

/** What `look` says about a floor with nothing on it. */
export const EMPTY_FLOOR_CUE = /The floor bears no abandoned curios/i;

export interface E2ePlayerState {
  current_room_id: string;
  respawn_room_id: string | null;
  tutorial_instance_id: string | null;
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

/** Put E2ETutorial back at the start of the tutorial (only while it is logged out). */
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

/** Log E2ETutorial out (a real departure: its instance is flushed) and back in (a fresh instance). */
export async function relogTutorialCharacter(tutorial: PlayerContext, resetFirst: boolean): Promise<void> {
  await logoutPlayer(tutorial.page, 25000, { spaFallback: true }).catch(() => {});
  await clearStoredSession(tutorial.page);
  if (resetFirst) {
    // Logging out first also stops the logout's own save from overwriting the reset.
    resetTutorialCharacterInDatabase();
  }
  await loginPlayer(tutorial.page, tutorial.player.username, tutorial.player.password);
  await waitForPlayableSession(tutorial.page, 30000);
}

/** Start a test with E2ETutorial in a brand new tutorial bedroom, holding its Sling. */
export async function startFreshTutorial(tutorial: PlayerContext): Promise<void> {
  await relogTutorialCharacter(tutorial, true);
  await executeCommand(tutorial.page, 'look');
  await waitForMessage(tutorial.page, TUTORIAL_BEDROOM_LOOK_CUE, 20000);
}
