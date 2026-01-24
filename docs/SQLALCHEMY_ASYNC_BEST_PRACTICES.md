# SQLAlchemy Async Best Practices

## Overview

This document outlines best practices for using SQLAlchemy in async contexts within the MythosMUD project to prevent
`ObjectNotExecutableError` and other async-related database issues.

## The Problem

When using SQLAlchemy 2.0+ in async contexts, raw SQL strings cannot be passed directly to `execute()` methods. This
causes the following error:

```
sqlalchemy.exc.ObjectNotExecutableError: Not an executable object: 'PRAGMA foreign_keys = ON'
```

## The Solution

### ✅ Correct Pattern

```python
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

async def correct_usage():
    async with async_session() as session:
        # Wrap raw SQL strings with text()

        await session.execute(text("PRAGMA foreign_keys = ON"))
        await session.execute(text("SELECT * FROM users WHERE id = :user_id"), {"user_id": user_id})
```

### ❌ Incorrect Pattern

```python
async def incorrect_usage():
    async with async_session() as session:
        # DON'T do this - causes ObjectNotExecutableError

        await session.execute("PRAGMA foreign_keys = ON")
        await session.execute("SELECT * FROM users WHERE id = :user_id", {"user_id": user_id})
```

## When to Use `text()`

Use `text()` wrapper for:

**Raw SQL strings** in async contexts

**PRAGMA statements** (SQLite-specific commands)

**Complex queries** not easily expressed with SQLAlchemy ORM

**Database-specific SQL** that doesn't have ORM equivalents

### Examples

```python
from sqlalchemy import text

# PRAGMA statements

await conn.execute(text("PRAGMA foreign_keys = ON"))
await conn.execute(text("PRAGMA journal_mode = WAL"))

# Raw SELECT queries

result = await session.execute(text("SELECT COUNT(*) FROM players WHERE level > :level"), {"level": 10})

# Raw INSERT/UPDATE/DELETE

await session.execute(text("DELETE FROM temp_data WHERE created_at < :cutoff"), {"cutoff": cutoff_date})

# Complex queries with database-specific features

await session.execute(text("SELECT * FROM players ORDER BY RANDOM() LIMIT 1"))
```

## When NOT to Use `text()`

Don't use `text()` for:

**ORM queries** (use SQLAlchemy ORM methods)

**Synchronous connections** (like `sqlite3.connect()`)

**Non-SQLAlchemy database libraries** (like `aiosqlite`)

### Examples

```python
# ✅ Use ORM for standard queries

users = await session.execute(select(User).where(User.is_active == True))

# ✅ Use sqlite3 directly (synchronous)

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = ON")  # No text() needed

# ✅ Use aiosqlite directly

async with aiosqlite.connect(db_path) as db:
    await db.execute("PRAGMA foreign_keys = ON")  # No text() needed
```

## Prevention Tools

### Custom Linter

We have a custom linter to catch these issues:

```bash
# Run the SQLAlchemy async pattern linter

make lint-sqlalchemy

# Or run directly

python scripts/lint_sqlalchemy_async.py [file_or_directory]
```

### Pre-commit Hooks

The linter runs automatically on pre-commit to catch issues before they're committed.

### IDE Integration

Consider adding these patterns to your IDE's code inspection rules:

- Warn on `await.*execute\(["']` without `text()` wrapper
- Suggest `text()` import when using raw SQL in async contexts

## Common Patterns in MythosMUD

### Database Initialization

```python
# server/database.py

from sqlalchemy import text

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
        # Enable foreign key constraints for SQLite

        await conn.execute(text("PRAGMA foreign_keys = ON"))
```

### NPC Database

```python
# server/npc_database.py

from sqlalchemy import text

async def init_npc_database():
    async with npc_engine.begin() as conn:
        await conn.run_sync(npc_metadata.create_all)
        await conn.execute(text("PRAGMA foreign_keys = ON"))
```

### Test Cleanup

```python
# In test files

from sqlalchemy import text

async def cleanup_test_data():
    await session.execute(text("DELETE FROM test_table"))
    await session.commit()
```

## Troubleshooting

### Error: `ObjectNotExecutableError`

**Cause**: Raw SQL string passed to async `execute()` without `text()` wrapper.

**Fix**: Wrap the SQL string with `text()`:

```python
# Before

await session.execute("SELECT * FROM users")

# After

from sqlalchemy import text
await session.execute(text("SELECT * FROM users"))
```

### Error: `NameError: name 'text' is not defined`

**Cause**: Missing import for `text` function.

**Fix**: Add the import:

```python
from sqlalchemy import text
```

### Performance Considerations

`text()` wrapper adds minimal overhead

- Prefer ORM queries when possible for better performance
- Use `text()` only when necessary for complex or database-specific SQL

## References

[SQLAlchemy 2.0 Async Documentation](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- [SQLAlchemy Core Text

  Constructs](<https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text>)

- [SQLAlchemy 2.0 Migration Guide](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html)

---

*"In the restricted archives of Miskatonic University, we learn that proper incantations are essential when working with
dimensional gateways. The `text()` ritual must be performed whenever raw SQL strings cross the threshold of async
execution, lest the ObjectNotExecutableError consume the unwary developer's code."*
