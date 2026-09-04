/**
 * Test Data Constants
 *
 * Centralized test data for E2E runtime tests.
 *
 * Canonical accounts (run e2e.bat, make ensure-e2e-database, or scripts/bootstrap_e2e_database.ps1):
 * - ArkanWolfshade / Cthulhu1 / character name ArkanWolfshade (admin)
 * - Ithaqua / Cthulhu1 / character name Ithaqua (regular)
 *
 * Playwright global-setup runs scripts/seed_e2e_users.py as an idempotent safety net.
 * Seeded players use DEFAULT_RESPAWN_ROOM (matches server.constants.spawn_defaults).
 */

/** Matches server.constants.spawn_defaults.DEFAULT_RESPAWN_ROOM (sanitarium foyer / Morgan). */
export const DEFAULT_RESPAWN_ROOM = 'earth_arkhamcity_sanitarium_room_foyer_001' as const;

/**
 * After `look`, foyer prose shows in Location / Room Description (not always Game Info).
 * Use for spawn-room assertions against the default (foyer) respawn room -- the gladiator arena
 * (#628) is intentionally a mechanics-testing space, not a player-facing default; see the
 * superseded sections of gladiator_ring_arena_6a674c58.plan.md for why.
 */
export const DEFAULT_SPAWN_LOOK_CUE =
  /Sanitarium\s*>\s*Main Foyer|Main Foyer|marble floor|respectability|disinfectant|Exits:\s*East/i;

/** Foyer east exit lands in Eastern Hallway Section 1 — use for room-split asserts (not bare Exits:). */
export const EASTERN_HALLWAY_LOOK_CUE = /Eastern Hallway|hallway, branching|first section of the eastern hallway/i;

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
