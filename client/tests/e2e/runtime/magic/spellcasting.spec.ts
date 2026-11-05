/**
 * Spellcasting, end to end: learning, the gates that refuse a cast, an instant self-heal and a delayed
 * Mythos spell that moves MP between two players.
 *
 * Three things keep it deterministic:
 * - INT 100: a cast rolls d100 against INT + mastery, and a failed roll still pays the costs.
 * - MP above the maximum: regeneration only runs below it, so a cost can be asserted exactly.
 * - Spells stay learned between runs (nothing resets player_spells), so learning accepts "already know",
 *   and the "not learned" gate uses a spell this spec never teaches.
 */

import { type Page } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  ensureFreshMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  resetPlayersToMainFoyer,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { despawnSanitariumCultists, ensurePlayableAlive, ensureStanding } from '../fixtures/player';
import { adoptSharedPlayers, expect, test } from '../fixtures/shared-session';
import { readE2ePlayerState, say, type E2ePlayerState } from '../fixtures/tutorial';

const CASTER = 'ArkanWolfshade';
const TARGET = 'Ithaqua';

/** Seeded in data/db/seed.sql; the spec depends on these costs. */
const HEAL_SELF_MP = 1;
const BIND_WOUND_MP = 4;
const POWER_DRAIN_MP = 14;
const POWER_DRAIN_AMOUNT = 10;

async function adminSet(admin: PlayerContext, stat: string, name: string, value: number): Promise<void> {
  await say(
    admin,
    `admin set ${stat} ${name} ${value}`,
    new RegExp(`Set .+['’]s ${stat} from .+ to ${value}`, 'i'),
    45000
  );
}

/** Set MP and wait until it is stored: the same reply may already be in the log from an earlier test. */
async function setMp(admin: PlayerContext, name: string, value: number): Promise<void> {
  await adminSet(admin, 'MP', name, value);
  await expect.poll(() => readE2ePlayerState(name).magic_points, { timeout: 15000 }).toBe(value);
}

async function learn(player: PlayerContext, spellId: string): Promise<void> {
  await say(player, `learn ${spellId}`, /You have learned|You already know/i, 20000);
}

async function expectMpMeter(page: Page, shown: RegExp): Promise<void> {
  await expect(page.getByTestId('magic-points-meter').locator('strong')).toHaveText(shown, { timeout: 20000 });
}

