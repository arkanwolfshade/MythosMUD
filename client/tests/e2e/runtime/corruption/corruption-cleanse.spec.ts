/**
 * Scenario CORR-01: Corruption Cleanse Rite
 *
 * End-to-end proof for #804's corruption subsystem: seeds a known corruption value via
 * `admin set`, verifies the client's chat-pane perceptual filter (`--corruption-intensity`,
 * ADR-025) reflects it, then exercises `/cleanse` end to end -- the CorruptionService write path,
 * the tier-crossing personal message, the live player_update push that keeps a connected client's
 * filter in sync (nothing else pushes corruption to the client), and the recovery cooldown.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, getMessages, recoverPlayableSession, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureFreshMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { despawnSanitariumCultists, ensurePlayableAlive } from '../fixtures/player';
import { DEFAULT_SPAWN_LOOK_CUE } from '../fixtures/test-data';

const SEED_CORRUPTION = 52; // Just above the "corrupted" floor (50) so one cleanse (-8) crosses down.
const AFTER_CLEANSE_CORRUPTION = SEED_CORRUPTION - 8; // 44, in the "marked" tier.

const ADMIN_SET_SUCCESS = new RegExp(`Set .+['’]s [Cc]orruption from \\d+ to ${SEED_CORRUPTION}`, 'i');
const CLEANSE_SUCCESS = /You complete the cleansing rite/i;
const CLEANSE_COOLDOWN = /cleansing rite still lingers in your blood/i;
const TIER_FALL_TO_MARKED = /taint loosens its grip/i;

async function assertLookVisible(page: Page): Promise<void> {
  await expect(page.getByText(DEFAULT_SPAWN_LOOK_CUE).first()).toBeVisible({ timeout: 45000 });
}

async function corruptionIntensity(page: Page): Promise<string> {
  const panel = page.getByTestId('chat-history-panel');
  await panel.waitFor({ state: 'visible', timeout: 15000 });
  return panel.evaluate(el => (el as HTMLElement).style.getPropertyValue('--corruption-intensity'));
}

async function prepAwForCorruptionTest(awContext: PlayerContext): Promise<void> {
  await awContext.page.bringToFront().catch(() => {});
  await ensurePlayerInGame(awContext, 30000);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  await despawnSanitariumCultists(awContext.page);
  awContext.page = await ensurePlayableAlive(awContext.page, awContext.player.username, awContext.player.password);
  await executeCommand(awContext.page, 'look');
  await assertLookVisible(awContext.page);
  await executeCommand(awContext.page, 'stand');
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

test.describe('Corruption Cleanse Rite (#804)', () => {
  test.describe.configure({ timeout: 300_000 });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    test.setTimeout(300_000);
    // ArkanWolfshade is the seeded admin test player -- admin set targets itself here, so no
    // second player is needed the way admin-set-stat-command.spec.ts needs one to test rejection.
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('seeding corruption updates the chat pane filter intensity', async ({ browser }) => {
    test.setTimeout(300_000);
    contexts = await ensureFreshMultiPlayerContexts(browser, contexts, ['ArkanWolfshade']);
    const awContext = contexts[0];

    await prepAwForCorruptionTest(awContext);
    await seedCorruption(awContext, 'ArkanWolfshade');

    await expect
      .poll(() => corruptionIntensity(awContext.page), {
        message: '--corruption-intensity should reflect the seeded corruption value',
        timeout: 15000,
      })
      .toBe((SEED_CORRUPTION / 100).toString());
  });

  test('/cleanse reduces corruption, crosses a tier, and pushes a live client update', async () => {
    const awContext = contexts[0];
    await awContext.page.bringToFront().catch(() => {});

    await executeCommand(awContext.page, 'cleanse');
    await waitForMessage(awContext.page, CLEANSE_SUCCESS, 45000);
    await waitForMessage(awContext.page, TIER_FALL_TO_MARKED, 45000);

    await expect
      .poll(() => corruptionIntensity(awContext.page), {
        message: '--corruption-intensity should reflect the post-cleanse value without a page reload',
        timeout: 15000,
      })
      .toBe((AFTER_CLEANSE_CORRUPTION / 100).toString());
  });

  test('a second immediate /cleanse is rejected on cooldown', async () => {
    const awContext = contexts[0];
    await awContext.page.bringToFront().catch(() => {});

    await executeCommand(awContext.page, 'cleanse');
    await waitForMessage(awContext.page, CLEANSE_COOLDOWN, 45000);
    const messages = await getMessages(awContext.page);
    expect(messages.some(msg => CLEANSE_COOLDOWN.test(msg))).toBe(true);
  });
});
