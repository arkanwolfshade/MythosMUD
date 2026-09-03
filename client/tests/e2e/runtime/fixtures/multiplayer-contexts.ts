/// <reference types="node" />

/**
 * Multiplayer context lifecycle: create, reopen, cleanup.
 */

import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

import './multiplayer-browser-window.d.ts';

import type { Browser, BrowserContext, Page } from '@playwright/test';
import {
  getLivePageForUsername,
  isPageConnected,
  loginPlayer,
  logoutPlayer,
  rememberPageSession,
  reopenClosedPage,
} from './auth';
import { ensurePlayableAlive, isPlayerDead } from './player';
import { TEST_PLAYERS, type TestPlayer } from './test-data';

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
 * If the Firefox page/context died mid-suite, open a fresh page on the same context and re-login.
 * Mutates playerContext.page so callers holding the context object see the new page.
 */
export async function reopenPlayerPageIfClosed(playerContext: PlayerContext): Promise<void> {
  const live = getLivePageForUsername(playerContext.player.username);
  if (live && (await isPageConnected(live))) {
    playerContext.page = live;
    playerContext.context = live.context();
    rememberPageSession(live, playerContext.player.username, playerContext.player.password);
    return;
  }
  // A page that survived a server-side disconnect (e.g. an abrupt context.close() detected
  // server-side, or /rest) can stay open showing a linkdead/reconnecting state -- not closed,
  // but not usable -- until the client eventually falls back to login on its own. Trusting
  // isClosed() alone reuses that dead session; require an actively connected WebSocket too.
  if (await isPageConnected(playerContext.page)) {
    rememberPageSession(playerContext.page, playerContext.player.username, playerContext.player.password);
    return;
  }
  playerContext.page = await reopenClosedPage(
    playerContext.page,
    playerContext.player.username,
    playerContext.player.password,
    45000
  );
  playerContext.context = playerContext.page.context();
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
  for (const { page, player } of contexts) {
    if (page.isClosed()) {
      continue;
    }
    // Heal only in teardown so the next spec starts clean; in-test death must assert, not silent-recover.
    if (await isPlayerDead(page).catch(() => false)) {
      await ensurePlayableAlive(page, player.username, player.password).catch(() => {});
    }
    // spaFallback: afterAll must not hang 90s when Exit is disabled in void/ward.
    await logoutPlayer(page, 25000, { spaFallback: true }).catch(() => {});
    await page
      .getByTestId('username-input')
      .waitFor({ state: 'visible', timeout: 10000 })
      .catch(() => {});
  }
  for (const { context } of contexts) {
    await context.close().catch(() => {
      // Ignore errors during cleanup
    });
  }
}
