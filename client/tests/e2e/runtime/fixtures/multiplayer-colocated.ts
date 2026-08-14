/// <reference types="node" />

/**
 * Multiplayer co-location: same-room checks, DB reset, admin teleport restore.
 */

import { spawnSync } from 'child_process';
import { join } from 'path';

import './multiplayer-browser-window.d.ts';

import type { Page } from '@playwright/test';
import { E2E_PROJECT_ROOT, loadE2eEnv } from '../../../../src/test/e2e-bootstrap';
import { MotdPage } from '../pages';
import {
  assertNoRestDisconnectPollution,
  ensurePlayableConnection,
  executeCommand,
  executeCommandTrusted,
  loginPlayer,
  logoutPlayer,
} from './auth';
import type { OccupantsSnapshot } from './multiplayer-browser-helpers';
import { reopenPlayerPageIfClosed, type PlayerContext } from './multiplayer-contexts';
import { ensurePlayerInGame, waitForAllPlayersInGame } from './multiplayer-ready';
import { assertPlayerAlive } from './player';
import { TEST_TIMEOUTS, type TestPlayer } from './test-data';

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
  for (const ctx of contexts) {
    await reopenPlayerPageIfClosed(ctx);
    await assertNoRestDisconnectPollution(ctx.page);
    await assertPlayerAlive(ctx.page, ctx.player.username);
  }

  // Step 0: Wait for all players' header connection status to show "Connected" (same as waitForAllPlayersInGame).
  // Do not require absence of "(linkdead)" in the whole body: the Occupants panel can show "Name (linkdead)"
  // even when the header already shows "Connected", which would otherwise block this step forever.
  const linkdeadWaitMs = Math.min(25000, timeoutMs);
  await Promise.all(
    contexts.map(async ctx => {
      await reopenPlayerPageIfClosed(ctx);
      try {
        ctx.page = await ensurePlayableConnection(ctx.page, {
          username: ctx.player.username,
          password: ctx.player.password,
          timeoutMs: linkdeadWaitMs,
        });
        ctx.context = ctx.page.context();
      } catch (err) {
        const msg =
          `[instrumentation] ensurePlayersInSameRoom failed: Player ${ctx.player.username} - ` +
          `Step 0: header still not Connected within ${linkdeadWaitMs}ms`;
        console.error(msg, err);
        throw Object.assign(new Error(msg), { cause: err });
      }
    })
  );

  for (const ctx of contexts) {
    await assertNoRestDisconnectPollution(ctx.page);
  }

  // Step 1: Wait for all players to see the expected number of occupants in their room
  // Detection supports: OccupantsPanel title "Occupants (n)", content "Players (n)", or RoomInfoPane "Occupants (n):"
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

  // Step 3: look-based mutual presence (server look text) — catches Occupants UI vs room mismatch.
  await Promise.all(
    contexts.map(async ctx => {
      const expectedNames = getOtherUsernames(ctx);
      if (expectedNames.length === 0) return;
      await executeCommandTrusted(ctx.page, 'look');
      await ctx.page
        .waitForFunction(
          (names: string[]) => {
            const t = document.body?.innerText ?? '';
            return names.every(n => t.toLowerCase().includes(n.toLowerCase()));
          },
          expectedNames,
          { timeout: Math.min(15000, timeoutMs) }
        )
        .catch(() => {
          throw new Error(
            `ensurePlayersInSameRoom: Player ${ctx.player.username} look did not list ${expectedNames.join(', ')}`
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
const MAX_COLOCATE_ATTEMPTS = 3;

/**
 * Reset E2E player rows in mythos_e2e (same script as global-teardown).
 * In-memory server state is stale until players relog; pair with {@link resyncE2ePlayersAfterDatabaseReset}.
 */
export function resetE2ePlayerRoomsInDatabase(): void {
  const seedEnv = { ...process.env, ...loadE2eEnv() };
  const scriptPath = join(E2E_PROJECT_ROOT, 'scripts', 'e2e_reset_players.py');
  const result = spawnSync('uv', ['run', 'python', scriptPath], {
    cwd: E2E_PROJECT_ROOT,
    // shell:false so timeout is honored on Windows (shell:true has hung the Playwright worker).
    shell: false,
    stdio: 'pipe',
    encoding: 'utf-8',
    env: seedEnv,
    timeout: 20000,
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
    undefined,
    { timeout: timeoutMs }
  );
}

async function resyncE2ePlayersAfterDatabaseReset(contexts: PlayerContext[], timeoutMs: number): Promise<void> {
  for (const ctx of contexts) {
    await reopenPlayerPageIfClosed(ctx);
    await ctx.page.bringToFront().catch(() => {});
    await logoutPlayer(ctx.page, Math.min(timeoutMs, 60000)).catch(() => {});
    await reopenPlayerPageIfClosed(ctx);
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
  if (attempt >= 2) {
    resetE2ePlayerRoomsInDatabase();
    await resyncE2ePlayersAfterDatabaseReset(contexts, timeoutMs);
  }

  for (const ctx of contexts) {
    await reopenPlayerPageIfClosed(ctx);
  }

  await awContext.page.bringToFront().catch(() => {});
  awContext.page = await ensurePlayableConnection(awContext.page, {
    username: awContext.player.username,
    password: awContext.player.password,
    timeoutMs: 30000,
  });
  awContext.context = awContext.page.context();
  // Admin-only: move AW to the other character before bringing them together (Ithaqua cannot teleport).
  await executeCommand(awContext.page, `goto ${otherCharName}`);
  await new Promise(r => setTimeout(r, 2000));
  await executeCommand(awContext.page, `teleport ${otherCharName}`);
  await new Promise(r => setTimeout(r, TELEPORT_SETTLE_BASE_MS + attempt * 2000));

  for (const ctx of contexts) {
    await reopenPlayerPageIfClosed(ctx);
    await ctx.page.bringToFront().catch(() => {});
    ctx.page = await ensurePlayableConnection(ctx.page, {
      username: ctx.player.username,
      password: ctx.player.password,
      timeoutMs: 30000,
    });
    ctx.context = ctx.page.context();
    await executeCommandTrusted(ctx.page, 'look');
    await new Promise(r => setTimeout(r, 2000));
  }

  // Wait until grace-period copy clears from Game Info (helper returns true when absent).
  await Promise.all(
    contexts.map(async ctx => {
      await reopenPlayerPageIfClosed(ctx);
      await ctx.page
        .waitForFunction(() => window.__mythosE2eIsDisconnectedBannerVisible?.() === true, undefined, {
          timeout: 15_000,
        })
        .catch(() => {});
      try {
        ctx.page = await ensurePlayableConnection(ctx.page, {
          username: ctx.player.username,
          password: ctx.player.password,
          timeoutMs: 35_000,
        });
        ctx.context = ctx.page.context();
      } catch {
        // Co-locate retry handles residual linkdead.
      }
    })
  );

  for (const ctx of contexts) {
    await reopenPlayerPageIfClosed(ctx);
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

  for (const c of contexts) {
    await reopenPlayerPageIfClosed(c);
  }

  await Promise.all(
    contexts.map(async c => {
      c.page = await ensurePlayableConnection(c.page, {
        username: c.player.username,
        password: c.player.password,
        timeoutMs: coLocateTimeoutMs,
      });
      c.context = c.page.context();
    })
  );

  await new Promise(r => setTimeout(r, 1000));
}
