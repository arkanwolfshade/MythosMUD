/**
 * Multiplayer Fixtures
 *
 * Helper functions for managing multiple browser contexts in multiplayer scenarios.
 */

import { type Browser, type BrowserContext, type Page } from '@playwright/test';
import { loginPlayer } from './auth';
import { TEST_PLAYERS, type TestPlayer } from './test-data';

export interface PlayerContext {
  context: BrowserContext;
  page: Page;
  player: TestPlayer;
}

/**
 * Create multiple authenticated browser contexts for multiplayer testing.
 *
 * @param browser - Playwright browser instance
 * @param playerUsernames - Array of usernames to create contexts for
 * @returns Array of PlayerContext objects
 */
export async function createMultiPlayerContexts(browser: Browser, playerUsernames: string[]): Promise<PlayerContext[]> {
  const contexts: PlayerContext[] = [];

  for (const username of playerUsernames) {
    const player = TEST_PLAYERS.find(p => p.username === username);
    if (!player) {
      throw new Error(`Test player not found: ${username}`);
    }

    // Create new context
    const context = await browser.newContext();
    const page = await context.newPage();

    // Login the player
    await loginPlayer(page, player.username, player.password);

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
 * Wait for a message to appear in a specific player's context.
 *
 * @param playerContext - PlayerContext to check
 * @param expectedText - Text to wait for (string or RegExp)
 * @param timeout - Timeout in milliseconds
 */
export async function waitForCrossPlayerMessage(
  playerContext: PlayerContext,
  expectedText: string | RegExp,
  timeout: number = 30000
): Promise<void> {
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
        // nosemgrep: javascript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
        // This is a test fixture. The RegExp source and flags come from expectedText (a test constant), not user input
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
}

/**
 * Get messages from a specific player's context.
 *
 * @param playerContext - PlayerContext to get messages from
 * @returns Array of message texts
 */
export async function getPlayerMessages(playerContext: PlayerContext): Promise<string[]> {
  return await playerContext.page.evaluate(() => {
    const messages = Array.from(document.querySelectorAll('[data-message-text]'));
    return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });
}
