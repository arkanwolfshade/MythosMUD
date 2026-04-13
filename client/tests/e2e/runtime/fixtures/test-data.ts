/**
 * Test Data Constants
 *
 * Centralized test data for E2E runtime tests.
 *
 * Canonical accounts (run e2e.bat or scripts/bootstrap_e2e_database.ps1 for a clean mythos_e2e):
 * - ArkanWolfshade / Cthulhu1 / character name ArkanWolfshade (admin)
 * - Ithaqua / Cthulhu1 / character name Ithaqua (regular)
 *
 * Playwright global-setup runs scripts/seed_e2e_users.py as an idempotent safety net.
 * Seeded players use DEFAULT_RESPAWN_ROOM (matches server.constants.spawn_defaults).
 */

/** Matches server.constants.spawn_defaults.DEFAULT_RESPAWN_ROOM */
export const DEFAULT_RESPAWN_ROOM = 'limbo_arena_arena_arena_5_5' as const;

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

/** Canonical players for E2E. Use in createMultiPlayerContexts for multiplayer flows. */
export const TEST_PLAYERS: TestPlayer[] = [
  {
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    userId: 'test-user-arkan-001',
    playerId: 'test-player-arkan-001',
    email: 'arkanwolfshade@test.local',
    isAdmin: true,
    isSuperuser: false,
    startingRoom: DEFAULT_RESPAWN_ROOM,
  },
  {
    username: 'Ithaqua',
    password: 'Cthulhu1',
    userId: 'test-user-ithaqua-001',
    playerId: 'test-player-ithaqua-001',
    email: 'ithaqua@test.local',
    isAdmin: false,
    isSuperuser: false,
    startingRoom: DEFAULT_RESPAWN_ROOM,
  },
];

export const TEST_ROOMS = {
  /** Sanitarium hub used by movement specs after navigation from spawn */
  MAIN_FOYER: 'earth_arkhamcity_sanitarium_room_foyer_001',
  DEFAULT_RESPAWN_ROOM,
} as const;

export const TEST_TIMEOUTS = {
  DEFAULT: 30000, // 30 seconds
  LOGIN: 30000, // 30 seconds
  MOTD: 30000, // 30 seconds
  GAME_LOAD: 30000, // 30 seconds
  COMMAND: 10000, // 10 seconds
  MESSAGE: 10000, // 10 seconds
} as const;
