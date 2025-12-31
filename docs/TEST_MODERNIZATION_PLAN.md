# MythosMUD Test Suite Modernization Plan

**Document Version:** 1.1
**Date:** November 4, 2025
**Status:** Phase 0 Complete - Phase 1 In Progress
**Author:** Miskatonic University Development Team
**Last Updated:** November 4, 2025 (Phase 0 Foundation Complete)

---

## Executive Summary

Following the successful architectural remediation, the test suite requires modernization to align with the new ApplicationContainer-based dependency injection pattern. This plan provides a structured approach to uplift or rewrite tests systematically.

**Current State:**

- 253 test files with ~5,061 test functions
- 445 instances of direct `app.state` access across 35 files
- 10 integration tests failing due to missing ApplicationContainer
- Mixed patterns: some tests use lifespan, some mock app.state manually

**Goal:**

- All tests use ApplicationContainer for dependency injection
- Consistent fixture patterns across all test categories
- Zero test failures related to architecture changes
- Improved test maintainability and clarity

---

## Test Suite Analysis

### Current Test Organization

```
server/tests/
├── unit/              (184 files) - Component isolation tests
├── integration/       (42 files)  - Component interaction tests
├── e2e/               (8 files)   - End-to-end workflows
├── coverage/          (5 files)   - Coverage improvement tests
├── security/          (4 files)   - Security validation tests
├── performance/       (3 files)   - Performance benchmarks
├── regression/        (3 files)   - Bug regression tests
├── monitoring/        (2 files)   - Monitoring tests
├── verification/      (2 files)   - System verification tests
└── conftest.py        - Shared fixtures
```

### Dependency Access Patterns

**Pattern 1: Direct app.state Access (Broken - 445 instances)**

```python
# CURRENT: Manually setting app.state
app.state.persistence = get_persistence()
app.state.player_service = PlayerService(mock_persistence)
app.state.connection_manager = connection_manager
```

**Pattern 2: Using Real Lifespan (Works - Limited)**

```python
# CURRENT: Some tests use actual lifespan
with TestClient(app) as client:
    # Lifespan runs, container initialized
    response = client.get("/api/health")
```

**Pattern 3: Fixture-Based Mocking (Mixed)**

```python
# CURRENT: Fixtures create services manually
@pytest.fixture
def test_client():
    app.state.persistence = get_persistence()
    return TestClient(app)
```

---

## Decision Framework: Uplift vs Greenfield Rewrite

### Recommendation: **PHASED UPLIFT** (Not Greenfield)

**Rationale:**

1. **Preserve Test Coverage** - 5,061 tests represent enormous investment
2. **Working Tests** - 224/234 tests pass (95.7% success rate)
3. **Incremental Risk** - Phased uplift allows verification at each step
4. **Domain Knowledge** - Existing tests encode critical business rules
5. **Time Efficiency** - Uplift faster than complete rewrite

**Greenfield Only If:**

- Test suite is fundamentally broken (not the case - 95.7% pass)
- Tests are unmaintainable (not the case - well organized)
- Architecture change is incompatible (not the case - backward compatible)

---

## Uplift Strategy

### Phase 0: Foundation (Week 1) ✅ **COMPLETE**

**Completion Date:** November 4, 2025
**Status:** All foundation fixtures implemented and working

**Major Accomplishments:**

- ✅ Created `server/tests/fixtures/container_fixtures.py` with comprehensive fixtures
- ✅ Fixed critical SQLAlchemy mapper issue (circular dependency via shared Base class)
- ✅ Created `server/models/base.py` for shared declarative base
- ✅ Container initialization working across all test contexts
- ✅ 227/237 tests passing (95.8% success rate)

**Critical Discovery & Fix:**
During implementation, discovered that models using separate `Base(DeclarativeBase)` classes prevented SQLAlchemy from resolving relationship string references. Created shared `server/models/base.py` that all models now use, eliminating the "failed to locate a name" error.

#### 0.1 Create Container Test Fixtures ✅

**Goal:** Provide reusable fixtures that properly initialize ApplicationContainer

**Implementation:** ✅ **COMPLETE**

