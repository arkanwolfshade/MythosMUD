/**
 * Multiplayer Fixtures
 *
 * Helper functions for managing multiple browser contexts in multiplayer scenarios.
 */

import { type Browser, type BrowserContext, type Page } from '@playwright/test';
import { loginPlayer } from './auth';
import { TEST_PLAYERS, TEST_TIMEOUTS, type TestPlayer } from './test-data';

const SERVER_URL = 'http://localhost:54731';
const SERVER_READY_POLL_MS = 500;
const SERVER_READY_TIMEOUT_MS = 30000;

/**
 * Poll server health endpoint until it responds 200 or timeout.
 * Ensures server is ready before first player login (avoids "still on login" when server was cold).
 */
async function waitForServerReady(): Promise<void> {
  const start = Date.now();
  while (Date.now() - start < SERVER_READY_TIMEOUT_MS) {
    try {
      const res = await fetch(`${SERVER_URL}/health`, { signal: AbortSignal.timeout(3000) });
      if (res.ok) return;
    } catch {
      // Server not ready, keep polling
    }
    await new Promise(r => setTimeout(r, SERVER_READY_POLL_MS));
  }
  throw new Error(`[instrumentation] Server not ready at ${SERVER_URL}/health within ${SERVER_READY_TIMEOUT_MS}ms`);
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
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:createMultiPlayerContexts:entry',
      message: 'createMultiPlayerContexts started',
      data: { playerUsernames },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'C',
    }),
  }).catch(() => {});
  // #endregion
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
    const page = await context.newPage();

    await loginPlayer(page, player.username, player.password);

    // Post-login stabilization: first player needs extra time for UI to fully render
    if (i === 0) {
      await new Promise(r => setTimeout(r, 2000));
    }

    // #region agent log
    fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        location: 'multiplayer.ts:createMultiPlayerContexts:afterLogin',
        message: 'loginPlayer completed for player',
        data: { username, index: i },
        timestamp: Date.now(),
        sessionId: 'debug-session',
        hypothesisId: 'B',
      }),
    }).catch(() => {});
    // #endregion

    contexts.push({ context, page, player });
  }

  return contexts;
}

/**
 * Cleanup multiple player contexts.
 *
 * @param contexts - Array of PlayerContext objects to cleanup
 */
