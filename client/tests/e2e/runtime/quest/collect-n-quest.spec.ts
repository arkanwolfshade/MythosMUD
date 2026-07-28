/**
 * collect_n quest E2E: ask / get / journal / turnin against a seeded example quest.
 *
 * Fixture below is content (sanitarium daisy + Dr. Morgan). Engine paths are generic.
 */

import { expect, test, type Page } from '@playwright/test';
import { spawnSync } from 'child_process';
import { join } from 'path';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import {
  ensurePlayableConnection,
  executeCommand,
  executeCommandWithoutRecovery,
  getMessages,
  loginPlayer,
  waitForMessage,
} from '../fixtures/auth';
import { ensureStanding } from '../fixtures/player';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

/** Example collect_n seed. Swap fields to exercise another definition without rewriting flow helpers. */
const COLLECT_N = {
  questId: 'gather_sanitarium_daisies',
  questTitle: 'Gather Sanitarium Daisies',
  prototypeId: 'misc.herb.sanitarium_daisy',
  itemGetAlias: 'daisy',
  itemDisplayName: 'Sanitarium Daisy',
  count: 3,
  npcSpawnId: 54,
  npcAskAlias: 'morgan',
  npcName: 'Dr. Francis Morgan',
  // generate_npc_id: name.lower().replace(' ', '_') -> dr._francis_morgan_<room>_<ts>_<n>
  npcInstanceIdRe: /dr\._francis_morgan_[a-z0-9_]+/gi,
  zone: 'arkhamcity/sanitarium',
} as const;

/** Quest-giver instance ids currently active in the fixture zone (authoritative vs stale Occupants UI). */
async function listActiveQuestGiverIds(page: Page): Promise<string[]> {
  await executeCommandWithoutRecovery(page, `npc zone ${COLLECT_N.zone}`);
  await waitForMessage(page, /NPC Zone Statistics/i, 15000).catch(() => {});
  const messages = await getMessages(page);
  const latest = [...messages].reverse().find(m => /NPC Zone Statistics/i.test(m));
  if (!latest) {
    return [];
  }
  const ids = new Set<string>();
  for (const match of latest.matchAll(COLLECT_N.npcInstanceIdRe)) {
    ids.add(match[0].replace(/npc$/i, ''));
  }
  return [...ids];
}

/** Despawn quest-giver instances only. Uses withoutRecovery to avoid login storms mid-setup. */
async function despawnQuestGiverInstances(page: Page): Promise<void> {
  const ids = await listActiveQuestGiverIds(page);
  for (const id of ids) {
    await executeCommandWithoutRecovery(page, `npc despawn ${id}`).catch(() => {});
  }
  await executeCommandWithoutRecovery(page, 'look').catch(() => {});
  await new Promise(r => setTimeout(r, 1500));
}

function resetCollectNQuestInstances(): void {
  loadE2eEnv();
  const scriptPath = join(E2E_PROJECT_ROOT, 'scripts', 'e2e_reset_collect_n_quest.py');
  const result = spawnSync('uv', ['run', 'python', scriptPath], {
    cwd: E2E_PROJECT_ROOT,
    encoding: 'utf-8',
    env: process.env,
  });
  if (result.status !== 0) {
    throw new Error(
      `e2e_reset_collect_n_quest.py failed (status ${result.status}): ${result.stdout ?? ''}\n${result.stderr ?? ''}`
    );
  }
}

async function assertQuestGiverVisible(page: Page): Promise<void> {
  await expect
    .poll(async () => (await listActiveQuestGiverIds(page)).length >= 1, {
      timeout: 30000,
      message: `Quest giver visible after npc spawn ${COLLECT_N.npcSpawnId}`,
    })
    .toBe(true);
}

/** Keep admin in foyer before npc spawn (spawn uses current room). */
async function ensureAdminInFoyer(page: Page): Promise<void> {
  await executeCommandWithoutRecovery(page, 'look').catch(() => {});
  const body = await page.locator('body').innerText();
  if (/Eastern Hallway|hallway, branching/i.test(body) && !/Main Foyer/i.test(body)) {
    await executeCommandWithoutRecovery(page, 'go west').catch(() => {});
    await waitForMessage(page, /You (move|go) west|Main Foyer|marble floor/i, 20000).catch(() => {});
  }
  if (/Eastern Hallway/i.test(await page.locator('body').innerText())) {
    await executeCommandWithoutRecovery(page, 'teleport ArkanWolfshade west').catch(() => {});
    await waitForMessage(page, /teleport|Main Foyer|marble floor/i, 20000).catch(() => {});
  }
  await executeCommandWithoutRecovery(page, 'look').catch(() => {});
}

