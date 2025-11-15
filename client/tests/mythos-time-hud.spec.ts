import { expect, test } from '@playwright/test';

test.describe('Mythos Time HUD', () => {
  test('displays connection banner and Mythos clock after login', async ({ page }) => {
    await page.goto('http://localhost:5173');

    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 15_000 });
    await expect(page.getByTestId('connection-banner')).toBeVisible();

    const mythosClock = page.getByTestId('mythos-clock');
    await expect(mythosClock).toBeVisible();
    await expect(mythosClock).toContainText(/Mythos/i);
  });
});
