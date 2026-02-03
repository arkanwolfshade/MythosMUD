/**
 * Player Utilities
 *
 * Helper functions for player management in E2E tests.
 */

import { type Page } from '@playwright/test';
import { executeCommand } from './auth';

/**
 * Ensure the player is standing before movement.
 * Server rejects "go" when sitting; call this before any movement command.
 * Waits for either the posture UI "standing" or the game message (e.g. "You rise to your feet.")
 * so we pass as soon as the server confirms; the Character Info panel can update later.
 * Uses .first() on posture locator (strict mode) and Promise.race with game message.
 *
 * @param page - Playwright page instance
 * @param timeoutMs - Max wait for standing confirmation (default: 5000)
 */
export async function ensureStanding(page: Page, timeoutMs: number = 5000): Promise<void> {
  await executeCommand(page, 'stand');
  const postureUi = page.locator('div:has-text("Posture")').filter({ hasText: 'standing' }).first();
  const gameMessage = page.getByText(/You rise to your feet|standing|already standing/i).first();
  await Promise.race([
    postureUi.waitFor({ state: 'visible', timeout: timeoutMs }),
    gameMessage.waitFor({ state: 'attached', timeout: timeoutMs }),
  ]);
}

/**
 * Reset a player's position to their starting room.
 * Note: This requires admin privileges or a test helper endpoint.
 *
 * @param page - Playwright page instance
 * @param targetPlayer - Username of player to reset (defaults to current player)
 */
export async function resetPlayerPosition(page: Page, targetPlayer?: string): Promise<void> {
  if (targetPlayer) {
    // Admin command to teleport player
    await executeCommand(page, `teleport ${targetPlayer} earth_arkhamcity_sanitarium_room_foyer_001`);
  } else {
    // Stand before movement (server rejects "go" when sitting)
    await ensureStanding(page, 5000);
    // Regular movement command (if player is already in starting room, this is a no-op)
    await executeCommand(page, 'go north');
    await new Promise(r => setTimeout(r, 1000));
    await ensureStanding(page, 5000);
    await executeCommand(page, 'go south');
    await new Promise(r => setTimeout(r, 1000));
  }
}

/**
 * Get player's current room ID from the game state.
 *
 * @param page - Playwright page instance
 * @returns Room ID or null if not found
 */
export async function getPlayerRoom(page: Page): Promise<string | null> {
  // Execute look command to get room information
  await executeCommand(page, 'look');
  await new Promise(r => setTimeout(r, 2000));

  // Try to extract room ID from look output
  const messages = await page.evaluate(() => {
    const messages = Array.from(document.querySelectorAll('[data-message-text]'));
    return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
  });

  // Look for room ID in messages (this is a simplified version)
  // In a real implementation, you'd parse the look output more carefully
  for (const msg of messages) {
    if (msg.includes('earth_arkhamcity_sanitarium_room_')) {
      const match = msg.match(/earth_arkhamcity_sanitarium_room_\w+/);
      if (match) {
        return match[0];
      }
    }
  }

  return null;
}
