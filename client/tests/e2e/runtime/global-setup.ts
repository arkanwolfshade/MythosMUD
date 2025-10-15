/**
 * Global Setup for Runtime E2E Tests
 *
 * Runs once before all tests to seed the test database.
 * This ensures all tests have access to baseline test players.
 */

import { seedTestDatabase } from './fixtures/database';

async function globalSetup() {
  console.log('\n🔧 Running global setup for runtime E2E tests...\n');

  try {
    await seedTestDatabase();
    console.log('\n✅ Global setup complete\n');
  } catch (error) {
    console.error('\n❌ Global setup failed:', error);
    throw error;
  }
}

export default globalSetup;
