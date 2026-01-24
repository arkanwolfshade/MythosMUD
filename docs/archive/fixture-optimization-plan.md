# Container Test Client Fixture Optimization Plan

## Current State Analysis

### Fixture: `container_test_client`

**Location**: `server/tests/fixtures/container_fixtures.py:130`

**Scope**: `function` (recreated for every test)

**Current setup time**: 26-30 seconds per test
- **Affected tests**: ~60 tests across multiple files

### Root Causes of Slow Setup

1. **ApplicationContainer initialization** (most expensive):

   - Database connection setup
   - Service layer initialization
   - EventBus setup
   - NATS service initialization
   - Cache service initialization
   - All happens synchronously in a new event loop

2. **FastAPI app creation** (`create_app()`):

   - Middleware stack initialization
   - Router registration
   - Dependency injection setup

3. **Event loop creation**:

   - Creating new event loop for each test
   - Running async initialization synchronously

4. **Database connection management**:

   - Connecting to PostgreSQL
   - Creating database engines
   - Setting up connection pools

## Optimization Strategy

### Phase 1: Fixture Scope Optimization (Immediate Impact)

**Option A: Class-scoped fixture** (Recommended for test classes)

- Change scope from `function` to `class`
- Share same container/app instance across all tests in a class
- **Pros**: 26-30s setup once per class instead of per test
- **Cons**: Need to ensure tests don't modify shared state
- **Impact**: For a class with 19 tests, saves ~500 seconds (8+ minutes)

**Option B: Module-scoped fixture** (For files with multiple classes)

- Share across entire test file
- **Pros**: Maximum sharing
- **Cons**: Higher risk of test pollution
- **Impact**: Largest time savings but requires careful state management

### Phase 2: App Instance Caching (Medium Impact)

Cache FastAPI app instance (app creation is expensive)

- Reuse app across fixtures where possible
- Reset state instead of recreating

### Phase 3: Container Initialization Optimization (Long-term)

Lazy initialization of services

- Connection pooling improvements
- Reduce redundant setup steps

## Recommended Implementation

### Step 1: Create class-scoped variant of container_test_client

Create a new fixture `container_test_client_class` with class scope that can be used for test classes that don't need strict isolation.

### Step 2: Update test classes to use class-scoped fixture

For test classes that don't modify shared container state, use the class-scoped fixture instead.

### Step 3: Verify test isolation

Ensure tests within classes don't interfere with each other when sharing the container.

## Implementation Details

```python
@pytest.fixture(scope="class")
def container_test_client_class():
    """Class-scoped version for tests that don't modify shared state."""
    # Same implementation as container_test_client but scope="class"
    # Add state reset between tests if needed

```

## Expected Impact

**Current**: 60 tests × 27s setup = 1,620 seconds overhead

**After class-scope**: ~6-8 classes × 27s setup = 162-216 seconds overhead

**Time saved**: ~1,400 seconds (23+ minutes)
- **New total test time**: ~6-8 minutes (within target range)

## Risk Assessment

**Low Risk**:

- Tests that only read from container (most API endpoint tests)
- Tests that mock persistence (can reset mocks between tests)

**Medium Risk**:

- Tests that modify app.state.container
- Tests that add dependency overrides

**Mitigation**:

- Add cleanup/reset logic between tests in class scope
- Use function scope where needed for tests that modify state
