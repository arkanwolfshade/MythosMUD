/// <reference types="node" />

/**
 * Multiplayer Fixtures
 *
 * Helper functions for managing multiple browser contexts in multiplayer scenarios.
 */

import { spawnSync } from 'child_process';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

import './multiplayer-browser-window.d.ts';

import { expect, type Browser, type BrowserContext, type Page } from '@playwright/test';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import { MotdPage } from '../pages';
import {
  ensurePlayableConnection,
  executeCommand,
  executeCommandTrusted,
  loginPlayer,
  logoutPlayer,
  waitForPlayableSession,
} from './auth';
import type { OccupantsSnapshot } from './multiplayer-browser-helpers';
import { TEST_PLAYERS, TEST_TIMEOUTS, type TestPlayer } from './test-data';

const __dirname = dirname(fileURLToPath(import.meta.url));
const BROWSER_HELPERS_BUNDLE = join(__dirname, 'multiplayer-browser-helpers.bundle.js');

async function installE2eBrowserHelpers(context: BrowserContext): Promise<void> {
  await context.addInitScript({ path: BROWSER_HELPERS_BUNDLE });
}

/** Use 127.0.0.1 to avoid localhost resolving to IPv6 (::1) when server listens on IPv4 only. */
const SERVER_URL = 'http://127.0.0.1:54768';
/** Versioned API base for v1 endpoints (health, etc.). */
const SERVER_API_V1 = `${SERVER_URL}/v1`;
const SERVER_READY_POLL_MS = 500;
/** Allow up to 60s for server/DB/NATS to become ready (cold start, CI). */
const SERVER_READY_TIMEOUT_MS = 60000;

/**
 * Poll server health endpoint until it responds 200/503 or timeout.
 * Ensures server is ready before first player login (avoids "still on login" when server was cold).
 * Uses versioned API path /v1/monitoring/health. Accepts 200 (healthy) or 503 (unhealthy but reachable).
 */
async function waitForServerReady(): Promise<void> {
  const healthUrl = `${SERVER_API_V1}/monitoring/health`;
  const start = Date.now();
  let lastStatus: number | null = null;
  while (Date.now() - start < SERVER_READY_TIMEOUT_MS) {
    try {
      const res = await fetch(healthUrl, { signal: AbortSignal.timeout(3000) });
      lastStatus = res.status;
      if (res.ok || res.status === 503) return;
    } catch {
      lastStatus = null;
    }
    await new Promise(r => setTimeout(r, SERVER_READY_POLL_MS));
  }
  const statusHint =
    lastStatus !== null ? ` Last response: ${lastStatus}.` : ' No response (connection refused or timeout).';
  throw new Error(
    `[instrumentation] Server not ready at ${healthUrl} within ${SERVER_READY_TIMEOUT_MS}ms.${statusHint} ` +
      'Runtime E2E tests require the server to be started first. ' +
      'Run ./scripts/start_local.ps1 from project root (after ./scripts/stop_server.ps1 if needed) and ensure port 54768 is free.'
  );
}

export interface PlayerContext {
  context: BrowserContext;
  page: Page;
  player: TestPlayer;
}

/**
 * Create multiple authenticated browser contexts for multiplayer testing.
 *
 * CRITICAL: Each player gets a separate browser context (browser.newContext()). Playwright
 * isolates localStorage, sessionStorage, and cookies per context. Logging in AW cannot
 * overwrite or clear Ithaqua's tokens (and vice versa)—no shared storage between tabs.
 * Do not reuse a single context or share storageState across players.
 *
 * @param browser - Playwright browser instance
 * @param playerUsernames - Array of usernames to create contexts for
 * @returns Array of PlayerContext objects
 */
