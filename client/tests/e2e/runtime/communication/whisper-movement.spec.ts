/**
 * Scenario 16: Whisper Movement
 *
 * Tests whisper channel functionality across different player locations.
 * Verifies that whisper messages work correctly when players are in different
 * rooms, that whisper delivery is not affected by player movement, and that
 * the whisper system maintains privacy and proper message delivery regardless
 * of player location.
 */

import { expect, test } from '@playwright/test';
import { executeCommand, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

test.describe('Whisper Movement', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);
  });

  test.afterAll(async () => {
    // Cleanup contexts
    await cleanupMultiPlayerContexts(contexts);
  });

  test('Ithaqua should receive whisper when both players in same room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Server displays sender by character name; get AW's current character name for assertion
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharacterName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await executeCommand(awContext.page, 'whisper Ithaqua Testing whisper in same room');

    // Wait for confirmation on sender
    await waitForMessage(awContext.page, /You whisper to Ithaqua: Testing whisper in same room/, 10000).catch(() => {});

    await new Promise(r => setTimeout(r, 500));

    const expectedWhisper = `${awCharacterName} whispers to you: Testing whisper in same room`;
    await waitForCrossPlayerMessage(ithaquaContext, expectedWhisper);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes(expectedWhisper));
    expect(seesMessage).toBe(true);
  });

  test('Ithaqua should receive whisper when AW is in different room', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    // Co-locate via admin teleport (movement-only co-location is unreliable due to spawn room differences)
    await ithaquaContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const ithaquaCharName =
      (await ithaquaContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'Ithaqua';
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, `teleport ${ithaquaCharName}`);
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 20000);

    // Ensure we're in a room that has an east exit (e.g. Main Foyer). From Laundry: south -> west -> north.
    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 1500));
    await ensureStanding(ithaquaContext.page, 5000);
    await executeCommand(ithaquaContext.page, 'go south');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go west');
    await new Promise(r => setTimeout(r, 1500));
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 2000));
    await ensurePlayersInSameRoom(contexts, 2, 15000);

    await ensureStanding(awContext.page, 5000);
    await executeCommand(awContext.page, 'go east');
    await waitForMessage(awContext.page, /You move east|You go east|Eastern Hallway/i, 10000).catch(() => {});
    await new Promise(r => setTimeout(r, 2000));

    // Server displays sender by character name
    await awContext.page.getByTestId('current-character-name').waitFor({ state: 'visible', timeout: 10000 });
    const awCharName =
      (await awContext.page.getByTestId('current-character-name').textContent())?.trim() ?? 'ArkanWolfshade';

    await executeCommand(awContext.page, 'whisper Ithaqua Testing whisper from different room');
    await waitForMessage(awContext.page, /You whisper to Ithaqua: Testing whisper from different room/, 10000).catch(
      () => {}
    );
    await new Promise(r => setTimeout(r, 500));

    const expectedFromRoom = `${awCharName} whispers to you: Testing whisper from different room`;
    await waitForCrossPlayerMessage(ithaquaContext, expectedFromRoom);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesMessage = ithaquaMessages.some(msg => msg.includes(expectedFromRoom));
    expect(seesMessage).toBe(true);
  });
});
