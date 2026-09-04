---
name: Async Persistence Migration
overview: Migrate the entire persistence subsystem to async by removing the synchronous PersistenceLayer shim and
migrating all callers to use AsyncPersistenceLayer directly. Delete all existing persistence unit tests and recreate
them greenfield for async code.
todos:

  - id: identify_callers

    content: Identify all files that use PersistenceLayer or get_persistence() - search codebase and document call sites
    status: pending

  - id: update_container

    content: Update ApplicationContainer to remove PersistenceLayer initialization and use async_persistence as
    persistence
    status: pending
    dependencies:

      - identify_callers

  - id: update_lifespan

    content: Update lifespan.py to remove global persistence singleton synchronization code
    status: pending
    dependencies:

      - update_container

  - id: migrate_api

    content: Migrate all API endpoints in server/api/ to use async_persistence with await
    status: pending
    dependencies:

      - update_container

  - id: migrate_services

    content: Migrate all services in server/services/ and server/game/ to use async_persistence
    status: pending
    dependencies:

      - update_container

  - id: migrate_commands

    content: Migrate command handlers in server/commands/ to use async_persistence where needed
    status: pending
    dependencies:

      - update_container

  - id: migrate_tests

    content: Update test fixtures and integration tests to use async_persistence
    status: pending
    dependencies:

      - update_container

  - id: delete_persistence_py

    content: Delete server/persistence.py entirely
    status: pending
    dependencies:

      - migrate_api

      - migrate_services

      - migrate_commands

      - migrate_tests

  - id: update_persistence_init

    content: Update server/persistence/__init__.py to remove PersistenceLayer exports
    status: pending
    dependencies:

      - delete_persistence_py

  - id: delete_unit_tests

    content: Delete all persistence unit test files in server/tests/unit/persistence/
    status: pending
    dependencies:

      - delete_persistence_py

  - id: create_async_tests

    content: Create greenfield async unit tests for all persistence operations
    status: pending
    dependencies:

      - delete_unit_tests

  - id: verify_migration

    content: Run make test and make lint to verify migration is complete and working
    status: pending
    dependencies:

      - create_async_tests

      - update_persistence_init

  - id: update_docs

    content: Update documentation to remove PersistenceLayer references
    status: pending
    dependencies:

      - verify_migration

---

# Async Persistence Migration Plan

## Overview

Remove `server/persistence.py` (synchronous shim layer) and migrate all code to use `AsyncPersistenceLayer` directly.
Delete all persistence-related unit tests and recreate them greenfield for async code.

## Current Architecture

**PersistenceLayer** (`server/persistence.py`): Synchronous shim that uses `_run_async()` to call async repositories via
thread pool executors

**AsyncPersistenceLayer** (`server/async_persistence.py`): True async layer using SQLAlchemy ORM with async
  repositories

- Both layers delegate to the same async repositories in `server/persistence/repositories/`
- `ApplicationContainer` initializes both layers, but most new code already uses `async_persistence`

## Phase 1: Identify All Sync Callers

### 1.1 Find all PersistenceLayer usage

Search for `persistence.` method calls (get_player, save_player, update_player, etc.)

- Search for `get_persistence()` calls
- Search for `container.persistence` usage
- Search for `app.state.persistence` usage

### 1.2 Document call sites

List all files that use sync persistence methods

- Categorize by: API endpoints, services, commands, tests, initialization code

## Phase 2: Migrate Callers to Async

### 2.1 Update ApplicationContainer

**File**: `server/container/main.py` (and bundles as needed)

- Remove `PersistenceLayer` import and initialization (line 262-264)
- Change `self.persistence = PersistenceLayer(...)` to `self.persistence = self.async_persistence`
- Update type hints if needed
- Remove any sync persistence initialization code

### 2.2 Update lifespan.py

**File**: `server/app/lifespan.py`

- Remove global persistence singleton synchronization code (lines 76-103)
- Update `app.state.persistence` to use `container.async_persistence` directly
- Remove `_persistence_lock` and `_persistence_instance` handling

### 2.3 Migrate API endpoints

**Files**: All files in `server/api/` that use `persistence`

- Convert sync methods to async
- Update FastAPI route handlers to `async def`
- Change `persistence.get_player()` to `await async_persistence.get_player_by_id()`
- Update dependency injection to use `async_persistence`

### 2.4 Migrate services

**Files**: `server/services/*.py`, `server/game/*.py`

- Convert service methods to async
- Update all persistence calls to use `async_persistence` with `await`
- Update service initialization to accept `async_persistence` instead of `persistence`

### 2.5 Migrate commands

**Files**: `server/commands/*.py`

- Convert command handlers to async where needed
- Update persistence calls to async versions
- Ensure command processing pipeline supports async

### 2.6 Update test fixtures

**File**: `server/tests/conftest.py`

- Update fixtures to use `AsyncPersistenceLayer`
- Remove `PersistenceLayer` fixtures
- Update test setup/teardown to be async

