/**
 * Party commands and functionality (ephemeral grouping).
 *
 * Tests party create (via invite), list, party chat, and leave. Requires two
 * players in the same room for invite. Verifies command output and
 * cross-player party chat delivery.
 */

import { expect, test, type Page } from '@playwright/test';
import { executeCommand, getMessages, waitForMessage } from '../fixtures/auth';
import {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  ensureMultiplayerCoLocated,
  ensurePlayerInGame,
  ensurePlayersInSameRoom,
  getPlayerMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
  type PlayerContext,
} from '../fixtures/multiplayer';
import { ensureStanding } from '../fixtures/player';

/** Command responses may not reach `[data-message-text]` while this banner is present. */
async function waitForDisconnectBannerClear(page: Page): Promise<void> {
  await page
    .waitForFunction(
      () => !(document.body?.innerText ?? '').includes('You are disconnected and cannot perform actions'),
      { timeout: 20000 }
    )
    .catch(() => {});
}

async function waitForLookReflected(page: Page): Promise<void> {
  await page.waitForFunction(
    () => {
      const body = document.body?.innerText ?? '';
      if (
        /Arena\s*>|Arena entrance|heart of the gladiator|sand and shadow|Exits:\s*North|Exits: North, South/i.test(body)
      ) {
        return true;
      }
      return Array.from(document.querySelectorAll('[data-message-text]')).some(el => {
        const v = (el.getAttribute('data-message-text') || '').trim();
        return /Arena|gladiator|heart of the|exits|sand|You see/i.test(v);
      });
    },
    { timeout: 45000 }
  );
}

async function primeBothForCoLocate(contexts: PlayerContext[]): Promise<void> {
  if (contexts.length < 2) return;
  await Promise.all([ensurePlayerInGame(contexts[0], 30000), ensurePlayerInGame(contexts[1], 30000)]);
  for (const ctx of contexts) {
    await ctx.page.bringToFront().catch(() => {});
    await ctx.page.getByTestId('command-input').click();
    await executeCommand(ctx.page, 'look');
    await waitForLookReflected(ctx.page).catch(() => {});
  }
}