- ✅ Created `server/tests/fixtures/container_fixtures.py`
- ✅ Implemented `container_test_client` fixture (sync with event loop handling)
- ✅ Implemented `async_container_test_client` fixture
- ✅ Implemented `mock_container` fixture for unit tests
- ✅ Implemented `player_factory` fixture (fixture factory pattern)
- ✅ Implemented `room_factory` fixture (fixture factory pattern)

**Files to Create:**

```python
# server/tests/fixtures/container_fixtures.py

@pytest.fixture
async def test_container():
    """Create ApplicationContainer for testing."""
    from server.container import ApplicationContainer

    container = ApplicationContainer()
    await container.initialize()

    yield container

    await container.shutdown()

@pytest.fixture
def container_test_client(test_container):
    """Create TestClient with ApplicationContainer."""
    from fastapi.testclient import TestClient
    from server.app.factory import create_app

    app = create_app()
    app.state.container = test_container

    # BACKWARD COMPATIBILITY: Also set services directly on app.state
    app.state.persistence = test_container.persistence
    app.state.player_service = test_container.player_service
    # ... etc

    return TestClient(app)

@pytest.fixture
def mock_container():
    """Create mock ApplicationContainer for unit tests."""
    from unittest.mock import MagicMock, AsyncMock

    container = MagicMock()
    container.persistence = AsyncMock()
    container.player_service = MagicMock()
    # ... etc

    return container
```

**Success Criteria:** ✅ **ALL MET**

- ✅ Fixtures available in conftest.py
- ✅ Can create test clients with container
- ✅ Can create mock containers for unit tests
- ✅ Backward compatible with existing tests

#### 0.2 Update conftest.py ✅

**Goal:** Make container fixtures available to all tests

**Changes:** ✅ **COMPLETE**

- ✅ Imported container fixtures in conftest.py
- ✅ Exposed all new fixtures globally
- ✅ Maintained backward compatibility with existing fixtures
- ✅ Added comprehensive docstrings following pytest best practices

**Files Modified:**

- ✅ `server/tests/conftest.py` - Added container fixture imports

**Success Criteria:** ✅ **ALL MET**

- ✅ New fixtures available globally (test_container, container_test_client, async_container_test_client, mock_container, player_factory, room_factory)
- ✅ Existing tests continue to work (227/237 passing)
- ✅ No test breakage from fixture updates

---

### Phase 1: Fix Failing Integration Tests (Week 1-2) 🚧 **IN PROGRESS**

**Current Status:** Infrastructure fixed, now addressing test expectations

#### 1.1 Identify All Failing Tests ✅

**Current Known Failures (10):** ✅ **IDENTIFIED & PARTIALLY FIXED**

- ✅ `test_api_player_creation_error_logging` - **Container working, needs mock config**
- ✅ `test_api_player_deletion_error_logging` - **Container working, needs mock config**
- ✅ `test_api_player_retrieval_error_logging` - **Container working, needs mock config**
- ✅ `test_create_player_success` - **Container working, needs mock config**
- ✅ `test_list_players_success` - **Container working, needs mock config**
- ✅ `test_get_player_success` - **Container working, needs mock config**
- ✅ `test_get_player_by_name_success` - **Container working, needs mock config**
- ✅ `test_delete_player_success` - **Container working, needs mock config**
- ✅ `test_apply_lucidity_loss_success` - **Container working, needs mock config**
- ✅ `test_apply_fear_success` - **Container working, needs mock config**

**Root Cause Analysis:** ✅ **RESOLVED**

- ~~Original Issue: `ApplicationContainer not found in app.state`~~ ✅ **FIXED**
- **New Issue:** Tests hitting real database, getting 404s (expected behavior)
- **Solution:** Update `mock_persistence_for_api` fixture to properly configure mocks

**Files Affected:**

- ✅ `server/tests/coverage/test_error_logging_coverage.py` - **Migrated to container_test_client**
- ✅ `server/tests/integration/api/test_api_players_integration.py` - **Migrated to container_test_client**

#### 1.2 Fix Integration Test Fixtures ✅ **INFRASTRUCTURE COMPLETE**

