/**
 * Tutorial bedroom lifecycle: a private, ephemeral instance per player.
 *
 * - Leaving the bedroom completes `leave_the_tutorial`, moves respawn to the Main Foyer, and the
 *   foyer has no way back into the bedroom template (its old `up` exit is gone).
 * - Whatever a player leaves on the bedroom floor goes to that player's own bank deposit box when the
 *   instance is flushed (on leaving, or on really logging out). Nobody else can take it: the shared
 *   foyer Lost-and-Found Chest no longer receives it. The owner gets it back at the bank.
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
  BANK_LOOK_CUE,
  BANK_ROOM_ID,
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

/**
 * The tutorial leaver's Sling must not be in the shared foyer chest: ArkanWolfshade finds none there.
 * (The reply names the container as typed ("chest"), not the furniture's full name.)
 */
async function awFindsNoSlingInChest(aw: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'get sling from chest');
  await waitForMessage(aw.page, /You don't see 'sling' in chest/i, 15000);
}

/** E2ETutorial drops its Sling in the bedroom and walks out: the flush banks it in their own box. */
async function dropSlingAndLeave(tutorial: PlayerContext): Promise<void> {
  await executeCommand(tutorial.page, 'drop 1');
  await waitForMessage(tutorial.page, /You drop 1x Sling/i, 15000);

  await executeCommand(tutorial.page, 'go down');
  await waitForMessage(tutorial.page, /Quest completed: Leave the Tutorial/i, 20000);
  await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id, { timeout: 15000 }).toBeNull();
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

  test("bedroom floor items go to the leaver's own deposit box, not the shared chest", async () => {
    await dropSlingAndLeave(tutorial);

    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);
    await awFindsNoSlingInChest(aw);
  });

  test('the owner can list, withdraw and re-deposit what they left behind, but only at a bank', async () => {
    await dropSlingAndLeave(tutorial);
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);

    // The foyer is not a bank: the commands refuse there.
    await executeCommand(tutorial.page, 'bank');
    await waitForMessage(tutorial.page, /You must be at a bank to do that/i, 15000);

    // The Sanitarium is far from downtown Arkham, so log back in standing in the bank.
    await relogTutorialCharacter(tutorial, false, BANK_ROOM_ID);
    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, BANK_LOOK_CUE, 20000);

    await executeCommand(tutorial.page, 'bank');
    await waitForMessage(tutorial.page, /Your deposit box at Arkham Savings & Trust \(1\/100\):/i, 15000);
    expect(await latestMessage(tutorial.page, /Your deposit box at Arkham Savings & Trust/i)).toMatch(/1\. 1x Sling/);

    await executeCommand(tutorial.page, 'withdraw sling');
    await waitForMessage(tutorial.page, /The clerk returns 1x Sling from your deposit box/i, 15000);
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual([]);

    await executeCommand(tutorial.page, 'bank');
    await waitForMessage(tutorial.page, /Your deposit box at Arkham Savings & Trust is empty/i, 15000);

    await executeCommand(tutorial.page, 'deposit sling');
    await waitForMessage(tutorial.page, /The clerk files 1x Sling away in your deposit box/i, 15000);
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);
  });

  test('logging out in the bedroom gives a fresh instance on return; the floor items go to the deposit box', async () => {
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

    // The first instance's Sling was flushed into the deposit box on logout, not into the shared chest.
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);
    await awFindsNoSlingInChest(aw);
  });
});
