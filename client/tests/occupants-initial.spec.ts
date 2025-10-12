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

test.describe('Room occupants - initial population and updates for second client', () => {
  test('second client shows existing occupant on join; updates on leave/re-enter', async ({ browser }) => {
    // Client A (ArkanWolfshade)
    const contextA = await browser.newContext();
    const pageA = await contextA.newPage();
    await installRealtimeFakes(pageA);
    await loginWithMock(pageA, 'ArkanWolfshade');

    // Wait for connection to be established (handled automatically by useGameConnection)
    await pageA.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    // Client B (Ithaqua)
    const contextB = await browser.newContext();
    const pageB = await contextB.newPage();
    await installRealtimeFakes(pageB);
    await loginWithMock(pageB, 'Ithaqua');

    // Wait for connection to be established (handled automatically by useGameConnection)
    await pageB.waitForFunction(() => {
      const w = window as unknown as { __fakeSSEs?: unknown[] };
      return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0;
    });

    const baseRoom = {
      id: 'earth_arkhamcity_downtown_001',
      name: 'Downtown Arkham',
      description: 'Streets of Arkham.',
      zone: 'arkhamcity',
      sub_zone: 'downtown',
      exits: { north: '...', south: '...' },
    } as const;

    // A first: initial state shows no other occupants
    await pageA.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      // Create room data with no other occupants initially
      const roomWithOccupants = {
        ...room,
        occupants: [],
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'ArkanWolfshade' },
          room: roomWithOccupants,
        },
      });
    }, baseRoom);

    // B joins: initial game_state includes existing occupant (A)
    await pageB.evaluate(room => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      // Create room data with the expected occupants (including current player)
      const roomWithOccupants = {
        ...room,
        occupants: ['ArkanWolfshade', 'Ithaqua'], // Include both players
        occupant_count: 2,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 2, // Use sequence 2 for player B
        data: {
          player: { name: 'Ithaqua' },
          room: roomWithOccupants,
        },
      });
    }, baseRoom);

    // Wait for the event to be processed
    await pageB.waitForTimeout(500);

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('2');
    await expect(pageB.locator('.room-occupants .occupant-name')).toHaveCount(2);
    await expect(pageB.locator('.room-occupants .occupant-name').first()).toContainText('Arkanwolfshade');
    await expect(pageB.locator('.room-occupants .occupant-name').nth(1)).toContainText('Ithaqua');

    // B leaves: occupants should show None for B
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      // Send game_state event with only current player (others left)
      const roomWithNoOccupants = {
        id: 'earth_arkhamcity_downtown_001',
        name: 'Downtown Arkham',
        description: 'Streets of Arkham.',
        zone: 'arkham',
        sub_zone: 'downtown',
        exits: { north: '...', south: '...' },
        occupants: ['Ithaqua'], // Only current player remains
        occupant_count: 1,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 3, // Use sequence 3 for leave event
        data: {
          player: { name: 'Ithaqua' },
          room: roomWithNoOccupants,
        },
      });
    });

    // Wait for the leave event to be processed
    await pageB.waitForTimeout(500);

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('1');
    await expect(pageB.locator('.room-occupants .occupant-name')).toHaveCount(1);
    await expect(pageB.locator('.room-occupants .occupant-name').first()).toContainText('Ithaqua');

    // B re-enters: occupants should again list A
    await pageB.evaluate(() => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      // Send game_state event with occupant back
      const roomWithOccupant = {
        id: 'earth_arkhamcity_downtown_001',
        name: 'Downtown Arkham',
        description: 'Streets of Arkham.',
        zone: 'arkham',
        sub_zone: 'downtown',
        exits: { north: '...', south: '...' },
        occupants: ['ArkanWolfshade', 'Ithaqua'], // Both players back
        occupant_count: 2,
      };
      w.__fakeSSEs[0].emit({
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 4, // Use sequence 4 for re-enter event
        data: {
          player: { name: 'Ithaqua' },
          room: roomWithOccupant,
        },
      });
    });

    // Wait for the re-enter event to be processed
    await pageB.waitForTimeout(500);

    await expect(pageB.locator('.room-occupants .occupant-count-badge')).toContainText('2');
    await expect(pageB.locator('.room-occupants .occupant-name')).toHaveCount(2);
    await expect(pageB.locator('.room-occupants .occupant-name').first()).toContainText('Arkanwolfshade');
    await expect(pageB.locator('.room-occupants .occupant-name').nth(1)).toContainText('Ithaqua');

    await contextA.close();
    await contextB.close();
  });
});
