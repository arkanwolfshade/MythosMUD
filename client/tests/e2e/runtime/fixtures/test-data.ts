/**
 * Test Data Constants for Runtime E2E Tests
 *
 * Provides centralized test data including player credentials, room IDs,
 * message templates, error messages, and timeout configurations.
 */

/**
 * Test Player Credentials
 *
 * These credentials match the seeded test database players.
 */
export const TEST_PLAYERS = {
  ARKAN_WOLFSHADE: {
    userId: 'test-user-arkan-001',
    playerId: 'test-player-arkan-001',
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    email: 'arkanwolfshade@test.local',
    isAdmin: true,
    isSuperuser: false,
  },
  ITHAQUA: {
    userId: 'test-user-ithaqua-001',
    playerId: 'test-player-ithaqua-001',
    username: 'Ithaqua',
    password: 'Cthulhu1',
    email: 'ithaqua@test.local',
    isAdmin: false,
    isSuperuser: false,
  },
  TEST_ADMIN: {
    userId: 'test-user-admin-001',
    playerId: 'test-player-admin-001',
    username: 'TestAdmin',
    password: 'Cthulhu1',
    email: 'admin@test.local',
    isAdmin: true,
    isSuperuser: true,
  },
} as const;

/**
 * Test Room IDs
 *
 * Room IDs used in test scenarios, all players start in Main Foyer.
 */
export const TEST_ROOMS = {
  MAIN_FOYER: 'earth_arkhamcity_sanitarium_room_foyer_001',
  EAST_ROOM: 'earth_arkhamcity_sanitarium_room_east_001',
  WEST_ROOM: 'earth_arkhamcity_sanitarium_room_west_001',
  NORTH_ROOM: 'earth_arkhamcity_sanitarium_room_north_001',
  SOUTH_ROOM: 'earth_arkhamcity_sanitarium_room_south_001',

  // Arkham test rooms (for movement testing)
  ARKHAM_TOWN_SQUARE: 'arkham_001',
  ARKHAM_UNIVERSITY_GATES: 'arkham_002',
  ARKHAM_RIVERSIDE: 'arkham_003',
  ARKHAM_TUNNELS: 'arkham_004',
  ARKHAM_WHISPER_STREET: 'arkham_005',
  ARKHAM_LIBRARY: 'arkham_006',
  ARKHAM_ARCHIVES: 'arkham_007',
} as const;

/**
 * Error Message Templates
 *
 * Expected error messages for various error conditions.
 */
export const ERROR_MESSAGES = {
  // Local channel errors
  LOCAL_EMPTY_MESSAGE: 'You must provide a message to send locally',
  LOCAL_MESSAGE_TOO_LONG: 'Local message too long',
  LOCAL_INVALID_SYNTAX: 'Invalid local command syntax',

  // Whisper errors
  WHISPER_PLAYER_NOT_FOUND: (playerName: string) => `Player '${playerName}' not found`,
  WHISPER_EMPTY_MESSAGE: 'You must provide a message to whisper',
  WHISPER_INVALID_SYNTAX: 'Usage: whisper <player> <message>',
  WHISPER_MESSAGE_TOO_LONG: 'Whisper message too long',
  WHISPER_TO_SELF: 'You cannot whisper to yourself',
  WHISPER_RATE_LIMIT_RECIPIENT: 'Rate limit exceeded. You can only send 3 whispers per minute to the same player.',
  WHISPER_RATE_LIMIT_GLOBAL: 'Rate limit exceeded. You can only send 5 whispers per minute.',

  // Logout errors
  LOGOUT_NETWORK_ERROR: 'Network error: Unable to logout',
  LOGOUT_SERVER_ERROR: 'Server error: Unable to logout',
  LOGOUT_SESSION_EXPIRED: 'Session expired: Please log in again',

  // Admin errors
  ADMIN_PERMISSION_DENIED: 'You do not have permission to use that command',
  ADMIN_PLAYER_NOT_FOUND: (playerName: string) => `Player '${playerName}' not found`,

  // General errors
  INVALID_COMMAND: 'Invalid command',
  COMMAND_FAILED: 'Command failed',
} as const;

/**
 * Success Message Templates
 *
 * Expected success messages for various actions.
 */
