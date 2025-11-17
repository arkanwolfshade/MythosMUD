# PostgreSQL Code Review - feature/sqlite-to-postgresql Branch

**Review Date:** 2025-01-27
**Reviewer:** AI Code Review Agent
**Branch:** feature/sqlite-to-postgresql
**Base:** main

## Executive Summary

This review identified **8 critical issues**, **5 performance issues**, and **3 code quality issues** related to PostgreSQL best practices. The issues range from security concerns (SELECT * over-fetching) to performance problems (missing indexes, inefficient connection management) to code quality issues (transaction management).

## Critical Issues

### 1. ⚠️ **SELECT * Anti-Pattern (Multiple Files)**

**Severity:** High
**Impact:** Performance degradation, unnecessary data transfer, potential security issues

**Location:** Multiple files use `SELECT *` instead of specifying columns

**Files Affected:**
- `server/async_persistence.py` (lines 123, 159, 193, 306, 351, 514, 558)
- `server/persistence.py` (lines 556, 585, 614, 820, 849, 1010, 1041)

**Issue:**
PostgreSQL best practices explicitly state: "Avoid using `SELECT *` and specify only the necessary columns." Using `SELECT *`:
- Transfers unnecessary data over the network
- Prevents query optimization
- Makes code brittle to schema changes
- Can expose sensitive columns unintentionally

**Example:**
```python
# ❌ WRONG - server/async_persistence.py:123
row = await conn.fetchrow("SELECT * FROM players WHERE name = $1", name)

# ✅ CORRECT
row = await conn.fetchrow(
    "SELECT player_id, user_id, name, current_room_id, profession_id, "
    "experience_points, level, stats, inventory, status_effects, "
    "created_at, last_active, is_admin FROM players WHERE name = $1",
    name
)
```

**Recommendation:**
Replace all `SELECT *` queries with explicit column lists. Consider creating helper functions or constants for common column sets.

---

### 2. 🔴 **Missing Index on Frequently Queried Column**

**Severity:** Critical
**Impact:** Severe performance degradation on common queries

**Location:** `db/schema/04_runtime_tables.sql`

**Issue:**
The `current_room_id` column in the `players` table is frequently queried (used in `get_players_in_room()` operations) but has no index. This causes full table scans on every room query.

**Evidence:**
- Query pattern: `SELECT * FROM players WHERE current_room_id = $1` (async_persistence.py:351)
- Query pattern: `SELECT * FROM players WHERE current_room_id = %s` (persistence.py:849)
- No index exists: `grep` found no index on `current_room_id`

**Current Schema:**
```sql
CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_players_user_id ON players(user_id);
CREATE INDEX IF NOT EXISTS idx_players_is_admin ON players(is_admin);
CREATE INDEX IF NOT EXISTS idx_players_profession_id ON players(profession_id);
-- ❌ MISSING: idx_players_current_room_id
```

**Recommendation:**
Add index to `db/schema/04_runtime_tables.sql`:
```sql
CREATE INDEX IF NOT EXISTS idx_players_current_room_id ON players(current_room_id);
```

---

### 3. 🔴 **Inefficient Connection Management in AsyncPersistenceLayer**

**Severity:** Critical
**Impact:** Performance degradation, connection exhaustion, resource waste

**Location:** `server/async_persistence.py`

**Issue:**
Every database operation creates a new connection and closes it immediately. This is extremely inefficient and violates PostgreSQL connection management best practices.

**Evidence:**
```python
# ❌ WRONG - Creates new connection for EVERY operation
async def get_player_by_name(self, name: str) -> Player | None:
    url = self.db_path.replace("postgresql+asyncpg://", "postgresql://")
    conn = await asyncpg.connect(url)  # New connection
    try:
        row = await conn.fetchrow("SELECT * FROM players WHERE name = $1", name)
    finally:
        await conn.close()  # Close immediately
```

This pattern is repeated in:
- `get_player_by_name()` (line 120)
- `get_player_by_id()` (line 156)
- `get_player_by_user_id()` (line 190)
- `save_player()` (line 225)
- `list_players()` (line 304)
- `get_players_in_room()` (line 349)
- `save_players()` (line 394)
- `delete_player()` (line 467)
- `get_professions()` (line 512)
- `get_profession_by_id()` (line 556)

