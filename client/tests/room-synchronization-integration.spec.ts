import { BrowserContext, Page, expect, test } from '@playwright/test';
import {
  SERVER_URL,
  TEST_CREDENTIALS,
  TestCredentials,
  emitMockGameStateEvent,
  installRealtimeFakes,
  loginWithMock,
  waitForRealtimeConnection,
} from './utils/mockAuth';

/**
 * Integration tests for room synchronization and UI consistency.
 * Tests room transition scenarios, movement commands with multiple players,
 * and Room Info panel display correctness.
 *
 * Based on findings from "Temporal Consistency in Non-Euclidean Spaces" - Dr. Armitage, 1928
 */

// Use standardized test credentials
const PLAYER_1_CREDENTIALS = TEST_CREDENTIALS.PLAYER_1;
const PLAYER_2_CREDENTIALS = TEST_CREDENTIALS.PLAYER_2;

interface RoomData {
  id: string;
  name: string;
  description: string;
  zone?: string;
  sub_zone?: string;
  exits?: Record<string, string | null>;
  occupants?: string[];
  occupant_count?: number;
}

class RoomSyncTestHelper {
  constructor(private page: Page) {}

  async login(credentials: TestCredentials, useMock: boolean = true, allUsernames: string[] = []): Promise<void> {
    if (useMock) {
      // Setup real-time fakes for SSE and WebSocket
      await installRealtimeFakes(this.page);

      // Use mock authentication with proper room data
      await loginWithMock(this.page, credentials, undefined, allUsernames);

      // Wait for real-time connection to be established
      await waitForRealtimeConnection(this.page);
    } else {
      // Use real authentication (for tests that need actual server)
      await this.page.goto(SERVER_URL);

      // Wait for login form
      await this.page.waitForSelector('input[placeholder="Username"]');

      // Fill login form
      await this.page.getByPlaceholder('Username').fill(credentials.username);
      await this.page.getByPlaceholder('Password').fill(credentials.password);

      // Submit login
      await this.page.getByRole('button', { name: 'Enter the Void' }).click();

      // Wait for game interface
      await this.page.waitForSelector('[data-testid="game-terminal"]', { timeout: 10000 });

      // Wait for initial room data to load
      await this.page.waitForSelector('[data-testid="room-info-panel"]', { timeout: 5000 });
    }
  }

  async getRoomInfo(): Promise<RoomData | null> {
    try {
      // Get room data from the Room Info panel
      const roomNameElement = await this.page.$('[data-testid="room-name"]');
      const roomDescriptionElement = await this.page.$('[data-testid="room-description"]');
      const zoneElement = await this.page.$('[data-testid="zone-value"]');
      const subZoneElement = await this.page.$('[data-testid="subzone-value"]');
      const occupantsElements = await this.page.$$('[data-testid="occupant-name"]');

      if (!roomNameElement) {
        return null;
      }

      const name = await roomNameElement.textContent();
      const description = roomDescriptionElement ? await roomDescriptionElement.textContent() : '';
      const zone = zoneElement ? await zoneElement.textContent() : undefined;
      const subZone = subZoneElement ? await subZoneElement.textContent() : undefined;

      const occupants = await Promise.all(occupantsElements.map(el => el.textContent()));

      return {
        id: `room-${name?.toLowerCase().replace(/\s+/g, '-')}`,
        name: name || '',
        description: description || '',
        zone: zone || undefined,
        sub_zone: subZone || undefined,
        occupants: occupants.filter(Boolean) as string[],
        occupant_count: occupants.length,
      };
    } catch (error) {
      console.error('Error getting room info:', error);
      return null;
    }
  }

  async sendCommand(command: string): Promise<void> {
    const commandInput = this.page.locator('[data-testid="command-input"]');
    await commandInput.fill(command);
    await commandInput.press('Enter');

    // Wait for command to be processed
    await this.page.waitForTimeout(1000);
  }

  async waitForRoomChange(expectedRoomName?: string, timeout: number = 5000): Promise<boolean> {
    try {
      if (expectedRoomName) {
        await this.page.waitForSelector(`[data-testid="room-name"]:has-text("${expectedRoomName}")`, { timeout });
      } else {
        // Wait for any room change (detect by checking if room name changed)
        const initialRoomName = await this.page.textContent('[data-testid="room-name"]');
        await this.page.waitForFunction(
          initialName => {
            const currentName = document.querySelector('[data-testid="room-name"]')?.textContent;
            return currentName && currentName !== initialName;
          },
          initialRoomName,
          { timeout }
        );
      }
      return true;
    } catch (error) {
      console.error('Room change timeout:', error);
      return false;
    }
  }

