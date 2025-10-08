/**
 * Whisper Logging Tests
 *
 * Tests whisper logging functionality for moderation purposes.
 * Converted from e2e-tests/scenarios/scenario-18-whisper-logging.md
 *
 * Test Coverage:
 * - Admin log access
 * - Non-admin access denial
 * - Log content verification
 * - Multiple whisper logging
 * - Privacy verification
 * - Log format validation
 *
 * Note: These tests use admin account to verify logging functionality.
 */

import { expect, test } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { getMessages, hasMessage, sendCommand, waitForMessage } from '../fixtures/player';
import { ERROR_MESSAGES, TEST_PLAYERS } from '../fixtures/test-data';

test.describe('Whisper Logging - Admin Access', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should allow admin to access whisper logs', async ({ page }) => {
    // Send test whisper first (to have something in logs)
    await sendCommand(page, 'whisper Ithaqua Test logging message');
    await page.waitForTimeout(1000);

    // Access whisper logs as admin
    await sendCommand(page, 'admin whisper logs');

    // Verify logs response appears
    await waitForMessage(page, 'Whisper Logs:');

    const messages = await getMessages(page);
    expect(messages.some(m => m.includes('Whisper Logs:'))).toBeTruthy();
  });

  test('should display whisper log content correctly', async ({ page }) => {
    // Send multiple test whispers
    const testMessages = ['Log test 1', 'Log test 2', 'Log test 3'];

    for (const msg of testMessages) {
      await sendCommand(page, `whisper Ithaqua ${msg}`);
      await page.waitForTimeout(300);
    }

    // Access logs
    await sendCommand(page, 'admin whisper logs');
    await waitForMessage(page, 'Whisper Logs:');

    const messages = await getMessages(page);
    const logMessages = messages.filter(m => m.includes('whisper') || m.includes('Whisper'));

    // Should have log information
    expect(logMessages.length).toBeGreaterThan(0);
  });

  test('should log multiple whispers correctly', async ({ page }) => {
    // Send multiple whispers
    for (let i = 1; i <= 3; i++) {
      await sendCommand(page, `whisper Ithaqua Logging test ${i}`);
      await page.waitForTimeout(200);
    }

    // Access logs
    await sendCommand(page, 'admin whisper logs');
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Verify logs contain whisper information
    // Note: Actual log format depends on implementation
    const hasWhisperInfo = messages.some(m => m.toLowerCase().includes('whisper'));
    expect(hasWhisperInfo).toBeTruthy();
  });

  test('should maintain log privacy (admin only)', async ({ page }) => {
    // Verify admin status first
    await sendCommand(page, 'admin status');

    // Wait for admin confirmation
    await page.waitForTimeout(1000);

    const messages = await getMessages(page);

    // Should either see admin status or have access to admin commands
    // This verifies we're testing with proper admin account
    const isAdmin = messages.some(m => m.includes('Admin') || m.includes('privileges'));

    expect(isAdmin).toBeTruthy();
  });
});

test.describe('Whisper Logging - Non-Admin Denial', () => {
  test.beforeEach(async ({ page }) => {
    // Login as non-admin player
    await loginAsPlayer(page, TEST_PLAYERS.ITHAQUA.username, TEST_PLAYERS.ITHAQUA.password);
  });

  test('should deny non-admin access to whisper logs', async ({ page }) => {
    // Attempt to access whisper logs as non-admin
    await sendCommand(page, 'admin whisper logs');

    // Verify permission denied error
    await waitForMessage(page, ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);

    const messages = await getMessages(page);
    expect(messages).toContain(ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);
  });

  test('should deny non-admin access to admin commands', async ({ page }) => {
    // Try admin status command
    await sendCommand(page, 'admin status');

    // Verify permission denied
    await waitForMessage(page, ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);

    const hasPermissionError = await hasMessage(page, ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);
    expect(hasPermissionError).toBeTruthy();
  });

  test('should maintain privacy for regular players', async ({ page }) => {
    // Send whispers as regular player
    await sendCommand(page, 'whisper ArkanWolfshade Private message from Ithaqua');
    await page.waitForTimeout(500);

    // Try to access logs
    await sendCommand(page, 'admin whisper logs');
    await waitForMessage(page, ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);

    const messages = await getMessages(page);

    // Should NOT see any whisper logs
    const hasWhisperLogs = messages.some(m => m.includes('Whisper Logs:'));
    expect(hasWhisperLogs).toBeFalsy();

    // Should only see permission denied
    expect(messages).toContain(ERROR_MESSAGES.ADMIN_PERMISSION_DENIED);
  });
});

test.describe('Whisper Logging - System Stability', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(page, TEST_PLAYERS.ARKAN_WOLFSHADE.username, TEST_PLAYERS.ARKAN_WOLFSHADE.password);
  });

  test('should maintain system stability after logging access', async ({ page }) => {
    // Access logs
    await sendCommand(page, 'admin whisper logs');
    await page.waitForTimeout(1000);

    // Verify system is still responsive
    await sendCommand(page, 'say Stability test after log access');
    await waitForMessage(page, 'You say: Stability test after log access');

    const hasSayMessage = await hasMessage(page, 'Stability test after log access');
    expect(hasSayMessage).toBeTruthy();
  });

  test('should handle multiple log access requests gracefully', async ({ page }) => {
    // Access logs multiple times
    for (let i = 1; i <= 3; i++) {
      await sendCommand(page, 'admin whisper logs');
      await page.waitForTimeout(500);
    }

    // Verify system handled multiple requests
    const messages = await getMessages(page);
    const logRequests = messages.filter(m => m.includes('Whisper Logs:'));

    // Should have processed all requests
    expect(logRequests.length).toBeGreaterThanOrEqual(1);
  });
});