export async function cleanupMultiPlayerContexts(contexts: PlayerContext[] | undefined): Promise<void> {
  if (!contexts || !Array.isArray(contexts)) {
    return;
  }
  for (const { context } of contexts) {
    await context.close().catch(() => {
      // Ignore errors during cleanup
    });
  }
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
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:waitForAllPlayersInGame:entry',
      message: 'waitForAllPlayersInGame started',
      data: { contextCount: contexts.length, usernames: contexts.map(c => c.player.username) },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'D',
    }),
  }).catch(() => {});
  // #endregion

  // Step 1: Wait for all players to reach game UI (not on login screen)
  // Broadened detection: command input, Game Info, game terminal, Player header, Mythos Time, or room content
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          () => {
            const hasLoginForm =
              document.querySelector('input[placeholder*="username" i], input[name*="username" i]') !== null &&
              Array.from(document.querySelectorAll('button')).some(
                btn => btn.textContent?.includes('Enter the Void') || btn.textContent?.includes('Login')
              );
            if (hasLoginForm) return false;
            const hasCommandInput =
              document.querySelector('input[placeholder*="command" i], textarea[placeholder*="command" i]') !== null ||
              document.querySelector('[data-testid="command-input"]') !== null;
            const hasGameInfo =
              document.querySelector('[data-testid="game-info-panel"]') !== null ||
              Array.from(document.querySelectorAll('*')).some(el => el.textContent?.includes('Game Info'));
            const bodyText = document.body?.innerText ?? '';
            const hasPlayerHeader = bodyText.includes('Player:') && !bodyText.includes('Enter the Void');
            const hasMythosTime = bodyText.includes('Mythos Time');
            const hasGameTerminal = document.querySelector('[data-testid="game-terminal"]') !== null;
            const hasRoomContent = bodyText.includes('Occupants') || bodyText.includes('Location');
            return (
              hasCommandInput || hasGameInfo || hasPlayerHeader || hasMythosTime || hasGameTerminal || hasRoomContent
            );
          },
          { timeout: timeoutMs }
        )
        .catch(err => {
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 1: game UI - still on login screen after ${timeoutMs}ms`;
          console.error(msg, err);
          throw new Error(msg);
        })
    )
  );

  // Step 2: Wait for all players' WebSocket connections to be established (status shows "Connected")
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          () => {
            // Look for connection status in the header - should show "Connected" when WebSocket is ready
            const statusElements = Array.from(document.querySelectorAll('*'));
            const hasConnectedStatus = statusElements.some(
              el =>
                el.textContent?.trim() === 'Connected' ||
                (el.textContent?.includes('Connected') && !el.textContent?.includes('linkdead'))
            );
            return hasConnectedStatus;
          },
          { timeout: Math.min(timeoutMs, 30000) } // Max 30s for WebSocket connection per player
        )
        .catch(err => {
          const wsTimeout = Math.min(timeoutMs, 30000);
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 2: WebSocket - status still shows linkdead after ${wsTimeout}ms`;
          console.error(msg, err);
          // #region agent log
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'multiplayer.ts:waitForAllPlayersInGame:websocketFail',
              message: 'WebSocket connection failed for player',
              data: { username: player.username, error: String(err?.message ?? err) },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              hypothesisId: 'WebSocket',
            }),
          }).catch(() => {});
          // #endregion
          throw new Error(msg);
        })
    )
  );

  // Step 3: Wait for all players' room subscriptions to be established (tick message appears)
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          () => {
            // Look for tick message in Game Info panel - format: "[Tick 123]"
            const gameInfoElements = Array.from(document.querySelectorAll('*'));
            const hasTickMessage = gameInfoElements.some(
              el => el.textContent?.includes('[Tick') && el.textContent?.includes(']')
            );
            return hasTickMessage;
          },
          { timeout: Math.min(timeoutMs, 30000) } // Max 30s for room subscription per player
        )
        .catch(err => {
          const tickTimeout = Math.min(timeoutMs, 30000);
          const msg =
            `[instrumentation] waitForAllPlayersInGame failed: Player ${player.username} - ` +
            `Step 3: room subscription (tick) - no tick message after ${tickTimeout}ms`;
          console.error(msg, err);
          // #region agent log
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'multiplayer.ts:waitForAllPlayersInGame:roomSubscriptionFail',
              message: 'Room subscription failed for player (no tick message)',
              data: { username: player.username, error: String(err?.message ?? err) },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              hypothesisId: 'RoomSubscription',
            }),
          }).catch(() => {});
          // #endregion
          throw new Error(msg);
        })
    )
  );

  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:waitForAllPlayersInGame:exit',
      message: 'waitForAllPlayersInGame all resolved - all players ready (UI, WebSocket, room subscription)',
      data: { contextCount: contexts.length },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'A',
    }),
  }).catch(() => {});
  // #endregion
  // Brief stability wait after all room subscriptions established
  await new Promise(resolve => setTimeout(resolve, 2000));
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
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:ensurePlayerInGame:entry',
      message: 'ensurePlayerInGame called',
      data: { username: playerContext.player.username },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'A',
    }),
  }).catch(() => {});
  // #endregion

  // Step 1: Wait for game UI to appear (not on login screen)
  // Broadened detection: command input, Game Info, game terminal, Player header, Mythos Time, or room content
  await playerContext.page
    .waitForFunction(
      () => {
        const hasLogin =
          document.querySelector('input[placeholder*="username" i]') !== null &&
          Array.from(document.querySelectorAll('button')).some(b => b.textContent?.includes('Enter the Void'));
        if (hasLogin) return false;
        const hasCommandInput =
          document.querySelector('[data-testid="command-input"]') !== null ||
          document.querySelector('input[placeholder*="command" i], textarea[placeholder*="command" i]') !== null;
        const hasGameInfo =
          document.querySelector('[data-testid="game-info-panel"]') !== null ||
          Array.from(document.querySelectorAll('*')).some(el => el.textContent?.includes('Game Info'));
        const bodyText = document.body?.innerText ?? '';
        const hasPlayerHeader = bodyText.includes('Player:') && !bodyText.includes('Enter the Void');
        const hasMythosTime = bodyText.includes('Mythos Time');
        const hasGameTerminal = document.querySelector('[data-testid="game-terminal"]') !== null;
        const hasRoomContent = bodyText.includes('Occupants') || bodyText.includes('Location');
        return hasCommandInput || hasGameInfo || hasPlayerHeader || hasMythosTime || hasGameTerminal || hasRoomContent;
      },
      { timeout: timeoutMs }
    )
    .catch(err => {
      // #region agent log
      fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: 'multiplayer.ts:ensurePlayerInGame:fail',
          message: 'ensurePlayerInGame failed - game UI not found',
          data: { username: playerContext.player.username, error: String(err?.message ?? err) },
          timestamp: Date.now(),
          sessionId: 'debug-session',
          hypothesisId: 'A',
        }),
      }).catch(() => {});
      // #endregion
      throw new Error(
        `Player ${playerContext.player.username} did not reach game UI within ${timeoutMs}ms (still on login?)`
      );
    });

  // Step 2: Wait for WebSocket connection to be established (status shows "Connected" not "linkdead")
  await playerContext.page
    .waitForFunction(
      () => {
        // Look for connection status in the header - should show "Connected" when WebSocket is ready
        const statusElements = Array.from(document.querySelectorAll('*'));
        const hasConnectedStatus = statusElements.some(
          el =>
            el.textContent?.trim() === 'Connected' ||
            (el.textContent?.includes('Connected') && !el.textContent?.includes('linkdead'))
        );
        return hasConnectedStatus;
      },
      { timeout: Math.min(timeoutMs, 30000) } // Max 30s for WebSocket connection
    )
    .catch(err => {
      // #region agent log
      fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: 'multiplayer.ts:ensurePlayerInGame:websocketFail',
          message: 'ensurePlayerInGame failed - WebSocket not connected',
          data: { username: playerContext.player.username, error: String(err?.message ?? err) },
          timestamp: Date.now(),
          sessionId: 'debug-session',
          hypothesisId: 'WebSocket',
        }),
      }).catch(() => {});
      // #endregion
      throw new Error(
        `Player ${playerContext.player.username} WebSocket did not connect within ${Math.min(
          timeoutMs,
          30000
        )}ms (status still shows linkdead?)`
      );
    });

  // Step 3: Wait for room subscription to be established (tick message appears in Game Info)
  // Tick messages indicate the player is subscribed to room updates via NATS
  await playerContext.page
    .waitForFunction(
      () => {
        // Look for tick message in Game Info panel - format: "[Tick 123]"
        const gameInfoElements = Array.from(document.querySelectorAll('*'));
        const hasTickMessage = gameInfoElements.some(
          el => el.textContent?.includes('[Tick') && el.textContent?.includes(']')
        );
        return hasTickMessage;
      },
      { timeout: Math.min(timeoutMs, 30000) } // Max 30s for room subscription
    )
    .catch(err => {
      // #region agent log
      fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location: 'multiplayer.ts:ensurePlayerInGame:roomSubscriptionFail',
          message: 'ensurePlayerInGame failed - room subscription not established (no tick message)',
          data: { username: playerContext.player.username, error: String(err?.message ?? err) },
          timestamp: Date.now(),
          sessionId: 'debug-session',
          hypothesisId: 'RoomSubscription',
        }),
      }).catch(() => {});
      // #endregion
      throw new Error(
        `Player ${playerContext.player.username} room subscription not established within ${Math.min(
          timeoutMs,
          30000
        )}ms (no tick message received)`
      );
    });

  // Brief stability wait after room subscription established
  await new Promise(resolve => setTimeout(resolve, 1000));

  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:ensurePlayerInGame:exit',
      message: 'ensurePlayerInGame succeeded - game UI, WebSocket, and room subscription all ready',
      data: { username: playerContext.player.username },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'A',
    }),
  }).catch(() => {});
  // #endregion
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
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:waitForCrossPlayerMessage:entry',
      message: 'waitForCrossPlayerMessage started',
      data: {
        username: playerContext.player.username,
        expectedText: typeof expectedText === 'string' ? expectedText : expectedText.source,
      },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'D',
    }),
  }).catch(() => {});
  // #endregion
  const messageLocator = playerContext.page.locator('[data-message-text]');

  if (typeof expectedText === 'string') {
    await messageLocator.filter({ hasText: expectedText }).first().waitFor({ state: 'visible', timeout });
  } else {
    // For RegExp, use page.waitForFunction to check messages dynamically
    // Serialize RegExp to source and flags for serialization
    const patternSource = expectedText.source;
    const patternFlags = expectedText.flags;
    await playerContext.page.waitForFunction(
      ({ source, flags }) => {
        const messages = Array.from(document.querySelectorAll('[data-message-text]'));
        // nosemgrep: javascript.lang.security.audit.detect-non-literal-regexp
        // Test fixture: RegExp from expectedText (test constant), not user input
        const patternRegex = new RegExp(source, flags);
        return messages.some(msg => {
          const text = (msg.getAttribute('data-message-text') || '').trim();
          return patternRegex.test(text);
        });
      },
      { source: patternSource, flags: patternFlags },
      { timeout }
    );
  }
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:waitForCrossPlayerMessage:exit',
      message: 'waitForCrossPlayerMessage succeeded',
      data: { username: playerContext.player.username },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'D',
    }),
  }).catch(() => {});
  // #endregion
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
 * (chat, local, whisper, etc.) to ensure players are properly synchronized.
 *
 * @param contexts - Array of PlayerContext objects
 * @param expectedOccupants - Expected number of players in the room (default: contexts.length)
 * @param timeoutMs - Max wait in milliseconds (default: 30000)
 */
