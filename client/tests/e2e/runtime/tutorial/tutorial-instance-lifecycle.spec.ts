/**
 * Tutorial bedroom lifecycle: a private, ephemeral instance per player.
 *
 * - Leaving the bedroom completes `leave_the_tutorial`, moves respawn to the Main Foyer, and the
 *   foyer has no way back into the bedroom template (its old `up` exit is gone).
 * - Whatever a player leaves on the bedroom floor goes to the foyer's Lost-and-Found Chest when the
 *   instance is flushed (on leaving, or on really logging out), and anyone can take it from there.
 * - Logging out inside the bedroom and back in gives a brand new instance.
 *
 * Every test starts with E2ETutorial reset into the tutorial (fixtures/tutorial.ts) and
 * ArkanWolfshade standing in the Main Foyer.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  resetPlayersToMainFoyer,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { DEFAULT_RESPAWN_ROOM, DEFAULT_SPAWN_LOOK_CUE } from '../fixtures/test-data';
import {
  EMPTY_FLOOR_CUE,
  TUTORIAL_BEDROOM_LOOK_CUE,
  TUTORIAL_USERNAME,
  readE2ePlayerState,
  relogTutorialCharacter,
  resetTutorialCharacterInDatabase,
  startFreshTutorial,
} from '../fixtures/tutorial';

const CHEST_CUE = /Lost-and-Found Chest/i;

/** The most recent message matching `cue` (the log keeps earlier `look`s). */
async function latestMessage(page: PlayerContext['page'], cue: RegExp): Promise<string> {
  const matches = (await getMessages(page)).filter(message => cue.test(message));
  return matches[matches.length - 1] ?? '';
}

/** ArkanWolfshade takes the Sling out of the foyer chest, then puts it back (keeps AW's inventory unchanged). */
async function awTakesSlingFromChest(aw: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'get sling from chest');
  // The reply names the container as typed ("chest"), not the furniture's full name.
  await waitForMessage(aw.page, /You get 1x Sling from chest/i, 15000);
  await executeCommand(aw.page, 'put sling into chest');
  await waitForMessage(aw.page, /You put 1x Sling into chest/i, 15000);
}

test.describe.serial('Tutorial bedroom lifecycle', () => {
  let contexts: PlayerContext[];
  let aw: PlayerContext;
  let tutorial: PlayerContext;

  test.beforeAll(async ({ browser }) => {
    // E2ETutorial must be in tutorial state before its first login.
    resetTutorialCharacterInDatabase();
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', TUTORIAL_USERNAME]);
    [aw, tutorial] = contexts;
  });

  test.beforeEach(async () => {
    await resetPlayersToMainFoyer([aw]);
    await startFreshTutorial(tutorial);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('leaving the bedroom completes the tutorial and moves respawn to the Main Foyer', async () => {
    const inTutorial = readE2ePlayerState(TUTORIAL_USERNAME);
    expect(inTutorial.tutorial_instance_id).toBeTruthy();
    expect(inTutorial.current_room_id).toMatch(/^instance_/);

    await executeCommand(tutorial.page, 'go down');
    await waitForMessage(tutorial.page, /Quest completed: Leave the Tutorial/i, 20000);

    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, DEFAULT_SPAWN_LOOK_CUE, 20000);
    const foyer = await latestMessage(tutorial.page, /Exits:/i);
    expect(foyer).toMatch(CHEST_CUE);
    expect(foyer).not.toMatch(/Exits:[^\n]*\bup\b/i);

    await expect
      .poll(() => readE2ePlayerState(TUTORIAL_USERNAME), { timeout: 15000 })
      .toMatchObject({ respawn_room_id: DEFAULT_RESPAWN_ROOM, tutorial_instance_id: null });
  });

  test('bedroom floor items go to the foyer Lost-and-Found Chest, and another player can take them', async () => {
    await executeCommand(tutorial.page, 'drop 1');
    await waitForMessage(tutorial.page, /You drop 1x Sling/i, 15000);

    await executeCommand(tutorial.page, 'go down');
    await waitForMessage(tutorial.page, /Quest completed: Leave the Tutorial/i, 20000);
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id, { timeout: 15000 }).toBeNull();

    await awTakesSlingFromChest(aw);
  });

  test('logging out in the bedroom gives a fresh instance on return; the floor items go to the chest', async () => {
    const firstInstance = readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id;
    await executeCommand(tutorial.page, 'drop 1');
    await waitForMessage(tutorial.page, /You drop 1x Sling/i, 15000);

    // A real logout (not a grace-period blip) flushes the instance; logging back in builds a new one.
    await relogTutorialCharacter(tutorial, false);
    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, TUTORIAL_BEDROOM_LOOK_CUE, 20000);
    const freshBedroom = await latestMessage(tutorial.page, TUTORIAL_BEDROOM_LOOK_CUE);
    expect(freshBedroom).toMatch(EMPTY_FLOOR_CUE);
    expect(freshBedroom).not.toMatch(/Sling/i);

    const secondInstance = readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id;
    expect(secondInstance).toBeTruthy();
    expect(secondInstance).not.toBe(firstInstance);

    await awTakesSlingFromChest(aw);
  });
});
