import { Page } from '@playwright/test';

/**
 * Shared mock authentication utilities for integration tests
 * Provides consistent authentication mocking across all test scenarios
 *
 * Based on findings from "Authentication Patterns in Non-Euclidean Testing" - Dr. Armitage, 1928
 */

// Test credentials from MULTIPLAYER_TEST_RULES.md
export const TEST_CREDENTIALS = {
  PLAYER_1: {
    username: 'test_player_1',
    password: 'test_password_123',
    email: 'test1@example.com',
  },
  PLAYER_2: {
    username: 'test_player_2',
    password: 'test_password_123',
    email: 'test2@example.com',
  },
  ARKAN: {
    username: 'ArkanWolfshade',
    password: 'test_password_123',
    email: 'arkan@example.com',
  },
  ITHAQUA: {
    username: 'Ithaqua',
    password: 'test_password_123',
    email: 'ithaqua@example.com',
  },
} as const;

// Standard server URL
export const SERVER_URL = 'http://localhost:5173';

// Type alias for all test credentials
export type TestCredentials =
  | typeof TEST_CREDENTIALS.PLAYER_1
  | typeof TEST_CREDENTIALS.PLAYER_2
  | typeof TEST_CREDENTIALS.ARKAN
  | typeof TEST_CREDENTIALS.ITHAQUA;

// Mock route patterns
export const MOCK_ROUTES = {
  LOGIN: '**/auth/login',
  MOTD: '**/motd',
  GAME_STATE: '**/game/state',
  COMMANDS: '**/commands/**',
  CHAT: '**/chat/**',
  PLAYERS: '**/players/**',
} as const;

// Mock response generators
export const MOCK_RESPONSES = {
  /**
   * Generate a mock login response
   */
  login: (username: string) => ({
    access_token: `test-token-${username}-${Date.now()}`,
    has_character: true,
    character_name: username,
    refresh_token: `test-refresh-token-${username}`,
    token_type: 'bearer',
    expires_in: 3600,
  }),

  /**
   * Generate a mock MOTD response
   */
  motd: () => ({
    title: 'Welcome to MythosMUD',
    content:
      'You have entered a realm of forbidden knowledge. The air is thick with the scent of old parchment and something else... something that makes your skin crawl.',
    version: '1.0.0',
    server_name: 'Miskatonic University',
    timestamp: new Date().toISOString(),
  }),

  /**
   * Generate a mock game state response
   */
  gameState: (username: string, roomData?: { room: unknown; exits: unknown[] }) => ({
    player: {
      name: username,
      level: 1,
      health: 100,
      sanity: 100,
    },
    room: roomData || {
      id: 'earth_arkham_city_downtown_001',
      name: 'Downtown Arkham',
      description:
        'A fog-shrouded street in the heart of Arkham. Victorian buildings loom overhead, their windows dark and foreboding.',
      zone: 'arkham',
      sub_zone: 'city',
      exits: {
        north: 'arkham_university',
        south: 'arkham_harbor',
        east: 'arkham_cemetery',
        west: 'arkham_residential',
      },
      occupants: [username],
      occupant_count: 1,
    },
    timestamp: new Date().toISOString(),
    sequence_number: 1,
  }),

  /**
   * Generate a mock command response
   */
  command: (command: string, result: string) => ({
    command,
    result,
    timestamp: new Date().toISOString(),
    success: true,
  }),

  /**
   * Generate a mock movement command response
   */
  movement: (command: string, newRoom: { room: unknown; exits: unknown[] }) => ({
    command,
    result: `You move ${command.split(' ')[1]}.`,
    timestamp: new Date().toISOString(),
    success: true,
    room: newRoom,
  }),
} as const;

/**
 * Generate new room data for movement commands
 */
