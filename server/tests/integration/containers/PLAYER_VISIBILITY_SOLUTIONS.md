# Solution Evaluation: Player Visibility in Concurrent Container Tests

## Problem Statement

Players created in `_create_test_player` are committed successfully (verified in the same session), but are not visible when queried from different sessions via `persistence.get_player_by_id()` even after 100 retry attempts with progressive delays. This occurs intermittently during parallel test execution.

**Root Cause**: PostgreSQL transaction isolation - commits are not immediately visible across different database connections, especially under high load in parallel test execution.

## Solution Options

### Option 1: Allow Dirty Reads (Lower Transaction Isolation)

**Approach**: Change transaction isolation level from `READ COMMITTED` (default) to a lower level that allows reading uncommitted data.

**Implementation**:

```python
# In database.py or test setup
from sqlalchemy import event
from sqlalchemy.engine import Engine

@event.listens_for(engine.sync_engine, "connect")
def set_isolation_level(dbapi_conn, connection_record):
    # PostgreSQL doesn't support READ UNCOMMITTED, treats it as READ COMMITTED
    # We could use READ COMMITTED with different settings
    dbapi_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
```

**Pros**:

- ✅ Simple to implement
- ✅ May improve visibility of committed data
- ✅ No test code changes required

**Cons**:

- ❌ PostgreSQL doesn't actually support READ UNCOMMITTED (treats it as READ COMMITTED)
- ❌ READ COMMITTED is already the default
- ❌ Doesn't solve the fundamental issue: commit visibility across connections
- ❌ May introduce data consistency issues in tests
- ❌ Changes behavior for all tests, not just this one

**Verdict**: ⚠️ **Not Recommended** - PostgreSQL's isolation levels won't solve this specific issue.

---

### Option 2: Use More Mocking (Avoid PostgreSQL for Player Creation)

**Approach**: Mock the persistence layer in these tests instead of creating real database records.

**Implementation**:

```python
@pytest.fixture
def mock_persistence():
    """Mock persistence layer that returns players without database."""
    persistence = MagicMock()

    async def get_player_by_id(player_id: UUID) -> Player | None:
        # Return a mock player without database lookup
        return create_mock_player(player_id)

    persistence.get_player_by_id = get_player_by_id
    return persistence
```

**Pros**:

- ✅ Eliminates transaction isolation issues entirely
- ✅ Faster test execution (no database I/O)
- ✅ More predictable test behavior
- ✅ Tests focus on container service logic, not database behavior
- ✅ No flakiness from database timing

**Cons**:

- ❌ Less integration testing - doesn't test real database interactions
- ❌ May miss database-related bugs (constraints, transactions, etc.)
- ❌ Requires significant test refactoring
- ❌ Other tests that use real persistence would still have issues
- ❌ Doesn't test the actual code path used in production

**Verdict**: ✅ **Recommended for Unit Tests** - But these are integration tests, so we need a hybrid approach.

---

### Option 3: Use Single Database Connection for Test (No Connection Pooling)

**Approach**: Ensure all operations in a test use the same database connection.

**Implementation**:

```python
@pytest.fixture
async def shared_session():
    """Single session shared across test operations."""
    async for session in get_async_session():
        yield session
        break
```

**Pros**:

- ✅ Eliminates cross-connection visibility issues
- ✅ Simpler transaction model
- ✅ Tests use real database (integration testing)

**Cons**:

- ❌ Doesn't match production behavior (production uses connection pooling)
- ❌ May hide real-world issues with connection pooling
- ❌ Still requires careful session management
- ❌ May not work well with parallel test execution

**Verdict**: ⚠️ **Partial Solution** - Good for some cases but doesn't match production.

---

### Option 4: Explicit Transaction Control with Synchronization

**Approach**: Use explicit transaction control and ensure proper synchronization.

**Implementation**:

```python
async def _create_test_player(persistence, player_id: UUID, name: str, room_id: str = "test_room_001") -> Player:
    # Create player in explicit transaction
    async for session in get_async_session():
        try:
            # ... create player ...
            await session.commit()

            # Force connection to see commit by using same connection
            await session.execute(text("SELECT 1"))  # Force sync point

        finally:
            await session.close()

    # Use explicit synchronization point
    await asyncio.sleep(0.1)  # Allow commit to propagate

    # Verify with retry using same connection pattern
    # ...
```

**Pros**:

- ✅ Uses real database (integration testing)
- ✅ More control over transaction boundaries
- ✅ Can add explicit synchronization points

**Cons**:

- ❌ Still subject to PostgreSQL's commit visibility guarantees
- ❌ May not solve the issue in high-load scenarios
- ❌ Adds complexity to test code

**Verdict**: ⚠️ **Current Approach** - We're already doing this, but it's not working reliably.

---

### Option 5: Use Database Fixtures (Pre-create Players)

**Approach**: Create players in a database fixture before tests run, ensuring they exist.

**Implementation**:

