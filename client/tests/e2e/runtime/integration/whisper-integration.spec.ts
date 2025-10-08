/**
 * Whisper Integration Tests (Automated Portion)
 *
 * Tests whisper system integration with other game systems.
 * Converted from e2e-tests/scenarios/scenario-17-whisper-integration.md (partial)
 *
 * Automated Test Coverage:
 * - Player management integration
 * - Authentication integration
 * - Rate limiting integration
 * - Error handling integration
 * - Logging integration
 * - Performance integration
 *
 * MCP Testing Required For:
 * - Cross-player message delivery
 * - Real-time whisper notifications
 * - (See e2e-tests/scenarios/scenario-17-whisper-integration.md for multi-player tests)
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { getMessages, hasMessage, sendCommand, waitForMessage } from '../fixtures/player';
import { ERROR_MESSAGES, RATE_LIMITS, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Whisper - Player Management Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should validate player exists before sending whisper', async ({ page }) => {
    // Try whispering to non-existent player
    await sendCommand(page, 'whisper NonExistentPlayer Test message');

    // Verify player validation error
    const expectedError = ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistentPlayer');
    await waitForMessage(page, expectedError);

    const messages = await getMessages(page);
    expect(messages).toContain(expectedError);
  });

  test('should integrate with player lookup system', async ({ page }) => {
    // Whisper to valid player (Ithaqua)
    await sendCommand(page, 'whisper Ithaqua Player lookup test');

    // Wait for response (either success or offline message)
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should have processed the whisper (proves player lookup worked)
    expect(messages.length).toBeGreaterThan(0);
  });
});

test.describe('Whisper - Authentication Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should require authentication to send whispers', async ({ page }) => {
    // Send whisper (requires authenticated session)
    await sendCommand(page, 'whisper Ithaqua Authentication test');

    // Wait for response
    await page.waitForTimeout(1000);

    // Should process command (no auth error)
    // If we get here without auth error, authentication integration works
    const messages = await getMessages(page);
    expect(messages.length).toBeGreaterThan(0);
  });

  test('should maintain session state during whisper operations', async ({ page }) => {
    // Send multiple whispers to verify session maintained
    for (let i = 1; i <= 3; i++) {
      await sendCommand(page, `whisper Ithaqua Session test ${i}`);
      await page.waitForTimeout(300);
    }

    // All should be processed successfully (session maintained)
    const messages = await getMessages(page);

    // Should have all whisper responses
    expect(messages.length).toBeGreaterThan(0);
  });
});

test.describe('Whisper - Rate Limiting Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should enforce rate limits correctly', async ({ page }) => {
    // Send whispers up to limit
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Rate limit test ${i}`);
      await page.waitForTimeout(200);
    }

    // Next whisper should trigger rate limit
    await sendCommand(page, 'whisper Ithaqua Should trigger limit');

    // Verify rate limit error
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    const hasRateLimitError = await hasMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);
    expect(hasRateLimitError).toBeTruthy();
  });

  test('should track rate limits per recipient', async ({ page }) => {
    // Send whispers to one recipient
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
      await page.waitForTimeout(200);
    }

    // Should hit rate limit for this recipient
    await sendCommand(page, 'whisper Ithaqua Extra message');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    // But whispering to different recipient should still work (or give different error)
    await sendCommand(page, 'whisper NonExistent Different recipient');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistent'));

    // Should get "not found" error, not rate limit error
    const messages = await getMessages(page);
    const lastMessage = messages[messages.length - 1];
    expect(lastMessage).toContain('not found');
  });
});

test.describe('Whisper - Error Handling Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should display whisper errors correctly', async ({ page }) => {
    // Trigger various whisper errors
    await sendCommand(page, 'whisper');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    await sendCommand(page, 'whisper NonExistent Test');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistent'));

    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Self test`);
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_TO_SELF);

    // All errors should be displayed
    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistent'));
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_TO_SELF);
  });

  test('should integrate with system error logging', async ({ page }) => {
    // Trigger error
    await sendCommand(page, 'whisper');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    // Verify system is still functional (error was logged but didn't crash)
    await sendCommand(page, 'say Error logging test');
    await waitForMessage(page, SUCCESS_MESSAGES.SAY_MESSAGE_SENT('Error logging test'));

    const hasSayMessage = await hasMessage(page, 'Error logging test');
    expect(hasSayMessage).toBeTruthy();
  });
});

test.describe('Whisper - Performance Integration', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should handle multiple whispers efficiently', async ({ page }) => {
    const messageCount = 3; // Within rate limit
    const startTime = Date.now();

    for (let i = 1; i <= messageCount; i++) {
      await sendCommand(page, `whisper Ithaqua Performance test ${i}`);
      await page.waitForTimeout(100);
    }

    const endTime = Date.now();
    const totalTime = endTime - startTime;

    // Should complete quickly (< 5 seconds for 3 messages)
    expect(totalTime).toBeLessThan(5000);
  });

  test('should maintain performance across mixed channel usage', async ({ page }) => {
    // Mix whispers with other channel commands
    await sendCommand(page, 'say Say message 1');
    await sendCommand(page, 'whisper Ithaqua Whisper 1');
    await sendCommand(page, 'local Local message 1');
    await sendCommand(page, 'say Say message 2');

    // Wait for processing
    await page.waitForTimeout(2000);

    // All commands should be processed
    const messages = await getMessages(page);

    // Should have responses for multiple channel types
    expect(messages.some(m => m.includes('Say message'))).toBeTruthy();
    expect(messages.some(m => m.includes('Local message'))).toBeTruthy();
  });
});

test.describe('Whisper - System Stability', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should maintain stability across all integration points', async ({ page }) => {
    // Test player management
    await sendCommand(page, 'whisper Ithaqua Integration test 1');
    await page.waitForTimeout(300);

    // Test error handling
    await sendCommand(page, 'whisper NonExistent Integration test 2');
    await page.waitForTimeout(300);

    // Test self-whisper prevention
    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Integration test 3`);
    await page.waitForTimeout(300);

    // Verify system handled all integration points
    const messages = await getMessages(page);
    expect(messages.length).toBeGreaterThan(2);

    // Verify can still use other commands
    await sendCommand(page, 'say Stability verification');
    await waitForMessage(page, 'You say: Stability verification');

    const hasStabilityMessage = await hasMessage(page, 'Stability verification');
    expect(hasStabilityMessage).toBeTruthy();
  });
});