**Approach:** Update test fixtures to initialize ApplicationContainer

**Status:** Infrastructure working, now need to fix mock configuration

**Pattern Migration:**

**BEFORE (Broken):**

```python
@pytest.fixture
def app():
    app = create_app()
    # Manual app.state setup
    app.state.persistence = get_persistence()
    app.state.player_service = PlayerService(...)
    return app
```

**AFTER (Fixed):**

```python
@pytest.fixture
async def app():
    from server.container import ApplicationContainer

    app = create_app()
    container = ApplicationContainer()
    await container.initialize()

    app.state.container = container
    # BACKWARD COMPATIBILITY: Also set direct references
    app.state.persistence = container.persistence
    app.state.player_service = container.player_service

    yield app

    await container.shutdown()
```

**Files to Update:**

- `server/tests/integration/api/test_api_players_integration.py`
- `server/tests/coverage/test_error_logging_coverage.py`
- Any other integration tests with custom app fixtures

**Success Criteria:**

- All 10 failing tests now pass
- Integration tests use ApplicationContainer
- No new test failures introduced

---

### Phase 2: Modernize Unit Test Patterns (Week 3-4)

#### 2.1 Categorize Unit Tests by Dependency Pattern

**Category A: Pure Unit Tests (No Dependencies)**

- Examples: Utility functions, value objects, simple validators
- **Action:** No changes needed
- **Count:** ~50 test files

**Category B: Service Layer Tests (Mock Dependencies)**

- Examples: PlayerService, RoomService, CombatService tests
- **Action:** Use `mock_container` fixture
- **Count:** ~80 test files

**Category C: Infrastructure Tests (Real Dependencies)**

- Examples: Database, NATS, EventBus tests
- **Action:** Use `test_container` fixture
- **Count:** ~40 test files

**Category D: API Endpoint Tests (App State)**

- Examples: API router tests
- **Action:** Use `container_test_client` fixture
- **Count:** ~30 test files

#### 2.2 Update Category B: Service Layer Tests

**Goal:** Services accept dependencies via constructor, not global state

**Pattern Migration:**

**BEFORE:**

```python
def test_player_service():
    from server.persistence import get_persistence

    persistence = get_persistence()
    service = PlayerService(persistence)
    result = service.get_player("test-id")
    assert result is not None
```

**AFTER:**

```python
def test_player_service(mock_container):
    service = mock_container.player_service
    service.get_player.return_value = MockPlayer()

    result = service.get_player("test-id")
    assert result is not None
```

**Files to Update:**

- `server/tests/unit/services/test_*.py` (~30 files)
- `server/tests/unit/game/test_*.py` (~10 files)

#### 2.3 Update Category C: Infrastructure Tests

**Goal:** Infrastructure tests use real ApplicationContainer

**Pattern Migration:**

**BEFORE:**

```python
def test_database_connection():
    from server.database import DatabaseManager

    db = DatabaseManager.get_instance()
    assert db.engine is not None
```

**AFTER:**

```python
async def test_database_connection(test_container):
    db = test_container.db_manager
    assert db.engine is not None
```

**Files to Update:**

- `server/tests/unit/infrastructure/test_*.py` (~20 files)
- `server/tests/unit/realtime/test_*.py` (~15 files)

#### 2.4 Update Category D: API Tests

**Goal:** API tests use container-initialized test client

**Pattern Migration:**

**BEFORE:**

```python
def test_get_player(test_client):
    response = test_client.get("/api/players/test-id")
    assert response.status_code == 200
```

**AFTER:**

```python
def test_get_player(container_test_client):
    response = container_test_client.get("/api/players/test-id")
    assert response.status_code == 200
```

**Files to Update:**

- `server/tests/unit/api/test_*.py` (~15 files)
- Update test_client fixture usage globally

---

### Phase 3: Modernize Test Patterns (Week 5)

#### 3.1 Adopt Modern pytest Patterns

**Pattern 1: Parametrize Instead of Multiple Tests**

**BEFORE:**

