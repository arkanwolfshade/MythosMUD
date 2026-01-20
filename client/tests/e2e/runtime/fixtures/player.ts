/**
 * Player Utilities
 *
 * Helper functions for player management in E2E tests.
 */

import { type Page } from '@playwright/test';
import { executeCommand } from './auth';

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
    // Regular movement command (if player is already in starting room, this is a no-op)
    await executeCommand(page, 'go north');
    await page.waitForTimeout(1000);
    await executeCommand(page, 'go south');
    await page.waitForTimeout(1000);
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
  await page.waitForTimeout(2000);

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