/** Exactly one quest giver in foyer: zone Active NPCs is truth; Occupants can lag after despawn. */
async function ensureQuestGiverPresent(page: Page): Promise<void> {
  await ensurePlayableConnection(page, {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    timeoutMs: 45000,
  });
  await ensureAdminInFoyer(page);

  for (let i = 0; i < 3; i++) {
    const ids = await listActiveQuestGiverIds(page);
    if (ids.length === 1) {
      await executeCommandWithoutRecovery(page, 'look').catch(() => {});
      return;
    }
    if (ids.length > 1) {
      await despawnQuestGiverInstances(page);
      continue;
    }
    // ids.length === 0
    await executeCommandWithoutRecovery(page, `npc spawn ${COLLECT_N.npcSpawnId}`);
    await waitForMessage(page, /NPC spawned successfully|spawned successfully/i, 20000).catch(() => {});
    await assertQuestGiverVisible(page);
  }

  const finalIds = await listActiveQuestGiverIds(page);
  if (finalIds.length !== 1) {
    throw new Error(`Expected exactly one ${COLLECT_N.npcName} in zone, found ${finalIds.length}`);
  }
}

test.describe('collect_n quest ask/turnin', () => {
  test.describe.configure({ mode: 'serial' });

  test.beforeAll(() => {
    resetCollectNQuestInstances();
  });

  test('quest ask fails when the target NPC is not in the room', async ({ page }) => {
    test.setTimeout(120_000);
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });
    await ensureStanding(page, 10000);
    await executeCommand(page, 'look');
    await waitForMessage(page, /Foyer|Exits|Sanitarium/i, 20000).catch(() => {});

    // Assert the not-in-room path without depending on quest-giver pollution.
    await executeCommand(page, 'quest ask definitely_not_an_npc_xyz');
    await waitForMessage(page, /You do not see ['"]?definitely_not_an_npc_xyz['"]? here/i, 25000);
    const messages = await getMessages(page);
    expect(messages.some(m => /You do not see ['"]?definitely_not_an_npc_xyz['"]? here/i.test(m))).toBe(true);
  });

  test('ask quest giver, collect items, turn in', async ({ page }) => {
    test.setTimeout(300_000);
    resetCollectNQuestInstances();

    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });
    await ensureStanding(page, 10000);
    await executeCommand(page, 'look');
    await waitForMessage(page, /Foyer|Exits|Sanitarium|Morgan|Arena/i, 20000).catch(() => {});

    await ensureQuestGiverPresent(page);

    await executeCommand(page, `quest abandon ${COLLECT_N.questId}`);
    await waitForMessage(page, /Quest abandoned|do not have this quest|Unknown quest|only abandon/i, 15000).catch(
      () => {}
    );

    const titleRe = new RegExp(
      `Quest started:\\s*${COLLECT_N.questTitle.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}|already have this quest`,
      'i'
    );
    await executeCommand(page, `quest ask ${COLLECT_N.npcAskAlias}`);
    await waitForMessage(page, titleRe, 25000);

    await executeCommand(page, `/summon ${COLLECT_N.prototypeId} ${COLLECT_N.count}`);
    await waitForMessage(page, new RegExp(`You summon\\s+${COLLECT_N.count}x|Summoning failed`, 'i'), 25000);
    const summonMsgs = await getMessages(page);
    expect(summonMsgs.some(m => new RegExp(`You summon\\s+${COLLECT_N.count}x`, 'i').test(m))).toBe(true);

    // get <item> [from] <container> [quantity]; room floor uses container "room"
    await executeCommand(page, `get ${COLLECT_N.itemGetAlias} from room ${COLLECT_N.count}`);
    const itemNameEsc = COLLECT_N.itemDisplayName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    await waitForMessage(page, new RegExp(`You get\\s+\\d+x|${COLLECT_N.itemGetAlias}|${itemNameEsc}`, 'i'), 25000);

    const protoEsc = COLLECT_N.prototypeId.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const titleEsc = COLLECT_N.questTitle.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    await executeCommand(page, 'journal');
    await waitForMessage(page, new RegExp(`${titleEsc}|${protoEsc}`, 'i'), 25000);
    const journalMsgs = await getMessages(page);
    expect(
      journalMsgs.some(
        m =>
          new RegExp(titleEsc, 'i').test(m) ||
          new RegExp(`${protoEsc}.*${COLLECT_N.count}\\s*/\\s*${COLLECT_N.count}`, 'i').test(m)
      )
    ).toBe(true);

    const completedRe = new RegExp(`Quest completed:\\s*${titleEsc}`, 'i');
    await executeCommand(page, `quest turnin ${COLLECT_N.npcAskAlias}`);
    await waitForMessage(page, completedRe, 25000);
    const turninMsgs = await getMessages(page);
    expect(turninMsgs.some(m => completedRe.test(m))).toBe(true);
  });
});
