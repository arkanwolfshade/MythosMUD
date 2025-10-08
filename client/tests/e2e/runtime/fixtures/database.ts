/**
 * Database Utilities for Runtime E2E Tests
 *
 * Provides functions for seeding and cleaning up the test database.
 * Uses the existing data/ directory structure with a separate unit_test_players.db file.
 */

import { hash } from 'argon2';
import Database from 'better-sqlite3';
import { copyFileSync, existsSync, mkdirSync, unlinkSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { DEFAULT_PLAYER_STATS, TEST_PLAYERS, type TestPlayer } from './test-data';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Path to test database
 * Uses data/unit_test/players/ directory for isolated test data
 */
const TEST_DB_PATH = join(__dirname, '../../../../../data/unit_test/players/unit_test_players.db');
const TEST_DB_DIR = join(__dirname, '../../../../../data/unit_test/players');

/**
 * Seed the test database with baseline test players
 *
 * Creates ArkanWolfshade (admin), Ithaqua (regular), and TestAdmin (superuser)
 * with known credentials and stats for predictable test execution.
 */
export async function seedTestDatabase(): Promise<void> {
  console.log('🌱 Seeding test database...');

  // Create data/players directory if it doesn't exist
  if (!existsSync(TEST_DB_DIR)) {
    mkdirSync(TEST_DB_DIR, { recursive: true });
    console.log('  Created data/players directory');
  }

  // Backup existing test database if present
  if (existsSync(TEST_DB_PATH)) {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const backupPath = `${TEST_DB_PATH}.backup.${timestamp}`;
    copyFileSync(TEST_DB_PATH, backupPath);
    console.log(`  Backed up existing database to ${backupPath}`);
  }

  // Create new database
  const db = new Database(TEST_DB_PATH);

  try {
    // Create schema
    await createDatabaseSchema(db);
    console.log('  Created database schema');

    // Seed test players
    const players = Object.values(TEST_PLAYERS);
    for (const player of players) {
      await seedPlayer(db, player);
    }

    console.log(`  Seeded ${players.length} test players`);
    console.log('✅ Test database seeded successfully');
  } finally {
    db.close();
  }
}

/**
 * Clean up test database by resetting player state
 *
 * Resets player positions to starting room, clears test-created data,
 * but preserves baseline test players for next test run.
 */
export async function cleanupTestDatabase(): Promise<void> {
  if (!existsSync(TEST_DB_PATH)) {
    console.log('⚠️ Test database not found, skipping cleanup');
    return;
  }

  const db = new Database(TEST_DB_PATH);

  try {
    // Reset player positions to main foyer
    db.prepare(
      `
      UPDATE players
      SET current_room_id = ?,
          last_active = CURRENT_TIMESTAMP
      WHERE player_id LIKE 'test-player-%'
    `
    ).run('earth_arkhamcity_sanitarium_room_foyer_001');

    // Clear test-created invites
    db.prepare(
      `
      DELETE FROM invites
      WHERE created_by_user_id LIKE 'test-user-%'
    `
    ).run();

    // Clear any session data (if sessions table exists)
    const tables = db
      .prepare(
        `
      SELECT name FROM sqlite_master WHERE type='table'
    `
      )
      .all() as Array<{ name: string }>;

    if (tables.some(t => t.name === 'sessions')) {
      db.prepare(
        `
        DELETE FROM sessions
        WHERE player_id LIKE 'test-player-%'
      `
      ).run();
    }

    console.log('✅ Test database cleaned successfully');
  } finally {
    db.close();
  }
}

/**
 * Completely remove test database
 *
 * Used for complete cleanup or when database schema needs to be recreated.
 */
export async function removeTestDatabase(): Promise<void> {
  if (existsSync(TEST_DB_PATH)) {
    unlinkSync(TEST_DB_PATH);
    console.log('🗑️ Test database removed');
  }
}

/**
 * Create database schema matching production structure
 *
 * @param db - SQLite database connection
 */
async function createDatabaseSchema(db: Database): Promise<void> {
  // Create users table
  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY NOT NULL,
      email TEXT UNIQUE NOT NULL,
      username TEXT UNIQUE NOT NULL,
      hashed_password TEXT NOT NULL,
      is_active BOOLEAN NOT NULL DEFAULT 1,
      is_superuser BOOLEAN NOT NULL DEFAULT 0,
      is_verified BOOLEAN NOT NULL DEFAULT 0,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Create players table
  db.exec(`
    CREATE TABLE IF NOT EXISTS players (
      player_id TEXT PRIMARY KEY NOT NULL,
      user_id TEXT NOT NULL UNIQUE,
      name TEXT UNIQUE NOT NULL,
      stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100}',
      inventory TEXT NOT NULL DEFAULT '[]',
      status_effects TEXT NOT NULL DEFAULT '[]',
      current_room_id TEXT NOT NULL DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
      experience_points INTEGER NOT NULL DEFAULT 0,
      level INTEGER NOT NULL DEFAULT 1,
      is_admin INTEGER NOT NULL DEFAULT 0,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
  `);

  // Create invites table
  db.exec(`
    CREATE TABLE IF NOT EXISTS invites (
      id TEXT PRIMARY KEY NOT NULL,
      invite_code TEXT UNIQUE NOT NULL,
      created_by_user_id TEXT,
      used_by_user_id TEXT,
      used BOOLEAN NOT NULL DEFAULT 0,
      expires_at DATETIME,
      created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (created_by_user_id) REFERENCES users(id) ON DELETE SET NULL,
      FOREIGN KEY (used_by_user_id) REFERENCES users(id) ON DELETE SET NULL
    )
  `);

  // Create indexes for performance
  db.exec(`
    CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
    CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
    CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
    CREATE INDEX IF NOT EXISTS idx_players_is_admin ON players(is_admin);
    CREATE INDEX IF NOT EXISTS idx_invites_code ON invites(invite_code);
    CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
  `);
}

/**
 * Seed a single test player into the database
 *
 * @param db - SQLite database connection
 * @param player - Test player data
 */
async function seedPlayer(db: Database, player: TestPlayer): Promise<void> {
  // Hash password using Argon2 (matching production configuration)
  const hashedPassword = await hash(player.password, {
    type: 2, // argon2id
    timeCost: 3,
    memoryCost: 65536,
    parallelism: 1,
  });

  // Insert user record
  db.prepare(
    `
    INSERT OR REPLACE INTO users
    (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
    VALUES (?, ?, ?, ?, 1, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
  `
  ).run(player.userId, player.email, player.username, hashedPassword, player.isSuperuser ? 1 : 0);

  // Insert player record
  const statsJson = JSON.stringify(DEFAULT_PLAYER_STATS);

  db.prepare(
    `
    INSERT OR REPLACE INTO players
    (player_id, user_id, name, stats, inventory, status_effects,
     current_room_id, experience_points, level, is_admin, created_at, last_active)
    VALUES (?, ?, ?, ?, '[]', '[]', ?, 0, 1, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
  `
  ).run(
    player.playerId,
    player.userId,
    player.username,
    statsJson,
    'earth_arkhamcity_sanitarium_room_foyer_001', // All players start in main foyer
    player.isAdmin ? 1 : 0
  );

  console.log(`  Seeded player: ${player.username} (admin: ${player.isAdmin})`);
}

/**
 * Verify test database exists and is properly seeded
 *
 * @returns true if database exists and has baseline players
 */
export function verifyTestDatabase(): boolean {
  if (!existsSync(TEST_DB_PATH)) {
    return false;
  }

  const db = new Database(TEST_DB_PATH);

  try {
    const playerCount = db
      .prepare('SELECT COUNT(*) as count FROM players WHERE player_id LIKE ?')
      .get('test-player-%') as { count: number };

    return playerCount.count >= 3; // At least 3 baseline players
  } catch {
    return false;
  } finally {
    db.close();
  }
}

/**
 * Export test player data for use in tests
 */
export { TEST_PLAYERS };
