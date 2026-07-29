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
  for (const match of Array.from(latest.matchAll(COLLECT_N.npcInstanceIdRe))) {
    ids.add(match[0].replace(/npc$/i, ''));
  }
  return Array.from(ids);
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
async function ensureQuestGiverPresent(page: Page): Promise<Page> {
  const live = await ensurePlayableConnection(page, {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    timeoutMs: 45000,
  });
  await ensureAdminInFoyer(live);

  for (let i = 0; i < 3; i++) {
    const ids = await listActiveQuestGiverIds(live);
    if (ids.length === 1) {
      await executeCommandWithoutRecovery(live, 'look').catch(() => {});
      return live;
    }
    if (ids.length > 1) {
      await despawnQuestGiverInstances(live);
      continue;
    }
    // ids.length === 0
    await executeCommandWithoutRecovery(live, `npc spawn ${COLLECT_N.npcSpawnId}`);
    await waitForMessage(live, /NPC spawned successfully|spawned successfully/i, 20000).catch(() => {});
    await assertQuestGiverVisible(live);
  }

  const finalIds = await listActiveQuestGiverIds(live);
  if (finalIds.length !== 1) {
    throw new Error(`Expected exactly one ${COLLECT_N.npcName} in zone, found ${finalIds.length}`);
  }
  return live;
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

async function loginAdminPlayable(page: Page): Promise<Page> {
  await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
  await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
  const live = await ensurePlayableConnection(page, {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    timeoutMs: 45000,
  });
  return ensureStanding(live, 10000);
}

async function abandonCollectNQuest(page: Page): Promise<void> {
  await executeCommand(page, `quest abandon ${COLLECT_N.questId}`);
  await waitForMessage(page, /Quest abandoned|do not have this quest|Unknown quest|only abandon/i, 15000).catch(
    () => {}
  );
}

async function askCollectNQuest(page: Page): Promise<void> {
  const titleRe = new RegExp(`Quest started:\\s*${escapeRegExp(COLLECT_N.questTitle)}|already have this quest`, 'i');
  await executeCommand(page, `quest ask ${COLLECT_N.npcAskAlias}`);
  await waitForMessage(page, titleRe, 25000);
}

async function summonAndPickupCollectItems(page: Page): Promise<void> {
  await executeCommand(page, `/summon ${COLLECT_N.prototypeId} ${COLLECT_N.count}`);
  await waitForMessage(page, new RegExp(`You summon\\s+${COLLECT_N.count}x|Summoning failed`, 'i'), 25000);
  const summonMsgs = await getMessages(page);
  expect(summonMsgs.some(m => new RegExp(`You summon\\s+${COLLECT_N.count}x`, 'i').test(m))).toBe(true);

  // get <item> [from] <container> [quantity]; room floor uses container "room"
  await executeCommand(page, `get ${COLLECT_N.itemGetAlias} from room ${COLLECT_N.count}`);
  const itemNameEsc = escapeRegExp(COLLECT_N.itemDisplayName);
  await waitForMessage(page, new RegExp(`You get\\s+\\d+x|${COLLECT_N.itemGetAlias}|${itemNameEsc}`, 'i'), 25000);
}

async function assertCollectNJournalComplete(page: Page): Promise<void> {
  const protoEsc = escapeRegExp(COLLECT_N.prototypeId);
  const titleEsc = escapeRegExp(COLLECT_N.questTitle);
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
}

async function turnInCollectNQuest(page: Page): Promise<void> {
  const completedRe = new RegExp(`Quest completed:\\s*${escapeRegExp(COLLECT_N.questTitle)}`, 'i');
  await executeCommand(page, `quest turnin ${COLLECT_N.npcAskAlias}`);
  await waitForMessage(page, completedRe, 25000);
  const turninMsgs = await getMessages(page);
  expect(turninMsgs.some(m => completedRe.test(m))).toBe(true);
}

test.describe('collect_n quest ask/turnin', () => {
  test.describe.configure({ mode: 'serial' });

  test.beforeAll(() => {
    resetCollectNQuestInstances();
  });

  test('quest ask fails when the target NPC is not in the room', async ({ page }) => {
    test.setTimeout(120_000);
    const live = await loginAdminPlayable(page);
    await executeCommand(live, 'look');
    await waitForMessage(live, /Foyer|Exits|Sanitarium/i, 20000).catch(() => {});

    // Assert the not-in-room path without depending on quest-giver pollution.
    await executeCommand(live, 'quest ask definitely_not_an_npc_xyz');
    await waitForMessage(live, /You do not see ['"]?definitely_not_an_npc_xyz['"]? here/i, 25000);
    const messages = await getMessages(live);
    expect(messages.some(m => /You do not see ['"]?definitely_not_an_npc_xyz['"]? here/i.test(m))).toBe(true);
  });

  test('ask quest giver, collect items, turn in', async ({ page }) => {
    test.setTimeout(300_000);
    resetCollectNQuestInstances();

    let live = await loginAdminPlayable(page);
    await executeCommand(live, 'look');
    await waitForMessage(live, /Foyer|Exits|Sanitarium|Morgan|Arena/i, 20000).catch(() => {});

    live = await ensureQuestGiverPresent(live);
    await abandonCollectNQuest(live);
    await askCollectNQuest(live);
    await summonAndPickupCollectItems(live);
    await assertCollectNJournalComplete(live);
    await turnInCollectNQuest(live);
    const messages = await getMessages(live);
    expect(
      messages.some(m => new RegExp(`Quest completed:\\s*${escapeRegExp(COLLECT_N.questTitle)}`, 'i').test(m))
    ).toBe(true);
  });
});
