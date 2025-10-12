import { expect, test } from '@playwright/test';

test.describe('UI Elements Visibility Tests', () => {
  test('should have all required data-testid attributes on login form', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Verify login form elements are present with correct attributes
    await expect(page.getByPlaceholder('Username')).toBeVisible();
    await expect(page.getByPlaceholder('Password')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Enter the Void' })).toBeVisible();

    // Verify the login container exists (this was added for testing)
    await expect(page.locator('.login-container')).toBeVisible();

    console.log('✅ Login form visibility test passed - all elements are present');
  });

  test('should verify game terminal structure after mock login', async ({ page }) => {
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

    // Verify main game terminal structure
    await expect(page.locator('[data-testid="game-terminal"]')).toBeVisible();

    console.log('✅ Game terminal structure test passed - main container is visible');
  });

  test('should verify room info panel elements are present', async ({ page }) => {
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

    // Wait for room info panel to load
    await page.waitForSelector('[data-testid="room-info-panel"]', { timeout: 5000 });

    // Verify room info panel elements
    await expect(page.locator('[data-testid="room-info-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="room-name"]')).toBeVisible();
    await expect(page.locator('[data-testid="room-description"]')).toBeVisible();
    await expect(page.locator('[data-testid="zone-value"]')).toBeVisible();
    await expect(page.locator('[data-testid="subzone-value"]')).toBeVisible();
    await expect(page.locator('[data-testid="occupant-count"]')).toBeVisible();

    console.log('✅ Room info panel visibility test passed - all elements are present');
  });

  test('should verify chat panel elements are present', async ({ page }) => {
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

    // Verify chat panel elements
    await expect(page.locator('[data-testid="chat-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="chat-messages"]')).toBeVisible();
    await expect(page.locator('[data-testid="chat-input"]')).toBeVisible();
    await expect(page.locator('[data-testid="channel-selector"]')).toBeVisible();

    console.log('✅ Chat panel visibility test passed - all elements are present');
  });

  test('should verify command panel elements are present', async ({ page }) => {
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

    // Wait for command panel to load
    await page.waitForSelector('[data-testid="command-panel"]', { timeout: 5000 });

    // Verify command panel elements
    await expect(page.locator('[data-testid="command-panel"]')).toBeVisible();
    await expect(page.locator('[data-testid="command-input"]')).toBeVisible();
    await expect(page.locator('[data-testid="command-history"]')).toBeVisible();

    console.log('✅ Command panel visibility test passed - all elements are present');
  });
});