**PostgreSQL Best Practice:**
"Use connection pooling to reduce the overhead of establishing new connections."

**Recommendation:**
1. Use asyncpg connection pool instead of creating connections per operation
2. Implement connection reuse pattern similar to `PostgresConnectionPool` in `postgres_adapter.py`
3. Consider using SQLAlchemy's async session management (already available via `DatabaseManager`)

**Example Fix:**
```python
class AsyncPersistenceLayer:
    def __init__(self, ...):
        self._pool: asyncpg.Pool | None = None

    async def _get_pool(self) -> asyncpg.Pool:
        if self._pool is None:
            url = self.db_path.replace("postgresql+asyncpg://", "postgresql://")
            self._pool = await asyncpg.create_pool(
                url,
                min_size=1,
                max_size=10,
                command_timeout=60
            )
        return self._pool

    async def get_player_by_name(self, name: str) -> Player | None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow("SELECT ... FROM players WHERE name = $1", name)
            # Connection automatically returned to pool
```

---

### 4. ⚠️ **Transaction Management Issues**

**Severity:** Medium-High
**Impact:** Data consistency risks, potential data corruption

**Location:** `server/async_persistence.py`, `server/persistence.py`

**Issue:**
Some operations that should be transactional are not explicitly wrapped in transactions. PostgreSQL best practices state: "Use explicit transactions to ensure data consistency and atomicity."

**Evidence:**
- `save_players()` in `async_persistence.py` (line 383) saves multiple players in a loop without a transaction
- If one player save fails, previous saves are not rolled back
- No explicit `BEGIN`/`COMMIT`/`ROLLBACK` in async operations

**Recommendation:**
Wrap multi-step operations in explicit transactions:
```python
async def save_players(self, players: list[Player]) -> None:
    pool = await self._get_pool()
    async with pool.acquire() as conn:
        async with conn.transaction():  # Explicit transaction
            for player in players:
                # Save operations
```

---

### 5. ⚠️ **Missing Index on respawn_room_id**

**Severity:** Medium
**Impact:** Performance degradation if respawn queries are added

**Location:** `db/schema/04_runtime_tables.sql`

**Issue:**
The `respawn_room_id` column has no index. While not currently queried, if respawn functionality is implemented, this will cause performance issues.

**Recommendation:**
Add index proactively:
```sql
CREATE INDEX IF NOT EXISTS idx_players_respawn_room_id ON players(respawn_room_id);
```

---

### 6. ⚠️ **Potential N+1 Query Problem**

**Severity:** Medium
**Impact:** Performance degradation under load

**Location:** `server/async_persistence.py:383` (`save_players()`)

**Issue:**
The `save_players()` method saves players one-by-one in a loop. This creates N queries instead of a single batch operation.

**Current Code:**
```python
for player in players:
    await conn.execute("INSERT INTO players ... ON CONFLICT ...")
```

**PostgreSQL Best Practice:**
"Use JOIN operations instead of subqueries where possible" and "Consider using batch operations for bulk inserts."

**Recommendation:**
Use PostgreSQL's `COPY` or batch insert with `executemany()`:
```python
# Option 1: Use executemany for batch operations
await conn.executemany(
    "INSERT INTO players ... ON CONFLICT ...",
    [player_data_1, player_data_2, ...]
)

# Option 2: Use asyncpg's copy_records_to_table for large batches
```

---

### 7. ⚠️ **No Query Performance Monitoring**

**Severity:** Medium
**Impact:** Cannot identify slow queries

**Location:** All database query code

**Issue:**
PostgreSQL best practices recommend: "Use `EXPLAIN ANALYZE` to analyze query execution plans and identify performance bottlenecks." There's no query performance monitoring or slow query logging.

**Recommendation:**
1. Enable PostgreSQL's `log_min_duration_statement` for slow query logging
2. Add query timing in application code
3. Consider using `pg_stat_statements` extension for query analysis

---

### 8. ⚠️ **Missing Foreign Key Indexes**

**Severity:** Low-Medium
**Impact:** Slower foreign key constraint checks

**Location:** `db/schema/04_runtime_tables.sql`

**Issue:**
PostgreSQL automatically creates indexes on primary keys, but foreign keys should also be indexed for optimal performance. Some foreign keys are indexed (e.g., `idx_players_user_id`), but we should verify all are covered.

