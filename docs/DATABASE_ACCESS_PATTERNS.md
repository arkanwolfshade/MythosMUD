# Database Access Patterns

This document explains when to use each database access pattern in the MythosMUD codebase and provides guidance on migrating between patterns.

## Overview

The codebase currently uses three different database access patterns:

1. **PersistenceLayer** (sync psycopg2) - Legacy synchronous code
2. **AsyncPersistenceLayer** (async asyncpg) - New async code, performance-critical
3. **SQLAlchemy ORM** (async) - Preferred for new code, relationships, complex queries

## Pattern 1: PersistenceLayer (Synchronous psycopg2)

**Location**: `server/persistence.py`

**When to Use**:
- Legacy synchronous code that hasn't been migrated yet
- Code that must remain synchronous for compatibility
- Migration path from SQLite to PostgreSQL

**Characteristics**:
- Uses `psycopg2` for synchronous PostgreSQL connections
- Raw SQL queries with parameterized placeholders (`%s`)
- Thread-safe with `RLock`
- Connection pooling via `PostgresConnectionPool`

**Example**:
```python
from server.persistence import get_persistence

persistence = get_persistence()
player = persistence.get_player_by_name("Alice")
```

**Limitations**:
- Blocks the event loop (not suitable for async code)
- No eager loading support (raw SQL)
- Manual relationship handling

**Migration Path**:
- Use `AsyncPersistenceLayer` for new async code
- Migrate to SQLAlchemy ORM for relationship-heavy queries

## Pattern 2: AsyncPersistenceLayer (Asynchronous asyncpg)

**Location**: `server/async_persistence.py`

**When to Use**:
- New async code paths
- Performance-critical operations
- When you need async but don't need ORM features
- Direct asyncpg connection pool access

**Characteristics**:
- Uses `asyncpg` for true async PostgreSQL operations
- Raw SQL queries with parameterized placeholders (`$1`, `$2`, etc.)
- Connection pooling with configurable pool size
- Non-blocking event loop operations

**Example**:
```python
from server.async_persistence import get_async_persistence

async_persistence = get_async_persistence()
player = await async_persistence.get_player_by_id(player_id)
```