```python
def test_player_creation_valid():
    assert create_player("Alice") is not None

def test_player_creation_empty_name():
    with pytest.raises(ValueError):
        create_player("")

def test_player_creation_long_name():
    with pytest.raises(ValueError):
        create_player("a" * 100)
```

**AFTER:**

```python
@pytest.mark.parametrize("name,should_succeed", [
    ("Alice", True),
    ("", False),
    ("a" * 100, False),
])
def test_player_creation(name, should_succeed):
    if should_succeed:
        assert create_player(name) is not None
    else:
        with pytest.raises(ValueError):
            create_player(name)
```

**Pattern 2: Fixture Factories Instead of Multiple Fixtures**

**BEFORE:**

```python
@pytest.fixture
def test_player_alice():
    return Player(name="Alice", level=1)

@pytest.fixture
def test_player_bob():
    return Player(name="Bob", level=5)

@pytest.fixture
def test_player_charlie():
    return Player(name="Charlie", level=10)
```

**AFTER:**

```python
@pytest.fixture
def player_factory():
    def _create_player(name="TestPlayer", level=1, **kwargs):
        return Player(name=name, level=level, **kwargs)
    return _create_player

def test_something(player_factory):
    alice = player_factory(name="Alice", level=1)
    bob = player_factory(name="Bob", level=5)
```

**Pattern 3: Async Test Helpers**

**BEFORE:**

```python
def test_async_operation():
    loop = asyncio.new_event_loop()
    result = loop.run_until_complete(async_function())
    assert result == expected
```

**AFTER:**

```python
@pytest.mark.asyncio
async def test_async_operation():
    result = await async_function()
    assert result == expected
```

#### 3.2 Eliminate Global State Dependencies

**Goal:** No tests should rely on module-level globals

**Pattern Migration:**

**BEFORE:**

```python
def test_persistence():
    from server.persistence import get_persistence, reset_persistence

    reset_persistence()  # Clear global state
    persistence = get_persistence()
    assert persistence is not None
```

**AFTER:**

```python
def test_persistence(test_container):
    persistence = test_container.persistence
    assert persistence is not None
```

**Files to Update:**

- All tests using `reset_persistence()` (~50 files)
- All tests using `get_persistence()` (~100 files)
- All tests using `reset_config()` (~30 files)

#### 3.3 Consolidate Duplicate Test Fixtures

**Goal:** Reduce fixture proliferation, use fixture factories

**Current Issues:**

- Multiple `test_player` fixtures with slight variations
- Duplicate app initialization patterns
- Inconsistent mock patterns

**Actions:**

1. Audit all fixtures in test files
2. Extract common fixtures to conftest.py
3. Convert specific fixtures to fixture factories
4. Remove duplicate fixture definitions

**Success Criteria:**

- <50 total fixtures (down from ~100+)
- All common fixtures in conftest.py
- No duplicate fixture names

---

### Phase 4: Add Container Integration Tests (Week 6)

#### 4.1 Test ApplicationContainer Itself

**New Tests to Add:**

```python
# server/tests/unit/infrastructure/test_application_container.py

class TestApplicationContainer:
    async def test_container_initialization(self):
        """Test that container initializes all services correctly."""
        container = ApplicationContainer()
        await container.initialize()

        assert container.config is not None
        assert container.database_manager is not None
        assert container.event_bus is not None
        assert container.persistence is not None
        assert container.async_persistence is not None
        assert container.connection_manager is not None
        assert container.player_service is not None

        await container.shutdown()

    async def test_container_shutdown_cleanup(self):
        """Test that container properly cleans up resources."""
        container = ApplicationContainer()
        await container.initialize()
        await container.shutdown()

        # Verify cleanup happened
        assert container.event_bus._running is False

    async def test_container_service_dependencies(self):
        """Test that services have correct dependencies injected."""
        container = ApplicationContainer()
        await container.initialize()

        # Verify dependency injection worked
        assert container.player_service.persistence == container.persistence
        assert container.connection_manager._event_bus == container.event_bus

        await container.shutdown()
```

#### 4.2 Test Dependency Injection

**New Tests to Add:**

