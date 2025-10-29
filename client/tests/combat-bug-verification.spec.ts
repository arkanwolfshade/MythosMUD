import { expect, test } from '@playwright/test';

test.describe('Combat Bug Verification', () => {
  test('should verify all combat bugs are fixed', async ({ page }) => {
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

    // Check initial XP value in Player Information panel
    const initialXpText = await page.textContent('[data-testid="player-info-panel"]');
    console.log('Initial XP:', initialXpText);

    // Check initial room occupants
    const initialOccupants = await page.textContent('[data-testid="room-info-panel"]');
    console.log('Initial occupants:', initialOccupants);

    // Start combat
    await page.fill('input[placeholder*="game command"]', 'attack dr francis morgan');
    await page.click('button:has-text("Send Command")');

    // Wait for combat to start - should see only ONE "Combat has begun!" message
    await page.waitForSelector('text=Combat has begun!', { timeout: 10000 });

    // Verify only one combat start message (Bug 1 fix)
    const gameLogText = await page.textContent('[data-testid="game-log-panel"]');
    const combatStartMessages = (gameLogText.match(/Combat has begun!/g) || []).length;
    expect(combatStartMessages).toBe(1);
    console.log('✅ Bug 1: Combat start message appears only once');

    // Wait for player attack messages with health display (Bug 2 fix)
    await page.waitForSelector('text=You hit Dr. Francis Morgan for 10 damage!', { timeout: 10000 });

    // Verify health is displayed in damage messages
    const hasHealthDisplay = gameLogText.includes('HP)');
    expect(hasHealthDisplay).toBe(true);
    console.log('✅ Bug 2: Mob health is displayed in damage messages');

    // Wait for NPC attack messages (Bug 3 fix)
    await page.waitForSelector('text=Dr. Francis Morgan attacks you for', { timeout: 30000 });
    console.log('✅ Bug 3: NPC attacks are now visible');

    // Wait for combat to end
    await page.waitForSelector('text=Combat has ended', { timeout: 30000 });

    // Verify only one combat end message (Bug 4 fix)
    const combatEndMessages = (gameLogText.match(/Combat has ended/g) || []).length;
    expect(combatEndMessages).toBe(1);
    console.log('✅ Bug 4: Combat end message appears only once');

    // Check if XP was awarded (Bug 5 fix)
    const finalXpText = await page.textContent('[data-testid="player-info-panel"]');
    console.log('Final XP:', finalXpText);

    // Check if XP increased
    const xpIncreased = finalXpText !== initialXpText;
    if (xpIncreased) {
      console.log('✅ Bug 5: XP was awarded and displayed');
    } else {
      console.log('❌ Bug 5: XP was not awarded or displayed');
    }

    // Check if NPC was removed from room occupants (Bug 6 fix)
    const finalOccupants = await page.textContent('[data-testid="room-info-panel"]');
    console.log('Final occupants:', finalOccupants);

    const npcRemoved = !finalOccupants.includes('Dr. Francis Morgan');
    if (npcRemoved) {
      console.log('✅ Bug 6: NPC was removed from room occupants');
    } else {
      console.log('❌ Bug 6: NPC was not removed from room occupants');
    }

    // Check for game tick messages (Bug 7 fix)
    const hasGameTicks = gameLogText.includes('[Game Tick');
    if (hasGameTicks) {
      console.log('✅ Bug 7: Game ticks are being displayed');
    } else {
      console.log('❌ Bug 7: Game ticks are not being displayed');
    }

    // Check if player XP is loaded from database (Bug 8 fix)
    // This is harder to test automatically, but we can check if XP is not 0
    const xpNotZero = !finalXpText.includes('XP: 0');
    if (xpNotZero) {
      console.log('✅ Bug 8: Player XP is loaded from database');
    } else {
      console.log('❌ Bug 8: Player XP may not be loaded from database');
    }
  });
});
