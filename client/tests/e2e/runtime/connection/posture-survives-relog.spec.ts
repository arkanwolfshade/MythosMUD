/**
 * Posture survives a logout and login (ADR-029 step 8a).
 *
 * Logout used to copy the connection manager's cached `position` into the player's stats and save the whole row. That
 * cache is set at connect and on respawn only, so it put an old posture back: the player came back standing whatever
 * they were doing when they left. The registry owns posture, and logout now changes only `last_active`.
 *
 * The "Exit the Realm" button runs `/rest`, which sits the player down and disconnects, and the client then sends
 * `logout`. A player who leaves that way must come back sitting, whether they were standing, sitting or lying: the
 * `logout` used to overwrite that sitting with the stale "standing" the connection manager cached when they connected.
 *
 * Plays E2ETutorial, because nothing else shares the character and a reset puts it back to a known state, but placed
 * in the bank, out of the tutorial: a lost tutorial instance restarts the run with full DP and standing by design
 * (the reconnect's `restored`), which would mask exactly what is under test. The relog is a real logout and login with
 * no reset in between. Posture is read from the server's player registry, not the page.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { cleanupMultiPlayerContexts, createMultiPlayerContexts, type PlayerContext } from '../fixtures/multiplayer';
import {
  BANK_ROOM_ID,
  TUTORIAL_USERNAME,
  readE2ePlayerState,
  relogTutorialCharacter,
  resetTutorialCharacterInDatabase,
} from '../fixtures/tutorial';

const SITTING = { command: 'sit', position: 'sitting', message: /You settle into a seated position/i } as const;
const LYING = { command: 'lie', position: 'lying', message: /You stretch out and lie down/i } as const;

const CASES = [
  { title: 'standing', before: null },
  { title: 'sitting', before: SITTING },
  { title: 'lying', before: LYING },
] as const;

test.describe.serial('Posture survives a logout and login', () => {
  let contexts: PlayerContext[];
  let tutorial: PlayerContext;

  test.beforeAll(async ({ browser }) => {
    // E2ETutorial must be reset before its first login.
    await resetTutorialCharacterInDatabase();
    contexts = await createMultiPlayerContexts(browser, [TUTORIAL_USERNAME]);
    [tutorial] = contexts;
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  const position = async () => (await readE2ePlayerState(TUTORIAL_USERNAME)).position;

  async function settleInto(before: (typeof CASES)[number]['before']): Promise<void> {
    if (!before) return;
    await executeCommand(tutorial.page, before.command);
    await waitForMessage(tutorial.page, before.message, 20000);
    await expect.poll(position, { timeout: 15000 }).toBe(before.position);
  }

  for (const { title, before } of CASES) {
    test(`a character ${title} when they leave with Exit the Realm comes back sitting`, async () => {
      test.setTimeout(240000);

      // Reset, then placed in the bank (which also takes the character out of the tutorial) and logged in standing.
      await relogTutorialCharacter(tutorial, true, BANK_ROOM_ID);
      expect(await position()).toBe('standing');

      await settleInto(before);
      // The relog helper leaves with the Exit the Realm button, then logs in again: no reset, no placement.
      await relogTutorialCharacter(tutorial, false);

      await expect
        .poll(position, { timeout: 15000, message: 'the logout did not leave the character sitting' })
        .toBe('sitting');
    });
  }
});
