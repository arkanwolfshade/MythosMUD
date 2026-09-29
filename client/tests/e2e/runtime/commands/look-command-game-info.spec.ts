/**
 * Panel routing contract (#672): `look` output must be visible in the Game Info panel.
 *
 * #672 reported `look` producing no visible feedback in Game Info; investigation found the
 * routing (`handleCommandResponse` / `command_response` projector handler) already correct —
 * this spec locks the observable contract in E2E so the routing cannot silently regress.
 */

import { expect, test } from '@playwright/test';
import { ensurePlayableConnection, executeCommand, loginPlayer } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

test.describe('look command routes to Game Info', () => {
  test('look output appears in the Game Info panel', async ({ page }) => {
    await loginPlayer(page, 'ArkanWolfshade', 'Cthulhu1');
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await ensurePlayableConnection(page, {
      username: 'ArkanWolfshade',
      password: 'Cthulhu1',
      timeoutMs: 45000,
    });

    // Room-agnostic (#916): earlier specs leave the character in arbitrary rooms, and the #672 contract
    // is only that look output reaches Game Info. Every room description ends with an "Exits:" line, so
    // wait for a new one to appear after `look`.
    const exitsLines = page.getByTestId('game-panel-gameInfo').getByText(/Exits:/i);
    const before = await exitsLines.count();

    await executeCommand(page, 'look');

    await expect.poll(() => exitsLines.count(), { timeout: 25000 }).toBeGreaterThan(before);
  });
});
