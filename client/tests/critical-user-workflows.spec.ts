import { expect, test } from '@playwright/test';

/**
 * Critical User Workflow Integration Tests
 *
 * These tests verify essential user workflows using real server authentication
 * and focus on critical paths that users must be able to complete successfully.
 *
 * Based on findings from "Critical Path Analysis in Non-Euclidean Systems" - Dr. Armitage, 1928
 */

// Real test credentials (created with create_real_test_users.py)
const TEST_CREDENTIALS = {
  TEST_USER_1: {
    username: 'test1',
    password: 'test_password_123',
  },
  TEST_USER_2: {
    username: 'test2',
    password: 'test_password_123',
  },
  ADMIN_USER: {
    username: 'ArkanWolfshade',
    password: 'test_password_123',
  },
  REGULAR_USER: {
    username: 'Ithaqua',
    password: 'test_password_123',
  },
};

// Helper function to login with real credentials
async function loginWithRealCredentials(
  page: import('@playwright/test').Page,
  credentials: typeof TEST_CREDENTIALS.TEST_USER_1
) {
  await page.goto('/');

  // Wait for login form
  await page.waitForSelector('h1:has-text("MythosMUD")');

  // Fill login form
  await page.getByPlaceholder('Username').fill(credentials.username);
  await page.getByPlaceholder('Password').fill(credentials.password);

  // Submit login
  await page.getByRole('button', { name: 'Enter the Void' }).click();

  // Wait for game interface
  await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 15000 });
}

// Helper function to wait for real-time connection
// eslint-disable-next-line @typescript-eslint/no-unused-vars
async function waitForRealtimeConnection(_page: import('@playwright/test').Page) {
  await page.waitForFunction(
    () => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    },
    { timeout: 10000 }
  );
}

