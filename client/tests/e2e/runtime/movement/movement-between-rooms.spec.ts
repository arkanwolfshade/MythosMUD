/**
 * Scenario 3: Movement Between Rooms
 *
 * Tests multiplayer visibility when players move between different rooms.
 * Verifies that movement messages are properly broadcast to other players
 * in the same room, and that players can see each other's room transitions.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

async function nudgeStandBoth(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

test.describe('Movement Between Rooms', () => {
  test.describe.configure({ mode: 'serial' });
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
    // Movement tests require both in the same room and that room must have an east exit
    // (so AW can "go east" and Ithaqua sees "ArkanWolfshade leaves the room"). Co-locate
    // via admin teleport, then move both to Main Foyer using path south -> west -> north
    // (works from Laundry Room or from Main Foyer; both end in Main Foyer which has east).
    const [awContext, ithaquaContext] = contexts;
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'teleport Ithaqua');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
    // Navigate both to Main Foyer (has east exit): south -> west -> north
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 1500));
    await ensureStanding(ithaquaContext.page, 5000);
    await executeCommand(ithaquaContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see AW leave when AW moves east', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });
    await ensurePlayerInGame(awContext, 30000);
    await ensurePlayerInGame(ithaquaContext, 30000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await nudgeStandBoth(awContext, ithaquaContext);

    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';
    const leavePattern = new RegExp(`${escapeRegExp(awCharName)} leaves the room`, 'i');

    await ithaquaContext.page.bringToFront().catch(() => {});
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await ithaquaContext.page.getByTestId('command-input').click();
    await executeCommand(ithaquaContext.page, 'look');
    await waitForMessage(ithaquaContext.page, /Arena|exits|gladiator|sand|Foyer|Hallway/i, 20000).catch(() => {});

    const awMovesEast = async (): Promise<void> => {
      await awContext.page.bringToFront().catch(() => {});
      await ensureStanding(awContext.page, 8000);
      // Movement echoes are system-typed -> Game Info only (Chat stays empty). Prime WS/projector like other MP specs.
      await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
      await awContext.page.getByTestId('command-input').click();
      await executeCommand(awContext.page, 'look');
      await waitForMessage(awContext.page, /Arena|Foyer|Hallway|gladiator|sand|exits|Room/i, 30000).catch(() => {});
      await executeCommand(awContext.page, 'go east');
      await waitForMessage(awContext.page, /You go east|You move east|You head east|Eastern|Hallway/i, 45000);
    };

    await awMovesEast();

    try {
      await waitForCrossPlayerMessage(ithaquaContext, leavePattern, 45000);
    } catch {
      await ensurePlayerInGame(awContext, 30000);
      await ensurePlayerInGame(ithaquaContext, 30000);
      await ensurePlayersInSameRoom(contexts, 2, 45000);
      await nudgeStandBoth(awContext, ithaquaContext);
      await ithaquaContext.page.bringToFront().catch(() => {});
      await ithaquaContext.page.getByTestId('command-input').click();
      await executeCommand(ithaquaContext.page, 'look');
      await new Promise(r => setTimeout(r, 1500));
      await awContext.page.bringToFront().catch(() => {});
      await ensureStanding(awContext.page, 8000);
      await executeCommand(awContext.page, 'go west');
      await new Promise(r => setTimeout(r, 2000));
      await ensurePlayersInSameRoom(contexts, 2, 45000);
      await awMovesEast();
      await waitForCrossPlayerMessage(ithaquaContext, leavePattern, 45000);
    }

    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesAWLeave = ithaquaMessages.some(msg => leavePattern.test(msg));
    expect(seesAWLeave).toBe(true);
  });

  test('AW should not see self-movement messages', async () => {
    const awContext = contexts[0];

    // Check for self-movement messages
    const awMessages = await getMessages(awContext.page);
    const selfMovementMessages = awMessages.filter(
      msg => msg.includes('ArkanWolfshade enters the room') || msg.includes('ArkanWolfshade leaves the room')
    );

    // AW should see NO self-movement messages
    expect(selfMovementMessages).toHaveLength(0);
  });

  test('AW should see Ithaqua enter when Ithaqua moves to same room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Re-ensure both in game before move (avoids timeout when second player left)
    await ensurePlayerInGame(awContext, 10000);
    await ensurePlayerInGame(ithaquaContext, 10000);
    await new Promise(r => setTimeout(r, 2000));

    // AW is in Eastern Hallway from previous test; Ithaqua is in Main Foyer - Ithaqua goes east to join AW
    await ensureStanding(ithaquaContext.page, 5000);
    await ithaquaContext.page.bringToFront().catch(() => {});
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await ithaquaContext.page.getByTestId('command-input').click();
    await executeCommand(ithaquaContext.page, 'go east');
    await waitForMessage(ithaquaContext.page, /You go east|You move east|You head east|Eastern|Hallway/i, 45000).catch(
      () => {}
    );

    // Verify AW sees Ithaqua enter
    await waitForCrossPlayerMessage(awContext, 'Ithaqua enters the room', 45000);
    const awMessages = await getMessages(awContext.page);
    const seesIthaquaEnter = awMessages.some(msg => msg.includes('Ithaqua enters the room'));
    expect(seesIthaquaEnter).toBe(true);
  });

  test('Ithaqua should not see self-movement messages', async () => {
    const ithaquaContext = contexts[1];

    // Check for self-movement messages
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const selfMovementMessages = ithaquaMessages.filter(
      msg => msg.includes('Ithaqua enters the room') || msg.includes('Ithaqua leaves the room')
    );

    // Ithaqua should see NO self-movement messages
    expect(selfMovementMessages).toHaveLength(0);
  });
});