```python
# server/tests/unit/infrastructure/test_dependency_injection_container.py

class TestDependencyInjection:
    def test_get_container_from_request(self, container_test_client):
        """Test that get_container() retrieves container from app.state."""
        from server.dependencies import get_container

        # Make a request to trigger dependency injection
        response = container_test_client.get("/api/health")
        # Verify container was accessible (if health check uses it)

    def test_get_player_service_from_container(self, container_test_client):
        """Test that get_player_service() retrieves from container."""
        from server.dependencies import get_player_service

        # Test endpoint that uses get_player_service dependency
        response = container_test_client.get("/api/players")
        assert response.status_code in [200, 401]  # Auth may fail, but DI should work
```

---

## Implementation Phases

### Phase 0: Foundation (Week 1) - 40 hours

**Tasks:**

1. Create `server/tests/fixtures/container_fixtures.py` (8 hours)
2. Implement `test_container` fixture (4 hours)
3. Implement `container_test_client` fixture (4 hours)
4. Implement `async_container_test_client` fixture (4 hours)
5. Implement `mock_container` fixture (4 hours)
6. Update `conftest.py` to expose fixtures (2 hours)
7. Write tests for container fixtures (8 hours)
8. Documentation and examples (6 hours)

**Deliverables:**

- Working container fixtures
- Comprehensive fixture documentation
- Example usage patterns
- All existing tests still pass

### Phase 1: Fix Failing Tests (Week 1-2) - 40 hours

**Tasks:**

1. Update `test_api_players_integration.py` (6 hours)
2. Update `test_error_logging_coverage.py` (6 hours)
3. Fix any cascading failures (10 hours)
4. Verify all integration tests pass (8 hours)
5. Update integration test documentation (4 hours)
6. Create integration test patterns guide (6 hours)

**Deliverables:**

- Zero test failures
- All integration tests use container
- Integration test pattern guide

### Phase 2: Unit Test Modernization (Week 3-4) - 80 hours

**Phase 2A: Service Layer Tests (Week 3)**

1. Audit service layer tests (8 hours)
2. Create service test pattern guide (4 hours)
3. Update PlayerService tests (8 hours)
4. Update RoomService tests (6 hours)
5. Update CombatService tests (8 hours)
6. Update remaining service tests (20 hours)
7. Verify all service tests pass (6 hours)

**Phase 2B: Infrastructure Tests (Week 4)**

1. Audit infrastructure tests (6 hours)
2. Update database tests (8 hours)
3. Update NATS tests (8 hours)
4. Update EventBus tests (8 hours)
5. Update connection manager tests (10 hours)
6. Verify all infrastructure tests pass (8 hours)

**Deliverables:**

- All service tests use mock_container
- All infrastructure tests use test_container
- Service test pattern guide
- Infrastructure test pattern guide

### Phase 3: Test Pattern Modernization (Week 5) - 40 hours

**Tasks:**

1. Audit for parametrize opportunities (8 hours)
2. Convert repetitive tests to parametrized (12 hours)
3. Create fixture factories (8 hours)
4. Eliminate duplicate fixtures (6 hours)
5. Standardize async test patterns (4 hours)
6. Documentation update (2 hours)

**Deliverables:**

- 50% reduction in test code duplication
- <50 total fixtures (down from ~100+)
- Standardized async patterns
- Modern pytest patterns guide

### Phase 4: Add Coverage for New Architecture (Week 6) - 40 hours

**Tasks:**

1. Test ApplicationContainer (8 hours)
2. Test dependency injection (8 hours)
3. Test container lifecycle (8 hours)
4. Test MessageBroker abstraction (8 hours)
5. Test domain layer structure (4 hours)
6. Update coverage reports (4 hours)

**Deliverables:**

- 100% coverage of new architecture
- Container lifecycle tests
- DI pattern validation tests
- Coverage report >85%

---

## Modern Testing Patterns

### Pattern 1: Container-Based Fixtures

```python
@pytest.fixture
async def app_with_container():
    """Create app with fully initialized ApplicationContainer."""
    from server.app.factory import create_app
    from server.container import ApplicationContainer

    app = create_app()
    container = ApplicationContainer()
    await container.initialize()

    app.state.container = container

    yield app

    await container.shutdown()
```

