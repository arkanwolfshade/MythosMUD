import { expect, test } from '@playwright/test';

test.describe('ChatPanel Component Tests', () => {
  test('should render chat panel with data-testid', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Wait for login form
    await page.waitForSelector('input[placeholder="Username"]');

    // Fill login form with mock credentials
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Submit login
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for game interface
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Wait for chat panel to load
    await page.waitForSelector('[data-testid="chat-panel"]', { timeout: 5000 });

    // Verify chat panel is visible
    const chatPanel = page.locator('[data-testid="chat-panel"]');
    await expect(chatPanel).toBeVisible();

    console.log('✅ ChatPanel component test passed - panel is visible');
  });

  test('should display chat messages area', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Wait for login form
    await page.waitForSelector('input[placeholder="Username"]');

    // Fill login form with mock credentials
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Submit login
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for game interface
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Wait for chat panel to load
    await page.waitForSelector('[data-testid="chat-panel"]', { timeout: 5000 });

    // Verify chat messages area is present
    const chatMessages = page.locator('[data-testid="chat-messages"]');
    await expect(chatMessages).toBeVisible();

    console.log('✅ ChatPanel component test passed - messages area is visible');
  });

  test('should display chat input with data-testid', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Wait for login form
    await page.waitForSelector('input[placeholder="Username"]');

    // Fill login form with mock credentials
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Submit login
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for game interface
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Wait for chat panel to load
    await page.waitForSelector('[data-testid="chat-panel"]', { timeout: 5000 });

    // Verify chat input is present
    const chatInput = page.locator('[data-testid="chat-input"]');
    await expect(chatInput).toBeVisible();

    console.log('✅ ChatPanel component test passed - chat input is visible');
  });

  test('should allow typing in chat input', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Wait for login form
    await page.waitForSelector('input[placeholder="Username"]');

    // Fill login form with mock credentials
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Submit login
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for game interface
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Wait for chat panel to load
    await page.waitForSelector('[data-testid="chat-panel"]', { timeout: 5000 });

    // Find and interact with chat input
    const chatInput = page.locator('[data-testid="chat-input"]');
    await chatInput.fill('Hello, world!');

    // Verify the input was filled
    const inputValue = await chatInput.inputValue();
    expect(inputValue).toBe('Hello, world!');

    console.log('✅ ChatPanel component test passed - chat input accepts text');
  });

  test('should display channel selector', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Wait for login form
    await page.waitForSelector('input[placeholder="Username"]');

    // Fill login form with mock credentials
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Submit login
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for game interface
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Wait for chat panel to load
    await page.waitForSelector('[data-testid="chat-panel"]', { timeout: 5000 });

    // Verify channel selector is present
    const channelSelector = page.locator('[data-testid="channel-selector"]');
    await expect(channelSelector).toBeVisible();

    console.log('✅ ChatPanel component test passed - channel selector is visible');
  });
});