function generateNewRoomData(direction: string, username: string): { room: unknown; exits: unknown[] } {
  const roomNames = {
    north: 'Northern Chamber',
    south: 'Southern Hall',
    east: 'Eastern Corridor',
    west: 'Western Passage',
    up: 'Upper Level',
    down: 'Lower Level',
  };

  const roomDescriptions = {
    north: 'A dimly lit chamber to the north. Ancient symbols line the walls.',
    south: 'A grand hall extending southward. Dust motes dance in the air.',
    east: 'A narrow corridor stretching eastward. Your footsteps echo.',
    west: 'A winding passage leading west. Shadows gather in the corners.',
    up: 'An upper level accessible by stairs. The air feels thinner here.',
    down: 'A lower level accessible by stairs. The temperature drops noticeably.',
  };

  const roomId = `room_${direction}_${Date.now()}`;
  const roomName = roomNames[direction as keyof typeof roomNames] || `Room to the ${direction}`;
  const roomDescription =
    roomDescriptions[direction as keyof typeof roomDescriptions] || `You have moved ${direction}.`;

  return {
    id: roomId,
    name: roomName,
    description: roomDescription,
    zone: 'test-zone',
    sub_zone: 'test-subzone',
    exits: {
      north: direction === 'south' ? 'original-room' : null,
      south: direction === 'north' ? 'original-room' : null,
      east: direction === 'west' ? 'original-room' : null,
      west: direction === 'east' ? 'original-room' : null,
    },
    occupants: [username],
    occupant_count: 1,
  };
}

/**
 * Setup mock routes for authentication flow
 */
export async function setupMockRoutes(
  page: Page,
  username: string,
  roomData?: { room: unknown; exits: unknown[] }
): Promise<void> {
  // Mock login endpoint
  await page.route(MOCK_ROUTES.LOGIN, async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify(MOCK_RESPONSES.login(username)),
    });
  });

  // Mock MOTD endpoint
  await page.route(MOCK_ROUTES.MOTD, async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify(MOCK_RESPONSES.motd()),
    });
  });

  // Mock game state endpoint
  await page.route(MOCK_ROUTES.GAME_STATE, async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify(MOCK_RESPONSES.gameState(username, roomData)),
    });
  });

  // Mock command endpoints
  await page.route(MOCK_ROUTES.COMMANDS, async route => {
    const url = route.request().url();
    const command = url.split('/').pop() || 'unknown';

    // Handle movement commands specially
    if (command.startsWith('go ') || command.startsWith('move ')) {
      const direction = command.split(' ')[1];
      const newRoom = generateNewRoomData(direction, username);

      // Send command response through fake SSE
      await emitMockCommandResponse(page, command, `You move ${direction}.`);

      // Also emit game state update with new room
      await emitMockGameStateEvent(page, {
        player: {
          name: username,
          level: 1,
          health: 100,
          sanity: 100,
        },
        room: newRoom,
      });

      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(MOCK_RESPONSES.movement(command, newRoom)),
      });
    } else {
      // Send command response through fake SSE
      await emitMockCommandResponse(page, command, `Command executed: ${command}`);

      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(MOCK_RESPONSES.command(command, `Mock response for ${command}`)),
      });
    }
  });
}

/**
 * Standard mock authentication flow
 */
export async function loginWithMock(
  page: Page,
  credentials: TestCredentials,
  roomData?: { room: unknown; exits: unknown[] },
  allUsernames: string[] = []
): Promise<void> {
  // Use provided room data or generate with all usernames
  const finalRoomData =
    roomData || getStandardRoomData(allUsernames.length > 0 ? allUsernames : [credentials.username]);

  // Setup real-time fakes for SSE and WebSocket
  await installRealtimeFakes(page);

  // Setup mock routes
  await setupMockRoutes(page, credentials.username, finalRoomData);

  // Navigate to login page
  await page.goto(SERVER_URL);

  // Wait for login form
  await page.waitForSelector('input[placeholder="Username"]');

  // Fill login form
  await page.getByPlaceholder('Username').fill(credentials.username);
  await page.getByPlaceholder('Password').fill(credentials.password);

  // Submit login
  await page.getByRole('button', { name: 'Enter the Void' }).click();

  // No MOTD screen in current app flow - goes directly to game interface

  // Wait for game interface
  await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

  // Wait for real-time connection to be established and emit initial game state
  try {
    console.log('Setting up real-time connection for:', credentials.username);
    await waitForRealtimeConnection(page, credentials.username, finalRoomData);
    console.log('Real-time connection established successfully');
  } catch (error) {
    console.error('Error in waitForRealtimeConnection:', error);
    // Continue anyway - the connection might still work
  }

  // Wait for room info panel to load
  await page.waitForSelector('[data-testid="room-info-panel"]', { timeout: 5000 });
}

/**
 * Real authentication flow (for tests that need actual server)
 */
