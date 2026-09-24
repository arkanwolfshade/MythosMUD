/**
 * #688: Inventory actions write to inventory.log
 *
 * Drives a real equip/unequip flow and asserts the server actually wrote the corresponding
 * lines to logs/e2e_test/inventory.log -- not just that the client displayed a message.
 *
 * Equip/unequip already log "Item equipped"/"Item unequipped" at INFO with full player/item/
 * slot context in server/commands/inventory_{equip,unequip}_command.py; DEFAULT_LOG_CATEGORIES
 * routes those two command loggers into the "inventory" category alongside "commands" (see
 * server/structured_logging/logging_file_categories.py). This test is the regression guard for
 * that routing, and readLogTail's sibling helpers (fixtures/server-logs.ts) are reusable for
 * other log categories.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import { escapeRegExpLiteral } from '../fixtures/message-match';
import { createMultiPlayerContexts, cleanupMultiPlayerContexts, ensurePlayerInGame } from '../fixtures/multiplayer';
import { logOffset, waitForLogLine } from '../fixtures/server-logs';

const SLING_ITEM_ID = 'pack_dark_ages.weapon.sling';
const SLING_ITEM_ID_ESCAPED = escapeRegExpLiteral(SLING_ITEM_ID);

/** Match a structured log line containing both `event='<event>'` and `item_id='<SLING_ITEM_ID>'`,
 * in either order -- structlog's key ordering follows call-site kwarg order, not a fixed schema. */
function inventoryLogLinePattern(event: string): RegExp {
  return new RegExp(`(?=.*event='${event}')(?=.*item_id='${SLING_ITEM_ID_ESCAPED}')`);
}

test.describe('Inventory actions write to inventory.log', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade']);
    await ensurePlayerInGame(contexts[0], 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('equip and unequip log to inventory.log', async () => {
    const awContext = contexts[0];
    const page = awContext.page;

    await executeCommand(page, `/summon ${SLING_ITEM_ID} 1`);
    await waitForMessage(page, /You summon\s+1x/i, 15000);

    await executeCommand(page, 'pickup sling');
    await waitForMessage(page, /You pick up/i, 10000);

    try {
      const preEquipOffset = logOffset('inventory');
      await executeCommand(page, 'equip sling');
      await waitForMessage(page, /You equip/i, 10000);
      const equippedLine = await waitForLogLine(
        'inventory',
        preEquipOffset,
        inventoryLogLinePattern('Item equipped'),
        10000
      );
      expect(equippedLine).toContain("logger='server.commands.inventory_equip_command'");

      const preUnequipOffset = logOffset('inventory');
      await executeCommand(page, 'unequip main_hand');
      await waitForMessage(page, /You remove/i, 10000);
      const unequippedLine = await waitForLogLine(
        'inventory',
        preUnequipOffset,
        inventoryLogLinePattern('Item unequipped'),
        10000
      );
      expect(unequippedLine).toContain("logger='server.commands.inventory_unequip_command'");
    } finally {
      // Leave AW's persistent inventory unchanged regardless of assertion outcome. `drop` only
      // accepts a 1-based inventory index, not a name search -- after unequip, the sling is the
      // sole (and thus first) inventory stack.
      await executeCommand(page, 'drop 1');
      await waitForMessage(page, /You drop/i, 10000).catch(() => {});
    }
  });
});
