/// <reference types="node" />

/**
 * Multiplayer in-game readiness and cross-player messaging helpers.
 */

import './multiplayer-browser-window.d.ts';

import { expect, type Browser } from '@playwright/test';
import { assertNoRestDisconnectPollution, ensurePlayableConnection, loginPlayer, waitForPlayableSession } from './auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  reopenPlayerPageIfClosed,
  type PlayerContext,
} from './multiplayer-contexts';
import { assertPlayerAlive } from './player';
import { TEST_TIMEOUTS } from './test-data';

async function waitForPlayerGameUi(page: PlayerContext['page'], username: string, timeoutMs: number): Promise<void> {
  try {
    await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, undefined, { timeout: timeoutMs });
  } catch {
    const diagnostics = await page.evaluate(() => window.__mythosE2eCaptureGameUiDiagnostics?.()).catch(() => null);
    throw new Error(
      `Player ${username} did not reach game UI within ${timeoutMs}ms (still on login?). ` +
        `Diagnostics: ${JSON.stringify(diagnostics)}`
    );
  }
}

async function waitForPlayerWebSocket(page: PlayerContext['page'], username: string, timeoutMs: number): Promise<void> {
  const wsTimeoutMs = Math.min(timeoutMs, 30000);
  try {
    await page.waitForFunction(() => window.__mythosE2eHasConnectedStatus?.() === true, undefined, {
      timeout: wsTimeoutMs,
    });
  } catch {
    throw new Error(
      `Player ${username} WebSocket did not connect within ${wsTimeoutMs}ms (status still shows linkdead?)`
    );
  }
}

async function waitForPlayerRoomSubscription(
  page: PlayerContext['page'],
  username: string,
  timeoutMs: number
): Promise<void> {
  const tickTimeoutMs = Math.min(timeoutMs, 50000);
  try {
    await page.waitForFunction(() => window.__mythosE2eHasRoomSubscription?.() === true, undefined, {
      timeout: tickTimeoutMs,
    });
  } catch {
    throw new Error(
      `Player ${username} room subscription not established within ${tickTimeoutMs}ms (no tick message or room state received)`
    );
  }
}

/**
 * Recreate multiplayer contexts when pages/browsers died or a player landed on login.
 * Keeps conditionals out of Playwright test bodies (playwright/no-conditional-in-test).
 */
export async function ensureFreshMultiPlayerContexts(
  browser: Browser,
  contexts: PlayerContext[],
  playerUsernames: string[],
  waitMs: number = 60000
): Promise<PlayerContext[]> {
  let needsFresh = contexts.some(c => c.page.isClosed()) || contexts.some(c => !c.context.browser()?.isConnected());
  if (!needsFresh) {
    for (const c of contexts) {
      const onLogin = await c.page
        .getByTestId('username-input')
        .isVisible({ timeout: 1500 })
        .catch(() => false);
      if (onLogin) {
        needsFresh = true;
        break;
      }
    }
  }
  if (!needsFresh) {
    return contexts;
  }
  await cleanupMultiPlayerContexts(contexts).catch(() => {});
  const next = await createMultiPlayerContexts(browser, playerUsernames);
  await waitForAllPlayersInGame(next, waitMs);
  return next;
}

/**
 * Wait until all player contexts are fully ready for multiplayer testing.
 * Call this after createMultiPlayerContexts in beforeAll so tests that assume both
 * players are in game (who, chat, whisper, local, movement, summon) run only when ready.
 *
 * This function performs a 3-step verification for ALL players:
 * 1. Game UI loaded (not on login screen)
 * 2. WebSocket connected (status shows "Connected" not "linkdead")
 * 3. Room subscription established (tick message received via NATS)
 *
 * @param contexts - Array of PlayerContext objects (from createMultiPlayerContexts)
 * @param timeoutMs - Timeout per context in milliseconds (default: TEST_TIMEOUTS.GAME_LOAD)
 */
