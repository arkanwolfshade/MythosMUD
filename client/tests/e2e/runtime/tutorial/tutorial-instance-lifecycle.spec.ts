/**
 * First Exposure instance lifecycle: a private, ephemeral instance per player.
 *
 * - A new character gets their own instance at Independence Square, with the first quest started, and the
 *   tutorial has no way out: the square has only the walk east.
 * - Whatever a player leaves on an instance floor goes to that player's own bank deposit box when the instance
 *   is flushed (here, on really logging out). Nobody else can take it: the shared foyer Lost-and-Found Chest
 *   does not receive it. The owner gets it back at the bank.
 * - Logging out inside the tutorial and back in gives a brand new instance.
 *
 * Every test starts with E2ETutorial reset to the start of the tutorial (fixtures/tutorial.ts) and
 * ArkanWolfshade standing in the Main Foyer. (The whole tutorial, start to finish, is first-exposure.spec.ts.)
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  resetPlayersToMainFoyer,
  type PlayerContext,
} from '../fixtures/multiplayer';
import {
  BANK_LOOK_CUE,
  BANK_ROOM_ID,
  EMPTY_FLOOR_CUE,
  TUTORIAL_SQUARE_LOOK_CUE,
  TUTORIAL_USERNAME,
  readE2ePlayerState,
  relogTutorialCharacter,
  resetTutorialCharacterInDatabase,
  startFreshTutorial,
  tutorialRoomPattern,
} from '../fixtures/tutorial';

/** The most recent message matching `cue` (the log keeps earlier `look`s). */
async function latestMessage(page: PlayerContext['page'], cue: RegExp): Promise<string> {
  const matches = (await getMessages(page)).filter(message => cue.test(message));
  return matches[matches.length - 1] ?? '';
}

/**
 * The tutorial character's Sling must not be in the shared foyer chest: ArkanWolfshade finds none there.
 * (The reply names the container as typed ("chest"), not the furniture's full name.)
 */
async function awFindsNoSlingInChest(aw: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'get sling from chest');
  await waitForMessage(aw.page, /You don't see 'sling' in chest/i, 15000);
}

/** E2ETutorial drops its Sling on the floor, then really logs out and back in: the flush banks it in their own box. */
async function dropSlingAndRelog(tutorial: PlayerContext): Promise<void> {
  await executeCommand(tutorial.page, 'drop 1');
  await waitForMessage(tutorial.page, /You drop 1x Sling/i, 15000);
  await relogTutorialCharacter(tutorial, false);
}

test.describe.serial('First Exposure instance lifecycle', () => {
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

  test('a new character gets their own instance at the square, with the first quest started and no way out', async () => {
    const started = readE2ePlayerState(TUTORIAL_USERNAME);
    expect(started.tutorial_instance_id).toBeTruthy();
    expect(started.tutorial_instance_id).not.toBe('pending');
    expect(started.current_room_id).toMatch(tutorialRoomPattern('independence_square'));
    await expect
      .poll(() => readE2ePlayerState(TUTORIAL_USERNAME).quests, { timeout: 15000 })
      .toMatchObject({ first_exposure_dusk: 'active' });

    // Only the walk east: the tutorial has no exit, and delirium is the only way out.
    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE, 20000);
    // Only the Exits line: the room description above it uses words like "up".
    const exits = (await latestMessage(tutorial.page, /Exits:/i)).match(/Exits:\s*(.*)$/im)?.[1] ?? '';
    expect(exits).toMatch(/\beast\b/i);
    expect(exits).not.toMatch(/\b(north|south|west|up|down)\b/i);
  });

  test('logging out in the tutorial gives a fresh instance on return; the floor items go to the deposit box', async () => {
    const firstInstance = readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id;

    await dropSlingAndRelog(tutorial);
    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE, 20000);
    const freshSquare = await latestMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE);
    expect(freshSquare).toMatch(EMPTY_FLOOR_CUE);
    expect(freshSquare).not.toMatch(/Sling/i);

    const secondInstance = readE2ePlayerState(TUTORIAL_USERNAME).tutorial_instance_id;
    expect(secondInstance).toBeTruthy();
    expect(secondInstance).not.toBe(firstInstance);

    // The first instance's Sling was flushed into the deposit box on logout, not into the shared chest.
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);
    await awFindsNoSlingInChest(aw);
  });

  test('restarting in a fresh instance starts the run over: first act active, later acts not started, vitals restored', async () => {
    const before = readE2ePlayerState(TUTORIAL_USERNAME);

    // Get a step into the run: walking east off the square makes progress on the first act.
    await executeCommand(tutorial.page, 'go east');
    await waitForMessage(tutorial.page, /Lamplighter offers a wary nod in greeting/i, 20000);
    expect(readE2ePlayerState(TUTORIAL_USERNAME).current_room_id).toMatch(tutorialRoomPattern('gravel_walk'));

    await relogTutorialCharacter(tutorial, false);
    await executeCommand(tutorial.page, 'look');
    await waitForMessage(tutorial.page, TUTORIAL_SQUARE_LOOK_CUE, 20000);

    // The square again, the first act running again; the later acts reset to not started (abandoned rows are hidden).
    expect(readE2ePlayerState(TUTORIAL_USERNAME).current_room_id).toMatch(tutorialRoomPattern('independence_square'));
    await expect
      .poll(() => readE2ePlayerState(TUTORIAL_USERNAME).quests, { timeout: 15000 })
      .toMatchObject({ first_exposure_dusk: 'active' });
    const after = readE2ePlayerState(TUTORIAL_USERNAME);
    for (const later of ['first_exposure_burying_ground', 'first_exposure_below']) {
      expect(['active', 'completed']).not.toContain(after.quests[later]);
    }
    // Full DP and the starting lucidity; corruption is a floor and is left alone.
    expect(after.current_dp).toBe(before.current_dp);
    expect(after.current_lcd).toBe(100);
    expect(after.corruption).toBe(before.corruption);
  });

  test('the owner can list, withdraw and re-deposit what an instance banked, but only at a bank', async () => {
    await dropSlingAndRelog(tutorial);
    await expect.poll(() => readE2ePlayerState(TUTORIAL_USERNAME).bank_items, { timeout: 15000 }).toEqual(['Sling']);

    // The tutorial is not a bank: the commands refuse there.
    await executeCommand(tutorial.page, 'bank');
    await waitForMessage(tutorial.page, /You must be at a bank to do that/i, 15000);

    // The Sanitarium is far from downtown Arkham, so log back in standing in the bank (out of the tutorial).
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
});
