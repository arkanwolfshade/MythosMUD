# Database Access Patterns

This document explains when to use each database access pattern in the MythosMUD codebase and provides guidance on
migrating between patterns.

## Overview

The codebase currently uses two database access patterns:

1. **AsyncPersistenceLayer** (async asyncpg) - Performance-critical operations, direct database access
2. **SQLAlchemy ORM** (async) - Preferred for new code, relationships, complex queries

**Note**: The legacy `PersistenceLayer` (synchronous psycopg2) has been removed. All code now uses async patterns.

## Pattern 1: AsyncPersistenceLayer (Asynchronous asyncpg)

**Location**: `server/async_persistence.py`

**When to Use**:

- Performance-critical operations
- When you need async but don't need ORM features
- Direct asyncpg connection pool access
- Simple queries without relationships

**Characteristics**:

- Uses `asyncpg` for true async PostgreSQL operations
- Raw SQL queries with parameterized placeholders (`$1`, `$2`, etc.)
- Connection pooling with configurable pool size
- Non-blocking event loop operations
- Access via `ApplicationContainer.async_persistence` (container from `server/container/` package)

**Example**:

```python
from server.container import ApplicationContainer  # server/container/ package

container = ApplicationContainer.get_instance()
async_persistence = container.async_persistence
player = await async_persistence.get_player_by_id(player_id)
```

**Advantages**:

- True async (doesn't block event loop)
- High performance for simple operations
- Connection pooling built-in

**Limitations**:

- No eager loading support (raw SQL)
- Manual relationship handling
- More verbose than ORM

**Migration Path**:
Migrate to SQLAlchemy ORM when you need relationships or complex queries

## Pattern 2: SQLAlchemy ORM (Asynchronous)

**Location**: `server/database.py`, `server/services/`, `server/game/`

**When to Use**:
**Preferred for all new code**

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
├─ Yes → Use SQLAlchemy ORM (Pattern 2)
└─ No → Use AsyncPersistenceLayer (Pattern 1)
```

## Migration Strategy

### From AsyncPersistenceLayer to SQLAlchemy ORM

**When**: You need relationships or want better query capabilities

**Steps**:

1. Replace raw SQL with SQLAlchemy `select()` statements
2. Use `get_async_session()` dependency for session management
3. Add eager loading with `selectinload()` where needed
4. Use model classes instead of raw dictionaries

**Example**:

```python
# Before (AsyncPersistenceLayer)

from server.container import ApplicationContainer

async def get_player(player_id: str) -> Player | None:
    container = ApplicationContainer.get_instance()
    return await container.async_persistence.get_player_by_id(player_id)

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

### AsyncPersistenceLayer (Pattern 1)

**Pros**: Fastest execution, direct database access

**Cons**: No relationship handling, manual query optimization

**Use When**: Simple queries, performance-critical paths, no relationships needed

### SQLAlchemy ORM (Pattern 2)

**Pros**: Relationship handling, eager loading, type safety

**Cons**: Slight overhead, requires ORM knowledge

**Use When**: Relationships needed, complex queries, maintainability important

## Error Handling Patterns

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

**Current State**: Persistence layers use f-strings with compile-time constants (e.g., `PLAYER_COLUMNS`). These are safe
from SQL injection but represent an anti-pattern.

**Limitation**: Full migration to SQLAlchemy ORM requires architectural changes:

- `AsyncPersistenceLayer` uses `asyncpg` directly (not SQLAlchemy)
- Would need to be refactored to use SQLAlchemy sessions for full ORM migration

**Current Approach**:

- F-strings separated from execution for better readability
- Documentation added explaining why f-strings are safe (constants)
- Future ORM migration noted in code comments

**Next Steps**:

- Incrementally migrate new code to SQLAlchemy ORM
- Refactor persistence layers to use SQLAlchemy when feasible
- Prefer ORM for all new database operations

## References

[SQLAlchemy Best Practices](./.cursor/rules/sqlalchemy.mdc)

- [SQLAlchemy Async Best Practices](./docs/SQLALCHEMY_ASYNC_BEST_PRACTICES.md)
- [SQLAlchemy Code Review](./docs/SQLALCHEMY_CODE_REVIEW.md)

---

*"In the restricted archives, we learn that different incantations serve different purposes. The raw SQL rituals provide
direct power, while the ORM ceremonies offer safety and convenience. Choose wisely based on your needs, but always
prefer the ORM for new work, lest you summon the N+1 query demon."*