  async getChatMessages(): Promise<Array<{ text: string; timestamp: string; type?: string }>> {
    const messageElements = await this.page.$$('[data-testid="chat-message"]');

    return Promise.all(
      messageElements.map(async element => {
        const text = (await element.textContent()) || '';
        const timestamp = (await element.getAttribute('data-timestamp')) || '';
        const type = (await element.getAttribute('data-message-type')) || '';

        return { text, timestamp, type };
      })
    );
  }

  async waitForPlayerMessage(playerName: string, timeout: number = 5000): Promise<boolean> {
    try {
      await this.page.waitForSelector(`[data-testid="chat-message"]:has-text("${playerName}")`, { timeout });
      return true;
    } catch (error) {
      console.error(`Player message timeout for ${playerName}:`, error);
      return false;
    }
  }

  async emitMockGameStateEvent(eventData: unknown, eventIndex: number = 0): Promise<void> {
    await emitMockGameStateEvent(this.page, eventData, eventIndex);
  }
}

test.describe('Room Synchronization Integration Tests', () => {
  let player1Context: BrowserContext;
  let player2Context: BrowserContext;
  let player1Page: Page;
  let player2Page: Page;
  let player1Helper: RoomSyncTestHelper;
  let player2Helper: RoomSyncTestHelper;

  test.beforeAll(async ({ browser }) => {
    // Create two browser contexts for two players
    player1Context = await browser.newContext();
    player2Context = await browser.newContext();

    player1Page = await player1Context.newPage();
    player2Page = await player2Context.newPage();

    player1Helper = new RoomSyncTestHelper(player1Page);
    player2Helper = new RoomSyncTestHelper(player2Page);
  });

  test.afterAll(async () => {
    await player1Context.close();
    await player2Context.close();
  });

  test('should synchronize room state between multiple players', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    // Wait for both players to be in the same initial room
    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    const player1InitialRoom = await player1Helper.getRoomInfo();
    const player2InitialRoom = await player2Helper.getRoomInfo();

    // Both players should see the same initial room
    expect(player1InitialRoom).toBeTruthy();
    expect(player2InitialRoom).toBeTruthy();
    expect(player1InitialRoom?.name).toBe(player2InitialRoom?.name);
    expect(player1InitialRoom?.id).toBe(player2InitialRoom?.id);

    // Both players should see each other as occupants (formatted names)
    const formattedPlayer1 =
      PLAYER_1_CREDENTIALS.username.charAt(0).toUpperCase() + PLAYER_1_CREDENTIALS.username.slice(1);
    const formattedPlayer2 =
      PLAYER_2_CREDENTIALS.username.charAt(0).toUpperCase() + PLAYER_2_CREDENTIALS.username.slice(1);

    expect(player1InitialRoom?.occupants).toContain(formattedPlayer1);
    expect(player1InitialRoom?.occupants).toContain(formattedPlayer2);
    expect(player2InitialRoom?.occupants).toContain(formattedPlayer1);
    expect(player2InitialRoom?.occupants).toContain(formattedPlayer2);

    // Occupant counts should be consistent
    expect(player1InitialRoom?.occupant_count).toBe(2);
    expect(player2InitialRoom?.occupant_count).toBe(2);
  });

  test('should handle room transitions with proper synchronization', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    const initialRoom = await player1Helper.getRoomInfo();
    expect(initialRoom).toBeTruthy();

    // Player 1 moves to a different room - emit mock game state event
    await player1Helper.sendCommand('go north');

    // Emit mock game state event for Player 1's new room
    const newRoomData = {
      player: {
        name: PLAYER_1_CREDENTIALS.username,
        level: 1,
        health: 100,
        sanity: 100,
      },
      room: {
        id: 'room_north_' + Date.now(),
        name: 'Northern Chamber',
        description: 'A dimly lit chamber to the north. Ancient symbols line the walls.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: {
          south: 'original-room',
          east: null,
          west: null,
        },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 2,
    };

    await player1Helper.emitMockGameStateEvent(newRoomData);

    // Wait for room change
    const roomChanged = await player1Helper.waitForRoomChange();
    expect(roomChanged).toBe(true);

    // Get updated room info for both players
    const player1NewRoom = await player1Helper.getRoomInfo();
    const player2RoomAfterMove = await player2Helper.getRoomInfo();

    // Player 1 should be in a different room
    expect(player1NewRoom?.name).not.toBe(initialRoom?.name);
    expect(player1NewRoom?.id).not.toBe(initialRoom?.id);

    // Player 2 should still see the original room but without Player 1
    expect(player2RoomAfterMove?.name).toBe(initialRoom?.name);
    expect(player2RoomAfterMove?.occupants).not.toContain(PLAYER_1_CREDENTIALS.username);
    expect(player2RoomAfterMove?.occupants).toContain(PLAYER_2_CREDENTIALS.username);
    expect(player2RoomAfterMove?.occupant_count).toBe(1);

    // Player 1 should see only themselves in the new room
    expect(player1NewRoom?.occupants).toContain(PLAYER_1_CREDENTIALS.username);
    expect(player1NewRoom?.occupants).not.toContain(PLAYER_2_CREDENTIALS.username);
    expect(player1NewRoom?.occupant_count).toBe(1);
  });

  test('should display consistent room information across players', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Get room info from both players
    const player1Room = await player1Helper.getRoomInfo();
    const player2Room = await player2Helper.getRoomInfo();

    // Room data should be consistent
    expect(player1Room?.name).toBe(player2Room?.name);
    expect(player1Room?.description).toBe(player2Room?.description);
    expect(player1Room?.zone).toBe(player2Room?.zone);
    expect(player1Room?.sub_zone).toBe(player2Room?.sub_zone);

    // Occupant counts should match
    expect(player1Room?.occupant_count).toBe(player2Room?.occupant_count);

    // Both players should see the same occupants
    const player1Occupants = player1Room?.occupants?.sort() || [];
    const player2Occupants = player2Room?.occupants?.sort() || [];
    expect(player1Occupants).toEqual(player2Occupants);
  });

  test('should handle rapid movement commands correctly', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Player 1 performs rapid movement with mock events
    await player1Helper.sendCommand('go north');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_north_' + Date.now(),
        name: 'Northern Chamber',
        description: 'A dimly lit chamber to the north.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { south: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 2,
    });
    await player1Page.waitForTimeout(500);

    await player1Helper.sendCommand('go south');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_south_' + Date.now(),
        name: 'Southern Hall',
        description: 'A grand hall extending southward.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { north: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 3,
    });
    await player1Page.waitForTimeout(500);

    await player1Helper.sendCommand('go east');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_east_' + Date.now(),
        name: 'Eastern Corridor',
        description: 'A narrow corridor stretching eastward.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { west: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 4,
    });
    await player1Page.waitForTimeout(500);

    // Wait for final room change
    await player1Page.waitForTimeout(1000);

    // Get final room states
    const player1FinalRoom = await player1Helper.getRoomInfo();
    const player2RoomAfterRapidMove = await player2Helper.getRoomInfo();

    // Both players should have valid room data
    expect(player1FinalRoom).toBeTruthy();
    expect(player2RoomAfterRapidMove).toBeTruthy();

    // Room data should be consistent and valid
    expect(player1FinalRoom?.name).toBeTruthy();
    expect(player1FinalRoom?.description).toBeTruthy();
    expect(player1FinalRoom?.occupant_count).toBeGreaterThanOrEqual(0);
  });

  test('should validate room info panel consistency during transitions', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Get initial room info
    const initialRoom = await player1Helper.getRoomInfo();
    expect(initialRoom).toBeTruthy();

    // Player 1 moves with mock event
    await player1Helper.sendCommand('go north');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_north_' + Date.now(),
        name: 'Northern Chamber',
        description: 'A dimly lit chamber to the north.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { south: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 2,
    });

    // Wait for room change
    await player1Helper.waitForRoomChange();

    // Verify Room Info panel displays correct data
    const roomNameElement = player1Page.locator('[data-testid="room-name"]');
    const roomDescriptionElement = player1Page.locator('[data-testid="room-description"]');
    const zoneElement = player1Page.locator('[data-testid="zone-value"]');
    const subZoneElement = player1Page.locator('[data-testid="subzone-value"]');
    const occupantCountElement = player1Page.locator('[data-testid="occupant-count"]');

    // All elements should be present and have content
    await expect(roomNameElement).toBeVisible();
    await expect(roomDescriptionElement).toBeVisible();
    await expect(zoneElement).toBeVisible();
    await expect(subZoneElement).toBeVisible();
    await expect(occupantCountElement).toBeVisible();

    // Content should not be empty
    const roomName = await roomNameElement.textContent();
    const roomDescription = await roomDescriptionElement.textContent();
    const zone = await zoneElement.textContent();
    const subZone = await subZoneElement.textContent();
    const occupantCount = await occupantCountElement.textContent();

    expect(roomName).toBeTruthy();
    expect(roomDescription).toBeTruthy();
    expect(zone).toBeTruthy();
    expect(subZone).toBeTruthy();
    expect(occupantCount).toBeTruthy();
  });

  test('should handle edge cases in room synchronization', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Test invalid movement command
    await player1Helper.sendCommand('go invalid_direction');
    await player1Page.waitForTimeout(1000);

    // Player should still have valid room data
    const roomAfterInvalidMove = await player1Helper.getRoomInfo();
    expect(roomAfterInvalidMove).toBeTruthy();
    expect(roomAfterInvalidMove?.name).toBeTruthy();

    // Test empty movement command
    await player1Helper.sendCommand('');
    await player1Page.waitForTimeout(1000);

    // Room data should remain valid
    const roomAfterEmptyCommand = await player1Helper.getRoomInfo();
    expect(roomAfterEmptyCommand).toBeTruthy();
    expect(roomAfterEmptyCommand?.name).toBeTruthy();

    // Test movement to non-existent room
    await player1Helper.sendCommand('go nowhere');
    await player1Page.waitForTimeout(1000);

    // Room data should remain valid
    const roomAfterNonExistentMove = await player1Helper.getRoomInfo();
    expect(roomAfterNonExistentMove).toBeTruthy();
    expect(roomAfterNonExistentMove?.name).toBeTruthy();
  });

  test('should maintain occupant count consistency during player movements', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Get initial room states
    const player1InitialRoom = await player1Helper.getRoomInfo();
    const player2InitialRoom = await player2Helper.getRoomInfo();

    expect(player1InitialRoom?.occupant_count).toBe(2);
    expect(player2InitialRoom?.occupant_count).toBe(2);

    // Player 1 moves with mock event
    await player1Helper.sendCommand('go north');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_north_' + Date.now(),
        name: 'Northern Chamber',
        description: 'A dimly lit chamber to the north.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { south: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 2,
    });

    await player1Helper.waitForRoomChange();

    // Wait for synchronization
    await player1Page.waitForTimeout(1000);
    await player2Page.waitForTimeout(1000);

    // Get updated room states
    const player1NewRoom = await player1Helper.getRoomInfo();
    const player2UpdatedRoom = await player2Helper.getRoomInfo();

    // Player 1's new room should have count of 1 (only themselves)
    expect(player1NewRoom?.occupant_count).toBe(1);
    const formattedPlayer1 =
      PLAYER_1_CREDENTIALS.username.charAt(0).toUpperCase() + PLAYER_1_CREDENTIALS.username.slice(1);
    const formattedPlayer2 =
      PLAYER_2_CREDENTIALS.username.charAt(0).toUpperCase() + PLAYER_2_CREDENTIALS.username.slice(1);

    expect(player1NewRoom?.occupants).toContain(formattedPlayer1);
    expect(player1NewRoom?.occupants).not.toContain(formattedPlayer2);

    // Player 2's room should have count of 1 (only themselves)
    expect(player2UpdatedRoom?.occupant_count).toBe(1);
    expect(player2UpdatedRoom?.occupants).toContain(formattedPlayer2);
    expect(player2UpdatedRoom?.occupants).not.toContain(formattedPlayer1);
  });

  test('should handle network delay simulation gracefully', async () => {
    // Define all usernames for the shared room
    const allUsernames = [PLAYER_1_CREDENTIALS.username, PLAYER_2_CREDENTIALS.username];

    // Login both players with shared room data
    await player1Helper.login(PLAYER_1_CREDENTIALS, true, allUsernames);
    await player2Helper.login(PLAYER_2_CREDENTIALS, true, allUsernames);

    await player1Page.waitForTimeout(2000);
    await player2Page.waitForTimeout(2000);

    // Simulate network delay by throttling connection
    await player1Page.route('**/*', route => {
      setTimeout(() => route.continue(), 100); // 100ms delay
    });

    // Player 1 moves with simulated delay and mock event
    await player1Helper.sendCommand('go north');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_north_' + Date.now(),
        name: 'Northern Chamber',
        description: 'A dimly lit chamber to the north.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { south: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 2,
    });

    // Wait longer for delayed response
    await player1Page.waitForTimeout(2000);

    // Room data should still be valid despite delay
    const roomWithDelay = await player1Helper.getRoomInfo();
    expect(roomWithDelay).toBeTruthy();
    expect(roomWithDelay?.name).toBeTruthy();
    expect(roomWithDelay?.description).toBeTruthy();

    // Remove route throttling
    await player1Page.unroute('**/*');

    // Normal operation should resume
    await player1Helper.sendCommand('go south');
    await player1Helper.emitMockGameStateEvent({
      player: { name: PLAYER_1_CREDENTIALS.username, level: 1, health: 100, sanity: 100 },
      room: {
        id: 'room_south_' + Date.now(),
        name: 'Southern Hall',
        description: 'A grand hall extending southward.',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { north: 'original-room' },
        occupants: [PLAYER_1_CREDENTIALS.username],
        occupant_count: 1,
      },
      timestamp: new Date().toISOString(),
      sequence_number: 3,
    });
    await player1Page.waitForTimeout(1000);

    const roomAfterDelay = await player1Helper.getRoomInfo();
    expect(roomAfterDelay).toBeTruthy();
    expect(roomAfterDelay?.name).toBeTruthy();
  });
});
