import { expect, test } from '@playwright/test';

test.describe('RoomInfoPanel Component Tests', () => {
  test('should render room info panel with data-testid', async ({ page }) => {
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

    // Verify room info panel is visible
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    console.log('✅ RoomInfoPanel component test passed - panel is visible');
  });

  test('should display room name with data-testid', async ({ page }) => {
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

    // Verify room name is displayed
    const roomName = page.locator('[data-testid="room-name"]');
    await expect(roomName).toBeVisible();

    console.log('✅ RoomInfoPanel component test passed - room name is displayed');
  });

  test('should display room description with data-testid', async ({ page }) => {
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

    // Verify room description is displayed
    const roomDescription = page.locator('[data-testid="room-description"]');
    await expect(roomDescription).toBeVisible();

    console.log('✅ RoomInfoPanel component test passed - room description is displayed');
  });

  test('should display zone and subzone with data-testids', async ({ page }) => {
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

    // Verify zone and subzone are displayed
    const zoneValue = page.locator('[data-testid="zone-value"]');
    const subzoneValue = page.locator('[data-testid="subzone-value"]');

    await expect(zoneValue).toBeVisible();
    await expect(subzoneValue).toBeVisible();

    console.log('✅ RoomInfoPanel component test passed - zone and subzone are displayed');
  });

  test('should display occupant count with data-testid', async ({ page }) => {
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

    // Verify occupant count is displayed
    const occupantCount = page.locator('[data-testid="occupant-count"]');
    await expect(occupantCount).toBeVisible();

    console.log('✅ RoomInfoPanel component test passed - occupant count is displayed');
  });
});