**Current State:**
- ✅ `user_id` has index: `idx_players_user_id`
- ✅ `profession_id` has index: `idx_players_profession_id`
- ❓ Need to verify all foreign keys have indexes

**Recommendation:**
Audit all foreign key columns and ensure they have indexes. PostgreSQL doesn't automatically index foreign keys.

---

## Performance Issues

### 9. **Connection Pool Configuration**

**Location:** `server/database.py:147-153`

**Current Configuration:**
```python
pool_kwargs.update({
    "pool_size": 5,
    "max_overflow": 10,
    "pool_timeout": 30,
})
```

**Issue:**
Pool size may be too small for high-concurrency scenarios. No configuration option to adjust based on environment.

**Recommendation:**
- Make pool size configurable via environment variables
- Consider increasing default for production
- Document pool sizing guidelines

---

### 10. **No Connection Timeout Configuration**

**Location:** `server/async_persistence.py`, `server/database.py`

**Issue:**
No explicit connection timeout configuration. PostgreSQL best practices recommend: "Configure connection timeouts to prevent idle connections from consuming resources."

**Recommendation:**
Add connection timeout configuration:
```python
self._pool = await asyncpg.create_pool(
    url,
    min_size=1,
    max_size=10,
    command_timeout=60,  # Query timeout
    server_settings={
        'statement_timeout': '30s'  # PostgreSQL-level timeout
    }
)
```

---

## Code Quality Issues

### 11. **Inconsistent Error Handling**

**Location:** `server/async_persistence.py`

**Issue:**
Some operations catch `asyncpg.PostgresError` specifically, others catch generic `Exception`. This makes error handling inconsistent.

**Recommendation:**
Standardize error handling patterns across all database operations.

---

### 12. **Missing Query Comments**

**Location:** All SQL query code

**Issue:**
PostgreSQL best practices state: "Use clear and concise comments to explain complex logic and intentions." Complex queries lack explanatory comments.

**Recommendation:**
Add comments to complex queries explaining business logic:
```python
# Get all players in a room for broadcasting messages
# Uses index on current_room_id for optimal performance
rows = await conn.fetch("SELECT ... FROM players WHERE current_room_id = $1", room_id)
```

---

### 13. **No Prepared Statement Caching**

**Location:** `server/async_persistence.py`

**Issue:**
asyncpg supports prepared statement caching, but it's not being used. This can improve performance for frequently executed queries.

**Recommendation:**
Use asyncpg's prepared statement support for frequently executed queries:
```python
# Prepare statement once
stmt = await conn.prepare("SELECT ... FROM players WHERE name = $1")

# Reuse prepared statement
row = await stmt.fetchrow(name)
```

---

## Summary of Recommendations

### Immediate Actions (Critical):
1. ✅ Add index on `current_room_id` column
2. ✅ Replace all `SELECT *` with explicit column lists
3. ✅ Implement connection pooling in `AsyncPersistenceLayer`
4. ✅ Add explicit transactions to multi-step operations

### High Priority:
5. ✅ Add index on `respawn_room_id` (proactive)
6. ✅ Optimize `save_players()` to use batch operations
7. ✅ Add query performance monitoring

### Medium Priority:
8. ✅ Audit and add indexes for all foreign keys
9. ✅ Make connection pool size configurable
10. ✅ Add connection timeout configuration
11. ✅ Standardize error handling patterns
12. ✅ Add query comments for complex operations
13. ✅ Implement prepared statement caching

---

## Files Requiring Changes

1. `db/schema/04_runtime_tables.sql` - Add missing indexes
2. `server/async_persistence.py` - Connection pooling, SELECT *, transactions
3. `server/persistence.py` - SELECT * replacements
4. `server/database.py` - Connection pool configuration
5. `server/config/models.py` - Add pool configuration options (if needed)

---

## Testing Recommendations

After implementing fixes, test:
1. Query performance with `EXPLAIN ANALYZE`
2. Connection pool behavior under load
3. Transaction rollback scenarios
4. Batch insert performance vs. individual inserts

---

## References

- PostgreSQL Best Practices: `.cursor/rules/postgresql.mdc`
- SQLAlchemy Async Best Practices: `docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md`
- Connection Pooling: PostgreSQL documentation on connection pooling
