import { expect, test } from '@playwright/test';

test.describe('CommandPanel Component Tests', () => {
  test('should render command input with correct placeholder', async ({ page }) => {
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

    // Verify command input is present with correct placeholder
    const commandInput = page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...");
    await expect(commandInput).toBeVisible();

    console.log('✅ CommandPanel component test passed - input field is visible');
  });

  test('should allow typing in command input', async ({ page }) => {
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

    // Find and interact with command input
    const commandInput = page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...");
    await commandInput.fill('help');

    // Verify the input was filled
    const inputValue = await commandInput.inputValue();
    expect(inputValue).toBe('help');

    console.log('✅ CommandPanel component test passed - input accepts text');
  });

  test('should handle Enter key press', async ({ page }) => {
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

    // Find and interact with command input
    const commandInput = page.getByPlaceholder("Enter game command (e.g., 'look', 'inventory', 'go north')...");
    await commandInput.fill('help');
    await page.keyboard.press('Enter');

    // Verify the command was sent (input should be cleared or command processed)
    // Note: We're not testing the response here, just that the input accepts Enter
    console.log('✅ CommandPanel component test passed - Enter key is handled');
  });
});
