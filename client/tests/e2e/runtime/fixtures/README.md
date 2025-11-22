# E2E Test Fixtures

## Database Seeding

Database seeding for E2E tests is now handled by the PostgreSQL test database managed by the Python backend. The client-side SQLite database fixtures have been removed.

### Optional Dependencies

The `argon2` package is configured as an `optionalDependency` in `client/package.json` for potential future use, but is not currently required for E2E tests.

### Local Development

E2E tests use the PostgreSQL test database configured in the server's test environment. No client-side database setup is required.
