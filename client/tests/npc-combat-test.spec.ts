import { expect, test } from '@playwright/test';

test.describe('NPC Combat Attack Events', () => {
  test('should display NPC attack messages in Game Log', async ({ page }) => {
    // Navigate to the game
    await page.goto('http://localhost:5173');

    // Wait for the login form to be visible
    await page.waitForSelector('input[placeholder="Username"]', { timeout: 10000 });

    // Login
    await page.fill('input[placeholder="Username"]', 'Ithaqua');
    await page.fill('input[placeholder="Password"]', 'Cthulhu1');
    await page.click('button:has-text("Enter the Void")');

    // Wait for game to load
    await page.waitForSelector('button:has-text("Enter the Realm")', { timeout: 10000 });
    await page.click('button:has-text("Enter the Realm")');

    // Wait for game interface to load
    await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

    // Start combat
    await page.fill('input[placeholder*="game command"]', 'attack dr francis morgan');
    await page.click('button:has-text("Send Command")');

    // Wait for combat to start
    await page.waitForSelector('text=Combat has begun!', { timeout: 10000 });

    // Wait for combat to progress and check for NPC attacks
    // We'll wait up to 30 seconds for NPC attacks to appear
    const npcAttackMessage = await page.waitForSelector('text=Dr. Francis Morgan attacks', { timeout: 30000 });

    // Verify NPC attack message appears
    expect(npcAttackMessage).toBeTruthy();

    // Check that the message appears in the Game Log
    const gameLogText = await page.textContent('[data-testid="game-log-panel"]');
    expect(gameLogText).toContain('Dr. Francis Morgan attacks');
  });
});
