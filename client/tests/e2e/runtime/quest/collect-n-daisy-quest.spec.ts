/**
 * collect_n quest: quest ask / get / turnin with Dr. Morgan (npc spawn 54).
 *
 * Starts in DEFAULT_RESPAWN_ROOM (sanitarium foyer). Spawns Morgan if needed,
 * summons daisies, then ask → get → journal progress → turnin.
 */

import { expect, test } from '@playwright/test';
import { spawnSync } from 'child_process';
import { join } from 'path';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import { ensurePlayableConnection, executeCommand, getMessages, loginPlayer, waitForMessage } from '../fixtures/auth';
import { ensureStanding } from '../fixtures/player';
import { EASTERN_HALLWAY_LOOK_CUE, TEST_TIMEOUTS } from '../fixtures/test-data';

const MORGAN_NAME = 'Dr. Francis Morgan';
const DAISY_PROTOTYPE = 'misc.herb.sanitarium_daisy';

function resetDaisyQuestInstances(): void {
  loadE2eEnv();
  const scriptPath = join(E2E_PROJECT_ROOT, 'scripts', 'e2e_reset_collect_n_quest.py');
  const result = spawnSync('uv', ['run', '--no-sync', 'python', scriptPath], {
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

async function assertMorganVisible(page: import('@playwright/test').Page): Promise<void> {
  const escaped = MORGAN_NAME.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  await expect
    .poll(
      async () => {
        const body = await page.evaluate(() => (document.body?.innerText ?? '').toLowerCase());
        if (body.includes('dr. francis morgan') || body.includes('morgan')) return true;
        const texts = await page.evaluate(() =>
          Array.from(document.querySelectorAll('[data-message-text]')).map(
            el => el.getAttribute('data-message-text') || el.textContent || ''
          )
        );
        return texts.some(t => new RegExp(escaped, 'i').test(t));
      },
      { timeout: 30000, message: 'Morgan visible after npc spawn 54' }
    )
    .toBe(true);
}

async function spawnMorgan(page: import('@playwright/test').Page): Promise<void> {
  for (let attempt = 0; attempt < 3; attempt++) {
    await executeCommand(page, 'npc spawn 54');
    try {
      await assertMorganVisible(page);
      await waitForMessage(page, /NPC spawned successfully|spawned successfully/i, 20000).catch(() => {});
      return;
    } catch {
      await executeCommand(page, 'look').catch(() => {});
    }
  }
  await assertMorganVisible(page);
}

test.describe('collect_n daisy quest ask/turnin', () => {
  test.describe.configure({ mode: 'serial' });

  test.beforeAll(() => {
    resetDaisyQuestInstances();
  });

  test('quest ask fails when Morgan is not in the room', async ({ page }) => {
    test.setTimeout(120_000);
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });
    await ensureStanding(page);
    await executeCommand(page, 'look');
    await waitForMessage(page, /Foyer|Exits|Sanitarium/i, 20000).catch(() => {});

    // Leave foyer so Morgan is not present (teleport does not accept room ids).
    await ensureStanding(page);
    await executeCommand(page, 'go east');
    // Movement replies "You go east."; the room description arrives via room_state into the
    // Location panel, not the message log. Assert on the panel, not on [data-message-text].
    await expect(page.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 25000 });

    await executeCommand(page, 'quest ask morgan');
    // Server: You do not see '{npc_name}' here. — npc_name is the typed arg (case preserved).
    const notHere = /do not see\s*['"]?morgan['"]?\s*here/i;
    await waitForMessage(page, notHere, 25000);
    const messages = await getMessages(page);
    const body = await page.evaluate(() => document.body?.innerText ?? '');
    expect(messages.some(m => notHere.test(m)) || notHere.test(body)).toBe(true);
  });

  test('ask Morgan, collect daisies, turn in', async ({ page }) => {
    test.setTimeout(180_000);
    resetDaisyQuestInstances();

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

    await spawnMorgan(page);

    await executeCommand(page, 'quest abandon gather_sanitarium_daisies');
    await waitForMessage(page, /Quest abandoned|do not have this quest|Unknown quest|only abandon/i, 15000).catch(
      () => {}
    );

    await executeCommand(page, 'quest ask morgan');
    await waitForMessage(page, /Quest started:\s*Gather Sanitarium Daisies|already have this quest/i, 25000);

    await executeCommand(page, `/summon ${DAISY_PROTOTYPE} 3`);
    await waitForMessage(page, /You summon\s+3x|Summoning failed/i, 25000);
    const summonMsgs = await getMessages(page);
    expect(summonMsgs.some(m => /You summon\s+3x/i.test(m))).toBe(true);

    // get <item> [from] <container> [quantity]; room floor uses container "room"
    await executeCommand(page, 'get daisy from room 3');
    await waitForMessage(page, /You get\s+\d+x|daisy|Sanitarium Daisy/i, 25000);

    await executeCommand(page, 'journal');
    await waitForMessage(page, /Gather Sanitarium Daisies|misc\.herb\.sanitarium_daisy/i, 25000);
    const journalMsgs = await getMessages(page);
    expect(
      journalMsgs.some(m => /Gather Sanitarium Daisies/i.test(m) || /misc\.herb\.sanitarium_daisy.*3\s*\/\s*3/i.test(m))
    ).toBe(true);

    await executeCommand(page, 'quest turnin morgan');
    await waitForMessage(page, /Quest completed:\s*Gather Sanitarium Daisies/i, 25000);
    const turninMsgs = await getMessages(page);
    expect(turninMsgs.some(m => /Quest completed:\s*Gather Sanitarium Daisies/i.test(m))).toBe(true);

    // Panel routing contract (#674): quest lifecycle lines are Game Info, never Chat History.
    const questCompletedCue = /Quest completed:\s*Gather Sanitarium Daisies/i;
    const gameInfoText = await page.getByTestId('game-panel-gameInfo').innerText();
    const chatHistoryText = await page.getByTestId('game-panel-chatHistory').innerText();
    expect(questCompletedCue.test(gameInfoText)).toBe(true);
    expect(questCompletedCue.test(chatHistoryText)).toBe(false);
  });
});
