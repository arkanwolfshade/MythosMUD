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
import { clickWithoutStability, executeCommand, waitForMessage } from '../fixtures/auth';
import { cleanupMultiPlayerContexts, createMultiPlayerContexts, ensurePlayerInGame } from '../fixtures/multiplayer';
import {
  containerRow,
  despawnSanitariumCultists,
  ensurePlayableAlive,
  killPlayerAndProduceCorpse,
  openCorpseWithRetry,
} from '../fixtures/player';

const LOOT_ITEM_ID = 'pack_dark_ages.weapon.sling';
const LEADING_ITEM_ID = 'artifact.miskatonic.codex';

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
    // A kill cycle (combat death + respawn + corpse check) can take ~90s, and
    // killPlayerAndProduceCorpse retries it, so 180s could expire before the looting assertions
    // ran at all -- reporting a bare timeout instead of whatever actually went wrong.
    test.setTimeout(420_000);
    const awContext = contexts[0];
    const creds = { username: awContext.player.username, password: awContext.player.password };

    // Corpse contents follow pickup order, so picking up the Codex first guarantees the Sling is
    // never the corpse's first row: a Transfer click not scoped to the Sling's row (#980) then
    // moves the wrong item every time instead of only when a previous run left items behind.
    // waitForMessage also matches older log lines, so each wait names its item.
    await executeCommand(awContext.page, `/summon ${LEADING_ITEM_ID} 1`);
    await waitForMessage(awContext.page, /You summon\s+1x\s+Codex/i, 15000);
    await executeCommand(awContext.page, 'pickup codex');
    await waitForMessage(awContext.page, /You pick up\s+\d+x\s+Codex/i, 10000);

    await executeCommand(awContext.page, `/summon ${LOOT_ITEM_ID} 1`);
    await waitForMessage(awContext.page, /You summon\s+1x\s+Sling/i, 15000);
    await executeCommand(awContext.page, 'pickup sling');
    await waitForMessage(awContext.page, /You pick up\s+\d+x\s+Sling/i, 10000);

    try {
      // Die, respawn back into the death room (= DEFAULT_RESPAWN_ROOM), and guarantee the corpse
      // actually exists -- a tick-decay death creates none, so this retries until one does.
      awContext.page = await killPlayerAndProduceCorpse(awContext.page, creds);

      // CorpseOverlay (client/src/components/ui-v2/containers/CorpseOverlay.tsx) renders from the
      // room's container.created broadcast -- the owner's Open button is enabled during grace.
      // Returns the Container column of the modal that actually holds the Sling, so the transfer
      // below cannot act on a stale corpse's modal.
      const corpseColumn = await openCorpseWithRetry(awContext.page, 'Sling');

      // ContainerTransferModal shows the corpse's contents (the player's own inventory at death).
      // Scope to the Container column: transferring moves the Sling into the modal's Inventory
      // column, where an unscoped locator would still see it and the assertion could never pass.
      const slingRow = corpseColumn.getByText('Sling', { exact: true }).first();
      await expect(slingRow).toBeVisible({ timeout: 15000 });
      // Same reason as the Open buttons in openCorpseWithRetry: Playwright's stability check can
      // fail to settle for controls in this modal stack in Firefox, so dispatch the click directly.
      // Scoped to the Sling's row: the Codex is listed first, so an unscoped click moves it (#980).
      await clickWithoutStability(containerRow(corpseColumn, 'Sling').getByRole('button', { name: 'Transfer' }));
      await expect(slingRow).not.toBeVisible({ timeout: 15000 });
    } finally {
      await despawnSanitariumCultists(awContext.page);
      awContext.page = await ensurePlayableAlive(awContext.page, creds.username, creds.password);
    }
  });
});