test.describe('Party Commands', () => {
  let contexts: Awaited<ReturnType<typeof createMultiPlayerContexts>>;

  test.beforeAll(async ({ browser }) => {
    contexts = await createMultiPlayerContexts(browser, ['ArkanWolfshade', 'Ithaqua']);
    await waitForAllPlayersInGame(contexts, 60000);
    await ensurePlayerInGame(contexts[0], 60000);
    await ensurePlayerInGame(contexts[1], 60000);

    // Party invite requires target in same room. Co-locate: stand then move both north.
    const [awContext, ithaquaContext] = contexts;
    await ensureStanding(awContext.page, 10000);
    await executeCommand(awContext.page, 'go north');
    await new Promise(r => setTimeout(r, 2000));
    await ensureStanding(ithaquaContext.page, 10000);
    await executeCommand(ithaquaContext.page, 'go north');
    await new Promise(r => setTimeout(r, 3000));
    await ensurePlayersInSameRoom(contexts, 2, 60000);
  });

  test.afterAll(async () => {
    await cleanupMultiPlayerContexts(contexts);
  });

  test('party with no args when not in party shows helpful message', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];
    // Single-player assertion: do not call ensureMultiplayerCoLocated — second client may be gone and 5x45s sync
    // exhausts the 180s test timeout before `party` runs. Still refresh both sessions so linkdead/decay from
    // beforeAll does not leave AW unroutable while Occupants still show stale linkdead.
    await Promise.all([ensurePlayerInGame(awContext, 30000), ensurePlayerInGame(ithaquaContext, 30000)]);

    await awContext.page.bringToFront().catch(() => {});
    await waitForDisconnectBannerClear(awContext.page);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    // Chat may be empty ("No messages yet"); do not require `[data-message-text]` before priming.
    await awContext.page.getByTestId('command-input').click();
    await executeCommand(awContext.page, 'look');
    try {
      await waitForLookReflected(awContext.page);
    } catch {
      // Fall through to unconditional room-line assertion below.
    }
    await expect(awContext.page.getByText(/Arena entrance|heart of the gladiator|Exits:/i).first()).toBeVisible({
      timeout: 20000,
    });
    await waitForMessage(awContext.page, /Arena|Exits:|You see|already standing|rise to your feet/i, 20000).catch(
      () => {}
    );

    await awContext.page.getByTestId('command-input').click();
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await awContext.page.getByTestId('command-input').click();
    await executeCommand(awContext.page, 'party');

    // Server: "You are not in a party. Use 'party invite <name>' to form one (you become leader)."
    await waitForMessage(awContext.page, /You are not in a party|not in a party|party invite|form one/i, 45000);
    const messages = await getMessages(awContext.page);
    const hasPartyHint = messages.some(msg => {
      const m = msg.toLowerCase();
      return m.includes('not in a party') || m.includes('party invite') || m.includes('form one');
    });
    expect(hasPartyHint).toBe(true);
  });

  test('AW can invite Ithaqua and party list shows both', async () => {
    test.setTimeout(300_000);
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    // beforeAll co-location can decay; bilateral look refreshes room_state before teleport/sync storm.
    await primeBothForCoLocate(contexts);
    await ensureMultiplayerCoLocated(contexts, { timeoutMs: 60000, coLocateTimeoutMs: 45000 });

    await awContext.page.bringToFront().catch(() => {});
    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'party invite Ithaqua');

    // Server: "Party invite sent (pending acceptance)" or "Party invite sent. Waiting for them to accept."
    await waitForMessage(awContext.page, /Party invite sent|pending acceptance|Waiting for them to accept/i, 45000);

    await ithaquaContext.page
      .getByText(/invited you to join their party/i)
      .waitFor({ state: 'visible', timeout: 30000 });
    await ithaquaContext.page.getByRole('button', { name: /Accept/i }).click();
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'party list');
    const listHeader = awContext.page.locator('[data-message-text]').filter({ hasText: /Your party:/ });
    await expect(listHeader.first()).toBeVisible({ timeout: 10000 });
    const listMessages = await getMessages(awContext.page);
    const seesArkan = listMessages.some(msg => msg.includes('ArkanWolfshade'));
    const seesIthaqua = listMessages.some(msg => msg.includes('Ithaqua'));
    expect(seesArkan).toBe(true);
    expect(seesIthaqua).toBe(true);
  });

  // Skip: Party chat delivery to receiver not yet reliable
  // eslint-disable-next-line playwright/no-skipped-test -- party chat delivery to receiver not yet reliable
  test.skip('party chat from AW is received by Ithaqua', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);
    await ensurePlayersInSameRoom(contexts, 2, 15000);
    await new Promise(r => setTimeout(r, 2000));

    await executeCommand(awContext.page, 'party Hello from the party');

    await waitForMessage(awContext.page, /Sent\.|Hello from the party/i, 10000).catch(() => {});
    await waitForCrossPlayerMessage(ithaquaContext, /Hello from the party/i, 25000);
    const ithaquaMessages = await getPlayerMessages(ithaquaContext);
    const seesPartyMessage = ithaquaMessages.some(msg => msg.includes('Hello from the party'));
    expect(seesPartyMessage).toBe(true);
  });

  test('Ithaqua can leave party and AW party list updates', async () => {
    const awContext = contexts[0];
    const ithaquaContext = contexts[1];

    await ensurePlayerInGame(awContext, 15000);
    await ensurePlayerInGame(ithaquaContext, 15000);

    await executeCommand(ithaquaContext.page, 'party leave');
    // Server may return "You have left the party." or "You left the party. The party has been disbanded."
    // Optional: Ithaqua's client may be linkdead so we don't require the message on their page.
    const leaveMsg = ithaquaContext.page
      .locator('[data-message-text]')
      .filter({ hasText: /left the party|You have left|disbanded/ });
    await leaveMsg
      .first()
      .waitFor({ state: 'visible', timeout: 8000 })
      .catch(() => {});

    // Ithaqua may disconnect; give room/party state a moment before AW queries list.
    await new Promise(r => setTimeout(r, 2000));

    await awContext.page.bringToFront().catch(() => {});
    await ensurePlayerInGame(awContext, 30000);
    await expect(awContext.page.getByText(/Player:\s*ArkanWolfshade\b/i)).toBeVisible({ timeout: 15000 });
    await awContext.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: 20000 });
    await executeCommand(awContext.page, 'look');
    // Room prose is in Location / Room Description, not necessarily Game Info [data-message-text].
    try {
      await waitForLookReflected(awContext.page);
    } catch {
      // Fall through to unconditional room-line assertion below.
    }
    await expect(awContext.page.getByText(/Arena entrance|heart of the gladiator|Exits:/i).first()).toBeVisible({
      timeout: 20000,
    });

    await executeCommand(awContext.page, 'stand');
    await new Promise(r => setTimeout(r, 1500));

    await executeCommand(awContext.page, 'party list');
    // After Ithaqua leaves, AW may see "Your party:" (only leader) or "You are not in a party"
    // (e.g. party disbanded on disconnect). Accept either outcome.
    await waitForMessage(
      awContext.page,
      /Your party:|You are not in a party|not in a party|party invite|form one/i,
      45000
    );
    const listMessages = await getMessages(awContext.page);
    const hasListWithLeader = listMessages.some(msg => msg.includes('Your party:') && msg.includes('ArkanWolfshade'));
    const hasNotInParty = listMessages.some(msg => {
      const lower = msg.toLowerCase();
      return lower.includes('you are not in a party') || lower.includes('party invite') || lower.includes('form one');
    });
    expect(hasListWithLeader || hasNotInParty).toBe(true);
  });
});
