/**
 * Dialogue trees E2E (#583): player talk / talk n; admin Content Tools editor.
 */

import { expect, test, type Page } from '@playwright/test';
import {
  clickWithoutStability,
  ensurePlayableConnection,
  executeCommand,
  executeCommandWithoutRecovery,
  getMessages,
  loginPlayer,
  waitForMessage,
} from '../fixtures/auth';
import { ensureStanding } from '../fixtures/player';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

const DIALOGUE = {
  npcSpawnId: 53,
  npcTalkAlias: 'armitage',
  npcName: 'Professor Henry Armitage',
  npcInstanceIdRe: /professor_henry_armitage_[a-z0-9_]+/gi,
  zone: 'arkhamcity/sanitarium',
  greetingCue: /seeker of knowledge|What brings you to the stacks/i,
  optionCue: /Ask about the library|talk <number>/i,
  libraryCue: /shelves hold truths|Choose carefully what you pursue/i,
  endCue: /conversation ends/i,
} as const;

const E2E_DIALOGUE_ID = `e2e_dialogue_${Date.now()}`;

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

async function listArmitageIds(page: Page): Promise<string[]> {
  await executeCommandWithoutRecovery(page, `npc zone ${DIALOGUE.zone}`);
  await waitForMessage(page, /NPC Zone Statistics/i, 15000).catch(() => {});
  const messages = await getMessages(page);
  const latest = [...messages].reverse().find(m => /NPC Zone Statistics/i.test(m));
  if (!latest) {
    return [];
  }
  const ids = new Set<string>();
  for (const match of Array.from(latest.matchAll(DIALOGUE.npcInstanceIdRe))) {
    ids.add(match[0].replace(/npc$/i, ''));
  }
  return Array.from(ids);
}

async function despawnArmitage(page: Page): Promise<void> {
  const ids = await listArmitageIds(page);
  for (const id of ids) {
    await executeCommandWithoutRecovery(page, `npc despawn ${id}`).catch(() => {});
  }
  await executeCommandWithoutRecovery(page, 'look').catch(() => {});
}

async function ensureArmitagePresent(page: Page): Promise<Page> {
  const live = await ensurePlayableConnection(page, {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    timeoutMs: 45000,
  });
  await executeCommandWithoutRecovery(live, 'look').catch(() => {});

  for (let i = 0; i < 3; i++) {
    const ids = await listArmitageIds(live);
    if (ids.length === 1) {
      await executeCommandWithoutRecovery(live, 'look').catch(() => {});
      return live;
    }
    if (ids.length > 1) {
      await despawnArmitage(live);
      continue;
    }
    await executeCommandWithoutRecovery(live, `npc spawn ${DIALOGUE.npcSpawnId}`);
    await waitForMessage(live, /NPC spawned successfully|spawned successfully/i, 20000).catch(() => {});
    await expect
      .poll(async () => (await listArmitageIds(live)).length >= 1, {
        timeout: 30000,
        message: `Armitage visible after npc spawn ${DIALOGUE.npcSpawnId}`,
      })
      .toBe(true);
  }

  const finalIds = await listArmitageIds(live);
  if (finalIds.length < 1) {
    throw new Error(`Expected ${DIALOGUE.npcName} in zone after spawn`);
  }
  return live;
}

test.describe('dialogue trees (#583)', () => {
  test.describe.configure({ mode: 'serial' });

  test('player talk / talk n navigates a seeded dialogue tree', async ({ page }) => {
    test.setTimeout(180_000);
    let live = await loginAdminPlayable(page);
    live = await ensureArmitagePresent(live);

    await executeCommand(live, 'help talk');
    await waitForMessage(live, /TALK Command|talk <npc>|dialogue tree/i, 25000);

    await executeCommand(live, `talk ${DIALOGUE.npcTalkAlias}`);
    await waitForMessage(live, DIALOGUE.greetingCue, 25000);
    await waitForMessage(live, DIALOGUE.optionCue, 10000);
    const afterStart = await getMessages(live);
    expect(afterStart.some(m => DIALOGUE.greetingCue.test(m))).toBe(true);

    await executeCommand(live, 'talk 1');
    await waitForMessage(live, DIALOGUE.libraryCue, 25000);
    const afterChoice = await getMessages(live);
    expect(afterChoice.some(m => DIALOGUE.libraryCue.test(m))).toBe(true);

    await executeCommand(live, 'talk 1');
    await waitForMessage(live, DIALOGUE.endCue, 25000);

    // No cursor: numbered talk should guide the player.
    await executeCommand(live, 'talk 1');
    await waitForMessage(live, /not in a conversation|talk <npc>/i, 25000);

    await despawnArmitage(live);
  });

  test('admin Content Tools Dialogue editor can save and delete a tree', async ({ page }) => {
    test.setTimeout(120_000);
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });

    await page.goto('/admin/content/dialogue', { waitUntil: 'domcontentloaded' });
    await expect(page.getByRole('heading', { name: /Content Tools — Dialogue/i })).toBeVisible({
      timeout: 15000,
    });

    await page.getByRole('button', { name: 'New' }).click();
    await page.getByTestId('dialogue-id-input').fill(E2E_DIALOGUE_ID);
    await page.getByTestId('dialogue-npc-id-input').fill('');
    const tree = {
      start: 'greeting',
      nodes: {
        greeting: {
          text: 'E2E dialogue smoke line.',
          options: [{ label: 'Farewell', next: null }],
        },
      },
    };
    await page.getByTestId('dialogue-tree-json').fill(JSON.stringify(tree, null, 2));
    await clickWithoutStability(page.getByTestId('dialogue-save'));

    await expect(page.getByRole('status')).toContainText(new RegExp(`Saved\\s+${E2E_DIALOGUE_ID}`), {
      timeout: 20000,
    });
    await expect(page.getByRole('button', { name: E2E_DIALOGUE_ID })).toBeVisible({ timeout: 10000 });

    await clickWithoutStability(page.getByRole('button', { name: E2E_DIALOGUE_ID }));
    await clickWithoutStability(page.getByTestId('dialogue-delete'));
    await expect(page.getByRole('status')).toContainText(new RegExp(`Deleted\\s+${E2E_DIALOGUE_ID}`), {
      timeout: 20000,
    });
  });
});
