/**
 * First Exposure: the whole tutorial, played through the real client from Independence Square to Dr. Morgan.
 *
 * One long serial test, because every step depends on the last: the walk and the dusk quest, the hostile
 * ghoul that cannot be beaten (it breaks off once the player is hurt enough), the friendly ghoul that mends
 * them and leaves corruption at 1, the jade amulet, the gated stair, the coffin that starts the Hound, delirium,
 * the Recovery Ward, and the debrief. Server state is asserted straight from Postgres at each milestone
 * (scripts/e2e_player_state.py), never inferred from what the client happens to render.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { cleanupMultiPlayerContexts, createMultiPlayerContexts, type PlayerContext } from '../fixtures/multiplayer';
import { DEFAULT_RESPAWN_ROOM } from '../fixtures/test-data';
import {
  RECOVERY_WARD_LOOK_CUE,
  RECOVERY_WARD_ROOM_ID,
  TUTORIAL_USERNAME,
  readE2ePlayerState,
  resetTutorialCharacterInDatabase,
  startFreshTutorial,
  tutorialRoomPattern,
} from '../fixtures/tutorial';

const state = () => readE2ePlayerState(TUTORIAL_USERNAME);
const exactRoom = (roomId: string): RegExp => new RegExp(`^${roomId}$`);

/** Walk one step and wait until the server has the player in the expected room. */
async function walk(player: PlayerContext, direction: string, room: RegExp): Promise<void> {
  await executeCommand(player.page, `go ${direction}`);
  await expect
    .poll(() => state().current_room_id, { timeout: 20000, message: `after "go ${direction}"` })
    .toMatch(room);
}

/** Say a command and wait for a line of the reply. */
async function say(player: PlayerContext, command: string, reply: RegExp, timeout = 20000): Promise<void> {
  await executeCommand(player.page, command);
  await waitForMessage(player.page, reply, timeout);
}