### Pattern 2: Mock Container for Unit Tests

```python
@pytest.fixture
def mock_container():
    """Mock container for isolated unit tests."""
    from unittest.mock import MagicMock, AsyncMock

    container = MagicMock()

    # Mock all services
    container.persistence = AsyncMock()
    container.player_service = MagicMock()
    container.event_bus = MagicMock()

    # Configure common return values
    container.persistence.get_player.return_value = None
    container.player_service.create_player.return_value = MockPlayer()

    return container
```

### Pattern 3: Parametrized Integration Tests

```python
@pytest.mark.parametrize("endpoint,expected_status", [
    ("/api/players", 200),
    ("/api/rooms", 200),
    ("/api/health", 200),
    ("/api/nonexistent", 404),
])
async def test_api_endpoints(container_test_client, endpoint, expected_status):
    response = container_test_client.get(endpoint)
    assert response.status_code == expected_status
```

### Pattern 4: Fixture Factories

```python
@pytest.fixture
def player_factory():
    """Factory for creating test players with varied configurations."""
    def _create(name="TestPlayer", level=1, **kwargs):
        return Player(
            id=str(uuid4()),
            name=name,
            level=level,
            stats=Stats(**kwargs.get("stats", {})),
            **kwargs
        )
    return _create

def test_player_levels(player_factory):
    beginner = player_factory(level=1)
    veteran = player_factory(level=50)
    master = player_factory(level=100)

    assert beginner.level < veteran.level < master.level
```

### Pattern 5: Async Test Context Managers

```python
@pytest.mark.asyncio
async def test_with_container_lifecycle():
    """Test using container as async context manager."""
    from server.container import ApplicationContainer

    async with ApplicationContainer() as container:
        await container.initialize()

        # Test operations
        player = await container.player_service.create_player("Test")
        assert player is not None

        # Container shutdown handled automatically
```

---

## Backward Compatibility Strategy

### Three-Layer Compatibility

**Layer 1: New Tests (Use Container)**

- All new tests use container fixtures
- Follow modern patterns exclusively
- No backward compatibility needed

**Layer 2: Updated Tests (Hybrid)**

- Updated tests use container fixtures
- Maintain fallback to legacy patterns during transition
- Gradual migration path

**Layer 3: Legacy Tests (Unchanged)**

- Existing tests continue to work
- Use legacy fixtures (test_client, etc.)
- Updated only when touched

### Migration Flags

```python
# conftest.py
USE_CONTAINER_FIXTURES = os.getenv("USE_CONTAINER_FIXTURES", "true").lower() == "true"

@pytest.fixture
def test_client():
    """Backward compatible test client."""
    if USE_CONTAINER_FIXTURES:
        # Use new container-based client
        return container_test_client()
    else:
        # Use legacy manual setup
        return legacy_test_client()
```

---

## Testing Requirements

### Phase 0 Testing

- [ ] Container fixtures work correctly
- [ ] Can create test clients with container
- [ ] Existing tests unaffected

### Phase 1 Testing

- [ ] All 10 failing tests now pass
- [ ] No new test failures
- [ ] Integration tests use container

### Phase 2 Testing

- [ ] All service tests use mock_container
- [ ] All infrastructure tests use test_container
- [ ] Test suite passes 100%

### Phase 3 Testing

- [ ] Parametrized tests work correctly
- [ ] Fixture factories work correctly
- [ ] No test duplication

### Phase 4 Testing

- [ ] Container tests achieve 100% coverage
- [ ] DI tests validate proper injection
- [ ] Architecture coverage >85%

---

## Success Metrics

### Quantitative Metrics

| Metric           | Before          | Target | Measurement             |
| ---------------- | --------------- | ------ | ----------------------- |
| Passing Tests    | 224/234 (95.7%) | 100%   | pytest exit code 0      |
| Test Coverage    | ~82%            | >85%   | pytest-cov report       |
| Fixture Count    | ~100+           | <50    | Fixture audit           |
| Code Duplication | High            | Low    | Duplicate code analysis |
| app.state Access | 445 instances   | 0      | grep count              |
| Container Usage  | 0 tests         | 100%   | grep count              |

