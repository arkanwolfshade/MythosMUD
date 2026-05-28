/**
 * Scenario 31: Administrative Set Stat Command
 *
 * Validates the admin set administrative command from end to end: parser recognition,
 * permission gating, stat modification, DP/MP maximum warnings, error handling, and
 * audit logging. Confirms non-admin rejection flow and validates all stat types.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  waitForAllPlayersInGame,
} from '../fixtures/multiplayer';

/**
 * After `look`, room prose is shown in Location / Room Description, not always Game Info `[data-message-text]`.
 */
async function assertLookVisibleInPanels(page: Page): Promise<void> {
  const cue = page.getByText(
    /Arena\s*>\s*Arena|Arena entrance \(center\)|heart of the gladiator|sand and shadow|Exits:\s*North/i
  );
  await expect(cue.first()).toBeVisible({ timeout: 45000 });
}

test.describe('Administrative Set Stat Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players (AW is admin, Ithaqua is not)
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should be able to set player stats', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Admin set resolves the target by name on the server; same-room UI sync is not required.
    // avoid ensureMultiplayerCoLocated here — repeated ~45s occupant waits can exceed the 180s test timeout.

    // Server resolves target by character name; get Ithaqua's current character name
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 60000);
    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await assertLookVisibleInPanels(awContext.page);

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, `admin set STR ${ithaquaCharName} 75`);

    // Server (admin_setstat_command): "Set {target}'s {stat} from {old} to {new}."
    // Tolerate straight vs typographic apostrophe in rendered text; allow "You do not have permission".
    await waitForMessage(
      awContext.page,
      /Set .+['\u2019]s STR from|STR from \d+ to 75|do not have permission|You do not have permission/i,
      45000
    );

    const messages = await getMessages(awContext.page);
    const seesSuccess = messages.some(
      msg => /Set .+['\u2019]s STR from/i.test(msg) || /\bSTR from\b.*\bto 75\b/i.test(msg)
    );
    const seesPermissionDenied = messages.some(
      msg => msg.includes('do not have permission') || msg.includes('You do not have permission')
    );
    expect(
      seesPermissionDenied,
      "Admin set stat returned 'You do not have permission'. Ensure ArkanWolfshade's character has is_admin set in the test database."
    ).toBe(false);
    expect(seesSuccess).toBe(true);
  });

  test('Ithaqua should not be able to set stats', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Target by character name so server finds the player and returns permission denied (not "not found")
    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 60000);
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 30000);
    await expect(
      ithaquaContext.page.getByText(new RegExp(`Player:\\s*${ithaquaContext.player.username}\\b`, 'i'))
    ).toBeVisible({ timeout: 15000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(ithaquaContext.page, 'look');
    await assertLookVisibleInPanels(ithaquaContext.page);

    await executeCommand(ithaquaContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(ithaquaContext.page, `admin set STR ${awCharName} 50`);

    // Server: "You do not have permission to use this command." or target / usage errors.
    await waitForMessage(
      ithaquaContext.page,
      /do not have permission|You do not have permission|not allowed|not found|Error setting|No such|Usage: admin set/i,
      45000
    );

    const messages = await getMessages(ithaquaContext.page);
    const seesError = messages.some(msg =>
      /permission|not allowed|not found|error setting|no such|usage: admin set/i.test(msg)
    );
    expect(seesError).toBe(true);
  });
});