### 2.7 Update integration tests

**Files**: All test files that use persistence

- Convert test functions to `async def` with `@pytest.mark.asyncio`
- Update all persistence calls to use `await`
- Update fixtures to provide `async_persistence`

## Phase 3: Remove PersistenceLayer

### 3.1 Delete persistence.py

**File**: `server/persistence.py` - DELETE ENTIRE FILE

- This removes ~1400 lines of sync shim code

### 3.2 Update persistence package

**File**: `server/persistence/__init__.py`

- Remove re-exports of `get_persistence` and `reset_persistence`
- Remove `PersistenceLayer` imports
- Keep only repository exports

### 3.3 Remove hook decorator

The `@register_hook` decorator in `persistence.py` will be deleted

- If hooks are still needed, move to `AsyncPersistenceLayer` or remove if unused

### 3.4 Update imports

Search for any remaining `from server.persistence import PersistenceLayer`

- Search for `from server.persistence import get_persistence`
- Replace with `from server.async_persistence import AsyncPersistenceLayer`

## Phase 4: Delete Persistence Unit Tests

### 4.1 Identify test files to delete

`server/tests/unit/persistence/test_player_health_persistence.py`

- `server/tests/unit/persistence/test_player_position_persistence.py`
- `server/tests/unit/persistence/test_container_persistence.py`
- `server/tests/unit/persistence/test_inventory_validation_runtime.py`
- Any other files in `server/tests/unit/persistence/` that test sync persistence

### 4.2 Delete test files

Delete all identified persistence unit test files

- Remove any persistence test fixtures from `conftest.py` that are sync-specific

### 4.3 Update integration tests

Review integration tests that use persistence

- Update to use async persistence, but keep integration test structure

## Phase 5: Create Greenfield Async Tests

### 5.1 Test structure

Create new test files in `server/tests/unit/persistence/`

- Use `@pytest.mark.asyncio` for all test functions
- Use async fixtures from `conftest.py`

### 5.2 Test coverage areas

**Player operations**: get, save, update, delete, list

**Room operations**: get, save, list

**Container operations**: create, get, update, delete

**Health operations**: damage, heal, update stats

**Experience operations**: gain, update

- **Inventory operations**: save, load, validate
- **Profession operations**: get, list

### 5.3 Test patterns

Use `AsyncPersistenceLayer` directly

- Use async database sessions from fixtures
- Test async/await patterns correctly
- Use proper async test isolation
- Test error handling with async exceptions

### 5.4 Test utilities

Create async test helpers if needed

- Use async context managers for test data setup/teardown
- Ensure proper async cleanup in fixtures

## Phase 6: Verification and Cleanup

### 6.1 Code verification

Run `make lint` to check for issues

- Verify no remaining `PersistenceLayer` references
- Verify no remaining `get_persistence()` calls
- Verify all async/await patterns are correct

### 6.2 Test verification

Run `make test` to ensure all tests pass

- Verify test coverage meets requirements (80%+)
- Check that new async tests are comprehensive

### 6.3 Documentation updates

Update `docs/DATABASE_ACCESS_PATTERNS.md` to remove PersistenceLayer references

- Update any architecture documentation
- Update code comments that reference sync persistence

### 6.4 Final cleanup

Remove any unused imports

- Remove any dead code paths
- Update type hints throughout codebase
- Ensure consistent async patterns

## Implementation Notes

### Key Changes Required

1. **Method name mapping** (sync → async):

- `get_player(player_id)` → `await get_player_by_id(player_id)`
- `get_player_by_name(name)` → `await get_player_by_name(name)`
- `save_player(player)` → `await save_player(player)`
- `update_player_health(...)` → `await update_player_health(...)`
- Similar mappings for all other methods

1. **Async context requirements**:

- All callers must be in async context
- Use `@pytest.mark.asyncio` for tests
- Use `async def` for all functions that call persistence

1. **Error handling**:

- Async exceptions propagate differently
- Update error handling to use `try/except` with async operations
- Ensure proper exception chaining

### Risks and Mitigations

1. **Risk**: Breaking changes to API endpoints

**Mitigation**: Test all API endpoints thoroughly after migration

1. **Risk**: Performance issues from async overhead

**Mitigation**: Async should improve performance, but monitor for regressions

1. **Risk**: Test coverage gaps

**Mitigation**: Create comprehensive greenfield tests covering all operations

1. **Risk**: Integration test failures

**Mitigation**: Update integration tests carefully, test incrementally

## Success Criteria

[ ] `server/persistence.py` is deleted

- [ ] All code uses `AsyncPersistenceLayer` directly
- [ ] No `PersistenceLayer` or `get_persistence()` references remain
- [ ] All tests pass with async persistence
- [ ] Test coverage maintained at 80%+
- [ ] All API endpoints work correctly
- [ ] All services work correctly
- [ ] Code is properly linted and formatted
