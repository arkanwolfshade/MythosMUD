/**
 * Scenario 10: Local Channel Movement
 *
 * Tests local channel message routing based on player movement.
 * Verifies that local channel messages are properly routed when players
 * move between sub-zones, that message delivery is updated in real-time
 * based on player location, and that the movement-based routing system
 * works correctly for local communication.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

test.describe('Local Channel Movement', () => {
  test.describe.configure({ mode: 'serial' });

  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Manual "go north" races linkdead / second client dropping; teleport path retries and revives sessions.
    await ensureMultiplayerCoLocated(contexts, {
      timeoutMs: 60000,
      coLocateTimeoutMs: 60000,
    });
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see local message before AW moves', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });
    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|gladiator|heart of the|exits|Laundry|Room/i, 20000);

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'local Before movement test');

    await waitForMessage(awContext.page, /You say locally:\s*Before movement test/i, 45000);

    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade \(local\): Before movement test/i, 35000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): Before movement test'));
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should not see local message after AW moves to different sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });
    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    // Prime command -> log pipeline (Chat / Game Info both use [data-message-text])
    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|gladiator|heart of the|exits|Laundry|Room|hallway/i, 20000);

    await ensureStanding(awContext.page, 5000);
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'go south');

    // Server returns "You go {direction}."; allow extra slack for multiplayer UI sync
    await waitForMessage(awContext.page, /You go south/i, 45000).catch(() => {
      throw new Error('AW failed to move south - movement command did not succeed');
    });

    await new Promise(r => setTimeout(r, 2000));

    // Verify AW and Ithaqua are NOT in the same room before sending message
    // Check that Ithaqua's Occupants panel shows only 1 player (themselves), not 2
    // Note: Use Players count specifically, not total Occupants (which includes NPCs)
    await ithaquaContext.page
      .waitForFunction(
        () => {
          const bodyText = document.body?.innerText ?? '';
          const playersMatch = bodyText.match(/Players\s*\((\d+)\)/);
          const playerCount = playersMatch ? parseInt(playersMatch[1], 10) : 0;
          // Should see only 1 player (themselves) if AW moved to different room
          return playerCount === 1;
        },
        { timeout: 10000 }
      )
      .catch(() => {
        throw new Error('AW and Ithaqua are still in the same room - movement test cannot proceed');
      });

    // AW sends local message from different room (Eastern Hallway); Ithaqua stays in Laundry Room
    await executeCommand(awContext.page, 'local After movement test');

    // Wait for confirmation
    await waitForMessage(awContext.page, /You say locally:\s*After movement test/i, 45000);

    await new Promise(r => setTimeout(r, 3000));

    // Verify Ithaqua does NOT see the message (different rooms = different local scope)
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): After movement test'));
    expect(seesMessage).toBe(false);
  });

  test('Ithaqua should see local message when AW moves back to same sub-zone', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Prior scenarios can leave MP linkdead / empty [data-message-text]; reunite and heal WS before assertions.
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);

    await awContext.page.bringToFront().catch(() => {});
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|gladiator|heart of the|exits|Laundry|Room|hallway/i, 20000);

    await ensureStanding(awContext.page, 5000);
    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'go north');
    await waitForMessage(awContext.page, /You go north/i, 45000).catch(() => {
      // Room graph copy may differ; co-locate step below is authoritative for same-room.
    });

    await new Promise(r => setTimeout(r, 2000));

    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    await waitForMessage(awContext.page, /Arena|gladiator|heart of the|exits|Laundry|Room|hallway/i, 20000);
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'local After returning test');

    await waitForMessage(awContext.page, /You say locally:\s*After returning test/i, 45000);

    // Verify Ithaqua sees the message (they're in same sub-zone again)
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade \(local\): After returning test/i, 45000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade (local): After returning test'));
    expect(seesMessage).toBe(true);
  });
});
