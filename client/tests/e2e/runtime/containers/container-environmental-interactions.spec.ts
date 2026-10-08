/**
 * Scenario 24: Environmental Container Interactions
 *
 * Environmental containers are room furniture: a room's `attributes.furniture` names an item
 * prototype that defines `metadata.container`, and the server creates the container at startup
 * (server/services/room_furniture_loader.py). The Sanitarium Main Foyer has one: the
 * Lost-and-Found Chest (200 slots). It is shared -- anyone can put items in and take them out.
 * (Items left in tutorial bedrooms no longer land here; they go to the leaver's bank deposit box.)
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  resetPlayersToMainFoyer,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

const LOOT_ITEM_ID = 'pack_dark_ages.weapon.sling';

test.describe('Environmental Container Interactions', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.beforeEach(async () => {
    await resetPlayersToMainFoyer(contexts);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('the foyer Lost-and-Found Chest is listed in the room', async () => {
    const awContext = contexts[0];

    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /You see:[^\n]*Lost-and-Found Chest/i, 15000);
    expect((await getMessages(awContext.page)).some(message => /Lost-and-Found Chest/i.test(message))).toBe(true);
  });

  test('one player can put an item in the chest and another can take it out', async () => {
    const [awContext, ithaquaContext] = contexts;

    // A known item to deposit: AW (admin) summons a Sling and picks it up.
    await executeCommand(awContext.page, `/summon ${LOOT_ITEM_ID} 1`);
    await waitForMessage(awContext.page, /You summon\s+1x/i, 15000);
    await executeCommand(awContext.page, 'pickup sling');
    await waitForMessage(awContext.page, /You pick up/i, 10000);

    // Replies name the container as typed ("chest"), not the furniture's full name.
    await executeCommand(awContext.page, 'put sling into chest');
    await waitForMessage(awContext.page, /You put 1x Sling into chest/i, 15000);

    await executeCommand(ithaquaContext.page, 'get sling from chest');
    await waitForMessage(ithaquaContext.page, /You get 1x Sling from chest/i, 15000);
    expect(await getMessages(ithaquaContext.page)).toContainEqual(expect.stringMatching(/You get 1x Sling/i));

    // Leave Ithaqua's persistent inventory as it was.
    await executeCommand(ithaquaContext.page, 'put sling into chest');
    await waitForMessage(ithaquaContext.page, /You put 1x Sling into chest/i, 15000);
  });
});