### Qualitative Metrics

| Quality Attribute     | Before | Target | Notes                            |
| --------------------- | ------ | ------ | -------------------------------- |
| Test Maintainability  | 6/10   | 9/10   | Clear patterns, less duplication |
| Test Clarity          | 7/10   | 9/10   | Modern pytest patterns           |
| Fixture Reusability   | 5/10   | 9/10   | Factories, shared fixtures       |
| Container Integration | 0/10   | 10/10  | All tests use container          |
| Test Speed            | 7/10   | 8/10   | Optimized fixtures               |

---

## Risk Mitigation

### Strategies

1. **Incremental Migration** - Update tests in phases, not all at once
2. **Backward Compatibility** - Maintain legacy fixtures during transition
3. **Continuous Validation** - Run test suite after each phase
4. **Feature Flags** - Use env vars to control fixture behavior
5. **Rollback Points** - Git branch for each phase

### Known Risks

| Risk                    | Probability | Impact | Mitigation                           |
| ----------------------- | ----------- | ------ | ------------------------------------ |
| Breaking existing tests | Medium      | High   | Maintain backward compatibility      |
| Performance regression  | Low         | Medium | Benchmark test execution time        |
| Introducing new bugs    | Medium      | High   | Run full test suite after each phase |
| Time overrun            | Medium      | Medium | Prioritize critical tests first      |

---

## Implementation Approach Decision

### Recommended: **PHASED UPLIFT**

**Pros:**

- ✅ Preserves 5,061 tests worth of domain knowledge
- ✅ 95.7% tests already passing
- ✅ Incremental risk (validate each phase)
- ✅ Faster than greenfield rewrite
- ✅ Maintains test coverage throughout migration

**Cons:**

- ⚠️ May carry forward some technical debt
- ⚠️ Requires maintaining backward compatibility during transition

### Alternative: **GREENFIELD REWRITE**

**Would Choose If:**

- ❌ Test suite fundamentally broken (NOT TRUE - 95.7% pass)
- ❌ Tests unmaintainable (NOT TRUE - well organized)
- ❌ Business logic changed completely (NOT TRUE - same domain)
- ❌ Time not a constraint (NOT TRUE - want to ship features)

**Verdict:** Greenfield not justified. Phased uplift is optimal.

---

## Test Modernization Checklist

### Phase 0: Foundation

- [ ] Create container_fixtures.py
- [ ] Implement test_container fixture
- [ ] Implement container_test_client fixture
- [ ] Implement async_container_test_client fixture
- [ ] Implement mock_container fixture
- [ ] Update conftest.py imports
- [ ] Write fixture documentation
- [ ] Verify existing tests unaffected

### Phase 1: Fix Failures

- [ ] Identify all failing tests (10 known)
- [ ] Update integration test fixtures
- [ ] Fix test_api_players_integration.py
- [ ] Fix test_error_logging_coverage.py
- [ ] Verify all tests pass
- [ ] Document integration patterns

### Phase 2: Modernize Units

- [ ] Categorize all unit tests (A/B/C/D)
- [ ] Update Category B (service tests)
- [ ] Update Category C (infrastructure tests)
- [ ] Update Category D (API tests)
- [ ] Verify all units pass
- [ ] Document unit test patterns

### Phase 3: Pattern Updates

- [ ] Identify parametrize opportunities
- [ ] Convert to parametrized tests
- [ ] Create fixture factories
- [ ] Eliminate duplicate fixtures
- [ ] Standardize async patterns
- [ ] Update test documentation

### Phase 4: New Coverage

- [ ] Write ApplicationContainer tests
- [ ] Write dependency injection tests
- [ ] Write MessageBroker tests
- [ ] Write domain layer tests
- [ ] Verify coverage >85%
- [ ] Update coverage reports

---

## Timeline Estimate

