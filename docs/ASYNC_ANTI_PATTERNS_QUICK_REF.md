# Async Anti-Patterns Quick Reference

**Purpose**: Quick reference for avoiding common async/await anti-patterns in MythosMUD
**Audience**: All developers working with async code
**Last Updated**: December 3, 2025

---

## ❌ NEVER DO THIS → ✅ DO THIS INSTEAD

### 1. Blocking the Event Loop

#### ❌ WRONG - Synchronous call from async function

```python
async def process_player(player_id: str):
    # This BLOCKS the entire event loop!

    player = persistence.get_player(player_id)  # Synchronous database call
    room = persistence.get_room(player.room_id)  # Synchronous database call
    return player
```

#### ✅ CORRECT - Async all the way

```python
async def process_player(player_id: str):
    # Non-blocking async operations

    player = await persistence.async_get_player(player_id)
    room = await persistence.async_get_room(player.room_id)
    return player
```

#### ✅ CORRECT - Thread pool for blocking operations

```python
async def process_player(player_id: str):
    # Run blocking operation in thread pool (temporary solution)

    player = await asyncio.to_thread(persistence.get_player, player_id)
    room = await asyncio.to_thread(persistence.get_room, player.room_id)
    return player
```

**Why**: Synchronous I/O operations block the entire event loop, preventing ALL other async operations from running.
This causes lag, delays, and poor performance.

**Detection**: If you call a non-async function that does I/O (database, file, network) from an async function, you're
probably blocking.

---

### 2. Using asyncio.run() Incorrectly

#### ❌ WRONG - asyncio.run() in library code

```python
def mark_room_explored(player_id: str, room_id: str):
    async def _mark():
        # ...async database operation...

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(_mark())
    except RuntimeError:
        # This can STILL fail if there's a loop but not running!

        asyncio.run(_mark())  # ❌ DANGEROUS
```

#### ✅ CORRECT - Make the function async

```python
async def mark_room_explored(player_id: str, room_id: str):
    # Just make it async!
    # ...async database operation...

```

#### ✅ CORRECT - Fire-and-forget with proper error handling

```python
def mark_room_explored_sync(player_id: str, room_id: str):
    async def _mark():
        # ...async database operation...

    try:
        loop = asyncio.get_running_loop()
        # Fire and forget - don't await

        task = loop.create_task(_mark())
        # Add error callback

        task.add_done_callback(lambda t: logger.error("Error", error=str(t.exception())) if t.exception() else None)
    except RuntimeError:
        # No loop - log and defer

        logger.warning("No event loop, deferring operation")
        # Add to queue or skip

```

**Why**: `asyncio.run()` creates a new event loop. If called from within an existing event loop context, it raises
RuntimeError. Only use `asyncio.run()` in entry points (main(), scripts).

**Rule of Thumb**: If your file imports anything from `server/`, don't use `asyncio.run()`.

---

### 3. F-String Logging (Destroys Structured Logging)

#### ❌ WRONG - F-strings destroy structured logging

```python
async def start_combat(attacker: str, target: str):
    logger.info(f"Starting combat between {attacker} and {target}")
    logger.error(f"Combat failed: {error}")
    logger.debug(f"Combat data: {combat_data}")
```

**Problems**:

- Cannot search logs by specific field (e.g., all combats with attacker="Alice")
- Cannot create alerts based on structured data
- Cannot correlate events across log entries
- Slower performance (string formatting)
- Breaks log aggregation tools

#### ✅ CORRECT - Structured key-value pairs

```python
async def start_combat(attacker: str, target: str):
    logger.info("Starting combat", attacker=attacker, target=target, room_id=room_id)
    logger.error("Combat failed", error=str(error), operation="combat_start")
    logger.debug("Combat data", combat_data=combat_data, combat_type=combat_type)
```

**Benefits**:

- Searchable by any field
- Can create alerts: "alert if combat_failed AND target=boss"
- Can correlate: "show all events where attacker=Alice"
- Faster (no string formatting)
- Works with log aggregation tools (ELK, Splunk, etc.)

**Rule of Thumb**: NEVER use f-strings with logger. Always use key=value pairs.

---

### 4. Missing Exception Handling in Async Code

#### ❌ WRONG - Unhandled exceptions crash the app

```python
async def create_connection_pool():
    # This can raise ConnectionError, asyncpg.PostgresError, etc.

    pool = await asyncpg.create_pool(url)  # ❌ No error handling
    return pool
```

#### ✅ CORRECT - Proper exception handling

```python
async def create_connection_pool():
    try:
        pool = await asyncpg.create_pool(
            url,
            min_size=1,
            max_size=10,
            command_timeout=60,
        )
        logger.info("Created connection pool", pool_size=10)
        return pool
    except (asyncpg.PostgresError, ConnectionError, OSError) as e:
        context = create_error_context()
        context.metadata["operation"] = "create_connection_pool"
        log_and_raise(
            DatabaseError,
            f"Failed to create database connection pool: {e}",
            context=context,
            details={
                "database_url": url[:50],  # Truncate for security
                "error": str(e),
                "error_type": type(e).__name__
            },
            user_friendly="Database connection failed",
        )
```

