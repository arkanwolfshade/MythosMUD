import { Page, expect, test } from '@playwright/test';

// Local utilities mirrored from occupants-two-client.spec.ts
async function installRealtimeFakes(page: Page) {
  await page.addInitScript(() => {
    // Fake EventSource allowing tests to emit events
    class FakeEventSource {
      url: string;
      onopen: ((ev: unknown) => void) | null = null;
      onmessage: ((ev: { data: string }) => void) | null = null;
      onerror: ((ev: unknown) => void) | null = null;
      constructor(url: string) {
        this.url = url;
        interface WindowWithFakes extends Window {
          __fakeSSEs: FakeEventSource[];
        }
        const w = window as unknown as WindowWithFakes;
        w.__fakeSSEs = w.__fakeSSEs || [];
        w.__fakeSSEs.push(this);
        setTimeout(() => {
          if (this.onopen) this.onopen({});
        }, 0);
      }
      emit(payload: unknown) {
        if (this.onmessage) this.onmessage({ data: JSON.stringify(payload) });
      }
      close() {}
    }
    (window as unknown as { EventSource: unknown }).EventSource = FakeEventSource as unknown as typeof EventSource;

    // Fake WebSocket that immediately opens and captures sends
    class FakeWebSocket {
      url: string;
      readyState = 1; // OPEN
      onopen: ((ev: unknown) => void) | null = null;
      onmessage: ((ev: { data: string }) => void) | null = null;
      onerror: ((ev: unknown) => void) | null = null;
      onclose: ((ev: unknown) => void) | null = null;
      constructor(url: string) {
        this.url = url;
        interface WindowWithWS extends Window {
          __fakeWS: FakeWebSocket[];
        }
        const w = window as unknown as WindowWithWS;
        w.__fakeWS = w.__fakeWS || [];
        w.__fakeWS.push(this);
        setTimeout(() => {
          if (this.onopen) this.onopen({});
        }, 0);
      }
      send(_data: string) {}
      close() {
        this.readyState = 3; // CLOSED
        if (this.onclose) this.onclose({});
      }
    }
    (window as unknown as { WebSocket: unknown }).WebSocket = FakeWebSocket as unknown as typeof WebSocket;
  });
}

async function loginWithMock(page: Page, username: string) {
  // Mock login response
  await page.route('**/api/auth/login', async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ access_token: 'test-token', user_id: `${username}-id` }),
    });
  });

  await page.goto('/');
  await expect(page.locator('h1')).toContainText('MythosMUD');

  await page.getByLabel('Username:').fill(username);
  await page.getByLabel('Password:').fill('irrelevant');
  await page.getByRole('button', { name: 'Enter the MUD' }).click();

  // Wait for the terminal view
  await page.waitForSelector('.game-terminal');
}

test.describe('Room occupants - initial population and updates for second client', () => {
  test('second client shows existing occupant on join; updates on leave/re-enter', async ({ browser }) => {
    // Client A (ArkanWolfshade)
    const contextA = await browser.newContext();
    const pageA = await contextA.newPage();
    await installRealtimeFakes(pageA);
    await loginWithMock(pageA, 'ArkanWolfshade');
    await pageA.getByRole('button', { name: 'Connect to Game' }).click();
    await pageA.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Client B (Ithaqua)
    const contextB = await browser.newContext();
    const pageB = await contextB.newPage();
    await installRealtimeFakes(pageB);
    await loginWithMock(pageB, 'Ithaqua');
    await pageB.getByRole('button', { name: 'Connect to Game' }).click();
    await pageB.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    const baseRoom = {
      id: 'earth_arkham_city_downtown_001',
      name: 'Downtown Arkham',
      description: 'Streets of Arkham.',
      zone: 'arkham_city',
      sub_zone: 'downtown',
      exits: { north: '...', south: '...' },
    } as const;

    // A first: initial state shows no other occupants
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        data: { player: { name: 'ArkanWolfshade' }, room, occupants: [] },
      });
    }, baseRoom);

    // B joins: initial game_state includes existing occupant (A)
    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        data: { player: { name: 'Ithaqua' }, room, occupants: ['ArkanWolfshade'] },
      });
    }, baseRoom);

    await expect(pageB.locator('.room-occupants .occupants-label')).toContainText('(1)');
    await expect(pageB.locator('.room-occupants .occupants-text')).toContainText('ArkanWolfshade');

    // B leaves: occupants should show None for B
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: [], count: 0 } });
    });
    await expect(pageB.locator('.room-occupants .occupants-label')).toContainText('(0)');
    await expect(pageB.locator('.room-occupants .occupants-text')).toContainText('None');

    // B re-enters: occupants should again list A
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: ['ArkanWolfshade'], count: 1 } });
    });
    await expect(pageB.locator('.room-occupants .occupants-label')).toContainText('(1)');
    await expect(pageB.locator('.room-occupants .occupants-text')).toContainText('ArkanWolfshade');

    await contextA.close();
    await contextB.close();
  });
});
