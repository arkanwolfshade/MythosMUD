/**
 * Global Teardown for Runtime E2E Tests
 *
 * Runs once after all tests.
 * Note: Database cleanup is now handled by the PostgreSQL test database.
 */

async function globalTeardown() {
  console.log('\n🧹 Running global teardown for runtime E2E tests...\n');

  try {
    // Database cleanup is handled by PostgreSQL test database
    console.log('\n✅ Global teardown complete\n');
  } catch (error) {
    console.error('\n❌ Global teardown failed:', error);
    // Don't throw - allow cleanup to fail gracefully
  }
}

export default globalTeardown;
