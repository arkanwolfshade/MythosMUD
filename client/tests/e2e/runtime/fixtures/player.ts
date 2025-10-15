/**
 * Player Utilities for Runtime E2E Tests
 *
 * Provides functions for interacting with the game as a player,
 * including sending commands, reading messages, and checking player state.
 */

import { Page, expect } from '@playwright/test';
import { SELECTORS, TIMEOUTS } from './test-data';

/**
 * Send a command in the game
 *
 * Fills the command input field and presses Enter to submit.
 *
 * @param page - Playwright page object
 * @param command - Command to send (e.g., "say Hello", "go north")
 */
export async function sendCommand(page: Page, command: string): Promise<void> {
  const commandInput = page.locator(SELECTORS.COMMAND_INPUT);
  await commandInput.fill(command);
  await commandInput.press('Enter');
}

/**
 * Wait for a specific message to appear
 *
 * Waits for a message containing the specified text to become visible.
 *
 * @param page - Playwright page object
 * @param messageText - Text to wait for in a message
 * @param timeout - Maximum time to wait (default: 10 seconds)
 */
export async function waitForMessage(
  page: Page,
  messageText: string,
  timeout: number = TIMEOUTS.MESSAGE_APPEAR
): Promise<void> {
  await expect(page.locator(SELECTORS.MESSAGE_CONTAINER, { hasText: messageText })).toBeVisible({ timeout });
}

/**
 * Get all messages currently displayed in chat
 *
 * Extracts text content from all message elements.
 *
 * @param page - Playwright page object
 * @returns Array of message text content
 */
export async function getMessages(page: Page): Promise<string[]> {
  // Get message text from data-message-text attribute to exclude timestamps
  const messageElements = await page.locator('.message-text').all();
  const messages = await Promise.all(messageElements.map(el => el.getAttribute('data-message-text')));
  return messages.map(m => m?.trim() || '').filter(m => m.length > 0);
}

/**
 * Get player's current location from UI
 *
 * @param page - Playwright page object
 * @returns Current room/location display text
 */
export async function getPlayerLocation(page: Page): Promise<string> {
  try {
    const locationDisplay = page.locator(SELECTORS.LOCATION_DISPLAY);
    const location = await locationDisplay.textContent({ timeout: 5000 });
    return location?.trim() || '';
  } catch {
    return '';
  }
}

/**
 * Clear all messages from the chat display
 *
 * Removes all message elements from the DOM.
 * Useful for test cleanup or focusing on new messages only.
 *
 * @param page - Playwright page object
 */
export async function clearMessages(page: Page): Promise<void> {
  await page.evaluate(() => {
    const messages = document.querySelectorAll('.message');
    messages.forEach(msg => msg.remove());
  });
}

/**
 * Check if a specific message exists in chat
 *
 * @param page - Playwright page object
 * @param messageText - Text to search for
 * @returns true if message exists, false otherwise
 */
export async function hasMessage(page: Page, messageText: string): Promise<boolean> {
  const messages = await getMessages(page);
  return messages.some(m => m.includes(messageText));
}

/**
 * Get messages of a specific type
 *
 * Filters messages by type (e.g., error messages, system messages).
 *
 * @param page - Playwright page object
 * @param messageType - CSS class for message type (e.g., 'error', 'system')
 * @returns Array of messages of the specified type
 */
export async function getMessagesByType(page: Page, messageType: string): Promise<string[]> {
  const messageElements = await page.locator(`.message.${messageType}`).all();
  const messages = await Promise.all(messageElements.map(el => el.textContent()));
  return messages.map(m => m?.trim() || '').filter(m => m.length > 0);
}

/**
 * Wait for message to disappear
 *
 * Useful for testing that error messages clear or that
 * temporary messages are removed.
 *
 * @param page - Playwright page object
 * @param messageText - Text that should disappear
 * @param timeout - Maximum time to wait
 */
export async function waitForMessageToDisappear(
  page: Page,
  messageText: string,
  timeout: number = TIMEOUTS.MESSAGE_APPEAR
): Promise<void> {
  await expect(page.locator(SELECTORS.MESSAGE_CONTAINER, { hasText: messageText })).toBeHidden({ timeout });
}

/**
 * Get the last N messages
 *
 * @param page - Playwright page object
 * @param count - Number of messages to retrieve
 * @returns Array of last N messages
 */
export async function getLastMessages(page: Page, count: number): Promise<string[]> {
  const allMessages = await getMessages(page);
  return allMessages.slice(-count);
}

/**
 * Count messages matching a pattern
 *
 * @param page - Playwright page object
 * @param pattern - Text pattern to match
 * @returns Number of matching messages
 */
export async function countMessages(page: Page, pattern: string): Promise<number> {
  const messages = await getMessages(page);
  return messages.filter(m => m.includes(pattern)).length;
}

/**
 * Wait for command to execute
 *
 * Sends a command and waits for any response message to appear.
 * Useful when you don't know exact response text but know something will appear.
 *
 * @param page - Playwright page object
 * @param command - Command to send
 * @param timeout - Maximum time to wait
 */
export async function sendCommandAndWait(
  page: Page,
  command: string,
  timeout: number = TIMEOUTS.COMMAND_EXECUTION
): Promise<void> {
  const messageCountBefore = await countMessages(page, '');
  await sendCommand(page, command);

  // Wait for message count to increase
  await page.waitForFunction(
    expectedCount => {
      const messages = document.querySelectorAll('.message');
      return messages.length > expectedCount;
    },
    messageCountBefore,
    { timeout }
  );
}

/**
 * Get player stats from UI
 *
 * Extracts player health, sanity, and other visible stats.
 *
 * @param page - Playwright page object
 * @returns Object containing player stats
 */
export async function getPlayerStats(page: Page): Promise<{
  health?: number;
  sanity?: number;
  level?: number;
}> {
  try {
    const stats = await page.evaluate(() => {
      const healthEl = document.querySelector('[data-stat="health"]');
      const sanityEl = document.querySelector('[data-stat="sanity"]');
      const levelEl = document.querySelector('[data-stat="level"]');

      return {
        health: healthEl ? parseInt(healthEl.textContent || '0') : undefined,
        sanity: sanityEl ? parseInt(sanityEl.textContent || '0') : undefined,
        level: levelEl ? parseInt(levelEl.textContent || '0') : undefined,
      };
    });

    return stats;
  } catch {
    return {};
  }
}

/**
 * Clear command input field
 *
 * @param page - Playwright page object
 */
export async function clearCommandInput(page: Page): Promise<void> {
  const commandInput = page.locator(SELECTORS.COMMAND_INPUT);
  await commandInput.clear();
}

/**
 * Check if command input is available
 *
 * @param page - Playwright page object
 * @returns true if command input is visible and enabled
 */
export async function isCommandInputAvailable(page: Page): Promise<boolean> {
  try {
    const commandInput = page.locator(SELECTORS.COMMAND_INPUT);
    const isVisible = await commandInput.isVisible({ timeout: 1000 });
    const isEnabled = await commandInput.isEnabled({ timeout: 1000 });
    return isVisible && isEnabled;
  } catch {
    return false;
  }
}
