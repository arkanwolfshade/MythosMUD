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
  // Mock login response with proper format
  await page.route('**/auth/login', async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        access_token: 'test-token',
        has_character: true,
        character_name: username,
        refresh_token: 'test-refresh-token',
      }),
    });
  });

  // Mock MOTD response
  await page.route('**/api/motd', async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        title: 'Welcome to MythosMUD',
        content: 'Welcome to the realm of eldritch knowledge...',
      }),
    });
  });

  await page.goto('/');
  await expect(page.locator('h1')).toContainText('MythosMUD');

  await page.getByPlaceholder('Username').fill(username);
  await page.getByPlaceholder('Password').fill('irrelevant');
  await page.getByRole('button', { name: 'Enter the Void' }).click();

  // Wait for MOTD screen and click Continue
  await page.waitForSelector('text=Continue', { timeout: 10000 });
  await page.getByRole('button', { name: 'Continue' }).click();

  // Wait for the terminal view
  await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });
}

test.describe('Room occupants - two clients', () => {
  test('updates occupant lists and counts across two clients', async ({ browser }) => {
    // Client A (Alice)
    const contextA = await browser.newContext();
    const pageA = await contextA.newPage();
    await installRealtimeFakes(pageA);
    await loginWithMock(pageA, 'Alice');

    // Wait for connection to be established (handled automatically by useGameConnection)
    await pageA.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Client B (Bob)
    const contextB = await browser.newContext();
    const pageB = await contextB.newPage();
    await installRealtimeFakes(pageB);
    await loginWithMock(pageB, 'Bob');

    // Wait for connection to be established (handled automatically by useGameConnection)
    await pageB.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Send initial game_state (empty occupants) to both clients
    const baseRoom = {
      id: 'earth_arkhamcity_downtown_001',
      name: 'Downtown Arkham',
      description: 'Streets of Arkham.',
      zone: 'arkhamcity',
      sub_zone: 'downtown',
      exits: { north: '...', south: '...' },
    };

    // Send initial game_state to both clients
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithOccupants = {
        ...room,
        occupants: ['Alice'], // Only current player initially
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'Alice' },
          room: roomWithOccupants,
        },
      });
    }, baseRoom);

    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithOccupants = {
        ...room,
        occupants: ['Bob'], // Only current player initially
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'Bob' },
          room: roomWithOccupants,
        },
      });
    }, baseRoom);

    // Now simulate both players being in the room
    // Alice receives updated room with Bob present
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithBothOccupants = {
        ...room,
        occupants: ['Alice', 'Bob'], // Both players present
        occupant_count: 2,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          player: { name: 'Alice' },
          room: roomWithBothOccupants,
        },
      });
    }, baseRoom);

    // Bob receives updated room with Alice present
    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithBothOccupants = {
        ...room,
        occupants: ['Alice', 'Bob'], // Both players present
        occupant_count: 2,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          player: { name: 'Bob' },
          room: roomWithBothOccupants,
        },
      });
    }, baseRoom);

    // Wait for events to be processed
    await pageA.waitForTimeout(500);
    await pageB.waitForTimeout(500);

    // Verify RoomInfoPanel shows names and counts for both players
    await expect(pageA.locator('.room-occupants .occupant-count-badge')).toContainText('2');
    await expect(pageA.locator('.room-occupants .occupant-name')).toHaveCount(2);
    await expect(pageA.locator('.room-occupants .occupant-name').first()).toContainText('Alice');
    await expect(pageA.locator('.room-occupants .occupant-name').nth(1)).toContainText('Bob');

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('2');
    await expect(pageB.locator('.room-occupants .occupant-name')).toHaveCount(2);
    await expect(pageB.locator('.room-occupants .occupant-name').first()).toContainText('Alice');
    await expect(pageB.locator('.room-occupants .occupant-name').nth(1)).toContainText('Bob');

    // Simulate Bob leaving: only Alice remains
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithOnlyAlice = {
        ...room,
        occupants: ['Alice'], // Only Alice remains
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          player: { name: 'Alice' },
          room: roomWithOnlyAlice,
        },
      });
    }, baseRoom);

    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      const roomWithOnlyBob = {
        ...room,
        occupants: ['Bob'], // Only Bob remains (from Bob's perspective)
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          player: { name: 'Bob' },
          room: roomWithOnlyBob,
        },
      });
    }, baseRoom);

    // Wait for events to be processed
    await pageA.waitForTimeout(500);
    await pageB.waitForTimeout(500);

    await expect(pageA.locator('.room-occupants .occupant-count-badge')).toContainText('1');
    await expect(pageA.locator('.room-occupants .occupant-name')).toHaveCount(1);
    await expect(pageA.locator('.room-occupants .occupant-name').first()).toContainText('Alice');

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('1');
    await expect(pageB.locator('.room-occupants .occupant-name')).toHaveCount(1);
    await expect(pageB.locator('.room-occupants .occupant-name').first()).toContainText('Bob');

    await contextA.close();
    await contextB.close();
  });
});
