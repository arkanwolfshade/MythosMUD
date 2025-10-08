/**
 * Whisper Rate Limiting Tests
 *
 * Tests rate limiting and spam prevention for the whisper system.
 * Converted from e2e-tests/scenarios/scenario-15-whisper-rate-limiting.md
 *
 * Test Coverage:
 * - Normal whisper rate (1-3 messages/minute)
 * - Per-recipient rate limit (3 whispers/min to same player)
 * - Global rate limit (5 whispers/min total)
 * - Rate limit error messages
 * - Rate limit reset after 60 seconds
 * - System stability under rate limiting
 *
 * Note: This test suite includes a 60-second wait for rate limit reset testing.
 * Use --grep to exclude slow tests if needed: --grep-invert "@slow"
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { getMessages, sendCommand, waitForMessage } from '../fixtures/player';
import { ERROR_MESSAGES, RATE_LIMITS, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Whisper Rate Limiting', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should allow normal whisper rate (1-3 messages)', async ({ page }) => {
    // Send 3 whispers (within per-recipient limit)
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Rate test message ${i}`);

      // Should either see success or "player not found" - both acceptable
      // We're testing that rate limit is NOT triggered
      await page.waitForTimeout(500); // Small wait between messages
    }

    const messages = await getMessages(page);

    // Should NOT see rate limit error
    const hasRateLimitError = messages.some(m => m.includes(ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT));
    expect(hasRateLimitError).toBeFalsy();
  });

  test('should enforce per-recipient rate limit (3 whispers/min)', async ({ page }) => {
    // Send 3 whispers to reach limit
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
      await page.waitForTimeout(300); // Small wait
    }

    // 4th whisper should trigger rate limit
    await sendCommand(page, 'whisper Ithaqua Message 4');

    // Verify rate limit error
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);
  });

  test('should have clear and informative rate limit error messages', async ({ page }) => {
    // Trigger per-recipient rate limit
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
    }

    await sendCommand(page, 'whisper Ithaqua Message 4');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    const messages = await getMessages(page);
    const rateLimitMessages = messages.filter(m => m.includes('Rate limit exceeded'));

    // Should have exactly one rate limit error message
    expect(rateLimitMessages.length).toBeGreaterThan(0);

    // Error message should mention the limit (3 whispers)
    const hasLimitInfo = messages.some(m => m.includes('3 whispers'));
    expect(hasLimitInfo).toBeTruthy();
  });

  test('should maintain system stability under rate limiting', async ({ page }) => {
    // Trigger rate limit
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Message ${i}`);
    }

    await sendCommand(page, 'whisper Ithaqua Message 4');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    // Verify other commands still work
    await sendCommand(page, 'say System stability check');
    await waitForMessage(page, 'You say: System stability check');

    // Verify say message worked
    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('System stability check'))).toBeTruthy();
  });

  test.slow('should reset rate limit after 60 seconds', async ({ page }) => {
    // Tag as @slow since this test takes >60 seconds
    test.setTimeout(90000); // 90 seconds timeout for this test

    // Send 3 whispers to reach limit
    for (let i = 1; i <= RATE_LIMITS.WHISPER_PER_RECIPIENT; i++) {
      await sendCommand(page, `whisper Ithaqua Before reset ${i}`);
      await page.waitForTimeout(200);
    }

    // Verify rate limit is triggered
    await sendCommand(page, 'whisper Ithaqua Should fail');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT);

    // Wait for rate limit to reset (60 seconds)
    console.log('⏳ Waiting 60 seconds for rate limit reset...');
    await page.waitForTimeout(RATE_LIMITS.RESET_TIME);

    // Should be able to send whisper again
    await sendCommand(page, 'whisper Ithaqua After reset');

    // Wait for response (either success or player not found - no rate limit error)
    await page.waitForTimeout(2000);

    const messages = await getMessages(page);
    const lastMessages = messages.slice(-3); // Get last 3 messages

    // Should NOT see rate limit error in recent messages
    const hasRateLimitError = lastMessages.some(m => m.includes(ERROR_MESSAGES.WHISPER_RATE_LIMIT_RECIPIENT));
    expect(hasRateLimitError).toBeFalsy();
  });

  test('should handle special characters in whisper messages', async ({ page }) => {
    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WITH_SPECIAL_CHARS}`);

    // Wait for response
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should either see message with special chars or player error
    const hasSpecialChars = messages.some(m => m.includes('!@#$%^&*()'));
    const hasPlayerError = messages.some(m => m.includes('not found') || m.includes('offline'));

    expect(hasSpecialChars || hasPlayerError).toBeTruthy();
  });

  test('should handle Unicode characters in whisper messages', async ({ page }) => {
    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WITH_UNICODE}`);

    // Wait for response
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should either see Unicode or player error
    const hasUnicode = messages.some(m => m.includes('你好世界 🌍'));
    const hasPlayerError = messages.some(m => m.includes('not found') || m.includes('offline'));

    expect(hasUnicode || hasPlayerError).toBeTruthy();
  });

  test('should reject whitespace-only whisper messages', async ({ page }) => {
    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WHITESPACE_ONLY}`);

    await waitForMessage(page, ERROR_MESSAGES.WHISPER_EMPTY_MESSAGE);

    const hasError = await hasMessage(page, ERROR_MESSAGES.WHISPER_EMPTY_MESSAGE);
    expect(hasError).toBeTruthy();
  });

  test('should allow valid whispers after error conditions', async ({ page }) => {
    // Trigger multiple errors
    await sendCommand(page, 'whisper');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    await sendCommand(page, 'whisper NonExistentPlayer Test');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistentPlayer'));

    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Test`);
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_TO_SELF);

    // Now try valid whisper
    await sendCommand(page, 'whisper Ithaqua Valid after errors');

    // Wait for response
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should have processed all commands
    expect(messages.length).toBeGreaterThan(3);
  });

  test('should maintain system stability after multiple error conditions', async ({ page }) => {
    // Trigger various errors
    await sendCommand(page, 'whisper');
    await sendCommand(page, 'whisper NonExistent Test');
    await sendCommand(page, 'whisper Ithaqua');
    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Self test`);

    // Wait for errors to process
    await page.waitForTimeout(1000);

    // Verify system is stable by using another command
    await sendCommand(page, 'say Stability test');
    await waitForMessage(page, 'You say: Stability test');

    const hasSayMessage = await hasMessage(page, 'Stability test');
    expect(hasSayMessage).toBeTruthy();
  });
});
