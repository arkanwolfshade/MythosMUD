/**
 * Panel routing contract (#672): `look` output must be visible in the Game Info panel.
 *
 * #672 reported `look` producing no visible feedback in Game Info; investigation found the
 * routing (`handleCommandResponse` / `command_response` projector handler) already correct —
 * this spec locks the observable contract in E2E so the routing cannot silently regress.
 */

import { expect, test } from '@playwright/test';
import { ensurePlayableConnection, executeCommand, loginPlayer } from '../fixtures/auth';
import { DEFAULT_SPAWN_LOOK_CUE, TEST_TIMEOUTS } from '../fixtures/test-data';

test.describe('look command routes to Game Info', () => {
  test('look output appears in the Game Info panel', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });

    await executeCommand(page, 'look');

    const gameInfoPanel = page.getByTestId('game-panel-gameInfo');
    await expect(gameInfoPanel.getByText(DEFAULT_SPAWN_LOOK_CUE)).toBeVisible({ timeout: 25000 });
  });
});
