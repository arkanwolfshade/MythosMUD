/**
 * Command registry routing (#813): `read`, `stop`, `teach`, and `global` were registered
 * handlers in `_COMMAND_HANDLERS` with no matching `CommandType` member (or, for `global`,
 * no factory entry), so `CommandParser.parse_command()` rejected them before the handler ever
 * ran -- a player typing any of these got "Unknown command" / "Unsupported command" instead of
 * the handler's real response.
 *
 * This spec proves each command now reaches its handler by asserting a handler-specific
 * response, not just the absence of the parser-rejection text. It also locks in that the six
 * lucidity/recovery commands (#813's original report) remain intentionally unreachable --
 * `pray` still returns "Unknown command", confirming the park (see #868-#872) holds.
 */

import { expect, test } from '@playwright/test';
import { ensurePlayableConnection, executeCommand, getMessages, loginPlayer, waitForMessage } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

test.describe('command registry routing (#813)', () => {
  test.beforeEach(async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });
  });

  test('global reaches the chat handler and broadcasts the message', async ({ page }) => {
    const ack = /You say \(global\): hello from the routing spec/i;
    await executeCommand(page, 'global hello from the routing spec');
    await waitForMessage(page, ack, 25000);
    expect((await getMessages(page)).some(msg => ack.test(msg))).toBe(true);
  });

  test("g alias resolves to global (not 'Unknown command: g')", async ({ page }) => {
    const ack = /You say \(global\): hello via the g alias/i;
    await executeCommand(page, 'g hello via the g alias');
    await waitForMessage(page, ack, 25000);
    expect((await getMessages(page)).some(msg => ack.test(msg))).toBe(true);
  });

  test('read reaches its handler and returns its usage string', async ({ page }) => {
    const usage = /Usage: \/read <item_name> \[spell_name\]/i;
    await executeCommand(page, 'read');
    await waitForMessage(page, usage, 25000);
    expect((await getMessages(page)).some(msg => usage.test(msg))).toBe(true);
  });

  test('teach reaches its handler and returns its usage string', async ({ page }) => {
    const usage = /Usage: \/teach <npc_name> <spell_name>/i;
    await executeCommand(page, 'teach');
    await waitForMessage(page, usage, 25000);
    expect((await getMessages(page)).some(msg => usage.test(msg))).toBe(true);
  });

  test('stop reaches the magic handler (not casting a spell)', async ({ page }) => {
    const ack = /You are not casting a spell\./i;
    await executeCommand(page, 'stop');
    await waitForMessage(page, ack, 25000);
    expect((await getMessages(page)).some(msg => ack.test(msg))).toBe(true);
  });

  test('pray remains intentionally unreachable (parked, not routing-broken)', async ({ page }) => {
    const unknown = /Unknown command: pray/i;
    await executeCommand(page, 'pray');
    await waitForMessage(page, unknown, 25000);
    expect((await getMessages(page)).some(msg => unknown.test(msg))).toBe(true);
  });
});
