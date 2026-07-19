/**
 * Panel minimize dock (issue #170): minimize to bottom tray, restore prior layout.
 */

import { expect, test, type Locator, type Page } from '@playwright/test';
import { loginPlayer } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

const PANEL_LAYOUT_STORAGE_KEY = 'mythosmud-ui-v2-panel-layout';
const MINIMIZED_BAR_HEIGHT = 40;
const DOCK_BOTTOM_PADDING = 8;

async function waitForGameReady(page: Page): Promise<void> {
  await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
  await page.getByTestId('game-panel-chatHistory').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
}

async function panelBottomEdge(page: Page, panel: Locator): Promise<number> {
  const box = await panel.boundingBox();
  expect(box).not.toBeNull();
  return box!.y + box!.height;
}

test.describe('Panel minimize dock', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(key => {
      localStorage.removeItem(key);
    }, PANEL_LAYOUT_STORAGE_KEY);
  });

  test('minimizes Chat History to bottom dock and restores expanded layout', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await waitForGameReady(page);

    const chatPanel = page.getByTestId('game-panel-chatHistory');
    await expect(chatPanel).toHaveAttribute('data-panel-minimized', 'false');

    const expandedBox = await chatPanel.boundingBox();
    expect(expandedBox).not.toBeNull();
    expect(expandedBox!.height).toBeGreaterThan(100);

    await page.getByTestId('game-panel-chatHistory-minimize').click();

    await expect(chatPanel).toHaveAttribute('data-panel-minimized', 'true');
    await expect(chatPanel.getByText('Chat', { exact: true })).toHaveCount(0);

    const minimizedBox = await chatPanel.boundingBox();
    expect(minimizedBox).not.toBeNull();
    expect(minimizedBox!.height).toBeLessThanOrEqual(MINIMIZED_BAR_HEIGHT + 4);

    const viewportHeight = page.viewportSize()?.height ?? 720;
    const bottomEdge = await panelBottomEdge(page, chatPanel);
    expect(bottomEdge).toBeGreaterThanOrEqual(viewportHeight - DOCK_BOTTOM_PADDING - 4);

    await page.getByTestId('game-panel-chatHistory-restore').click();

    await expect(chatPanel).toHaveAttribute('data-panel-minimized', 'false');
    await expect(chatPanel.getByText('Chat', { exact: true })).toBeVisible();

    const restoredBox = await chatPanel.boundingBox();
    expect(restoredBox).not.toBeNull();
    expect(restoredBox!.height).toBeGreaterThan(100);
    expect(Math.abs(restoredBox!.y - expandedBox!.y)).toBeLessThanOrEqual(8);
  });

  test('stacks multiple minimized panels along the bottom dock', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await waitForGameReady(page);

    await page.getByTestId('game-panel-gameInfo-minimize').click();
    await page.getByTestId('game-panel-chatHistory-minimize').click();

    const chatPanel = page.getByTestId('game-panel-chatHistory');
    const gameInfoPanel = page.getByTestId('game-panel-gameInfo');

    await expect(chatPanel).toHaveAttribute('data-panel-minimized', 'true');
    await expect(gameInfoPanel).toHaveAttribute('data-panel-minimized', 'true');

    const chatBox = await chatPanel.boundingBox();
    const infoBox = await gameInfoPanel.boundingBox();
    expect(chatBox).not.toBeNull();
    expect(infoBox).not.toBeNull();

    expect(chatBox!.x).toBeLessThan(infoBox!.x);
    expect(Math.abs(chatBox!.y - infoBox!.y)).toBeLessThanOrEqual(4);

    const viewportHeight = page.viewportSize()?.height ?? 720;
    expect(await panelBottomEdge(page, chatPanel)).toBeGreaterThanOrEqual(viewportHeight - DOCK_BOTTOM_PADDING - 4);
    expect(await panelBottomEdge(page, gameInfoPanel)).toBeGreaterThanOrEqual(viewportHeight - DOCK_BOTTOM_PADDING - 4);
  });
});
