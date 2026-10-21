/**
 * NPC speech E2E (#1053): an NPC `say` reaches the player through NATS.
 *
 * Player-to-player chat never carries NPC-only fields (speaker_disposition), so before this spec a schema
 * regression that dead-lettered every NPC line (#1036 / PR #1052) failed no test. A passive_mob NPC greets
 * each player who enters its room, so we spawn one in the foyer, step out, and walk back in.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, loginPlayer, waitForMessage } from '../fixtures/auth';
import { ensureStanding, goEastFromFoyer } from '../fixtures/player';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

// Seed NPC definition 56 (the Sanitarium patient, passive_mob). Its behavior_config authors a `greeting`, which is
// the NPC's own words and so goes out as speech (#1110); an NPC with no authored line gets a gesture emote instead
// ("<NPC> offers a wary nod in greeting.", #1103), which first-exposure.spec.ts covers with the lamplighter.
const PATIENT_DEFINITION_ID = 56;
const PATIENT_GREETING = /They\.\.\. they told me I was cured/i;

test.describe('NPC speech (#1053)', () => {
  test('a passive NPC greets a player entering its room', async ({ page }) => {
    test.setTimeout(120_000);
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    let live = await ensureStanding(page, 10000);

    await executeCommand(live, `npc spawn ${PATIENT_DEFINITION_ID}`);
    await waitForMessage(live, /spawned successfully/i, 20000);

    live = await goEastFromFoyer(live);
    await executeCommand(live, 'go west');

    // A dropped NPC line (schema rejection -> DLQ) never arrives, so this times out and fails the test.
    await waitForMessage(live, PATIENT_GREETING, 20000);
    await expect(live.locator('[data-message-text]').filter({ hasText: PATIENT_GREETING }).first()).toBeVisible();
  });
});