test.describe('Spellcasting', { tag: '@shared-session' }, () => {
  test.describe.configure({ mode: 'serial', timeout: 300_000 });

  let contexts: PlayerContext[];
  let caster: PlayerContext;
  let target: PlayerContext;
  let casterBefore: E2ePlayerState;
  let targetBefore: E2ePlayerState;

  test.beforeAll(async ({ browser, sharedPlayers }) => {
    test.setTimeout(300_000);
    contexts = await adoptSharedPlayers(browser, sharedPlayers);
    contexts = await ensureFreshMultiPlayerContexts(browser, contexts, [CASTER, TARGET]);
    await resetPlayersToMainFoyer(contexts);
    [caster, target] = contexts;
    await ensurePlayerInGame(caster, 30000);
    caster.page = await ensurePlayableAlive(caster.page, caster.player.username, caster.player.password);
    await despawnSanitariumCultists(caster.page);
    caster.page = await ensureStanding(caster.page, 8000);
    await ensureMultiplayerCoLocated(contexts);

    casterBefore = readE2ePlayerState(CASTER);
    targetBefore = readE2ePlayerState(TARGET);
    await adminSet(caster, 'INT', CASTER, 100);
    await say(caster, `admin setlucidity ${CASTER} 100`, /Set .+['’]s LCD from \d+ to 100/i, 45000);
  });

  test.afterAll(async () => {
    // These two characters are shared with other specs: leave them as they were.
    await adminSet(caster, 'INT', CASTER, casterBefore.intelligence ?? 50);
    await adminSet(caster, 'DP', CASTER, casterBefore.current_dp ?? 20);
    await adminSet(caster, 'MP', CASTER, casterBefore.magic_points ?? 10);
    await adminSet(caster, 'MP', TARGET, targetBefore.magic_points ?? 10);
    await adminSet(caster, 'corruption', CASTER, casterBefore.corruption ?? 0);
    await say(caster, `admin setlucidity ${CASTER} ${casterBefore.current_lcd ?? 100}`, /Set .+['’]s LCD from/i, 45000);
  });

  test('a spell the caster has not learned is refused', async () => {
    const mp = (readE2ePlayerState(CASTER).max_magic_points ?? 10) + 5;
    await setMp(caster, CASTER, mp);

    await say(caster, 'cast clerical_blessing', /You have not learned Blessing/i);

    expect(readE2ePlayerState(CASTER).magic_points).toBe(mp); // a refused cast costs nothing
  });

  test('a learned spell appears in the spell list', async () => {
    await learn(caster, 'heal_self');

    await executeCommand(caster.page, 'spells');

    await expect(caster.page.getByText(/Heal Self - Mastery: \d+%/).first()).toBeVisible({ timeout: 20000 });
  });

  test('an instant heal spends its MP and restores DP, and the meters follow', async () => {
    const maxMp = readE2ePlayerState(CASTER).max_magic_points ?? 10;
    const mpBefore = maxMp + 5;
    await setMp(caster, CASTER, mpBefore);
    await adminSet(caster, 'DP', CASTER, 5);
    await expect.poll(() => readE2ePlayerState(CASTER).current_dp, { timeout: 15000 }).toBe(5);

    await executeCommand(caster.page, 'cast heal_self');

    // Above the maximum nothing regenerates, so this is exactly the spell's cost.
    await expect.poll(() => readE2ePlayerState(CASTER).magic_points, { timeout: 15000 }).toBe(mpBefore - HEAL_SELF_MP);
    await expectMpMeter(caster.page, new RegExp(`^${mpBefore - HEAL_SELF_MP}\\s*/\\s*${maxMp}$`));
    await expect.poll(() => readE2ePlayerState(CASTER).current_dp, { timeout: 15000 }).toBeGreaterThan(5);
    const healedDp = readE2ePlayerState(CASTER).current_dp;
    await expect(caster.page.getByTestId('health-meter').getByRole('meter')).toHaveAttribute(
      'aria-valuenow',
      String(healedDp),
      { timeout: 20000 }
    );
  });

  test('a drained caster sees 0 MP and cannot cast', async () => {
    const maxMp = readE2ePlayerState(CASTER).max_magic_points ?? 10;
    await learn(caster, 'bind_wound');

    await adminSet(caster, 'MP', CASTER, 0);

    // Regeneration may already have added one by now, but never the 4 this spell costs.
    await expectMpMeter(caster.page, new RegExp(`^[01]\\s*/\\s*${maxMp}$`));
    await say(caster, 'cast bind_wound', new RegExp(`Not enough magic points. You need ${BIND_WOUND_MP} MP`, 'i'));
    expect(readE2ePlayerState(CASTER).magic_points).toBeLessThanOrEqual(1);
  });

  test('Power Drain moves MP from the target to the caster, and both meters follow', async () => {
    const casterMax = readE2ePlayerState(CASTER).max_magic_points ?? 10;
    const targetMax = readE2ePlayerState(TARGET).max_magic_points ?? 10;
    const casterMp = POWER_DRAIN_MP + 6;
    const targetMp = targetMax + 2;
    await learn(caster, 'power_drain');
    await setMp(caster, CASTER, casterMp);
    await setMp(caster, TARGET, targetMp);
    const corruptionBefore = readE2ePlayerState(CASTER).corruption ?? 0;

    await say(caster, `cast power_drain ${TARGET}`, /Power Drain/i);
    await waitForMessage(caster.page, new RegExp(`Drained \\d+ magic points from ${TARGET}`, 'i'), 30000);

    // Mastery can raise the amount on a re-run, and the target may regenerate one: both only make these looser.
    const targetAtMost = targetMp - POWER_DRAIN_AMOUNT + 1;
    await expect
      .poll(() => readE2ePlayerState(TARGET).magic_points, { timeout: 15000 })
      .toBeLessThanOrEqual(targetAtMost);
    // The caster pays the cost, then gains what was drained, up to their maximum.
    const casterExpected = Math.min(casterMax, casterMp - POWER_DRAIN_MP + POWER_DRAIN_AMOUNT);
    await expect
      .poll(() => readE2ePlayerState(CASTER).magic_points, { timeout: 15000 })
      .toBeGreaterThanOrEqual(casterExpected);
    await expectMpMeter(caster.page, new RegExp(`^${readE2ePlayerState(CASTER).magic_points}\\s*/\\s*${casterMax}$`));
    await expectMpMeter(target.page, new RegExp(`^\\d\\s*/\\s*${targetMax}$`));

    // A Mythos spell's other costs. Lucidity is written lazily, so it can lag the reply by a sweep.
    await expect
      .poll(() => readE2ePlayerState(CASTER).corruption ?? 0, { timeout: 15000 })
      .toBeGreaterThan(corruptionBefore);
    await expect.poll(() => readE2ePlayerState(CASTER).current_lcd ?? 100, { timeout: 15000 }).toBeLessThan(100);
  });
});
