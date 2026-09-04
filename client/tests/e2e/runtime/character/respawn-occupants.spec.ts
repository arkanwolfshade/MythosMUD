/**
 * Scenario 35: Respawn Occupants Panel (#776)
 *
 * A death respawn used to write `player`/`room` straight into client state, bypassing the
 * event-sourced projector's `ensureSelfListedInRoomPlayers` self-heal -- the respawn API's room
 * payload carries no occupant lists, so for ~10ms (until the deferred `player_respawned` event
 * caught up) the Occupants panel genuinely had an empty players list while the current player
 * existed, and the client reported `occupants_panel_empty_players` to the server. Verifies the
 * transient never fires (frame-intercept) and that the panel lists self once settled.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, loginPlayer, waitForPlayableSession } from '../fixtures/auth';
import { createInstrumentedContext } from '../fixtures/e2e-browser-helpers';
import { dismissDeathInterstitial, isPlayerDead } from '../fixtures/player';

test.describe('Respawn Occupants Panel', () => {
  test.describe.configure({ timeout: 60_000 });

  test('death respawn never reports an empty occupants panel and lists self once settled (#776)', async ({
    browser,
  }) => {
    const context = await createInstrumentedContext(browser);
    const page = await context.newPage();

    // Must be attached before login triggers the WebSocket connection -- Playwright only hands
    // out a WebSocket handle to a listener registered before the socket is created, and the
    // respawn's client_error_report (if any) rides that same connection.
    const sentFrames: string[] = [];
    page.on('websocket', ws => {
      ws.on('framesent', event => {
        if (typeof event.payload === 'string') {
          sentFrames.push(event.payload);
        }
      });
    });

    try {
      await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
      await waitForPlayableSession(page, 30000);

      // Defensive: a prior spec may have left the character dead.
      /* eslint-disable-next-line playwright/no-conditional-in-test -- defensive UI flow */
      if (await isPlayerDead(page)) {
        await dismissDeathInterstitial(page);
      }

      // -9 is one tick past mortally-wounded (0 >= dp > -10); the game tick loop (server_tick_rate,
      // default 100ms) decays it by 1 and crosses the -10 death threshold almost immediately --
      // the same path a real combat death takes, without needing to fight an NPC to death here.
      await executeCommand(page, 'admin set DP ArkanWolfshade -9');

      await expect
        .poll(() => isPlayerDead(page), { timeout: 15000, message: 'player did not reach Death > Void' })
        .toBe(true);

      await dismissDeathInterstitial(page);

      // Settled state: acceptance criterion 1 -- self is listed in the Occupants panel.
      await expect(page.getByTestId('occupants-other-players')).toHaveAttribute('data-names', /ArkanWolfshade/, {
        timeout: 15000,
      });

      // The transient: no frame sent across the whole death->respawn sequence carried the
      // diagnostic's error report. A settled-state assertion alone would have passed against the
      // buggy code, since the projector healed the state ~10ms after the direct write.
      const badFrame = sentFrames.find(f => f.includes('occupants_panel_empty_players'));
      expect(badFrame, `client sent occupants_panel_empty_players: ${badFrame}`).toBeUndefined();
    } finally {
      await context.close().catch(() => {});
    }
  });
});
