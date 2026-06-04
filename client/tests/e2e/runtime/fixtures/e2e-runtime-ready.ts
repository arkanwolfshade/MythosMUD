import { ensurePlayableConnection, waitForPlayableSession } from './auth';
import type { PlayerContext } from './multiplayer';

const DEFAULT_READY_TIMEOUT_MS = 60000;

/**
 * After createMultiPlayerContexts + waitForAllPlayersInGame: heal linkdead/command channel per page.
 * Call in test.beforeAll for communication specs that assume both players are in-game.
 */
export async function ensureE2eRuntimeReady(
  contexts: PlayerContext[],
  timeoutMs: number = DEFAULT_READY_TIMEOUT_MS
): Promise<void> {
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await waitForPlayableSession(ctx.page, ctx.player.username, ctx.player.password, timeoutMs);
    await ensurePlayableConnection(ctx.page, {
      username: ctx.player.username,
      password: ctx.player.password,
      timeoutMs,
    });
  }
}