**Why**: Async operations can fail in many ways. Without exception handling, these failures crash the application or
leave it in an inconsistent state.

---

### 5. Not Using asyncio.gather() Properly

#### ❌ WRONG - Sequential execution (slow)

```python
async def load_players(player_ids: list[str]):
    players = []
    for player_id in player_ids:
        player = await persistence.async_get_player(player_id)
        players.append(player)
    return players
```

#### ❌ WRONG - Concurrent but one failure cancels all

```python
async def load_players(player_ids: list[str]):
    # If ONE fails, ALL fail!

    players = await asyncio.gather(*[
        persistence.async_get_player(pid) for pid in player_ids
    ])
    return players
```

#### ✅ CORRECT - Concurrent with return_exceptions=True

```python
async def load_players(player_ids: list[str]):
    # All complete even if some fail

    results = await asyncio.gather(*[
        persistence.async_get_player(pid) for pid in player_ids
    ], return_exceptions=True)

    # Handle results

    players = []
    for pid, result in zip(player_ids, results):
        if isinstance(result, Exception):
            logger.error("Failed to load player", player_id=pid, error=str(result))
        else:
            players.append(result)

    return players
```

**Why**: `return_exceptions=True` ensures all tasks complete even if some fail. This is usually what you want for event
subscribers, bulk operations, etc.

---

### 6. Resource Leaks (Not Closing Async Resources)

#### ❌ WRONG - Pool never closed

```python
class MyService:
    async def init(self):
        self.pool = await asyncpg.create_pool(...)

    # No close method! Pool leaks on shutdown

```

#### ✅ CORRECT - Proper cleanup

```python
class MyService:
    async def init(self):
        self.pool = await asyncpg.create_pool(...)

    async def close(self):
        """Close resources during shutdown."""
        if self.pool is not None:
            await self.pool.close()
            self.pool = None
            logger.info("Closed connection pool")

# In ApplicationContainer.shutdown()

async def shutdown(self):
    if self.my_service:
        await self.my_service.close()
```

**Why**: Async resources (pools, connections, file handles) must be explicitly closed. Without cleanup, they leak
connections/memory.

**Rule of Thumb**: If you create a pool/connection/resource, add a `close()` method and call it from shutdown.

---

### 7. Not Using Async Context Managers

#### ❌ WRONG - Manual resource management

```python
async def save_player(player: Player):
    pool = await get_pool()
    conn = await pool.acquire()
    try:
        await conn.execute("INSERT INTO ...")
    finally:
        await pool.release(conn)
```

#### ✅ CORRECT - Async context managers

```python
async def save_player(player: Player):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO ...")
    # Connection automatically released

```

**Why**: `async with` guarantees cleanup even if exceptions occur. Less boilerplate, fewer bugs.

---

### 8. Mixing Sync and Async Code

#### ❌ WRONG - Calling async from sync without care

```python
def process_command(command: str):
    # This won't work! Can't await in sync function

    result = await execute_command(command)  # SyntaxError
    return result
```

#### ❌ WRONG - Using asyncio.run() everywhere

```python
def process_command(command: str):
    # This creates a new event loop every time!

    result = asyncio.run(execute_command(command))  # Slow, can fail
    return result
```

#### ✅ CORRECT - Make the function async

```python
async def process_command(command: str):
    # Just make it async!

    result = await execute_command(command)
    return result
```

#### ✅ CORRECT - Use asyncio.to_thread() if you must call sync from async

```python
async def async_function():
    # Run blocking sync function in thread pool

    result = await asyncio.to_thread(blocking_sync_function, arg1, arg2)
    return result
```

**Why**: Async code should be async all the way. If you find yourself fighting the async/sync boundary, you're probably
doing it wrong.

---

## 🚨 EMERGENCY DETECTION GUIDE

### "Is my code blocking the event loop?"

Ask yourself:

1. ✅ **YES** if: Calling a non-async function that does I/O (database, file, network, time.sleep)
2. ✅ **YES** if: Using `requests` library (synchronous HTTP)
3. ✅ **YES** if: Using `psycopg2` (synchronous PostgreSQL)
4. ✅ **YES** if: Using `open()` for files (synchronous file I/O)
5. ✅ **YES** if: Using `time.sleep()` (blocks event loop)
6. ✅ **NO** if: Using `await` on async functions
7. ✅ **NO** if: Using `asyncio.sleep()` (non-blocking)
8. ✅ **NO** if: Using `aiohttp` (async HTTP)
9. ✅ **NO** if: Using `asyncpg` (async PostgreSQL)
10. ✅ **NO** if: Using `aiofiles` (async file I/O)

### Quick Test

```python
async def my_function():
    result = some_function()  # ← Does this line have 'await'?

    # If NO await, ask:
    # - Does some_function() do I/O?
    # - Does some_function() take >1ms to run?
    #
    # If YES to either → YOU'RE BLOCKING THE EVENT LOOP
    #
    # Fix: await some_async_function() or await asyncio.to_thread(some_function)

```