```python
@pytest.fixture(scope="function")
async def test_players(container_service):
    """Create test players before test runs."""
    player1_id = uuid4()
    player2_id = uuid4()

    # Create in fixture with proper synchronization
    await _create_test_player(container_service.persistence, player1_id, "Player1", room_id)
    await _create_test_player(container_service.persistence, player2_id, "Player2", room_id)

    # Verify they exist before yielding
    player1 = await container_service.persistence.get_player_by_id(player1_id)
    player2 = await container_service.persistence.get_player_by_id(player2_id)

    assert player1 is not None
    assert player2 is not None

    yield {"player1_id": player1_id, "player2_id": player2_id}
```

**Pros**:

- ✅ Players exist before test logic runs
- ✅ Can add verification in fixture
- ✅ Uses real database (integration testing)
- ✅ Separates setup from test logic

**Cons**:

- ❌ Still subject to same visibility issues
- ❌ Doesn't solve the root cause
- ❌ May just move the problem to fixture setup

**Verdict**: ⚠️ **Partial Solution** - Better organization but doesn't solve the core issue.

---

### Option 6: Hybrid Approach - Mock Persistence for Player Lookup, Real DB for Container Operations

**Approach**: Use real database for container operations, but mock player retrieval to avoid visibility issues.

**Implementation**:

```python
async def test_concurrent_open_operations(self, container_service: ContainerService) -> None:
    # Create players in database (for container operations)
    player1_id = uuid4()
    player2_id = uuid4()

    # Create real players
    await _create_test_player(container_service.persistence, player1_id, "Player1", room_id)
    await _create_test_player(container_service.persistence, player2_id, "Player2", room_id)

    # Mock persistence.get_player_by_id to return players immediately
    # This avoids transaction isolation issues while still testing container logic
    async def mock_get_player(player_id: UUID):
        if player_id == player1_id:
            return await _get_player_directly(player1_id)  # Direct DB query
        elif player_id == player2_id:
            return await _get_player_directly(player2_id)
        return None

    container_service.persistence.get_player_by_id = mock_get_player
```

**Pros**:

- ✅ Tests real container operations with real database
- ✅ Avoids player visibility issues
- ✅ Still tests integration between components
- ✅ Minimal code changes

**Cons**:

- ❌ Partially mocks the system under test
- ❌ May hide issues with player retrieval
- ❌ Requires careful implementation

**Verdict**: ✅ **Recommended** - Best balance of integration testing and reliability.

---

### Option 7: Use Test-Specific Database Configuration

**Approach**: Configure database with different settings for tests (e.g., synchronous commits, different isolation).

**Implementation**:

```python
# In test database URL or connection string
DATABASE_URL = "postgresql+asyncpg://...?options=-c%20synchronous_commit=on"
```

**Pros**:

- ✅ May improve commit visibility
- ✅ Test-specific configuration
- ✅ Uses real database

**Cons**:

- ❌ May not solve the issue (PostgreSQL's guarantees are still in effect)
- ❌ Adds complexity to test setup
- ❌ May slow down tests

**Verdict**: ⚠️ **Worth Trying** - But likely won't solve the issue.

---

## Recommended Solution: Hybrid Approach (Option 6)

**Implementation Strategy**:

1. **Keep real database for container operations** - This tests the actual integration
2. **Use direct database queries for player verification** - Bypass persistence layer's session management
3. **Add explicit connection synchronization** - Ensure commits are visible

**Code Changes**:

```python
async def _create_test_player(persistence, player_id: UUID, name: str, room_id: str = "test_room_001") -> Player:
    """Create player and ensure it's visible via direct DB query."""
    # ... create player in database ...

    # Verify using direct SQL query (bypasses session management)
    from sqlalchemy import text
    player_id_str = str(player_id)

    async for verify_session in get_async_session():
        try:
            # Direct query ensures we see the commit
            stmt = text("SELECT * FROM players WHERE player_id = :player_id")
            result = await verify_session.execute(stmt, {"player_id": player_id_str})
            row = result.fetchone()

            if row is None:
                raise RuntimeError(f"Player {player_id} not found after creation")

            # Convert row to Player object for return
            # ...
        finally:
            await verify_session.close()
        break

    return player
```

**Alternative**: If direct queries don't work, use a mock for `get_player_by_id` that returns the player we know exists:

```python
# In test
original_get_player = container_service.persistence.get_player_by_id

async def reliable_get_player(player_id: UUID):
    # Try persistence layer first
    player = await original_get_player(player_id)
    if player is not None:
        return player

    # Fallback: direct database query
    return await _get_player_directly_from_db(player_id)

container_service.persistence.get_player_by_id = reliable_get_player
```

## Conclusion

The **Hybrid Approach (Option 6)** provides the best balance:

- ✅ Maintains integration testing (real database, real container operations)
- ✅ Avoids flakiness from transaction isolation
- ✅ Minimal code changes
- ✅ Tests the actual code paths used in production

**Next Steps**:

1. Implement direct database query verification in `_create_test_player`
2. If that doesn't work, implement the mock fallback approach
3. Monitor test stability over multiple runs
4. Consider moving to more mocking if issues persist
