/**
 * Scenario 5: Chat Messages Between Players
 *
 * Tests chat message broadcasting between players in the same room.
 * Verifies that players can send and receive chat messages, that messages
 * are properly formatted, and that the chat system works correctly for
 * multiplayer communication.
 */

import { expect, test, type Page } from '@playwright/test';
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
  type PlayerContext,
} from '../fixtures/multiplayer';

/**
 * Header can show Connected while Occupants still lists (linkdead); command_response may not
 * render on [data-message-text] until sessions recover. Matches local-channel-basic pattern.
 */
async function nudgeStandBothPlayers(aw: PlayerContext, other: PlayerContext): Promise<void> {
  await executeCommand(aw.page, 'stand');
  await executeCommand(other.page, 'stand');
  await new Promise(r => setTimeout(r, 3000));
}

/**
 * `look` often updates Location / Room Description panels while Game Info may not repeat the same
 * prose on `[data-message-text]`. Accept either so probes match real UI (Playwright: wait for user-visible outcome).
 */
async function waitForLookReflected(page: Page): Promise<void> {
  await page.waitForFunction(
    () => {
      const body = document.body?.innerText ?? '';
      if (/Arena\s*>|heart of the gladiator|Exits:\s*North/i.test(body)) return true;
      return Array.from(document.querySelectorAll('[data-message-text]')).some(el => {
        const v = (el.getAttribute('data-message-text') || '').trim();
        return /Arena|gladiator|heart of the|exits|sand|You see/i.test(v);
      });
    },
    { timeout: 45000 }
  );
}

/** Refresh room_state and [data-message-text] on both clients before teleport / occupant sync (linkdead recovery). */
async function primeBothForCoLocate(contexts: PlayerContext[]): Promise<void> {
  if (contexts.length < 2) return;
  await Promise.all([ensurePlayerInGame(contexts[0], 30000), ensurePlayerInGame(contexts[1], 30000)]);
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    // executeCommand uses fill(), which does not require Playwright's "stable" check. Avoid click() here:
    // focused command-input runs focus:animate-eldritch-border indefinitely and click() never stabilizes.
    await executeCommand(ctx.page, 'look');
    await waitForLookReflected(ctx.page).catch(() => {});
  }
}