| Phase                    | Duration    | Effort        | Deliverables          |
| ------------------------ | ----------- | ------------- | --------------------- |
| Phase 0: Foundation      | Week 1      | 40 hours      | Container fixtures    |
| Phase 1: Fix Failures    | Week 1-2    | 40 hours      | Zero test failures    |
| Phase 2: Modernize Units | Week 3-4    | 80 hours      | Modern unit tests     |
| Phase 3: Pattern Updates | Week 5      | 40 hours      | Clean patterns        |
| Phase 4: New Coverage    | Week 6      | 40 hours      | Architecture tests    |
| **Total**                | **6 weeks** | **240 hours** | **Modern test suite** |

**Note:** Can be parallelized with feature work after Phase 1 (zero failures)

---

## Quick Start: Minimal Viable Uplift

If time is constrained, this minimal approach fixes critical issues:

### Week 1: Critical Fixes Only

1. **Create minimal container fixture** (4 hours)

   ```python
   @pytest.fixture
   async def test_container():
       container = ApplicationContainer()
       await container.initialize()
       yield container
       await container.shutdown()
   ```

2. **Fix 10 failing tests** (8 hours)
   - Update fixtures to use container
   - Verify tests pass

3. **Document pattern** (2 hours)
   - Example for other developers

**Result:** Test suite passes, minimal disruption, foundation for future work

---

## References

### Related Documentation

- `ARCHITECTURE_REMEDIATION_PLAN.md` - Architecture changes requiring test updates
- `ARCHITECTURE_IMPLEMENTATION_SUMMARY.md` - Completed architecture work
- `.cursor/rules/pytest.mdc` - Pytest best practices
- `docs/DEVELOPMENT_AI.md` - Development guidelines

### Key Files

- `server/tests/conftest.py` - Global test fixtures
- `server/container.py` - ApplicationContainer implementation
- `server/dependencies.py` - Dependency injection functions
- `server/app/lifespan.py` - Application lifecycle

### Testing Resources

- pytest documentation: <https://docs.pytest.org/>
- pytest-asyncio: <https://pytest-asyncio.readthedocs.io/>
- FastAPI testing: <https://fastapi.tiangolo.com/tutorial/testing/>

---

## Appendices

### Appendix A: Test File Inventory

**Unit Tests by Category:**

- API: 15 files
- Commands: 25 files
- Chat: 8 files
- Services: 30 files
- Infrastructure: 20 files
- Models: 12 files
- Events: 10 files
- Realtime: 15 files
- Other: 49 files

**Integration Tests:** 42 files
**E2E Tests:** 8 files
**Other:** 20 files

### Appendix B: Direct app.state Access Locations

**High Priority (Integration Tests):**

- `server/tests/integration/api/*.py` (18 files, 50 instances)
- `server/tests/integration/comprehensive/*.py` (3 files, 20 instances)

**Medium Priority (Unit Tests):**

- `server/tests/unit/services/*.py` (30 files, 100 instances)
- `server/tests/unit/infrastructure/*.py` (20 files, 80 instances)

**Low Priority (Other):**

- `server/tests/coverage/*.py` (5 files, 40 instances)
- `server/tests/e2e/*.py` (8 files, 30 instances)

### Appendix C: Fixture Audit

**Current Fixture Categories:**

- App fixtures: test_client, async_test_client, app
- Database fixtures: test_database, test_npc_database
- Service fixtures: Various per-service fixtures
- Mock fixtures: Various per-component mocks
- Data fixtures: test players, rooms, NPCs

**Consolidation Opportunities:**

- Merge similar player fixtures into player_factory
- Consolidate app fixtures into container-based versions
- Standardize mock patterns with mock_container

---

## Next Steps

**Immediate (This Session):**

1. Review and approve this plan
2. Decide: Full uplift or minimal viable uplift?
3. Begin Phase 0 implementation

**Short Term (Week 1):**

1. Create container fixtures
2. Fix 10 failing tests
3. Achieve 100% test pass rate

**Medium Term (Weeks 2-6):**

1. Modernize all tests progressively
2. Adopt modern pytest patterns
3. Achieve >85% coverage

---

**Implementation Ready:** Awaiting Professor Wolfshade's approval to proceed
