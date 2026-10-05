/**
 * Consumables: drinking a folk tonic (#870).
 *
 * The first item usable via `/use` (aliases `drink` and `quaff`). A folk tonic restores lucidity and then
 * leaves the drinker unable to stomach another for 30 minutes -- a refused tonic must stay in the inventory.
 *
 * ArkanWolfshade (admin) summons the tonics so the test does not depend on the nurses' station floor drop,
 * which is only seeded once per server start. The folk_tonic cooldown is cleared by
 * `scripts/e2e_reset_players.py` (run by global setup), so reruns can drink again.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  resetPlayersToMainFoyer,
  type PlayerContext,
} from '../fixtures/multiplayer';

const TONIC = 'consumable.folk_tonic';

/** The most recent message matching `cue` (the log keeps earlier lines, e.g. repeated inventory listings). */
async function latestMessage(page: PlayerContext['page'], cue: RegExp): Promise<string> {
  const matches = (await getMessages(page)).filter(message => cue.test(message));
  return matches[matches.length - 1] ?? '';
}

test.describe.serial('Folk tonic consumable', () => {
  let contexts: PlayerContext[];
  let aw: PlayerContext;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    [aw] = contexts;
  });

  test.beforeEach(async () => {
    await resetPlayersToMainFoyer([aw]);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('drinking a tonic restores lucidity and spends one; a second is refused and kept', async () => {
    await executeCommand(aw.page, `summon ${TONIC} 2`);
    await waitForMessage(aw.page, /You summon 2x Folk Tonic/i, 25000);
    // Regression: the summon spec leaves an `artifact.miskatonic.codex` on this floor, and "tonic" is a substring
    // of its id. A whole word in an item's name must win over that. (`get folk tonic` would read as item + container.)
    await executeCommand(aw.page, 'get tonic');
    await waitForMessage(aw.page, /You (get|pick up) 2x Folk Tonic/i, 15000);

    await executeCommand(aw.page, 'drink tonic');
    await waitForMessage(aw.page, /You swallow the folk tonic.*LCD, now \d+\/100/is, 20000);

    // Still inside the 30-minute cooldown: refused, and the second tonic is not consumed.
    await executeCommand(aw.page, 'quaff tonic');
    await waitForMessage(aw.page, /You don't think you can stomach another tonic at this time/i, 20000);

    await executeCommand(aw.page, 'inventory');
    await waitForMessage(aw.page, /You are carrying/i, 15000);
    expect(await latestMessage(aw.page, /You are carrying/i)).toMatch(/Folk Tonic/i);

    // Leave the inventory as found: the lost-and-found chest in the foyer takes the leftover tonic.
    await executeCommand(aw.page, 'put tonic into chest');
    await waitForMessage(aw.page, /You put 1x Folk Tonic into chest/i, 15000);
  });

  test('use names the item it could not find', async () => {
    await executeCommand(aw.page, 'use nonexistent-thing');
    await waitForMessage(aw.page, /You do not have an item matching 'nonexistent-thing'/i, 15000);
    expect(await latestMessage(aw.page, /You do not have an item matching/i)).toContain('nonexistent-thing');
  });
});