export async function createMultiPlayerContexts(browser: Browser, playerUsernames: string[]): Promise<PlayerContext[]> {
  const contexts: PlayerContext[] = [];

  // Ensure server is ready before any login (avoids first-player "still on login" when server cold)
  await waitForServerReady();

  for (let i = 0; i < playerUsernames.length; i++) {
    const username = playerUsernames[i];
    const player = TEST_PLAYERS.find(p => p.username === username);
    if (!player) {
      throw new Error(`Test player not found: ${username}`);
    }

    // Stagger second (and later) player logins to reduce concurrent load and session thrash.
    // 5s gives server time to finish first player's WebSocket/subscriptions before second login.
    if (i > 0) {
      await new Promise(resolve => setTimeout(resolve, 5000));
    }

    // Fresh context per player (no storageState). Isolated storage prevents cross-login effects.
    const context = await browser.newContext();
    await installE2eBrowserHelpers(context);
    const page = await context.newPage();

    await loginPlayer(page, player.username, player.password);

    // Post-login stabilization: first player needs extra time for UI to fully render
    if (i === 0) {
      await new Promise(r => setTimeout(r, 2000));
    }

    contexts.push({ context, page, player });
  }

  return contexts;
}

/**
 * Cleanup multiple player contexts.
 *
 * Intentionally logs out each player before closing the browser context so the server
 * does not leave linkdead ghosts that poison the next serial test.
 *
 * @param contexts - Array of PlayerContext objects to cleanup
 */
export async function cleanupMultiPlayerContexts(contexts: PlayerContext[] | undefined): Promise<void> {
  if (!contexts || !Array.isArray(contexts)) {
    return;
  }
  for (const { page } of contexts) {
    await logoutPlayer(page, 90000).catch(() => {});
    await page
      .getByTestId('username-input')
      .waitFor({ state: 'visible', timeout: 15000 })
      .catch(() => {});
  }
  for (const { context } of contexts) {
    await context.close().catch(() => {
      // Ignore errors during cleanup
    });
  }
}

async function waitForPlayerGameUi(page: Page, username: string, timeoutMs: number): Promise<void> {
  try {
    await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, { timeout: timeoutMs });
  } catch {
    const diagnostics = await page.evaluate(() => window.__mythosE2eCaptureGameUiDiagnostics?.()).catch(() => null);
    throw new Error(
      `Player ${username} did not reach game UI within ${timeoutMs}ms (still on login?). ` +
        `Diagnostics: ${JSON.stringify(diagnostics)}`
    );
  }
}

async function waitForPlayerWebSocket(page: Page, username: string, timeoutMs: number): Promise<void> {
  const wsTimeoutMs = Math.min(timeoutMs, 30000);
  try {
    await page.waitForFunction(() => window.__mythosE2eHasConnectedStatus?.() === true, { timeout: wsTimeoutMs });
  } catch {
    throw new Error(
      `Player ${username} WebSocket did not connect within ${wsTimeoutMs}ms (status still shows linkdead?)`
    );
  }
}

async function waitForPlayerRoomSubscription(page: Page, username: string, timeoutMs: number): Promise<void> {
  const tickTimeoutMs = Math.min(timeoutMs, 50000);
  try {
    await page.waitForFunction(() => window.__mythosE2eHasRoomSubscription?.() === true, { timeout: tickTimeoutMs });
  } catch {
    throw new Error(
      `Player ${username} room subscription not established within ${tickTimeoutMs}ms (no tick message or room state received)`
    );
  }
}

function formatOccupantsSnapshotForError(snapshot: unknown): string {
  if (typeof snapshot !== 'object' || snapshot === null) {
    return String(snapshot);
  }
  if ('error' in snapshot) {
    return (snapshot as { error?: string }).error ?? 'page closed or evaluate failed';
  }
  const snap = snapshot as OccupantsSnapshot;
  return (
    `occupants=${snap.occupantsCount ?? '?'} ` +
    `players=${snap.playersCount ?? '?'} ` +
    `linkdead=${snap.hasLinkdead ?? '?'}`
  );
}