export const SUCCESS_MESSAGES = {
  // Local channel
  LOCAL_MESSAGE_SENT: (message: string) => `You say locally: ${message}`,
  LOCAL_MESSAGE_RECEIVED: (username: string, message: string) => `${username} says locally: ${message}`,

  // Whisper
  WHISPER_SENT: (recipient: string, message: string) => `You whisper to ${recipient}: ${message}`,
  WHISPER_RECEIVED: (sender: string, message: string) => `${sender} whispers to you: ${message}`,

  // Say channel
  SAY_MESSAGE_SENT: (message: string) => `You say: ${message}`,
  SAY_MESSAGE_RECEIVED: (username: string, message: string) => `${username} says: ${message}`,

  // Movement
  MOVEMENT_CONFIRMATION: (direction: string) => `You move ${direction}`,
  PLAYER_ENTERS: (username: string) => `${username} enters the room`,
  PLAYER_LEAVES: (username: string) => `${username} leaves the room`,

  // Connection
  PLAYER_CONNECTED: (username: string) => `${username} has entered the game`,
  PLAYER_DISCONNECTED: (username: string) => `${username} has left the game`,

  // Logout
  LOGOUT_CONFIRMATION: 'You have been logged out',
  LOGOUT_BROADCAST: (username: string) => `${username} has logged out`,

  // Muting
  MUTE_CONFIRMATION: (username: string) => `You have muted ${username}`,
  UNMUTE_CONFIRMATION: (username: string) => `You have unmuted ${username}`,

  // Admin
  ADMIN_STATUS: 'Admin privileges: Active',
  TELEPORT_CONFIRMATION: (username: string, direction: string) => `You teleport ${username} to the ${direction}`,
  TELEPORT_RECEIVED: (admin: string, direction: string) => `You are teleported to the ${direction} by ${admin}`,

  // Who command
  WHO_HEADER: 'Online Players:',
} as const;

/**
 * Timeout Configurations
 *
 * Timeout values for various test operations.
 */
export const TIMEOUTS = {
  // Page load timeouts
  PAGE_LOAD: 30000, // 30 seconds
  NAVIGATION: 30000, // 30 seconds

  // Element visibility timeouts
  ELEMENT_VISIBLE: 10000, // 10 seconds
  MESSAGE_APPEAR: 10000, // 10 seconds

  // Action timeouts
  LOGIN: 15000, // 15 seconds
  COMMAND_EXECUTION: 5000, // 5 seconds
  LOGOUT: 10000, // 10 seconds

  // Special timeouts
  MOTD_SCREEN: 30000, // 30 seconds
  GAME_LOAD: 30000, // 30 seconds
  ROOM_SUBSCRIPTION: 2000, // 2 seconds (for room subscription stabilization)

  // Rate limiting timeouts
  RATE_LIMIT_RESET: 60000, // 60 seconds
  RATE_LIMIT_WAIT: 2000, // 2 seconds (wait to ensure message would have arrived)
} as const;

/**
 * UI Element Selectors
 *
 * Data-testid selectors for UI elements.
 */
export const SELECTORS = {
  // Login page
  USERNAME_INPUT: '[data-testid="username-input"]',
  PASSWORD_INPUT: '[data-testid="password-input"]',
  LOGIN_BUTTON: '[data-testid="login-button"]',

  // MOTD screen
  CONTINUE_BUTTON: '[data-testid="continue-button"]',

  // Game interface
  COMMAND_INPUT: '[data-testid="command-input"]',
  MESSAGE_CONTAINER: '.message',
  ERROR_MESSAGE: '.error-message',
  SUCCESS_MESSAGE: '.success-message',
  LOCATION_DISPLAY: '.location-display',

  // Logout
  LOGOUT_BUTTON: '[data-testid="logout-button"]',

  // Chat
  CHAT_PANEL: '[data-testid="chat-panel"]',
  CHAT_MESSAGE: '.message',
} as const;

/**
 * Test Message Templates
 *
 * Pre-defined test messages for various scenarios.
 */
export const TEST_MESSAGES = {
  SIMPLE: 'Hello, this is a test message',
  WITH_SPECIAL_CHARS: 'Test message with !@#$%^&*()',
  WITH_UNICODE: 'Unicode test: 你好世界 🌍',
  LONG_MESSAGE: 'This is a very long message. '.repeat(20), // >500 chars
  WHITESPACE_ONLY: '   ',
  EMPTY: '',
} as const;

/**
 * Rate Limit Configuration
 *
 * Rate limiting values for whisper system.
 */
export const RATE_LIMITS = {
  WHISPER_PER_RECIPIENT: 3, // 3 whispers per minute to same player
  WHISPER_GLOBAL: 5, // 5 whispers per minute total
  RESET_TIME: 60000, // 60 seconds in milliseconds
} as const;

/**
 * Player Stats Template
 *
 * Default player stats for test players.
 */
export const DEFAULT_PLAYER_STATS = {
  health: 100,
  sanity: 100,
  strength: 50,
  dexterity: 50,
  constitution: 50,
  intelligence: 50,
  wisdom: 50,
  charisma: 50,
  occult_knowledge: 0,
  fear: 0,
  corruption: 0,
  cult_affiliation: 0,
  current_health: 100,
  max_health: 100,
  max_sanity: 100,
} as const;

/**
 * TypeScript Types
 */
export interface TestPlayer {
  userId: string;
  playerId: string;
  username: string;
  password: string;
  email: string;
  isAdmin: boolean;
  isSuperuser: boolean;
}

export interface TestMessage {
  sender: string;
  content: string;
  type: 'say' | 'local' | 'whisper' | 'system' | 'error' | 'emote';
  timestamp?: Date;
}

export interface PlayerStats {
  health: number;
  sanity: number;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
  occult_knowledge: number;
  fear: number;
  corruption: number;
  cult_affiliation: number;
  current_health: number;
  max_health: number;
  max_sanity: number;
}
