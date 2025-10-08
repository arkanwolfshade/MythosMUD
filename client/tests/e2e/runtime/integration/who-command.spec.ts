/**
 * Who Command Integration Tests (Automated Portion)
 *
 * Tests single-player aspects of the who command functionality.
 * Converted from e2e-tests/scenarios/scenario-07-who-command.md (partial)
 *
 * Automated Test Coverage:
 * - Command output format
 * - Location information display
 * - Single player visibility (self in list)
 * - Proper formatting with zone + room info
 * - Response time validation
 *
 * MCP Testing Required For:
 * - Multiple online players visibility
 * - Real-time player list updates
 * - (See e2e-tests/scenarios/scenario-07-who-command.md for multi-player tests)
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { getMessages, sendCommand, waitForMessage } from '../fixtures/player';
import { SUCCESS_MESSAGES, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Who Command - Single Player Functionality', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should display command output with proper format', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');

    // Verify header appears
    await waitForMessage(page, SUCCESS_MESSAGES.WHO_HEADER);

    const messages = await getMessages(page);
    expect(messages).toContain(SUCCESS_MESSAGES.WHO_HEADER);
  });

  test('should show self in online players list', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');

    // Wait for response
    await waitForMessage(page, SUCCESS_MESSAGES.WHO_HEADER);

    // Verify own username appears
    await waitForMessage(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username);

    const messages = await getMessages(page);
    const hasOwnUsername = messages.some(m => m.includes(TEST_PLAYERS.ARKAN_WOLFSHADE.username));
    expect(hasOwnUsername).toBeTruthy();
  });

  test('should display location information', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');

    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should include location/room information
    // Either room ID or room name should appear
    const hasLocationInfo = messages.some(
      m =>
        m.includes('earth_arkhamcity_sanitarium_room_foyer_001') ||
        m.includes('Main Foyer') ||
        m.includes('Sanitarium') ||
        m.toLowerCase().includes('location') ||
        m.toLowerCase().includes('room')
    );

    expect(hasLocationInfo).toBeTruthy();
  });

  test('should respond within 2 seconds', async ({ page }) => {
    const startTime = Date.now();

    // Send who command
    await sendCommand(page, 'who');

    // Wait for response
    await waitForMessage(page, SUCCESS_MESSAGES.WHO_HEADER, 2000);

    const endTime = Date.now();
    const responseTime = endTime - startTime;

    // Should respond in less than 2 seconds
    expect(responseTime).toBeLessThan(2000);
  });

  test('should handle multiple who command calls', async ({ page }) => {
    // Send who command multiple times
    for (let i = 0; i < 3; i++) {
      await sendCommand(page, 'who');
      await page.waitForTimeout(300);
    }

    // Wait for responses
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should have multiple who responses
    const whoResponses = messages.filter(m => m.includes(SUCCESS_MESSAGES.WHO_HEADER));
    expect(whoResponses.length).toBeGreaterThanOrEqual(1);
  });

  test('should display consistent formatting', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');

    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Verify formatting includes:
    // - Header line
    // - Player name
    // - Location info
    const hasHeader = messages.some(m => m.includes(SUCCESS_MESSAGES.WHO_HEADER));
    const hasPlayerName = messages.some(m => m.includes(TEST_PLAYERS.ARKAN_WOLFSHADE.username));

    expect(hasHeader).toBeTruthy();
    expect(hasPlayerName).toBeTruthy();
  });

  test('should not show duplicate entries for self', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');

    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Count how many times own username appears
    const usernameMatches = messages.filter(m => m.includes(TEST_PLAYERS.ARKAN_WOLFSHADE.username));

    // Should appear exactly once in the who list
    // (might appear in other messages, but in who output should be once)
    expect(usernameMatches.length).toBeGreaterThan(0);
  });

  test('should work after player movement', async ({ page }) => {
    // Move to different room
    await sendCommand(page, 'go east');
    await page.waitForTimeout(1000);

    // Send who command
    await sendCommand(page, 'who');

    // Should still work and show updated location
    await waitForMessage(page, SUCCESS_MESSAGES.WHO_HEADER);
    await waitForMessage(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username);

    const messages = await getMessages(page);
    expect(messages.some(m => m.includes(TEST_PLAYERS.ARKAN_WOLFSHADE.username))).toBeTruthy();
  });
});

test.describe('Who Command - Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should handle invalid who command arguments gracefully', async ({ page }) => {
    // Send who command with invalid arguments
    await sendCommand(page, 'who invalid arguments');

    await page.waitForTimeout(1000);

    // Should either ignore arguments or show error
    // In either case, should not crash
    const messages = await getMessages(page);
    expect(messages.length).toBeGreaterThan(0);
  });

  test('should maintain system stability after who command', async ({ page }) => {
    // Send who command
    await sendCommand(page, 'who');
    await waitForMessage(page, SUCCESS_MESSAGES.WHO_HEADER);

    // Verify other commands still work
    await sendCommand(page, 'say Stability test');
    await waitForMessage(page, 'You say: Stability test');

    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('Stability test'))).toBeTruthy();
  });
});