export async function waitForAllPlayersInGame(
  contexts: PlayerContext[],
  timeoutMs: number = TEST_TIMEOUTS.GAME_LOAD
): Promise<void> {
  // Step 1: Wait for all players to reach game UI (not on login screen)
  // Broadened detection: command input, Game Info, game terminal, Player header, Mythos Time, or room content
  await Promise.all(
    contexts.map(async ({ page, player }) => {
      try {
        await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, undefined, {
          timeout: timeoutMs,
        });
      } catch (err) {
        const diagnostics = await page.evaluate(() => window.__mythosE2eCaptureGameUiDiagnostics?.()).catch(() => null);
        const msg =
          `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
          `Step 1: game UI - still on login screen after ${timeoutMs}ms. ` +
          `Diagnostics: ${JSON.stringify(diagnostics)}`;
        console.error(msg, err);
        throw Object.assign(new Error(msg), { cause: err });
      }
    })
  );

  // Step 2: Wait for all players' WebSocket connections to be established (status shows "Connected")
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(() => window.__mythosE2eHasConnectedStatus?.() === true, undefined, {
          timeout: Math.min(timeoutMs, 30000), // Max 30s for WebSocket connection per player
        })
        .catch(err => {
          const wsTimeout = Math.min(timeoutMs, 30000);
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 2: WebSocket - status still shows linkdead after ${wsTimeout}ms`;
          console.error(msg, err);
          throw Object.assign(new Error(msg), { cause: err });
        })
    )
  );

  // Step 3: Wait for all players' room subscriptions to be established
  // Check for tick message OR room state indicators (more robust than tick-only)
  // Use a longer cap (50s) so the slower client has time to receive first tick after Connected.
  const step3Timeout = Math.min(timeoutMs, 50000);
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(() => window.__mythosE2eHasRoomSubscription?.() === true, undefined, { timeout: step3Timeout })
        .catch(err => {
          const tickTimeout = step3Timeout;
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 3: room subscription - no tick message or room state after ${tickTimeout}ms`;
          console.error(msg, err);
          throw Object.assign(new Error(msg), { cause: err });
        })
    )
  );

  // Brief stability wait after all room subscriptions established (allow room broadcasts to settle)
  await new Promise(resolve => setTimeout(resolve, 3000));
}

/**
 * Ensure a single player context is fully ready for multiplayer testing.
 * Call after waitForAllPlayersInGame when tests still see the second player on login.
 *
 * This function performs a 3-step verification:
 * 1. Game UI loaded (not on login screen)
 * 2. WebSocket connected (status shows "Connected" not "linkdead")
 * 3. Room subscription established (tick message received via NATS)
 *
 * @param playerContext - PlayerContext to ensure is in game
 * @param timeoutMs - Max wait in milliseconds (default: 60000)
 */
export async function ensurePlayerInGame(playerContext: PlayerContext, timeoutMs: number = 60000): Promise<void> {
  await reopenPlayerPageIfClosed(playerContext);
  const { player } = playerContext;
  // Relogin when still on the login screen; waiting alone leaves AW stuck after prior serial teardown.
  playerContext.page = await ensurePlayableConnection(playerContext.page, {
    username: player.username,
    password: player.password,
    timeoutMs: Math.min(timeoutMs, 45000),
  });
  playerContext.context = playerContext.page.context();
  const { page } = playerContext;
  await waitForPlayerGameUi(page, player.username, timeoutMs);
  await assertPlayerAlive(page, player.username);
  await waitForPlayerWebSocket(page, player.username, timeoutMs);
  await waitForPlayerRoomSubscription(page, player.username, timeoutMs);
  await new Promise(resolve => setTimeout(resolve, 1000));
}

/**
 * After switching which browser tab is foreground, restore command input when Send stayed disabled.
 * Reload only when already in the game UI; re-login if reload returns to the login screen.
 */
export async function ensureForegroundPlayerPlayable(
  playerContext: PlayerContext,
  timeoutMs: number = 45000
): Promise<void> {
  const { page, player } = playerContext;
  await page.bringToFront().catch(() => {});

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (onLogin) {
    await loginPlayer(page, player.username, player.password);
    return;
  }

  await ensurePlayerInGame(playerContext, timeoutMs);

  playerContext.page = await ensurePlayableConnection(playerContext.page, {
    username: player.username,
    password: player.password,
    timeoutMs,
  });
  playerContext.context = playerContext.page.context();
}

/**
 * Foreground the receiver and restore command input so Game Info renders inbound WS events.
 * Background Firefox tabs often show ticks but miss chat/combat lines until focused.
 */
export async function prepareReceiverForInboundMessages(
  playerContext: PlayerContext,
  timeoutMs: number = 20000
): Promise<void> {
  await reopenPlayerPageIfClosed(playerContext);
  const { page, player } = playerContext;
  await page.bringToFront().catch(() => {});
  await assertNoRestDisconnectPollution(page);

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (onLogin) {
    await loginPlayer(page, player.username, player.password);
    await ensurePlayerInGame(playerContext, timeoutMs);
    await assertNoRestDisconnectPollution(page);
    return;
  }

  await waitForPlayableSession(page, timeoutMs).catch(() => {});
  playerContext.page = await ensurePlayableConnection(page, {
    username: player.username,
    password: player.password,
    timeoutMs,
  }).catch(() => page);
  playerContext.context = playerContext.page.context();
  await assertNoRestDisconnectPollution(playerContext.page);
}

/**
 * Wait for a message to appear in a specific player's context.
 *
 * @param playerContext - PlayerContext to check
 * @param expectedText - Text to wait for (string or RegExp)
 * @param timeout - Timeout in milliseconds
 */
export async function waitForCrossPlayerMessage(
  playerContext: PlayerContext,
  expectedText: string | RegExp,
  timeout: number = 35000
): Promise<void> {
  await prepareReceiverForInboundMessages(playerContext, Math.min(timeout, 25000));

  // Use locator for both string and RegExp: Playwright's filter({ hasText }) accepts RegExp.
  // Prefer locator over waitForFunction for auto-wait, retries, and clearer timeout errors.
  // If this times out, the receiving player may have left the game or be in a different room
  // (say is room-scoped); check Game Info for "has left the game" and Occupants for co-location.
  const messageLocator = playerContext.page.locator('[data-message-text]');
  try {
    await expect
      .poll(
        async () => {
          const onLogin = await playerContext.page
            .getByTestId('username-input')
            .isVisible({ timeout: 500 })
            .catch(() => false);
          if (onLogin) {
            await loginPlayer(playerContext.page, playerContext.player.username, playerContext.player.password);
            await ensurePlayerInGame(playerContext, Math.min(timeout, 30000));
            await prepareReceiverForInboundMessages(playerContext, Math.min(timeout, 15000));
            return false;
          }
          return (await messageLocator.filter({ hasText: expectedText }).count()) > 0;
        },
        {
          timeout,
          message: 'cross-player message in Game Info',
        }
      )
      .toBe(true);
    await messageLocator.filter({ hasText: expectedText }).first().waitFor({ state: 'visible', timeout: 5000 });
  } catch (err) {
    const actualMessages = await getPlayerMessages(playerContext);
    const expectedStr = typeof expectedText === 'string' ? expectedText : expectedText.source;

    // Check if receiver has left the game (common cause of message delivery failure)
    const hasLeftMessage = actualMessages.some(
      msg => msg.toLowerCase().includes('has left the game') || msg.toLowerCase().includes('leaves the room')
    );
    const leftHint = hasLeftMessage ? ' Receiver appears to have left the game/room before message was sent.' : '';

    const onLoginAtTimeout = await playerContext.page
      .getByTestId('username-input')
      .isVisible({ timeout: 500 })
      .catch(() => false);
    const sessionHint = onLoginAtTimeout
      ? ' Receiver is on the login screen (session lost while sender tab had focus). ' +
        'Call prepareReceiverForInboundMessages(receiver) immediately after send and use Promise.all for sender echo + cross-player wait.'
      : '';

    throw Object.assign(
      new Error(
        `waitForCrossPlayerMessage timed out: Player ${playerContext.player.username} did not see "${expectedStr}" ` +
          `within ${timeout}ms. Received ${actualMessages.length} message(s): ${JSON.stringify(actualMessages.slice(-5))}. ` +
          `Possible causes: receiver in different room (say is room-scoped), mute filter blocking delivery, or network delay.${leftHint}${sessionHint}`
      ),
      { cause: err }
    );
  }
}

/**
 * Get messages from a specific player's context.
 *
 * @param playerContext - PlayerContext to get messages from
 * @returns Array of message texts
 */
export async function getPlayerMessages(playerContext: PlayerContext): Promise<string[]> {
  const messages = await playerContext.page.evaluate(() => {
    const msgs = Array.from(document.querySelectorAll('[data-message-text]'));
    return msgs.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });
  return messages;
}
