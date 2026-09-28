/**
 * Scenario 23: Multi-User Container Looting
 *
 * #711 changed the container access model: containers are no longer shared-open. Opening (and
 * transferring items) is exclusive to one player at a time, and a corpse additionally enforces an
 * owner-only grace period regardless of the exclusivity lock (server/services/
 * container_service_access.py::_deny_non_owner_during_grace_period). This spec covers that grace
 * period through the GUI: CorpseOverlay (client/src/components/ui-v2/containers/CorpseOverlay.tsx)
 * disables its Open button and shows the grace-period lock text for a non-owner, and enables it
 * for the owner.
 *
 * Only a genuine combat death creates a real corpse in this game (see fixtures/player.ts
 * ::killPlayerViaCombat and the note in container-corpse-looting.spec.ts). ArkanWolfshade is the
 * seeded admin account, and admins bypass the grace-period check entirely (can_access_corpse),
 * so AW must be the one who dies -- Ithaqua (the seeded regular account) is the only player who
 * can exercise the real non-owner denial path.
 */

import { expect, test } from '@playwright/test';
import { clickWithoutStability, executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';
import {
  corpseCard,
  despawnSanitariumCultists,
  ensurePlayableAlive,
  goEastFromFoyer,
  killPlayerAndProduceCorpse,
  openCorpseWithRetry,
} from '../fixtures/player';

const LOOT_ITEM_ID = 'pack_dark_ages.weapon.sling';

test.describe('Multi-User Container Looting', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await Promise.all([ensurePlayerInGame(contexts[0], 60000), ensurePlayerInGame(contexts[1], 60000)]);
    await waitForAllPlayersInGame(contexts, 20000);
  });

  test.afterAll(async () => {
    // cleanupMultiPlayerContexts walks each context in turn, and a single one can spend 25s in
    // logoutPlayer plus 10s waiting for the login form (more when it has to heal a dead player).
    // Two contexts therefore cannot finish inside the default 30s hook budget, which failed the
    // whole spec even when every assertion in it had passed.
    test.setTimeout(150_000);
    await cleanupMultiPlayerContexts(contexts);
  });

  test('non-owner is denied during the grace period; owner can loot', async () => {
    // Two player sessions plus a full kill/respawn/corpse cycle; 180s expired mid-test and
    // reported a bare timeout instead of the real assertion failure.
    test.setTimeout(420_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];
    const awCreds = { username: awContext.player.username, password: awContext.player.password };

    await executeCommand(awContext.page, `/summon ${LOOT_ITEM_ID} 1`);
    await waitForMessage(awContext.page, /You summon\s+1x/i, 15000);
    await executeCommand(awContext.page, 'pickup sling');
    await waitForMessage(awContext.page, /You pick up/i, 10000);

    try {
      // Move Ithaqua out before the kill: the cultist one-shots a full-DP player (25 dmg vs 20 DP),
      // so a bystander in the room dies too and ends up looking at their OWN corpse -- which would
      // make them the owner and silently invert this test. Re-entering afterwards also exercises
      // the room_state corpse backfill (they miss the container.created broadcast while away).
      ithaquaContext.page = await goEastFromFoyer(ithaquaContext.page);

      // AW dies and respawns; retried until a corpse actually exists (a tick-decay death makes none).
      awContext.page = await killPlayerAndProduceCorpse(awContext.page, awCreds);

      // Ithaqua returns to the death room and learns about the corpse from room_state, not the
      // live broadcast. Non-owner, non-admin: Open must be disabled with the grace-period lock
      // message, per container_service_access.py.
      await ithaquaContext.page.bringToFront().catch(() => {});
      await executeCommand(ithaquaContext.page, 'go west');
      await waitForMessage(ithaquaContext.page, /Main Foyer|marble|You (move|go) west/i, 20000).catch(() => {});
      // Scope to a grace-locked card: earlier specs can leave already-expired corpses in this
      // room, whose cards render the same strings and an enabled Open button.
      const lockedCorpse = corpseCard(ithaquaContext.page, { openable: false, graceActive: true }).first();
      await expect(lockedCorpse).toBeVisible({ timeout: 20000 });
      await expect(lockedCorpse.getByText(/Only the owner can access during grace period/i)).toBeVisible();
      await expect(lockedCorpse.getByRole('button', { name: 'Open' })).toBeDisabled();

      // Owner access still succeeds while the same grace period is active.
      await awContext.page.bringToFront().catch(() => {});
      // Returns the Container column of the modal holding the Sling -- this room also contains
      // corpses left by earlier specs, whose modals look identical but are empty.
      const corpseColumn = await openCorpseWithRetry(awContext.page, 'Sling');

      // Container column only: after the transfer the Sling reappears in the modal's Inventory
      // column, so an unscoped locator would never go invisible.
      const slingRow = corpseColumn.getByText('Sling', { exact: true }).first();
      await expect(slingRow).toBeVisible({ timeout: 15000 });
      // Same reason as the Open buttons in openCorpseWithRetry: Playwright's stability check can
      // fail to settle for controls in this modal stack in Firefox, so dispatch the click directly.
      await clickWithoutStability(corpseColumn.getByRole('button', { name: 'Transfer' }).first());
      await expect(slingRow).not.toBeVisible({ timeout: 15000 });
    } finally {
      await despawnSanitariumCultists(awContext.page);
      awContext.page = await ensurePlayableAlive(awContext.page, awCreds.username, awCreds.password);
      expect(awContext.page).toBeTruthy();
      expect(ithaquaContext.page).toBeTruthy();
    }
  });
});
