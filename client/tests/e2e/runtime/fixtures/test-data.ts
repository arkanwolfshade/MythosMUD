/**
 * Test Data Constants
 *
 * Centralized test data for E2E runtime tests.
 * These constants define test players, rooms, and other test data.
 */

export interface TestPlayer {
  username: string;
  password: string;
  userId: string;
  playerId: string;
  email: string;
  isAdmin: boolean;
  isSuperuser: boolean;
  startingRoom: string;
}

export const TEST_PLAYERS: TestPlayer[] = [
  {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    userId: 'test-user-arkan-001',
    playerId: 'test-player-arkan-001',
    email: 'arkanwolfshade@test.local',
    isAdmin: true,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001',
  },
  {
    username: 'Ithaqua',
    password: 'Cthulhu1',
    userId: 'test-user-ithaqua-001',
    playerId: 'test-player-ithaqua-001',
    email: 'ithaqua@test.local',
    isAdmin: false,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001',
  },
  {
    username: 'TestAdmin',
    password: 'Cthulhu1',
    userId: 'test-user-admin-001',
    playerId: 'test-player-admin-001',
    email: 'testadmin@test.local',
    isAdmin: true,
    isSuperuser: true,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001',
  },
];

export const TEST_ROOMS = {
  MAIN_FOYER: 'earth_arkhamcity_sanitarium_room_foyer_001',
} as const;

export const TEST_TIMEOUTS = {
  DEFAULT: 30000, // 30 seconds
  LOGIN: 30000, // 30 seconds
  MOTD: 30000, // 30 seconds
  GAME_LOAD: 30000, // 30 seconds
  COMMAND: 10000, // 10 seconds
  MESSAGE: 10000, // 10 seconds
} as const;