export async function ensurePlayersInSameRoom(
  contexts: PlayerContext[],
  expectedOccupants: number = contexts.length,
  timeoutMs: number = 30000
): Promise<void> {
  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:ensurePlayersInSameRoom:entry',
      message: 'ensurePlayersInSameRoom started',
      data: {
        contextCount: contexts.length,
        expectedOccupants,
        usernames: contexts.map(c => c.player.username),
      },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'RoomCoLocation',
    }),
  }).catch(() => {});
  // #endregion

  // Step 1: Wait for all players to see the expected number of occupants in their room
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          (expected: number) => {
            // Look for Occupants panel and count players
            const occupantsText = Array.from(document.querySelectorAll('*')).find(
              el => el.textContent?.includes('Occupants (') && el.textContent?.includes(')')
            )?.textContent;

            if (!occupantsText) return false;

            // Extract count from "Occupants (2)" format
            const match = occupantsText.match(/Occupants \((\d+)\)/);
            if (!match) return false;

            const occupantCount = parseInt(match[1], 10);
            return occupantCount >= expected;
          },
          expectedOccupants,
          { timeout: timeoutMs }
        )
        .catch(err => {
          const msg =
            `[instrumentation] ensurePlayersInSameRoom failed: Player ${player.username} - ` +
            `Step 1: occupants - did not see ${expectedOccupants} occupants within ${timeoutMs}ms ` +
            '(players not co-located)';
          console.error(msg, err);
          // #region agent log
          fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              location: 'multiplayer.ts:ensurePlayersInSameRoom:fail',
              message: 'Player did not see expected occupants in room',
              data: {
                username: player.username,
                expectedOccupants,
                error: String(err?.message ?? err),
              },
              timestamp: Date.now(),
              sessionId: 'debug-session',
              hypothesisId: 'RoomCoLocation',
            }),
          }).catch(() => {});
          // #endregion
          throw new Error(msg);
        })
    )
  );

  // Step 2: Require no linkdead in room so both players are actually connected and can receive broadcasts
  await Promise.all(
    contexts.map(({ page, player }) =>
      page
        .waitForFunction(
          () => {
            const bodyText = document.body?.innerText ?? '';
            const hasLinkdead = bodyText.includes('(linkdead)');
            return !hasLinkdead;
          },
          { timeout: Math.min(timeoutMs, 15000) }
        )
        .catch(err => {
          const ldTimeout = Math.min(timeoutMs, 15000);
          const msg =
            `[instrumentation] ensurePlayersInSameRoom failed: Player ${player.username} - ` +
            `Step 2: no-linkdead - still sees linkdead in room within ${ldTimeout}ms ` +
            '(other player not connected?)';
          console.error(msg, err);
          throw new Error(msg);
        })
    )
  );

  // Brief stability wait after all players see each other and are connected
  await new Promise(resolve => setTimeout(resolve, 1000));

  // #region agent log
  fetch('http://127.0.0.1:7242/ingest/cc3c5449-8584-455a-a168-f538b38a7727', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      location: 'multiplayer.ts:ensurePlayersInSameRoom:exit',
      message: 'ensurePlayersInSameRoom succeeded - all players co-located',
      data: { contextCount: contexts.length, expectedOccupants },
      timestamp: Date.now(),
      sessionId: 'debug-session',
      hypothesisId: 'RoomCoLocation',
    }),
  }).catch(() => {});
  // #endregion
}
