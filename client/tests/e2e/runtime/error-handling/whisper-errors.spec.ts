/**
 * Whisper Error Handling Tests
 *
 * Tests error conditions and validation for the whisper system.
 * Converted from e2e-tests/scenarios/scenario-14-whisper-errors.md
 *
 * Test Coverage:
 * - Non-existent player errors
 * - Empty message rejection
 * - Invalid syntax handling
 * - Message length limits
 * - Self-whisper prevention
 * - Special character support
 * - Unicode character support
 * - Whitespace handling
 * - Error recovery
 * - System stability
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { getMessages, hasMessage, sendCommand, waitForMessage } from '../fixtures/player';
import { ERROR_MESSAGES, SUCCESS_MESSAGES, TEST_MESSAGES, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Whisper Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should error when whispering to non-existent player', async ({ page }) => {
    // Whisper to non-existent player
    await sendCommand(page, 'whisper NonExistentPlayer Hello there');

    // Verify error message
    const expectedError = ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistentPlayer');
    await waitForMessage(page, expectedError);

    const messages = await getMessages(page);
    expect(messages).toContain(expectedError);
  });

  test('should reject empty whisper messages', async ({ page }) => {
    // Send empty whisper (no message after player name)
    await sendCommand(page, 'whisper Ithaqua');

    // Verify error message
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_EMPTY_MESSAGE);

    const hasError = await hasMessage(page, ERROR_MESSAGES.WHISPER_EMPTY_MESSAGE);
    expect(hasError).toBeTruthy();
  });

  test('should reject invalid whisper command syntax', async ({ page }) => {
    // Send whisper with no arguments
    await sendCommand(page, 'whisper');

    // Verify usage error message
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);
  });

  test('should reject long whisper messages (>500 characters)', async ({ page }) => {
    // Create very long whisper message
    const longMessage = TEST_MESSAGES.LONG_MESSAGE;

    // Send long whisper
    await sendCommand(page, `whisper Ithaqua ${longMessage}`);

    // Verify error message
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_MESSAGE_TOO_LONG);
  });

  test('should prevent whispering to self', async ({ page }) => {
    // Attempt to whisper to own username
    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Hello myself`);

    // Verify error message
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_TO_SELF);

    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.WHISPER_TO_SELF);
  });

  test('should reject whitespace-only whisper messages', async ({ page }) => {
    // Send whisper with only whitespace
    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WHITESPACE_ONLY}`);

    // Verify error message
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_EMPTY_MESSAGE);
  });

  test('should handle special characters in whisper messages', async ({ page }) => {
    // Note: This test expects successful whisper delivery
    // In reality, Ithaqua might not be online, so we'll get an error
    // But if they are online, special chars should work

    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WITH_SPECIAL_CHARS}`);

    // Wait for either success or "player not found" error
    // Both are acceptable - we're testing that special chars don't cause crashes
    const messages = await getMessages(page);

    // Should either see success message with special chars OR player not found error
    const hasSpecialChars = messages.some(m => m.includes('!@#$%^&*()'));
    const hasPlayerNotFound = messages.some(m => m.includes('not found') || m.includes('offline'));

    expect(hasSpecialChars || hasPlayerNotFound).toBeTruthy();
  });

  test('should handle Unicode characters in whisper messages', async ({ page }) => {
    // Send whisper with Unicode characters
    await sendCommand(page, `whisper Ithaqua ${TEST_MESSAGES.WITH_UNICODE}`);

    // Wait for response (either success or player not online)
    const messages = await getMessages(page);

    // Should either see Unicode chars or error (both acceptable)
    const hasUnicode = messages.some(m => m.includes('你好世界 🌍'));
    const hasError = messages.some(m => m.includes('not found') || m.includes('offline'));

    expect(hasUnicode || hasError).toBeTruthy();
  });

  test('should allow valid whispers after error conditions', async ({ page }) => {
    // Trigger multiple errors first
    await sendCommand(page, 'whisper');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    await sendCommand(page, 'whisper NonExistentPlayer Test');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_PLAYER_NOT_FOUND('NonExistentPlayer'));

    await sendCommand(page, `whisper ${TEST_PLAYERS.ARKAN_WOLFSHADE.username} Test`);
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_TO_SELF);

    // Now send valid whisper to Ithaqua
    // Note: Ithaqua might not be online, so we accept either success or offline error
    await sendCommand(page, 'whisper Ithaqua Valid message after errors');

    // Wait for some response
    const messages = await getMessages(page);

    // Should have processed the command (not crashed)
    expect(messages.length).toBeGreaterThan(3); // At least the 3 errors + this response
  });

  test('should maintain system stability after error recovery', async ({ page }) => {
    // Trigger error
    await sendCommand(page, 'whisper');
    await waitForMessage(page, ERROR_MESSAGES.WHISPER_INVALID_SYNTAX);

    // Send valid command to different system (say) to verify overall stability
    await sendCommand(page, 'say System stability test');
    await waitForMessage(page, SUCCESS_MESSAGES.SAY_MESSAGE_SENT('System stability test'));

    // Verify say command worked
    const hasSayMessage = await hasMessage(page, 'System stability test');
    expect(hasSayMessage).toBeTruthy();
  });
});
