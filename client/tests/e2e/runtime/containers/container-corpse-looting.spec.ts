/**
 * Scenario 26: Corpse Looting with Grace Periods
 *
 * Corpses are the only container type reachable in live game data today: environmental
 * containers have no production loader caller and no room defines a `container` block, and no
 * item prototype defines `inner_container` for wearable containers (see #711 investigation).
 * A corpse is created only by a genuine combat death (server/services/combat_death_handler.py
 * ::_create_corpse_on_death) -- the generic `admin set DP -9` tick-death path used elsewhere in
 * this suite does not create one. See fixtures/player.ts::killPlayerViaCombat for how this test
 * forces a real combat death.
 *
 * Drives the corpse via the GUI (CorpseOverlay -> ContainerTransferModal) rather than the `get`
 * text command: the corpse's room broadcast/CorpseOverlay is the primary, actually-shipped path
 * for #711, and asserting through it exercises the real feature end to end (open, grace-period
 * countdown, transfer) instead of only the server's text-command parsing.
 *
 * Covers: corpse creation on death, the owner looting during the grace period.
 * Non-owner grace-period denial is covered in container-multi-user-looting.spec.ts (it needs a
 * second, non-admin player).
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { cleanupMultiPlayerContexts, createMultiPlayerContexts, ensurePlayerInGame } from '../fixtures/multiplayer';
import {
  despawnSanitariumCultists,
  ensurePlayableAlive,
  killPlayerAndProduceCorpse,
  openCorpseWithRetry,
} from '../fixtures/player';

const LOOT_ITEM_ID = 'pack_dark_ages.weapon.sling';

test.describe('Corpse Looting with Grace Periods', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await ensurePlayerInGame(contexts[0], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('owner can loot their own corpse during the grace period', async () => {
    test.setTimeout(180_000);
    const awContext = contexts[0];
    const creds = { username: awContext.player.username, password: awContext.player.password };

    // Guarantee a known item in the corpse: summon and pick up a sling before dying.
    await executeCommand(awContext.page, `/summon ${LOOT_ITEM_ID} 1`);
    await waitForMessage(awContext.page, /You summon\s+1x/i, 15000);
    await executeCommand(awContext.page, 'pickup sling');
    await waitForMessage(awContext.page, /You pick up/i, 10000);

    try {
      // Die, respawn back into the death room (= DEFAULT_RESPAWN_ROOM), and guarantee the corpse
      // actually exists -- a tick-decay death creates none, so this retries until one does.
      awContext.page = await killPlayerAndProduceCorpse(awContext.page, creds);

      // CorpseOverlay (client/src/components/ui-v2/containers/CorpseOverlay.tsx) renders from the
      // room's container.created broadcast -- the owner's Open button is enabled during grace.
      await openCorpseWithRetry(awContext.page, 'Sling');

      // ContainerTransferModal shows the corpse's contents (the player's own inventory at death).
      const slingRow = awContext.page.getByText('Sling', { exact: true }).first();
      await awContext.page.getByRole('button', { name: 'Transfer' }).first().click();
      await expect(slingRow).not.toBeVisible({ timeout: 15000 });
    } finally {
      await despawnSanitariumCultists(awContext.page);
      awContext.page = await ensurePlayableAlive(awContext.page, creds.username, creds.password);
    }
  });
});