**Advantages**:
- True async (doesn't block event loop)
- Better performance than sync layer
- Connection pooling built-in

**Limitations**:
- No eager loading support (raw SQL)
- Manual relationship handling
- More verbose than ORM

**Migration Path**:
- Migrate to SQLAlchemy ORM when you need relationships or complex queries

## Pattern 3: SQLAlchemy ORM (Asynchronous)

**Location**: `server/database.py`, `server/services/`, `server/game/`

**When to Use**:
- **Preferred for all new code**
- When you need relationship access (e.g., `Player.user`)
- Complex queries with joins
- When you want eager loading to prevent N+1 queries
- Type-safe queries with IDE autocomplete

**Characteristics**:
- Uses SQLAlchemy 2.0 async ORM
- Async session management via `get_async_session()` dependency
- Eager loading support (`selectinload`, `joinedload`)
- Type-safe model access

**Example**:
```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from server.database import get_async_session
from server.models.player import Player

async for session in get_async_session():
    # Eagerly load user relationship to prevent N+1 queries
    stmt = select(Player).options(
        selectinload(Player.user)
    ).where(Player.player_id == player_id)

    result = await session.execute(stmt)
    player = result.scalar_one_or_none()
```

**Advantages**:
- Eager loading prevents N+1 queries
- Type-safe with IDE support
- Relationship handling automatic
- Complex queries easier to write
- Follows SQLAlchemy best practices

**Limitations**:
- Slightly more overhead than raw SQL
- Requires understanding of SQLAlchemy ORM

## Decision Tree

```
Do you need relationships (e.g., Player.user)?
├─ Yes → Use SQLAlchemy ORM (Pattern 3)
└─ No → Is this async code?
    ├─ Yes → Use AsyncPersistenceLayer (Pattern 2)
    └─ No → Use PersistenceLayer (Pattern 1) [Legacy]
```

## Migration Strategy

### From PersistenceLayer to AsyncPersistenceLayer

**When**: Migrating sync code to async

**Steps**:
1. Change method signature to `async def`
2. Replace `get_persistence()` with `get_async_persistence()`
3. Add `await` to all persistence calls
4. Change `%s` placeholders to `$1`, `$2`, etc. (if writing raw SQL)
5. Update error handling for async exceptions

**Example**:
```python
# Before (sync)
def get_player(name: str) -> Player | None:
    persistence = get_persistence()
    return persistence.get_player_by_name(name)

# After (async)
async def get_player(name: str) -> Player | None:
    async_persistence = get_async_persistence()
    return await async_persistence.get_player_by_name(name)
```

### From AsyncPersistenceLayer to SQLAlchemy ORM

**When**: You need relationships or want better query capabilities

**Steps**:
1. Replace raw SQL with SQLAlchemy `select()` statements
2. Use `get_async_session()` dependency for session management
3. Add eager loading with `selectinload()` where needed
4. Use model classes instead of raw dictionaries

**Example**:
```python
# Before (raw SQL)
async def get_player(player_id: str) -> Player | None:
    async_persistence = get_async_persistence()
    return await async_persistence.get_player_by_id(player_id)

# After (ORM with eager loading)
async def get_player(
    player_id: str,
    session: AsyncSession = Depends(get_async_session)
) -> Player | None:
    from sqlalchemy import select
    from sqlalchemy.orm import selectinload

    stmt = select(Player).options(
        selectinload(Player.user)
    ).where(Player.player_id == player_id)

    result = await session.execute(stmt)
    return result.scalar_one_or_none()
```

## Performance Considerations

### Raw SQL (Patterns 1 & 2)
- **Pros**: Fastest execution, direct database access
- **Cons**: No relationship handling, manual query optimization
- **Use When**: Simple queries, performance-critical paths, no relationships needed

### SQLAlchemy ORM (Pattern 3)
- **Pros**: Relationship handling, eager loading, type safety
- **Cons**: Slight overhead, requires ORM knowledge
- **Use When**: Relationships needed, complex queries, maintainability important

## Error Handling Patterns

### PersistenceLayer (Sync)
```python
try:
    player = persistence.get_player_by_name(name)
except psycopg2.Error as e:
    log_and_raise(DatabaseError, f"Database error: {e}")
```

### AsyncPersistenceLayer (Async)
```python
try:
    player = await async_persistence.get_player_by_name(name)
except asyncpg.PostgresError as e:
    log_and_raise(DatabaseError, f"Database error: {e}")
```

### SQLAlchemy ORM (Async)
```python
try:
    result = await session.execute(stmt)
    player = result.scalar_one_or_none()
except Exception as e:
    await session.rollback()
    log_and_raise(DatabaseError, f"Database error: {e}")
```

## Eager Loading Best Practices

Always use eager loading when accessing relationships:

```python
from sqlalchemy.orm import selectinload

# Good: Eagerly load relationships
stmt = select(Player).options(
    selectinload(Player.user),
    selectinload(Player.lucidity),  # if relationship exists
).where(Player.player_id == player_id)

# Bad: Lazy loading (causes N+1 queries)
stmt = select(Player).where(Player.player_id == player_id)
# Later: player.user  # This triggers additional query!
```

## Common Patterns

### Getting a Single Player with User
```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from server.models.player import Player

stmt = select(Player).options(
    selectinload(Player.user)
).where(Player.player_id == player_id)

result = await session.execute(stmt)
player = result.scalar_one_or_none()
```

### Listing Players with Eager Loading
```python
stmt = select(Player).options(
    selectinload(Player.user)
).order_by(Player.name)

result = await session.execute(stmt)
players = result.scalars().all()
```

### Complex Query with Joins
```python
from sqlalchemy import select
from server.models.player import Player
from server.models.lucidity import PlayerLucidity

stmt = select(Player, PlayerLucidity).join(
    PlayerLucidity, Player.player_id == PlayerLucidity.player_id
).where(Player.level > 5)

result = await session.execute(stmt)
for player, lucidity in result:
    # Both objects loaded in single query
    pass
```

## Future Migration Goals

1. **Short-term**: Document patterns and migration paths ✅ **COMPLETE**
2. **Medium-term**: Migrate f-string SQL to ORM (in progress - see notes below)
3. **Long-term**: Consolidate to SQLAlchemy ORM for all operations

## F-String SQL Migration Status

**Current State**: Persistence layers use f-strings with compile-time constants (e.g., `PLAYER_COLUMNS`). These are safe from SQL injection but represent an anti-pattern.

**Limitation**: Full migration to SQLAlchemy ORM requires architectural changes:
- `PersistenceLayer` uses synchronous `psycopg2` (not SQLAlchemy)
- `AsyncPersistenceLayer` uses `asyncpg` directly (not SQLAlchemy)
- Both would need to be refactored to use SQLAlchemy sessions

**Current Approach**:
- F-strings separated from execution for better readability
- Documentation added explaining why f-strings are safe (constants)
- Future ORM migration noted in code comments

**Next Steps**:
- Incrementally migrate new code to SQLAlchemy ORM
- Refactor persistence layers to use SQLAlchemy when feasible
- Prefer ORM for all new database operations

## References

- [SQLAlchemy Best Practices](./.cursor/rules/sqlalchemy.mdc)
- [SQLAlchemy Async Best Practices](./docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md)
- [SQLAlchemy Code Review](./docs/SQLALCHEMY_CODE_REVIEW.md)

---

*"In the restricted archives, we learn that different incantations serve different purposes. The raw SQL rituals provide direct power, while the ORM ceremonies offer safety and convenience. Choose wisely based on your needs, but always prefer the ORM for new work, lest you summon the N+1 query demon."*
