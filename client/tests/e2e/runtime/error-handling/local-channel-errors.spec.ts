/**
 * Local Channel Error Handling Tests
 *
 * Tests error conditions and edge cases for the local channel system.
 * Converted from e2e-tests/scenarios/scenario-11-local-channel-errors.md
 *
 * Test Coverage:
 * - Empty message rejection
 * - Invalid syntax handling
 * - Message length limits
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

test.describe('Local Channel Error Handling', () => {
  // Login before each test
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should reject empty local messages', async ({ page }) => {
    // Send empty local message
    await sendCommand(page, 'local');

    // Verify error message appears
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

    // Verify message is in chat
    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);
  });

  test('should reject whitespace-only local messages', async ({ page }) => {
    // Send whitespace-only message
    await sendCommand(page, `local ${TEST_MESSAGES.WHITESPACE_ONLY}`);

    // Verify error message appears
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

    // Verify error is displayed
    const hasError = await hasMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);
    expect(hasError).toBeTruthy();
  });

  test('should reject long local messages (>500 characters)', async ({ page }) => {
    // Create very long message
    const longMessage = TEST_MESSAGES.LONG_MESSAGE;
    expect(longMessage.length).toBeGreaterThan(500);

    // Send long message
    await sendCommand(page, `local ${longMessage}`);

    // Verify error message appears
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_MESSAGE_TOO_LONG);
  });

  test('should handle special characters in local messages', async ({ page }) => {
    // Send message with special characters
    await sendCommand(page, `local ${TEST_MESSAGES.WITH_SPECIAL_CHARS}`);

    // Verify message is sent successfully
    const expectedMessage = SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT(TEST_MESSAGES.WITH_SPECIAL_CHARS);
    await waitForMessage(page, expectedMessage);

    // Verify special characters are preserved
    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('!@#$%^&*()'))).toBeTruthy();
  });

  test('should handle Unicode characters in local messages', async ({ page }) => {
    // Send message with Unicode characters
    await sendCommand(page, `local ${TEST_MESSAGES.WITH_UNICODE}`);

    // Verify message is sent successfully
    const expectedMessage = SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT(TEST_MESSAGES.WITH_UNICODE);
    await waitForMessage(page, expectedMessage);

    // Verify Unicode characters are preserved
    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('你好世界 🌍'))).toBeTruthy();
  });

  test('should allow valid messages after error conditions', async ({ page }) => {
    // First, trigger an error
    await sendCommand(page, 'local');
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

    // Then send valid message
    const validMessage = 'Valid message after error';
    await sendCommand(page, `local ${validMessage}`);

    // Verify valid message is sent successfully
    const expectedMessage = SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT(validMessage);
    await waitForMessage(page, expectedMessage);

    // Verify message appears in chat
    const messages = await getMessages(page);
    expect(messages.some(m => m.includes(validMessage))).toBeTruthy();
  });

  test('should maintain system stability after multiple errors', async ({ page }) => {
    // Trigger multiple different errors
    await sendCommand(page, 'local');
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

    await sendCommand(page, `local ${TEST_MESSAGES.WHITESPACE_ONLY}`);
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

    await sendCommand(page, `local ${TEST_MESSAGES.LONG_MESSAGE}`);
    await waitForMessage(page, ERROR_MESSAGES.LOCAL_MESSAGE_TOO_LONG);

    // Verify system is still stable by sending valid message
    const stabilityTest = 'System stability test';
    await sendCommand(page, `local ${stabilityTest}`);

    const expectedMessage = SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT(stabilityTest);
    await waitForMessage(page, expectedMessage);

    // Verify message was delivered
    const hasStabilityMessage = await hasMessage(page, stabilityTest);
    expect(hasStabilityMessage).toBeTruthy();
  });

  test('should handle rapid successive commands gracefully', async ({ page }) => {
    // Send multiple commands in rapid succession
    const messages = ['First message', 'Second message', 'Third message'];

    for (const msg of messages) {
      await sendCommand(page, `local ${msg}`);
    }

    // Verify all messages were processed (either sent or errored)
    // Wait for last message to appear
    await waitForMessage(page, SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT(messages[messages.length - 1]));

    // Count successful messages
    const allMessages = await getMessages(page);
    const successfulMessages = messages.filter(msg => allMessages.some(m => m.includes(msg)));

    // All messages should have been processed
    expect(successfulMessages.length).toBe(messages.length);
  });
});