test.describe('Chat Messages Between Players', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // Room-based /say requires both in the same cell. "go north" from both clients often leaves
    // Occupants (1) when the arena grid or transient linkdead prevents room_state from matching;
    // ensureMultiplayerCoLocated teleports + retries like other runtime multiplayer specs.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 60000 });

    const [awContext, ithaquaContext] = contexts;
    // Unmute both players to ensure clean state (mute state may persist from previous scenarios)
    // Mute filtering happens on the receiving end, so both players need to unmute each other
    try {
      // Ithaqua unmutes AW (so Ithaqua can see AW's messages)
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await new Promise(r => setTimeout(r, 1000));

      // AW unmutes Ithaqua (so AW can see Ithaqua's messages)
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await new Promise(r => setTimeout(r, 1000));

      // Small additional wait to ensure mute state is cleared
      await new Promise(r => setTimeout(r, 1000));
    } catch {
      // Ignore unmute errors - players may not be muted to begin with
      // This is expected if mute state doesn't persist between test runs
    }
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should see AW chat message', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // Suite order / idle can leave both clients linkdead; prime before co-locate or 5x45s sync blows the 180s test budget.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    // Ensure Ithaqua has unmuted AW so the server delivers AW's say to Ithaqua (mute filter is per-receiver).
    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        8000
      );
    } catch {
      // Ignore if already unmuted or command fails
    }
    // Allow server mute state to be applied before we send the say (avoids filtered delivery).
    await new Promise(r => setTimeout(r, 2500));

    // Re-ensure receiver (Ithaqua) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await new Promise(r => setTimeout(r, 2000));

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    // Sender must be focused on some CI hosts; echo lands on [data-message-text] only when WS is healthy.
    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);

    // AW sends chat message
    await executeCommand(awContext.page, 'say Hello Ithaqua');

    // Regex: tolerate minor formatting drift; longer timeout after co-locate / linkdead recovery.
    await waitForMessage(awContext.page, /You say:\s*Hello Ithaqua/i, 45000);

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Hello Ithaqua/i, 45000);

    // Verify Ithaqua sees the message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.toLowerCase().includes('arkanwolfshade says: hello ithaqua'));
    expect(seesMessage).toBe(true);
  });

  test('AW should see Ithaqua chat message', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      // Receiver-focused client must run unmute; same as local-channel-basic (command_response on AW).
      await awContext.page.bringToFront().catch(() => {});
      await executeCommand(awContext.page, 'unmute Ithaqua');
      await waitForMessage(awContext.page, /You have unmuted Ithaqua|Failed to unmute Ithaqua/i, 30000);
      await new Promise(r => setTimeout(r, 1500));
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Re-ensure receiver (AW) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(awContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await new Promise(r => setTimeout(r, 2000));

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    // Sender must be the focused context for some CI hosts; echo is on Ithaqua's page, not AW's.
    await ithaquaContext.page.bringToFront().catch(() => {});
    // Prime after nudge: early wait can pass, then stand burst leaves no fresh command_response on chat.
    await ithaquaContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await ensurePlayerInGame(ithaquaContext, 30000);

    // Wrong browser / wrong session yields command history on one context and assertions on another.
    await expect(ithaquaContext.page.getByText(/Player:\s*Ithaqua\b/i)).toBeVisible({ timeout: 15000 });

    // Probe: ensure `look` landed in UI (panels and/or command log) before /say.
    await executeCommand(ithaquaContext.page, 'look');
    await waitForLookReflected(ithaquaContext.page);

    // Ithaqua sends chat message
    await executeCommand(ithaquaContext.page, 'say Hello ArkanWolfshade');

    // Regex: tolerate minor formatting drift; timeout above default 10s MESSAGE for slow command_response.
    await waitForMessage(ithaquaContext.page, /You say:\s*Hello ArkanWolfshade/i, 45000);

    // Wait for message to appear on AW's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(awContext, /Ithaqua says: Hello ArkanWolfshade/i, 45000);

    // Verify AW sees the message
    const awMessages = await getPlayerMessages(awContext);
    const seesMessage = awMessages.some(msg => msg.toLowerCase().includes('ithaqua says: hello arkanwolfshade'));
    expect(seesMessage).toBe(true);
  });

  test('chat messages should be properly formatted', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 15000 });
    await new Promise(r => setTimeout(r, 1500));

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    try {
      await executeCommand(ithaquaContext.page, 'unmute ArkanWolfshade');
      await waitForMessage(
        ithaquaContext.page,
        /You have unmuted ArkanWolfshade|Failed to unmute ArkanWolfshade/i,
        8000
      );
      await new Promise(r => setTimeout(r, 1500));
    } catch {
      // Ignore if already unmuted or command fails
    }

    // Re-ensure receiver (Ithaqua) is in game and same room; brief stability wait so receiver is not
    // linkdead when sender sends
    await ensurePlayerInGame(ithaquaContext, 10000);
    await ensurePlayersInSameRoom(contexts, 2, 45000);
    await new Promise(r => setTimeout(r, 2000));

    await nudgeStandBothPlayers(awContext, ithaquaContext);

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    // linkdead / quiet WS: command history updates but Game Info never gets echo; warm pipeline like Ithaqua probe.
    await executeCommand(awContext.page, 'look');
    await waitForLookReflected(awContext.page);
    await new Promise(r => setTimeout(r, 1000));

    // AW sends formatted message
    await executeCommand(awContext.page, 'say Testing message formatting');

    await waitForMessage(awContext.page, /You say:.*Testing message formatting/i, 45000);

    // Wait for message to appear on Ithaqua's side with increased timeout and flexibility
    await waitForCrossPlayerMessage(ithaquaContext, /ArkanWolfshade says: Testing message formatting/i, 45000);

    // Verify Ithaqua sees properly formatted message
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesFormattedMessage = ithaquaMessages.some(msg =>
      msg.toLowerCase().includes('arkanwolfshade says: testing message formatting')
    );
    expect(seesFormattedMessage).toBe(true);
  });
});
