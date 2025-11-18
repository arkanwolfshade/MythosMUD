/**
 * Global Teardown for Runtime E2E Tests
 *
 * Runs once after all tests to perform any necessary cleanup operations.
 *
 * NOTE: This function is intentionally minimal. Database cleanup and test data
 * teardown are now handled by the PostgreSQL test database infrastructure,
 * which manages test data lifecycle automatically. This file is kept to satisfy
 * Playwright's global teardown requirement and can be extended in the future
 * if additional post-test cleanup is needed (e.g., stopping external services,
 * cleaning up test artifacts, etc.).
 *
 * AI: This file serves as a placeholder for future teardown needs while
 * maintaining compatibility with Playwright's test configuration structure.
 */

async function globalTeardown() {
  console.log('\n🧹 Running global teardown for runtime E2E tests...\n');

  try {
    // Database cleanup and test data teardown are handled by PostgreSQL
    // test database infrastructure. No additional cleanup is required here.
    // Future cleanup operations (e.g., external service shutdown) can be added here.
    console.log('\n✅ Global teardown complete\n');
  } catch (error) {
    console.error('\n❌ Global teardown failed:', error);
    // Don't throw - allow cleanup to fail gracefully to avoid masking test failures
  }
}

export default globalTeardown;
