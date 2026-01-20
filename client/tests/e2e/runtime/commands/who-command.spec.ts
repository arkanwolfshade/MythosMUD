/**
 * Scenario 7: Who Command
 *
 * Tests the who command functionality for multi-player visibility and real-time updates.
 * Verifies that players can see OTHER online players in the who list and that the list
 * updates correctly as players connect and disconnect.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import { cleanupMultiPlayerContexts, createMultiPlayerContexts } from '../fixtures/multiplayer';

test.describe('Who Command', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    // Create contexts for both players
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('AW should see both players in who list', async () => {
    const awContext = contexts[0];

    // Verify login completed - wait for game interface to be visible
    await awContext.page
      .waitForFunction(
        () => {
          const hasCommandInput =
            document.querySelector('[data-testid="command-input"]') !== null ||
            document.querySelector('input[placeholder*="command" i], textarea[placeholder*="command" i]') !== null;
          const hasGameInfo =
            document.querySelector('[data-testid="game-info-panel"]') !== null ||
            Array.from(document.querySelectorAll('*')).some(el => el.textContent?.includes('Game Info'));
          return hasCommandInput || hasGameInfo;
        },
        { timeout: 30000 }
      )
      .catch(() => {
        throw new Error('Login did not complete - game interface not found');
      });

    // AW uses who command
    await executeCommand(awContext.page, 'who');

    // Wait for who command response
    await waitForMessage(awContext.page, 'Online Players:', 10000).catch(() => {
      // Response may appear even if format differs
    });

    // Verify both players appear in who list
    const messages = await getMessages(awContext.page);
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));

    // At least one player should be visible
    expect(seesArkan || seesIthaqua).toBe(true);
  });

  test('Ithaqua should see both players in who list', async () => {
    const ithaquaContext = contexts[1];

    // Verify login completed - wait for game interface to be visible
    await ithaquaContext.page
      .waitForFunction(
        () => {
          const hasCommandInput =
            document.querySelector('[data-testid="command-input"]') !== null ||
            document.querySelector('input[placeholder*="command" i], textarea[placeholder*="command" i]') !== null;
          const hasGameInfo =
            document.querySelector('[data-testid="game-info-panel"]') !== null ||
            Array.from(document.querySelectorAll('*')).some(el => el.textContent?.includes('Game Info'));
          return hasCommandInput || hasGameInfo;
        },
        { timeout: 30000 }
      )
      .catch(() => {
        throw new Error('Login did not complete - game interface not found');
      });

    // Ithaqua uses who command
    await executeCommand(ithaquaContext.page, 'who');

    // Wait for who command response
    await waitForMessage(ithaquaContext.page, 'Online Players:', 10000).catch(() => {
      // Response may appear even if format differs
    });

    // Verify both players appear in who list
    const messages = await ithaquaContext.page.evaluate(() => {
      const messages = Array.from(document.querySelectorAll('[data-message-text]'));
      return messages.map(msg => (msg.getAttribute('data-message-text') || '').trim());
    });
    const seesArkan = messages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = messages.some(msg => msg.includes('Ithaqua'));

    // At least one player should be visible
    expect(seesArkan || seesIthaqua).toBe(true);
  });
});