async function throwOccupantsWaitTimeout(
  page: Page,
  player: TestPlayer,
  expectedOccupants: number,
  timeoutMs: number
): Promise<never> {
  const snapshot = await page
    .evaluate(() => window.__mythosE2eCaptureOccupantsSnapshot?.())
    .catch(() => ({ error: 'page closed or evaluate failed' }));
  const snapshotStr = JSON.stringify(snapshot, null, 2);
  console.error(
    `[instrumentation] ensurePlayersInSameRoom Step 1 timeout - Player ${player.username} saw:`,
    snapshotStr
  );
  const shortSnap = formatOccupantsSnapshotForError(snapshot);
  const msg =
    `[instrumentation] ensurePlayersInSameRoom failed: Player ${player.username} - ` +
    `Step 1: occupants - did not see ${expectedOccupants} within ${timeoutMs}ms (saw: ${shortSnap})`;
  throw new Error(msg);
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
        await page.waitForFunction(() => window.__mythosE2eIsGameUiLoaded?.() === true, { timeout: timeoutMs });
      } catch (err) {
        const diagnostics = await page.evaluate(() => window.__mythosE2eCaptureGameUiDiagnostics?.()).catch(() => null);
        const msg =
          `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
          `Step 1: game UI - still on login screen after ${timeoutMs}ms. ` +
          `Diagnostics: ${JSON.stringify(diagnostics)}`;
        console.error(msg, err);
        throw new Error(msg, { cause: err });
      }
    })
  );

  // Step 2: Wait for all players' WebSocket connections to be established (status shows "Connected")
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(() => window.__mythosE2eHasConnectedStatus?.() === true, {
          timeout: Math.min(timeoutMs, 30000), // Max 30s for WebSocket connection per player
        })
        .catch(err => {
          const wsTimeout = Math.min(timeoutMs, 30000);
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 2: WebSocket - status still shows linkdead after ${wsTimeout}ms`;
          console.error(msg, err);
          throw new Error(msg, { cause: err });
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
        .waitForFunction(() => window.__mythosE2eHasRoomSubscription?.() === true, { timeout: step3Timeout })
        .catch(err => {
          const tickTimeout = step3Timeout;
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 3: room subscription - no tick message or room state after ${tickTimeout}ms`;
          console.error(msg, err);
          throw new Error(msg, { cause: err });
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
  const { page, player } = playerContext;
  await waitForPlayableSession(page, Math.min(timeoutMs, 30000)).catch(() => {});
  await waitForPlayerGameUi(page, player.username, timeoutMs);
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

  await ensurePlayableConnection(page, {
    username: player.username,
    password: player.password,
    timeoutMs,
  });
}

/**
 * Foreground the receiver and restore command input so Game Info renders inbound WS events.
 * Background Firefox tabs often show ticks but miss chat/combat lines until focused.
 */
export async function prepareReceiverForInboundMessages(
  playerContext: PlayerContext,
  timeoutMs: number = 20000
): Promise<void> {
  const { page, player } = playerContext;
  await page.bringToFront().catch(() => {});

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (onLogin) {
    await loginPlayer(page, player.username, player.password);
    await ensurePlayerInGame(playerContext, timeoutMs);
    return;
  }

  await waitForPlayableSession(page, timeoutMs).catch(() => {});
  await ensurePlayableConnection(page, {
    username: player.username,
    password: player.password,
    timeoutMs,
  }).catch(() => {});
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

    throw new Error(
      `waitForCrossPlayerMessage timed out: Player ${playerContext.player.username} did not see "${expectedStr}" ` +
        `within ${timeout}ms. Received ${actualMessages.length} message(s): ${JSON.stringify(actualMessages.slice(-5))}. ` +
        `Possible causes: receiver in different room (say is room-scoped), mute filter blocking delivery, or network delay.${leftHint}${sessionHint}`,
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

/**
 * Ensure all players are co-located in the same room by checking room occupant counts.
 * This function verifies that all players can see each other in the Occupants panel,
 * which indicates they are in the same room and can communicate via local channels.
 *
 * CRITICAL: Call this AFTER waitForAllPlayersInGame and BEFORE any communication tests
 * that require same room (/say, /local). Not required for /whisper or /teleport.
 *
 * @param contexts - Array of PlayerContext objects
 * @param expectedOccupants - Expected number of players in the room (default: contexts.length)
 * @param timeoutMs - Max wait in milliseconds (default: 45000)
 */
export async function ensurePlayersInSameRoom(
  contexts: PlayerContext[],
  expectedOccupants: number = contexts.length,
  timeoutMs: number = 45000
): Promise<void> {
  // Step 0: Wait for all players' header connection status to show "Connected" (same as waitForAllPlayersInGame).
  // Do not require absence of "(linkdead)" in the whole body: the Occupants panel can show "Name (linkdead)"
  // even when the header already shows "Connected", which would otherwise block this step forever.
  const linkdeadWaitMs = Math.min(25000, timeoutMs);
  await Promise.all(
    contexts.map(({ page, player }) =>
      ensurePlayableConnection(page, {
        username: player.username,
        password: player.password,
        timeoutMs: linkdeadWaitMs,
      }).catch(err => {
        const msg =
          `[instrumentation] ensurePlayersInSameRoom failed: Player ${player.username} - ` +
          `Step 0: header still not Connected within ${linkdeadWaitMs}ms`;
        console.error(msg, err);
        throw new Error(msg);
      })
    )
  );

  // Step 1: Wait for all players to see the expected number of occupants in their room
  // Detection supports: OccupantsPanel title "Occupants (n)", content "Players (n)", or RoomInfoPanel "Occupants (n):"
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          (expected: number) => window.__mythosE2eHasExpectedOccupantCount?.(expected) === true,
          expectedOccupants,
          { timeout: timeoutMs }
        )
        .catch(async () => throwOccupantsWaitTimeout(page, player, expectedOccupants, timeoutMs))
    )
  );

  // Step 2: Verify each player sees all other players by name in the Occupants section.
  // This catches edge cases where count >= 2 but the other test player is not actually co-located.
  const getOtherUsernames = (ctx: PlayerContext) =>
    contexts.filter(c => c.player.username !== ctx.player.username).map(c => c.player.username);
  await Promise.all(
    contexts.map(ctx => {
      const expectedNames = getOtherUsernames(ctx);
      if (expectedNames.length === 0) return Promise.resolve();
      return ctx.page
        .waitForFunction(
          (expectedNames: string[]) => window.__mythosE2eHasOtherPlayerNames?.(expectedNames) === true,
          expectedNames,
          { timeout: Math.min(20000, timeoutMs) }
        )
        .catch(() => {
          throw new Error(
            `ensurePlayersInSameRoom: Player ${ctx.player.username} does not see ${expectedNames.join(', ')} in room ` +
              `(required for room-scoped /say)`
          );
        });
    })
  );

  // Brief stability wait after all players see each other and are connected
  await new Promise(resolve => setTimeout(resolve, 1000));
}

export interface EnsureMultiplayerCoLocatedOptions {
  /** Max wait for waitForAllPlayersInGame / ensurePlayerInGame (default 60000). */
  timeoutMs?: number;
  /** Max wait for ensurePlayersInSameRoom occupant sync (default 45000). */
  coLocateTimeoutMs?: number;
}

const TELEPORT_SETTLE_BASE_MS = 6000;
const MAX_COLOCATE_ATTEMPTS = 5;

/**
 * Reset E2E player rows in mythos_e2e (same script as global-teardown).
 * In-memory server state is stale until players relog; pair with {@link resyncE2ePlayersAfterDatabaseReset}.
 */
export function resetE2ePlayerRoomsInDatabase(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const scriptPath = join(E2E_PROJECT_ROOT, 'scripts', 'e2e_reset_players.py');
  const result = spawnSync('uv', ['run', 'python', scriptPath], {
    cwd: E2E_PROJECT_ROOT,
    shell: true,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
  });
  if (result.status !== 0) {
    console.warn('[instrumentation] e2e_reset_players.py failed', result.status, result.stderr?.slice(0, 500) ?? '');
  }
}

/**
 * After `look`, room copy is usually in Location / Room Description, not only Game Info `[data-message-text]`.
 * Accept arena staging or any room that exposes exits (death void has none).
 */
export async function waitForLookReflectedInUi(page: Page, timeoutMs: number = 45000): Promise<void> {
  await page.waitForFunction(
    () => {
      const body = document.body?.innerText ?? '';
      if (
        /Arena\s*>|heart of the gladiator|gladiator ring|sand and shadow|Main Foyer|Hallway|Eastern|Laundry|Exits:\s*(North|north|east|west|south)/i.test(
          body
        )
      ) {
        return true;
      }
      if (/Exits:\s*\w+/i.test(body)) return true;
      return Array.from(document.querySelectorAll('[data-message-text]')).some(el => {
        const v = (el.getAttribute('data-message-text') || '').trim();
        return /Arena|gladiator|heart of the|Exits:|sand and shadow|Foyer|Hallway/i.test(v);
      });
    },
    { timeout: timeoutMs }
  );
}

async function resyncE2ePlayersAfterDatabaseReset(contexts: PlayerContext[], timeoutMs: number): Promise<void> {
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await logoutPlayer(ctx.page, Math.min(timeoutMs, 60000)).catch(() => {});
    await loginPlayer(ctx.page, ctx.player.username, ctx.player.password);
    await ensurePlayerInGame(ctx, timeoutMs);

    const motdVisible = await ctx.page
      .getByTestId('motd-enter-realm')
      .isVisible({ timeout: 2500 })
      .catch(() => false);
    if (motdVisible) {
      const motdPage = new MotdPage(ctx.page);
      await motdPage.enterRealm();
      await motdPage.waitForGameReady(TEST_TIMEOUTS.GAME_LOAD);
      await ensurePlayerInGame(ctx, timeoutMs);
    }

    await executeCommand(ctx.page, 'stand');
    await executeCommandTrusted(ctx.page, 'look');
    await waitForLookReflectedInUi(ctx.page, Math.min(timeoutMs, 35000)).catch(() => {});
  }
}

async function ensureMultiplayerReadyForCoLocate(contexts: PlayerContext[], timeoutMs: number): Promise<void> {
  await waitForAllPlayersInGame(contexts, timeoutMs);
  await Promise.all(contexts.map(c => ensurePlayerInGame(c, timeoutMs)));

  for (const ctx of contexts) {
    const motdVisible = await ctx.page
      .getByTestId('motd-enter-realm')
      .isVisible({ timeout: 2500 })
      .catch(() => false);
    if (motdVisible) {
      const motdPage = new MotdPage(ctx.page);
      await motdPage.enterRealm();
      await motdPage.waitForGameReady(TEST_TIMEOUTS.GAME_LOAD);
      await ensurePlayerInGame(ctx, timeoutMs);
    }
  }

  for (const ctx of contexts) {
    const onLogin = await ctx.page
      .getByTestId('username-input')
      .isVisible({ timeout: 2000 })
      .catch(() => false);
    if (onLogin) {
      await loginPlayer(ctx.page, ctx.player.username, ctx.player.password);
      await ensurePlayerInGame(ctx, timeoutMs);
    }
  }
}

async function resolveOtherCharacterName(otherContext: PlayerContext): Promise<string> {
  await otherContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 15000 });
  return (
    (await otherContext.page.getByTestId('current-character-name').textContent())?.trim() ||
    otherContext.player.username
  );
}

async function runCoLocateTeleportAttempt(
  awContext: PlayerContext,
  otherContext: PlayerContext,
  contexts: PlayerContext[],
  otherCharName: string,
  attempt: number,
  timeoutMs: number
): Promise<void> {
  if (attempt >= 1) {
    resetE2ePlayerRoomsInDatabase();
    await resyncE2ePlayersAfterDatabaseReset(contexts, timeoutMs);
  }

  await awContext.page.bringToFront().catch(() => {});
  await ensurePlayableConnection(awContext.page, {
    username: awContext.player.username,
    password: awContext.player.password,
    timeoutMs: 30000,
  });
  // Admin-only: move AW to the other character before bringing them together (Ithaqua cannot teleport).
  await executeCommand(awContext.page, `goto ${otherCharName}`);
  await new Promise(r => setTimeout(r, 2000));
  await executeCommand(awContext.page, `teleport ${otherCharName}`);
  await new Promise(r => setTimeout(r, TELEPORT_SETTLE_BASE_MS + attempt * 2000));

  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await ensurePlayableConnection(ctx.page, {
      username: ctx.player.username,
      password: ctx.player.password,
      timeoutMs: 30000,
    });
    await executeCommandTrusted(ctx.page, 'look');
    await new Promise(r => setTimeout(r, 2000));
  }

  // Wait until grace-period copy clears from Game Info (helper returns true when absent).
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(() => window.__mythosE2eIsDisconnectedBannerVisible?.() === true, { timeout: 15_000 })
        .catch(() => {})
        .then(() =>
          ensurePlayableConnection(page, {
            username: player.username,
            password: player.password,
            timeoutMs: 35_000,
          })
        )
        .catch(() => {})
    )
  );

  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await executeCommandTrusted(ctx.page, 'look');
    await new Promise(r => setTimeout(r, 500));
  }
}

async function retryCoLocateUntilSameRoom(
  awContext: PlayerContext,
  otherContext: PlayerContext,
  contexts: PlayerContext[],
  otherCharName: string,
  coLocateTimeoutMs: number,
  timeoutMs: number
): Promise<void> {
  for (let attempt = 0; attempt < MAX_COLOCATE_ATTEMPTS; attempt++) {
    await runCoLocateTeleportAttempt(awContext, otherContext, contexts, otherCharName, attempt, timeoutMs);

    try {
      await ensurePlayersInSameRoom(contexts, contexts.length, coLocateTimeoutMs);
      return;
    } catch (e) {
      const lastCoLocateError = e instanceof Error ? e : new Error(String(e));
      if (attempt === MAX_COLOCATE_ATTEMPTS - 1) {
        throw lastCoLocateError;
      }
      console.error(
        `[instrumentation] ensureMultiplayerCoLocated: co-locate attempt ${attempt + 1}/${MAX_COLOCATE_ATTEMPTS} failed; retrying teleport`,
        lastCoLocateError.message
      );
    }
  }
}

/**
 * Restore two-player co-location for runtime E2E tests.
 *
 * Earlier tests or idle timeouts may leave one character out of the world ("X has left the game");
 * `ensurePlayerInGame` alone does not fix that. This helper re-runs full readiness, brings any
 * player stuck on MOTD back in, then admin-teleports player 0 toward player 1's character and
 * waits until both browsers show the expected occupant count. After teleport, both players run
 * `look` so Occupants / room_state can catch up (receiver-only refresh still left AW at 2 vs other at 1).
 */
export async function ensureMultiplayerCoLocated(
  contexts: PlayerContext[],
  options?: EnsureMultiplayerCoLocatedOptions
): Promise<void> {
  if (contexts.length < 2) {
    return;
  }
  const timeoutMs = options?.timeoutMs ?? 60000;
  const coLocateTimeoutMs = options?.coLocateTimeoutMs ?? 45000;

  await ensureMultiplayerReadyForCoLocate(contexts, timeoutMs);

  const [awContext, otherContext] = contexts;
  const otherCharName = await resolveOtherCharacterName(otherContext);

  await retryCoLocateUntilSameRoom(awContext, otherContext, contexts, otherCharName, coLocateTimeoutMs, timeoutMs);

  await Promise.all(
    contexts.map(c =>
      ensurePlayableConnection(c.page, {
        username: c.player.username,
        password: c.player.password,
        timeoutMs: coLocateTimeoutMs,
      })
    )
  );

  await new Promise(r => setTimeout(r, 1000));
}