test.describe.serial('First Exposure: the whole tutorial', () => {
  let contexts: PlayerContext[];
  let tutorial: PlayerContext;

  test.beforeAll(async ({ browser }) => {
    // E2ETutorial must be reset before its first login.
    resetTutorialCharacterInDatabase();
    contexts = await createMultiPlayerContexts(browser, [TUTORIAL_USERNAME]);
    [tutorial] = contexts;
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('from the square to the ward and Dr. Morgan', async () => {
    test.setTimeout(540000);

    await test.step('Act I, Dusk: the square, the lamplighter, the newspaper, the lane', async () => {
      await startFreshTutorial(tutorial);
      await expect.poll(() => state().quests, { timeout: 15000 }).toMatchObject({ first_exposure_dusk: 'active' });
      // Quest notices arrive on the quest channel, not the system channel.
      await waitForMessage(tutorial.page, /\[QUEST\] Quest started: An Evening Walk/, 20000);
      // The Journal refreshes on progress without the player typing `journal`: the opening `look` met cmd_look.
      await expect(tutorial.page.getByTestId('game-panel-questLog')).toContainText('cmd_look: done', {
        timeout: 15000,
      });

      await walk(tutorial, 'east', tutorialRoomPattern('gravel_walk'));
      await say(tutorial, 'talk lamplighter', /Mind the gravel/i);
      await say(tutorial, 'talk 1', /Strays, the constable says/i);

      await walk(tutorial, 'east', tutorialRoomPattern('beneath_the_limes'));
      await executeCommand(tutorial.page, 'get advertiser');
      await expect.poll(() => state().inventory_items, { timeout: 15000 }).toContain('Arkham Advertiser');
      await say(tutorial, 'read advertiser', /GRAVES OPENED AGAIN/i);

      await walk(tutorial, 'east', tutorialRoomPattern('lane_off_the_square'));
      await walk(tutorial, 'east', tutorialRoomPattern('burying_ground_gate'));
      await waitForMessage(tutorial.page, /Quest completed: An Evening Walk/i, 20000);
      await expect
        .poll(() => state().quests, { timeout: 15000 })
        .toMatchObject({ first_exposure_dusk: 'completed', first_exposure_burying_ground: 'active' });
    });

    await test.step('Act II, the Burying Ground: a ghoul that cannot be beaten, and one that mends', async () => {
      await walk(tutorial, 'east', tutorialRoomPattern('leaning_stones'));
      // The Ragged Ghoul attacks on sight and breaks off once the player is hurt enough: the fight is not winnable.
      await waitForMessage(tutorial.page, /drops into the earth between the stones/i, 150000);
      const hurt = state();
      expect(hurt.current_dp).toBeGreaterThanOrEqual(1); // the no_death floor
      expect(hurt.current_lcd).toBeLessThan(100); // first sight of a ghoul costs lucidity
      expect(hurt.corruption).toBe(0); // only the friendly ghoul touches corruption

      await walk(tutorial, 'east', tutorialRoomPattern('old_yew'));
      // The Pale Ghoul speaks first (behavior_config.initiates_dialogue): no `talk ghoul` needed.
      await waitForMessage(tutorial.page, /lifts one hand, slowly/i, 20000);
      await say(tutorial, 'talk 1', /Its long fingers close over your wrist/i);
      await expect.poll(() => state().corruption, { timeout: 15000 }).toBe(1);
      await expect
        .poll(() => state().current_dp, { timeout: 40000, message: 'the heal-over-time effect restores DP' })
        .toBeGreaterThan(hurt.current_dp ?? 0);
      await say(tutorial, 'talk 1', /Bring it down the stair/i);

      await walk(tutorial, 'east', tutorialRoomPattern('robbed_grave'));
      await executeCommand(tutorial.page, 'get amulet');
      await expect.poll(() => state().inventory_items, { timeout: 15000 }).toContain('Jade Amulet');
      await waitForMessage(tutorial.page, /Quest completed: What the Robbers Stole/i, 20000);
    });

    await test.step('Act III, Below: the gated stair, the warrens, the coffin, the Hound', async () => {
      await walk(tutorial, 'south', tutorialRoomPattern('mausoleum_stair'));
      await walk(tutorial, 'down', tutorialRoomPattern('the_warrens'));
      await walk(tutorial, 'east', tutorialRoomPattern('charnel_gallery'));
      await walk(tutorial, 'east', tutorialRoomPattern('vault_of_the_owner'));
      await say(tutorial, 'put amulet in coffin', /something begins to bay/i);
      await expect.poll(() => state().inventory_items, { timeout: 15000 }).not.toContain('Jade Amulet');
      await waitForMessage(tutorial.page, /Quest completed: Not With Empty Hands/i, 20000);
      // Lucidity falls to -10 in about a minute and a half, then delirium.
      await waitForMessage(tutorial.page, /You realise the sound is following something/i, 60000);
    });

    await test.step('Delirium: acknowledge it and wake in the Recovery Ward', async () => {
      const acknowledge = tutorial.page.getByRole('button', { name: /Acknowledge your delirium/i });
      await expect(acknowledge).toBeVisible({ timeout: 150000 });
      await acknowledge.click();
      await say(tutorial, 'look', RECOVERY_WARD_LOOK_CUE, 30000);

      await expect
        .poll(() => state(), { timeout: 30000 })
        .toMatchObject({
          current_room_id: RECOVERY_WARD_ROOM_ID,
          tutorial_instance_id: null,
          current_lcd: 70,
          corruption: 1,
          debrief_pending: true,
        });
      const woken = state();
      expect(woken.inventory_items).toEqual(['Sling']); // the amulet is gone; nothing else was taken
      expect(woken.bank_items).toEqual([]); // and it did not end up in the bank
      expect(woken.quests).toMatchObject({
        first_exposure_dusk: 'completed',
        first_exposure_burying_ground: 'completed',
        first_exposure_below: 'completed',
        first_exposure_sanitarium: 'active',
      });
    });

    await test.step('Epilogue: follow the exit signs down to Dr. Morgan and be debriefed', async () => {
      await walk(tutorial, 'south', /recovery_hall_001$/);
      await walk(tutorial, 'west', /recovery_hall_002$/);
      await walk(tutorial, 'west', /main_staircase_001$/);
      await walk(tutorial, 'down', exactRoom(DEFAULT_RESPAWN_ROOM));

      await say(tutorial, 'talk morgan', /lucid enough to stand/i);
      await say(tutorial, 'talk 1', /debrief session concludes/i, 30000);
      await waitForMessage(tutorial.page, /Quest completed: Debrief/i, 20000);
      await expect
        .poll(() => state(), { timeout: 20000 })
        .toMatchObject({
          debrief_pending: false,
          respawn_room_id: DEFAULT_RESPAWN_ROOM,
          quests: expect.objectContaining({ first_exposure_sanitarium: 'completed' }),
        });
    });
  });
});