---

## 🎯 PRACTICAL CHECKLIST

Before committing async code, check:

- [ ] All database operations use `async_persistence` methods (not `persistence`)
- [ ] All database operations are awaited
- [ ] No `time.sleep()` in async functions (use `asyncio.sleep()`)
- [ ] No `requests` library (use `aiohttp`)
- [ ] No f-strings in logging calls (use key=value)
- [ ] All `asyncio.gather()` calls use `return_exceptions=True` unless you specifically want one failure to cancel all
- [ ] All async resources (pools, connections) have cleanup in shutdown
- [ ] No `asyncio.run()` in library code (only in entry points)
- [ ] All long-running sync operations wrapped in `asyncio.to_thread()`
- [ ] Exception handling for all async operations that can fail

---

## 📚 APPROVED PATTERNS

### Pattern 1: Structured Concurrency

```python
# Run multiple tasks, all complete even if some fail

tasks = [task1(), task2(), task3()]
results = await asyncio.gather(*tasks, return_exceptions=True)
for i, result in enumerate(results):
    if isinstance(result, Exception):
        logger.error("Task failed", task=i, error=str(result))
```

### Pattern 2: Async Context Manager

```python
# Automatic resource cleanup

async with pool.acquire() as conn:
    async with conn.transaction():
        await conn.execute("INSERT ...")
```

### Pattern 3: Fire-and-Forget Task

```python
# Create background task without awaiting

task = asyncio.create_task(background_operation())
# Add error callback

task.add_done_callback(
    lambda t: logger.error("Background task failed", error=str(t.exception()))
    if t.exception()
    else None
)
```

### Pattern 4: Thread Pool for Blocking Operations

```python
# Temporary solution until async version available

async def async_wrapper():
    result = await asyncio.to_thread(blocking_sync_function, arg1, arg2)
    return result
```

### Pattern 5: Retry with Exponential Backoff

```python
@retry_with_backoff(max_attempts=3, initial_delay=1.0)
async def flaky_operation():
    # Automatically retries on transient errors

    result = await external_api_call()
    return result
```

---

## 🔧 TOOLING

### Pre-Commit Hook

Add to `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: check-f-string-logging
      name: Check for f-string logging
      entry: bash -c 'if rg "logger\.(debug|info|warning|error|critical)\(f\"" --type py; then exit 1; fi'
      language: system
      types: [python]
```

### Linter Rules

Add to `.ruff.toml`:

```toml
[lint]
select = [
    "ASYNC",  # Detect async anti-patterns
    # ...

]
```

### IDE Warnings

Configure IDE to warn on:

- `time.sleep` in async functions
- Missing `await` keyword
- `asyncio.run()` outside of entry points

---

## 📞 QUESTIONS?

### "Should this function be async?"

**YES** if:

- It does I/O (database, file, network)
- It calls other async functions
- It waits for something (time, event, condition)

**NO** if:

- It's pure computation (math, string manipulation)
- It's a synchronous callback (e.g., `add_done_callback`)
- It's a property getter/setter

### "Should I use asyncio.to_thread()?"

**TEMPORARY YES** if:

- You need to call a blocking function from async code
- No async version of the function exists yet
- Migration to async version is planned

**LONG-TERM NO**:

- Prefer migrating to async version
- `asyncio.to_thread()` is overhead, not performance

### "When should I use return_exceptions=True?"

**YES** if:

- Event subscribers (one failing subscriber shouldn't cancel others)
- Bulk operations (load 100 players, some may fail)
- Fire-and-forget tasks (don't care about individual failures)

**NO** if:

- All operations must succeed or all fail (transactions)
- One failure should abort the rest
- You need to re-raise the exception

---

## 🎓 LEARNING RESOURCES

1. **Internal**:

   - `.cursor/rules/asyncio.mdc` - Comprehensive asyncio guidelines
   - `.cursor/rules/anyio.mdc` - AnyIO structured concurrency patterns
   - `docs/STRUCTURED_CONCURRENCY_PATTERNS.md` - Project-specific patterns
   - `docs/ASYNC_AUDIT_2025-12-03.md` - Full audit report

2. **External**:

   - [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
   - [Real Python asyncio Tutorial](https://realpython.com/async-io-python/)
   - [asyncpg Documentation](https://magicstack.github.io/asyncpg/)

---

## 🚫 BANNED PATTERNS

These patterns are **NEVER ALLOWED** in MythosMUD:

1. ❌ F-string logging: `logger.info(f"...")`
2. ❌ `asyncio.run()` in library code
3. ❌ Synchronous I/O from async functions without `asyncio.to_thread()`
4. ❌ `time.sleep()` in async functions
5. ❌ Unclosed async resources (pools, connections)
6. ❌ Missing exception handling in async operations
7. ❌ Blocking operations in NATS message handlers
8. ❌ Creating tasks without tracking (`asyncio.create_task()` without registry)

---

**Last Updated**: December 3, 2025
**Maintained By**: Architecture Team
**Questions**: Ask in #async-questions Slack channel
