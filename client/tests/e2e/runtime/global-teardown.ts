/**
 * Global Teardown for Runtime E2E Tests
 *
 * Runs once after all tests to clean up the test database.
 * This ensures the test environment is clean for the next test run.
 */

import { cleanupTestDatabase } from './fixtures/database';

async function globalTeardown() {
  console.log('\n🧹 Running global teardown for runtime E2E tests...\n');

  try {
    await cleanupTestDatabase();
    console.log('\n✅ Global teardown complete\n');
  } catch (error) {
    console.error('\n❌ Global teardown failed:', error);
    // Don't throw - allow cleanup to fail gracefully
  }
}

export default globalTeardown;
