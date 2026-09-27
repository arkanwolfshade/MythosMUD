/**
 * Scenario 24: Environmental Container Interactions
 *
 * #711 ported the container GUI (open/transfer/close via HTTP + `get`/`put` text commands both
 * work end to end now), but environmental containers -- chests, crates, and similar room fixtures
 * -- are not reachable in this game today:
 * - server/services/environmental_container_loader.py has zero production callers of
 *   `migrate_room_container_to_postgresql` anywhere in server/.
 * - No room JSON under data/ defines a `container` block for the loader to migrate.
 * Only corpse containers are reachable (created by a genuine combat death; see
 * container-corpse-looting.spec.ts and container-multi-user-looting.spec.ts). This test stays
 * skipped honestly rather than asserting against a container type nothing spawns -- unskip it
 * once an environmental container is actually seeded and wired into a room.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

test.describe('Environmental Container Interactions', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  // Skipped: no environmental container is reachable in live game data (see file header).
  // eslint-disable-next-line playwright/no-skipped-test -- unskip once a container is seeded in a room
  test.skip('should allow opening environmental containers', async () => {
    const awContext = contexts[0];

    await executeCommand(awContext.page, 'open container');
    await waitForMessage(awContext.page, 'container', 10000).catch(() => {});

    expect(awContext.page).toBeTruthy();
  });
});
