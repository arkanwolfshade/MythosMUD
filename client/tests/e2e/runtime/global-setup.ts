/**
 * Global Setup for Runtime E2E Tests
 *
 * Runs once before all tests.
 * Note: Database seeding is now handled by the PostgreSQL test database.
 */

async function globalSetup() {
  console.log('\n🔧 Running global setup for runtime E2E tests...\n');

  try {
    // Database seeding is handled by PostgreSQL test database
    console.log('\n✅ Global setup complete\n');
  } catch (error) {
    console.error('\n❌ Global setup failed:', error);
    throw error;
  }
}

export default globalSetup;
