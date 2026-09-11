/**
 * Scenario CORR-02: Room Corruption Flux -- Purification (#824)
 *
 * End-to-end proof for #815 PR-5's room corruption flux mechanic, purifying half: seeds a known
 * corruption value via `admin set`, walks the player into the Sanitarium Chapel (a consecrated
 * room authored for #824 with attributes.corruption: 0 / corruption_rate: 0.10), and confirms two
 * things the unit suite can only assert against mocks:
 *   1. the client's chat-pane perceptual filter (`--corruption-intensity`, ADR-025) actually falls
 *      while the player lingers in the room, driven by the real tick loop and the real
 *      apply_corruption_adjustment write path (reason_code: "room_flux") -- not a synthetic tick.
 *   2. it stops falling exactly at the bottom of the player's current tier (50, the CORRUPTED
 *      floor) rather than continuing down toward the room's target of 0 -- only `/cleanse` crosses
 *      a tier boundary downward (see PassiveCorruptionFluxService._tier_floor).
 *
 * The raising half (a lingering player converging upward toward a corrupt room's target, e.g. the
 * Innsmouth Waterfront Pier) is covered by a server-side unit test
 * (test_innsmouth_pier_converges_upward_and_clamps_at_its_own_ceiling) rather than a second e2e
 * walk -- the walk to Innsmouth is long, and the ceiling-clamp mechanism is identical code to the
 * floor-clamp mechanism this spec already exercises against the real tick loop.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, recoverPlayableSession, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureFreshMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  type PlayerContext,
} from '../fixtures/multiplayer';
import {
  despawnSanitariumCultists,
  ensurePlayableAlive,
  goEastFromFoyer,
  prepareForDirectionalMove,
} from '../fixtures/player';
import { CHAPEL_LOOK_CUE } from '../fixtures/test-data';

// CORRUPTED tier is >= 50; seeding just above its floor means one drop (-2) lands exactly on the
// floor, and a further wait proves the room stops there instead of continuing toward its own
// target of 0 -- the same seed/margin choice corruption-cleanse.spec.ts uses for its tier-crossing
// assertion, reused here for the opposite (within-tier, no crossing) case.
const SEED_CORRUPTION = 52;
const CHAPEL_FLOOR = 50; // CORRUPTED tier floor -- PassiveCorruptionFluxService._tier_floor(52).

const ADMIN_SET_SUCCESS = new RegExp(`Set .+['’]s [Cc]orruption from \\d+ to ${SEED_CORRUPTION}`, 'i');
// Chapel rate is 0.10 -> one point every (1 / 0.10) * 0.6s = 6s; two points plus tick-cadence and
// network slack comfortably fits inside a minute.
const FLOOR_POLL_TIMEOUT = 60_000;
// Long enough to cover several more tick cycles at the chapel's rate (6s/point) without the value
// moving past the floor -- proves the clamp holds rather than merely happening to be checked once.
const HOLD_AT_FLOOR_MS = 20_000;

async function corruptionIntensity(page: Page): Promise<string> {
  const panel = page.getByTestId('chat-history-panel');
  await panel.waitFor({ state: 'visible', timeout: 15000 });
  return panel.evaluate(el => (el as HTMLElement).style.getPropertyValue('--corruption-intensity'));
}

async function prepAwForRoomFluxTest(awContext: PlayerContext): Promise<void> {
  await awContext.page.bringToFront().catch(() => {});
  await ensurePlayerInGame(awContext, 30000);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  await despawnSanitariumCultists(awContext.page);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
}

async function seedCorruption(awContext: PlayerContext, characterName: string): Promise<void> {
  const runSeed = async (): Promise<void> => {
    await executeCommand(awContext.page, `admin set corruption ${characterName} ${SEED_CORRUPTION}`);
    await waitForMessage(awContext.page, ADMIN_SET_SUCCESS, 45000);
  };
  try {
    await runSeed();
  } catch {
    awContext.page = await recoverPlayableSession(
      awContext.page,
      awContext.player.username,
      awContext.player.password,
      45000
    );
    await runSeed();
  }
}

/** Foyer -> chapel is 6 "east" hops total; goEastFromFoyer already covers the first (foyer -> Eastern
 * Hallway Section 1), landing through hallway_003/005/007 to hallway_009 and finally the chapel. */
async function walkToChapel(page: Page): Promise<Page> {
  let live = await goEastFromFoyer(page);
  for (let hop = 0; hop < 4; hop += 1) {
    live = await prepareForDirectionalMove(live);
    await executeCommand(live, 'go east');
    await waitForMessage(live, /You (move|go) east|Eastern Hallway/i, 20000);
  }
  live = await prepareForDirectionalMove(live);
  await executeCommand(live, 'go east');
  await waitForMessage(live, /You (move|go) east|Sanitarium Chapel/i, 20000);
  await executeCommand(live, 'look').catch(() => {});
  await expect(live.getByText(CHAPEL_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  return live;
}

test.describe('Room Corruption Flux -- Purification (#824)', () => {
  test.describe.configure({ timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(300_000);
    // ArkanWolfshade is the seeded admin test player -- admin set targets itself here.
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('lingering in the Sanitarium Chapel purifies down to, and stops at, the tier floor', async ({ browser }) => {
    test.setTimeout(300_000);
    contexts = await ensureFreshMultiPlayerContexts(browser, contexts, ['ArkanWolfshade']);
    const awContext = contexts[0];

    await prepAwForRoomFluxTest(awContext);
    await seedCorruption(awContext, 'ArkanWolfshade');

    await expect
      .poll(() => corruptionIntensity(awContext.page), {
        message: '--corruption-intensity should reflect the seeded corruption value before moving',
        timeout: 15000,
      })
      .toBe((SEED_CORRUPTION / 100).toString());

    awContext.page = await walkToChapel(awContext.page);

    await expect
      .poll(() => corruptionIntensity(awContext.page), {
        message: 'lingering in the chapel should purify corruption down to the CORRUPTED tier floor',
        timeout: FLOOR_POLL_TIMEOUT,
      })
      .toBe((CHAPEL_FLOOR / 100).toString());

    // Hold here: the chapel's target is 0, but a room may not cross a tier boundary downward on
    // its own (_tier_floor) -- only /cleanse does that. Confirm the value does not keep falling.
    await new Promise(resolve => setTimeout(resolve, HOLD_AT_FLOOR_MS));
    await expect(corruptionIntensity(awContext.page)).resolves.toBe((CHAPEL_FLOOR / 100).toString());
  });
});