export async function loginWithRealCredentials(page: Page, credentials: TestCredentials): Promise<void> {
  // Navigate to login page
  await page.goto(SERVER_URL);

  // Wait for login form
  await page.waitForSelector('input[placeholder="Username"]');

  // Fill login form
  await page.getByPlaceholder('Username').fill(credentials.username);
  await page.getByPlaceholder('Password').fill(credentials.password);

  // Submit login
  await page.getByRole('button', { name: 'Enter the Void' }).click();

  // No MOTD screen in current app flow - goes directly to game interface

  // Wait for game interface
  await page.waitForSelector('[data-testid="game-terminal"]', { timeout: 15000 });

  // Wait for room info panel to load
  await page.waitForSelector('[data-testid="room-info-panel"]', { timeout: 10000 });

  // Wait additional time for room subscription to stabilize
  await page.waitForTimeout(3000);
}

/**
 * Setup real-time fakes for SSE and WebSocket
 */
export async function installRealtimeFakes(page: Page): Promise<void> {
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

      send(data: string) {
        // Capture sent data for testing
        console.log('Mock WebSocket send:', data);
      }

      close() {}
    }
    (window as unknown as { WebSocket: unknown }).WebSocket = FakeWebSocket as unknown as typeof WebSocket;
  });
}

/**
 * Wait for real-time connection to be established and emit initial game state
 */
export async function waitForRealtimeConnection(
  page: Page,
  username?: string,
  roomData?: { room: unknown; exits: unknown[] }
): Promise<void> {
  await page.waitForFunction(() => {
    const w = window as unknown as { __fakeSSEs?: unknown[]; __fakeWS?: unknown[] };
    return Array.isArray(w.__fakeSSEs) && w.__fakeSSEs.length > 0 && Array.isArray(w.__fakeWS) && w.__fakeWS.length > 0;
  });

  // Emit initial game state event if username and roomData are provided
  if (username && roomData) {
    const initialGameState = MOCK_RESPONSES.gameState(username, roomData);
    await emitMockGameStateEvent(page, initialGameState, 0);

    // Wait a bit for the event to be processed
    await page.waitForTimeout(500);
  }
}

/**
 * Emit a mock game state event
 */
export async function emitMockGameStateEvent(page: Page, eventData: unknown, eventIndex: number = 0): Promise<void> {
  await page.evaluate(
    ({ eventData, eventIndex }) => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      if (w.__fakeSSEs && w.__fakeSSEs[eventIndex]) {
        w.__fakeSSEs[eventIndex].emit({
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: Date.now(),
          data: eventData,
        });
      }
    },
    { eventData, eventIndex }
  );

  // Wait for UI to update
  await page.waitForTimeout(500);
}

/**
 * Emit a mock command response event
 */
export async function emitMockCommandResponse(
  page: Page,
  command: string,
  response: string,
  eventIndex: number = 0
): Promise<void> {
  await page.evaluate(
    ({ command, response, eventIndex }) => {
      const w = window as unknown as { __fakeSSEs: { emit: (payload: unknown) => void }[] };
      if (w.__fakeSSEs && w.__fakeSSEs[eventIndex]) {
        w.__fakeSSEs[eventIndex].emit({
          event_type: 'command_response',
          timestamp: new Date().toISOString(),
          sequence_number: Date.now(),
          data: {
            command,
            result: response,
            success: true,
          },
        });
      }
    },
    { command, response, eventIndex }
  );

  // Wait for UI to update
  await page.waitForTimeout(500);
}

/**
 * Get all messages from the chat panel
 */
export async function getAllMessages(page: Page): Promise<string[]> {
  return await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[data-testid="chat-message"]')).map(
      el => el.textContent?.trim() || ''
    );
  });
}

/**
 * Generate standard room data for testing with proper occupants
 */
export function getStandardRoomData(usernames: string[] = []): { room: unknown; exits: unknown[] } {
  return {
    id: 'earth_arkham_city_downtown_001',
    name: 'Downtown Arkham',
    description:
      'A fog-shrouded street in the heart of Arkham. Victorian buildings loom overhead, their windows dark and foreboding.',
    zone: 'arkham',
    sub_zone: 'city',
    exits: {
      north: 'arkham_university',
      south: 'arkham_harbor',
      east: 'arkham_cemetery',
      west: 'arkham_residential',
    },
    occupants: usernames,
    occupant_count: usernames.length,
  };
}

/**
 * Standard room data for testing (deprecated - use getStandardRoomData instead)
 */
export const STANDARD_ROOM_DATA = getStandardRoomData();