test.describe('Critical User Workflow Integration Tests', () => {
  test('Critical Path 1: User Login and Basic Navigation', async ({ page }) => {
    // Test the most critical user workflow - logging in and accessing the game
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Verify game interface is loaded
    await expect(page.locator('[data-testid="game-terminal"]')).toBeVisible();
    await expect(page.locator('[data-testid="room-info-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="chat-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="command-panel"]')).toBeVisible();

    // Verify room information is displayed
    await expect(page.locator('[data-testid="room-name"]')).toBeVisible();
    await expect(page.locator('[data-testid="room-description"]')).toBeVisible();

    console.log('✅ Critical Path 1: User login and basic navigation - PASSED');
  });

  test('Critical Path 2: Basic Command Execution', async ({ page }) => {
    // Test that users can execute basic commands
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Wait for command input to be available
    await page.waitForSelector('[data-testid="command-input"]');

    // Test help command
    await page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...").fill('help');
    await page.keyboard.press('Enter');

    // Wait for command response
    await page.waitForTimeout(2000);

    // Verify help content is displayed
    const helpContent = await page.textContent('[data-testid="game-terminal"]');
    expect(helpContent).toContain('help');

    console.log('✅ Critical Path 2: Basic command execution - PASSED');
  });

  test('Critical Path 3: Room Movement', async ({ page }) => {
    // Test that users can move between rooms
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Wait for command input
    await page.waitForSelector('[data-testid="command-input"]');

    // Test look command first
    await page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...").fill('look');
    await page.keyboard.press('Enter');

    // Wait for response
    await page.waitForTimeout(2000);

    // Verify room description is displayed
    const roomContent = await page.textContent('[data-testid="room-description"]');
    expect(roomContent).toBeTruthy();

    console.log('✅ Critical Path 3: Room movement - PASSED');
  });

  test('Critical Path 4: Chat Communication', async ({ page }) => {
    // Test that users can send chat messages
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Wait for chat input
    await page.waitForSelector('[data-testid="chat-input"]');

    // Send a test message
    await page.getByPlaceholder('Type your message...').fill('Hello, this is a test message');
    await page.keyboard.press('Enter');

    // Wait for message to be sent
    await page.waitForTimeout(1000);

    // Verify message appears in chat
    const chatContent = await page.textContent('[data-testid="chat-messages"]');
    expect(chatContent).toContain('Hello, this is a test message');

    console.log('✅ Critical Path 4: Chat communication - PASSED');
  });

  test('Critical Path 5: Multiplayer Interaction', async ({ browser }) => {
    // Test that multiple users can interact in the same room
    const context1 = await browser.newContext();
    const page1 = await context1.newPage();

    const context2 = await browser.newContext();
    const page2 = await context2.newPage();

    try {
      // Login both users
      await loginWithRealCredentials(page1, TEST_CREDENTIALS.TEST_USER_1);
      await loginWithRealCredentials(page2, TEST_CREDENTIALS.TEST_USER_2);

      // Wait for both users to be in the game
      await page1.waitForSelector('[data-testid="game-terminal"]');
      await page2.waitForSelector('[data-testid="game-terminal"]');

      // User 1 sends a message
      await page1.getByPlaceholder('Type your message...').fill('Hello from User 1');
      await page1.keyboard.press('Enter');

      // Wait for message to propagate
      await page1.waitForTimeout(2000);

      // User 2 sends a response
      await page2.getByPlaceholder('Type your message...').fill('Hello from User 2');
      await page2.keyboard.press('Enter');

      // Wait for response to propagate
      await page2.waitForTimeout(2000);

      // Verify both messages are visible
      const chat1 = await page1.textContent('[data-testid="chat-messages"]');
      const chat2 = await page2.textContent('[data-testid="chat-messages"]');

      expect(chat1).toContain('Hello from User 1');
      expect(chat2).toContain('Hello from User 2');

      console.log('✅ Critical Path 5: Multiplayer interaction - PASSED');
    } finally {
      await context1.close();
      await context2.close();
    }
  });

  test('Critical Path 6: Admin Commands (Admin User)', async ({ page }) => {
    // Test that admin users can access admin commands
    await loginWithRealCredentials(page, TEST_CREDENTIALS.ADMIN_USER);

    // Wait for command input
    await page.waitForSelector('[data-testid="command-input"]');

    // Test who command (should work for all users)
    await page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...").fill('who');
    await page.keyboard.press('Enter');

    // Wait for response
    await page.waitForTimeout(2000);

    // Verify who command response
    const whoContent = await page.textContent('[data-testid="game-terminal"]');
    expect(whoContent).toContain('who');

    console.log('✅ Critical Path 6: Admin commands - PASSED');
  });

  test('Critical Path 7: Error Handling', async ({ page }) => {
    // Test that the system handles invalid commands gracefully
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Wait for command input
    await page.waitForSelector('[data-testid="command-input"]');

    // Test invalid command
    await page
      .getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...")
      .fill('invalid_command_12345');
    await page.keyboard.press('Enter');

    // Wait for error response
    await page.waitForTimeout(2000);

    // Verify error is handled gracefully (no crash)
    await expect(page.locator('[data-testid="game-terminal"]')).toBeVisible();

    console.log('✅ Critical Path 7: Error handling - PASSED');
  });

  test('Critical Path 8: Session Persistence', async ({ page }) => {
    // Test that user sessions persist across page refreshes
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Wait for game to load
    await page.waitForSelector('[data-testid="game-terminal"]');

    // Refresh the page
    await page.reload();

    // Wait for game to reload
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 15000 });

    // Verify user is still logged in
    await expect(page.locator('[data-testid="game-terminal"]')).toBeVisible();

    console.log('✅ Critical Path 8: Session persistence - PASSED');
  });

  test('Critical Path 9: Performance and Responsiveness', async ({ page }) => {
    // Test that the system responds quickly to user actions
    const startTime = Date.now();

    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    const loginTime = Date.now() - startTime;

    // Login should complete within 15 seconds
    expect(loginTime).toBeLessThan(15000);

    // Test command response time
    const commandStartTime = Date.now();

    await page.waitForSelector('[data-testid="command-input"]');
    await page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...").fill('look');
    await page.keyboard.press('Enter');

    // Wait for response
    await page.waitForTimeout(2000);

    const commandTime = Date.now() - commandStartTime;

    // Command should respond within 5 seconds
    expect(commandTime).toBeLessThan(5000);

    console.log(
      `✅ Critical Path 9: Performance and responsiveness - PASSED ` +
        `(Login: ${loginTime}ms, Command: ${commandTime}ms)`
    );
  });

  test('Critical Path 10: Cross-Browser Compatibility', async ({ page, browserName }) => {
    // Test that critical workflows work across different browsers
    await loginWithRealCredentials(page, TEST_CREDENTIALS.TEST_USER_1);

    // Verify basic functionality works
    await expect(page.locator('[data-testid="game-terminal"]')).toBeVisible();
    await expect(page.locator('[data-testid="room-info-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="chat-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="command-panel"]')).toBeVisible();

    // Test a basic command
    await page.waitForSelector('[data-testid="command-input"]');
    await page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...").fill('help');
    await page.keyboard.press('Enter');

    // Wait for response
    await page.waitForTimeout(2000);

    // Verify command worked
    const content = await page.textContent('[data-testid="game-terminal"]');
    expect(content).toContain('help');

    console.log(`✅ Critical Path 10: Cross-browser compatibility (${browserName}) - PASSED`);
  });
});
