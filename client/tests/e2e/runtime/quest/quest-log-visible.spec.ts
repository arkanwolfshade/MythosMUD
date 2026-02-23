/**
 * Scenario 42: Quest log (Journal panel) visible after login.
 *
 * E2E test for quest subsystem: after login and entering the game, the Journal panel
 * is visible and shows either the quest log header/list or the empty state.
 */

import { expect, test } from '@playwright/test';
import { loginPlayer } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

test.describe('Quest log visible after login', () => {
  test('Journal panel shows quest log content or empty state after game load', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');

    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await page
      .getByTestId('current-character-name')
      .waitFor({ state: 'visible', timeout: 15000 })
      .catch(() => {});

    // Journal panel is in default layout (title "Journal"); body shows either
    // "Quest log" (header when entries exist) or "You have no active or completed quests."
    const questLogHeader = page.getByText('Quest log', { exact: true });
    const emptyState = page.getByText('You have no active or completed quests.');
    await expect(questLogHeader.or(emptyState)).toBeVisible({ timeout: TEST_TIMEOUTS.GAME_LOAD });
  });
});
