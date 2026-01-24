# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-10-08-e2e-playwright-cli-conversion/spec.md

## Test Database Strategy

The test database will use the existing `data/` directory structure with dedicated test databases that are completely isolated from development and production databases.

### Database Files

**Test Player Database**: `data/players/unit_test_players.db`

**Test NPC Database**: `data/npcs/test_npcs.db`

**Test Rooms**: `data/rooms/` (shared with development, no modifications needed)

### Baseline Test Players

The test database will be seeded with the following baseline players for test execution:

#### Test Player 1: ArkanWolfshade (Admin)

```sql
-- User record
INSERT INTO users (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
VALUES (
    'test-user-arkan-001',
    'arkanwolfshade@test.local',
    'ArkanWolfshade',
    '$argon2id$v=19$m=65536,t=3,p=1$test_hash_arkan',  -- Password: "Cthulhu1"
    1,
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Player record
INSERT INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
VALUES (
    'test-player-arkan-001',
    'test-user-arkan-001',
    'ArkanWolfshade',
    '{"health": 100, "lucidity": 100, "strength": 12, "dexterity": 14, "constitution": 10, "intelligence": 16, "wisdom": 8, "charisma": 10, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "max_health": 100, "max_lucidity": 100}',
    '[]',
    '[]',
    'earth_arkhamcity_sanitarium_room_foyer_001',
    0,
    1,
    1,  -- is_admin = TRUE
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

#### Test Player 2: Ithaqua (Regular Player)

```sql
-- User record
INSERT INTO users (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
VALUES (
    'test-user-ithaqua-001',
    'ithaqua@test.local',
    'Ithaqua',
    '$argon2id$v=19$m=65536,t=3,p=1$test_hash_ithaqua',  -- Password: "Cthulhu1"
    1,
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Player record
INSERT INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
VALUES (
    'test-player-ithaqua-001',
    'test-user-ithaqua-001',
    'Ithaqua',
    '{"health": 100, "lucidity": 100, "strength": 10, "dexterity": 12, "constitution": 14, "intelligence": 10, "wisdom": 16, "charisma": 8, "occult_knowledge": 0, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "max_health": 100, "max_lucidity": 100}',
    '[]',
    '[]',
    'earth_arkhamcity_sanitarium_room_foyer_001',
    0,
    1,
    0,  -- is_admin = FALSE
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

#### Test Player 3: TestAdmin (Admin for Testing)

```sql
-- User record
INSERT INTO users (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
VALUES (
    'test-user-admin-001',
    'admin@test.local',
    'TestAdmin',
    '$argon2id$v=19$m=65536,t=3,p=1$test_hash_admin',  -- Password: "Cthulhu1"
    1,
    1,  -- is_superuser = TRUE
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Player record
INSERT INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
VALUES (
    'test-player-admin-001',
    'test-user-admin-001',
    'TestAdmin',
    '{"health": 100, "lucidity": 100, "strength": 15, "dexterity": 15, "constitution": 15, "intelligence": 15, "wisdom": 15, "charisma": 15, "occult_knowledge": 100, "fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100, "max_health": 100, "max_lucidity": 100}',
    '[]',
    '[]',
    'earth_arkhamcity_sanitarium_room_foyer_001',
    1000,
    10,
    1,  -- is_admin = TRUE
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

## Test Data Seeding Implementation

### TypeScript Seeding Utility

Create `client/tests/e2e/runtime/fixtures/database.ts`:

```typescript
import { Database } from 'better-sqlite3';
import { join } from 'path';
import { copyFileSync, existsSync, mkdirSync } from 'fs';
import Argon2 from 'argon2';

interface TestPlayer {
  userId: string;
  playerId: string;
  email: string;
  username: string;
  password: string;
  isAdmin: boolean;
  isSuperuser: boolean;
  startingRoom: string;
}

const TEST_PLAYERS: TestPlayer[] = [
  {
    userId: 'test-user-arkan-001',
    playerId: 'test-player-arkan-001',
    email: 'arkanwolfshade@test.local',
    username: 'ArkanWolfshade',
    password: 'Cthulhu1',
    isAdmin: true,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001'
  },
  {
    userId: 'test-user-ithaqua-001',
    playerId: 'test-player-ithaqua-001',
    email: 'ithaqua@test.local',
    username: 'Ithaqua',
    password: 'Cthulhu1',
    isAdmin: false,
    isSuperuser: false,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001'
  },
  {
    userId: 'test-user-admin-001',
    playerId: 'test-player-admin-001',
    email: 'admin@test.local',
    username: 'TestAdmin',
    password: 'Cthulhu1',
    isAdmin: true,
    isSuperuser: true,
    startingRoom: 'earth_arkhamcity_sanitarium_room_foyer_001'
  }
];

export async function seedTestDatabase(): Promise<void> {
  const dbPath = join(__dirname, '../../../../../data/players/unit_test_players.db');

  // Create data/players directory if it doesn't exist
  const dbDir = join(__dirname, '../../../../../data/players');
  if (!existsSync(dbDir)) {
    mkdirSync(dbDir, { recursive: true });
  }

  // Backup existing test database if present
  if (existsSync(dbPath)) {
    const backupPath = `${dbPath}.backup.${Date.now()}`;
    copyFileSync(dbPath, backupPath);
  }

  const db = new Database(dbPath);

  // Create schema (reuse from server/tests/data/unit_test_players.db structure)
  await createDatabaseSchema(db);

  // Seed test players
  for (const player of TEST_PLAYERS) {
    const hashedPassword = await Argon2.hash(player.password, {
      type: Argon2.argon2id,
      timeCost: 3,
      memoryCost: 65536,
      parallelism: 1
    });

    // Insert user
    db.prepare(`
      INSERT OR REPLACE INTO users (id, email, username, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
      VALUES (?, ?, ?, ?, 1, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    `).run(player.userId, player.email, player.username, hashedPassword, player.isSuperuser ? 1 : 0);

    // Insert player
    const defaultStats = JSON.stringify({
      health: 100,
      lucidity: 100,
      strength: 10,
      dexterity: 10,
      constitution: 10,
      intelligence: 10,
      wisdom: 10,
      charisma: 10,
      occult_knowledge: 0,
      fear: 0,
      corruption: 0,
      cult_affiliation: 0,
      current_health: 100,
      max_health: 100,
      max_lucidity: 100
    });

    db.prepare(`
      INSERT OR REPLACE INTO players (player_id, user_id, name, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
      VALUES (?, ?, ?, ?, '[]', '[]', ?, 0, 1, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    `).run(player.playerId, player.userId, player.username, defaultStats, player.startingRoom, player.isAdmin ? 1 : 0);
  }

  db.close();
}

export async function cleanupTestDatabase(): Promise<void> {
  const dbPath = join(__dirname, '../../../../../data/players/unit_test_players.db');
  const db = new Database(dbPath);

  // Reset player positions to starting rooms
  db.prepare(`
    UPDATE players
    SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001',
        last_active = CURRENT_TIMESTAMP
    WHERE player_id IN (?, ?, ?)
  `).run('test-player-arkan-001', 'test-player-ithaqua-001', 'test-player-admin-001');

  // Clear any test-created data (invites, sessions, etc.)
  db.prepare(`DELETE FROM invites WHERE created_by_user_id LIKE 'test-user-%'`).run();

  db.close();
}

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
      stats TEXT NOT NULL DEFAULT '{"health": 100, "lucidity": 100, "strength": 10}',
      inventory TEXT NOT NULL DEFAULT '[]',
      status_effects TEXT NOT NULL DEFAULT '[]',
      current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',
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

  // Create indexes
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

export { TEST_PLAYERS };
```

## Database Cleanup Hooks

### Playwright Global Setup

Create `client/tests/e2e/runtime/global-setup.ts`:

```typescript
import { seedTestDatabase } from './fixtures/database';

async function globalSetup() {
  console.log('🌱 Seeding test database...');
  await seedTestDatabase();
  console.log('✅ Test database seeded successfully');
}

export default globalSetup;
```

### Playwright Global Teardown

Create `client/tests/e2e/runtime/global-teardown.ts`:

```typescript
import { cleanupTestDatabase } from './fixtures/database';

async function globalTeardown() {
  console.log('🧹 Cleaning up test database...');
  await cleanupTestDatabase();
  console.log('✅ Test database cleaned successfully');
}

export default globalTeardown;
```

### Test-Level Cleanup

In each test file, use `beforeEach` and `afterEach` hooks:

```typescript
import { test } from '@playwright/test';
import { cleanupTestDatabase } from '../fixtures/database';

test.beforeEach(async () => {
  await cleanupTestDatabase();
});

test.afterEach(async () => {
  // Optional: Additional cleanup specific to test
});
```

## Rationale

### Database Isolation

**Separate Test Database**: Using `unit_test_players.db` instead of the development database ensures complete isolation

**No Development Data Contamination**: Tests cannot affect development or production data

**Predictable Test Environment**: Every test run starts with known baseline data

### Seeding Strategy

**Argon2 Password Hashing**: Use same hashing algorithm as production for realistic authentication testing

**Baseline Players**: Three core test players cover all test scenarios (admin, regular, superuser)

**Shared Room Data**: Reuse existing `data/rooms/` structure to avoid duplication and maintenance overhead

### Cleanup Strategy

**Global Setup/Teardown**: One-time seeding and cleanup for entire test suite

**Per-Test Cleanup**: Reset player state between tests to prevent test interdependencies

**Backup Mechanism**: Preserve previous test database for debugging if needed

### Performance Considerations

**SQLite Speed**: In-memory or file-based SQLite is fast enough for test data operations

**Minimal Seeding**: Only seed data required for tests, not full production-like dataset

**Index Optimization**: Create indexes matching production for realistic query performance

### Maintenance Considerations

**Schema Alignment**: Test database schema matches production schema exactly

**Migration Compatibility**: Test seeding works with same migration scripts as production

**Future-Proof**: Easy to add new test players or modify baseline data as tests evolve
