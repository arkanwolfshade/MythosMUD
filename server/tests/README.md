# MythosMUD Test Suite

This is the greenfield test suite for MythosMUD server code.

## Structure

- `unit/` - Unit tests with mocks/fakes, no real I/O
- `integration/` - Integration tests with real PostgreSQL database
- `e2e/` - End-to-end tests (placeholder for now)
- `fixtures/` - Shared test fixtures organized by tier

## Running Tests

### All Tests

```bash
# From repo root
make test-server
```

### By Tier

```bash
# Unit tests only
pytest -m unit server/tests

# Integration tests only
pytest -m integration server/tests

# E2E tests only
pytest -m e2e server/tests
```

### With Coverage

```bash
make test-server-coverage
```

## Test Markers

Tests are automatically marked based on their directory:

- Tests in `unit/` → `@pytest.mark.unit`
- Tests in `integration/` → `@pytest.mark.integration`
- Tests in `e2e/` → `@pytest.mark.e2e`

Additional markers:

- `@pytest.mark.slow` - Slow running tests
- `@pytest.mark.serial` - Must run sequentially (not in parallel)
- `@pytest.mark.xdist_group(name="...")` - Group tests for xdist worker assignment

## Coverage Policy

- **Critical paths**: 90% minimum coverage
  - Auth (`server/auth/**`, `server/auth_utils.py`)
  - Commands (`server/commands/**`, `server/validators/**`)
  - Services (`server/services/**`)
  - Persistence (`server/persistence/**`, `server/async_persistence.py`)
  - Config (`server/config/__init__.py`, `server/config/models.py`)
  - Events/Realtime (`server/events/**`, `server/realtime/**`)
  - API (`server/api/**`, `server/routes/**`)
  - Security (`server/security_utils.py`, `server/exceptions.py`)

- **All other code**: 70% minimum coverage (global floor)

## Adding New Tests

### Unit Tests

- Place in `server/tests/unit/`
- Use `strict_mocker` fixture for mocking (autospec enabled by default)
- Use `dummy_request` fixture for request objects
- No real database, network, or filesystem access

### Integration Tests

- Place in `server/tests/integration/`
- Use `session_factory` fixture for database sessions
- Use `db_cleanup` fixture for test isolation
- Real PostgreSQL database required

### E2E Tests

- Place in `server/tests/e2e/`
- Full system tests with running server/client
- Use Playwright MCP for browser automation

## Fixtures

### Shared Fixtures (`fixtures/shared/`)

- `make_user_dict()` - Create user dictionaries
- `make_player_dict()` - Create player dictionaries
- `fake_clock` - Monotonic time counter
- `stub_persistence` - Stub persistence layer

### Unit Fixtures (`fixtures/unit/`)

- `strict_mocker` - Mock helper with autospec=True
- `dummy_request` - Minimal request object
- `fakerandom` - Deterministic random seed

### Integration Fixtures (`fixtures/integration/`)

- `integration_db_url` - Database URL for tests
- `integration_engine` - SQLAlchemy async engine
- `session_factory` - Async session factory
- `db_cleanup` - Automatic table truncation after tests

## Parallel Execution

Tests run in parallel by default using `pytest-xdist`. To prevent race conditions:

1. Use `@pytest.mark.serial` for tests that modify global state
2. Use `@pytest.mark.xdist_group(name="...")` to group related tests
3. Ensure proper test isolation (no shared mutable state)

## Environment Variables

Required for tests:

- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_NPC_URL` - NPC database connection string
- `MYTHOSMUD_ADMIN_PASSWORD` - Admin password
- `SERVER_PORT` - Server port (default: 54731)
- `LOGGING_ENVIRONMENT` - Logging environment (default: unit_test)
- `GAME_ALIASES_DIR` - Aliases directory path

These are set automatically by `conftest.py` fixtures.
