import { Page, expect, test } from '@playwright/test';

// Utility to inject fake SSE and WebSocket before the app loads
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
          if (this.onopen) {
            this.onopen({});
          }
        }, 0);
      }
      emit(payload: unknown) {
        if (this.onmessage) {
          this.onmessage({ data: JSON.stringify(payload) });
        }
      }
      close() {}
    }
    {
      interface WindowWithEventSource extends Window {
        EventSource: typeof EventSource;
      }
      const w = window as unknown as WindowWithEventSource;
      // Assign our fake
      (w as unknown as { EventSource: unknown }).EventSource = FakeEventSource as unknown as typeof EventSource;
    }

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
          if (this.onopen) {
            this.onopen({});
          }
        }, 0);
      }
      send(_data: string) {}
      close() {
        this.readyState = 3; // CLOSED
        if (this.onclose) {
          this.onclose({});
        }
      }
    }
    {
      interface WindowWithWSAssign extends Window {
        WebSocket: typeof WebSocket;
      }
      const w = window as unknown as WindowWithWSAssign;
      (w as unknown as { WebSocket: unknown }).WebSocket = FakeWebSocket as unknown as typeof WebSocket;
    }
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

test.describe('Room occupants - two clients', () => {
  test('updates occupant lists and counts across two clients', async ({ browser }) => {
    // Client A (Alice)
    const contextA = await browser.newContext();
    const pageA = await contextA.newPage();
    await installRealtimeFakes(pageA);
    await loginWithMock(pageA, 'Alice');
    // Click Connect to create SSE/WebSocket connections
    await pageA.getByRole('button', { name: 'Connect to Game' }).click();
    await pageA.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Client B (Bob)
    const contextB = await browser.newContext();
    const pageB = await contextB.newPage();
    await installRealtimeFakes(pageB);
    await loginWithMock(pageB, 'Bob');
    await pageB.getByRole('button', { name: 'Connect to Game' }).click();
    await pageB.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Send initial game_state (empty occupants) to both clients
    const baseRoom = {
      id: 'earth_arkham_city_downtown_001',
      name: 'Downtown Arkham',
      description: 'Streets of Arkham.',
      zone: 'arkham_city',
      sub_zone: 'downtown',
      exits: { north: '...', south: '...' },
    };

    await pageA.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        data: { player: { name: 'Alice' }, room: {} as Record<string, never>, occupants: [] },
      });
    });
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'game_state', data: { player: { name: 'Alice' }, room, occupants: [] } });
    }, baseRoom);

    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'game_state', data: { player: { name: 'Bob' }, room, occupants: [] } });
    }, baseRoom);

    // Now simulate room_occupants broadcasts
    // Alice receives occupants [Bob]
    await pageA.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: ['Bob'], count: 1 } });
    });

    // Bob receives occupants [Alice]
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: ['Alice'], count: 1 } });
    });

    // Verify RoomInfoPanel shows names and counts
    await expect(pageA.locator('.room-occupants .occupant-count-badge')).toContainText('1');
    await expect(pageA.locator('.room-occupants .occupant-name')).toContainText('Bob');

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('1');
    await expect(pageB.locator('.room-occupants .occupant-name')).toContainText('Alice');

    // Simulate Bob leaving: occupants update to [] for Alice, and [] for Bob as well
    await pageA.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: [], count: 0 } });
    });
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      w.__fakeSSEs[0].emit({ event_type: 'room_occupants', data: { occupants: [], count: 0 } });
    });

    await expect(pageA.locator('.room-occupants .occupant-count-badge')).toContainText('0');
    await expect(pageA.locator('.room-occupants .no-occupants-text')).toContainText('No other players present');

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('0');
    await expect(pageB.locator('.room-occupants .no-occupants-text')).toContainText('No other players present');

    await contextA.close();
    await contextB.close();
  });
});
