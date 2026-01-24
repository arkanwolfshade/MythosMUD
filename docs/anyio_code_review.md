# AnyIO Code Review - Anti-Patterns and Issues

**Date**: 2026-01-13
**Reviewer**: AI Assistant
**Scope**: Full codebase review against `.cursor/rules/anyio.mdc` best practices

## Executive Summary

The codebase extensively uses `asyncio` directly instead of `anyio`, violating the established best practices. While
`anyio` is present as a transitive dependency (via `httpx`), it is not explicitly declared and not used. The codebase
should migrate to `anyio` for:

1. **Backend-agnostic async code** - Can run on asyncio or Trio
2. **Structured concurrency** - Better task lifecycle management
3. **Unified API** - Consistent async primitives across the codebase
4. **Performance** - Backend-specific optimizations (e.g., uvloop)

## Critical Issues

### 1. Entry Point Anti-Pattern: `asyncio.run()` Usage

**Rule Violation**: Section 1 - "Always use `anyio.run()` as your application's entry point"

**Affected Files** (Scripts using `asyncio.run()`):

#### Server Scripts

`server/scripts/check_invites_schema.py:45`

- `server/scripts/rename_used_to_is_active.py:168`
- `server/scripts/add_fastapi_users_columns.py:192`
- `server/scripts/check_invite_status.py:39`
- `server/scripts/list_active_invites.py:29`
- `server/scripts/migrate_combat_data.py:300`
- `server/scripts/add_used_by_user_id_column.py:170`
- `server/scripts/check_users_schema.py:47`
- `server/scripts/verify_npc_occupants.py:204`
- `server/scripts/add_hashed_password_column.py:170`
- `server/scripts/rename_invites_columns.py:283`

#### Root Scripts

`scripts/load_seed_via_asyncpg.py:68`

- `scripts/verify_and_load_seed.py:95`
- `scripts/add_flavor_text_column.py:53`
- `scripts/apply_players_migration.py:110`
- `scripts/bench_cache_npc.py:73`
- `scripts/check_and_apply_map_migrations.py:168`
- `scripts/load_world_seed.py:236`
- `scripts/load_seed_using_project_db.py:71`
- `scripts/bench_cache.py:65`
- `scripts/verify_migration.py:407`

**Impact**: Scripts bypass AnyIO's entry point, missing backend optimizations and structured concurrency benefits.

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
asyncio.run(main())

# ✅ GOOD

from anyio import run
run(main)
```

### 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage

**Rule Violation**: Should use `anyio` equivalents for backend-agnostic code

#### 2.1 `asyncio.sleep()` Usage

**Affected Files** (Sample - many more exist):

- `server/utils/retry.py:138`
- `server/services/nats_service.py:462, 495, 1189`
- `server/realtime/nats_retry_handler.py:161, 238`
- `server/realtime/disconnect_grace_period.py:58`
- `server/realtime/login_grace_period.py:78`
- `server/services/game_tick_service.py:121, 129`
- `server/app/game_tick_processing.py:536, 544`
- `server/database.py:378, 387`
- `server/npc_database.py:362, 371`
- `scripts/bench_cache.py:24`
- `scripts/bench_cache_npc.py:22, 26, 30`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
await asyncio.sleep(0.1)

# ✅ GOOD

from anyio import sleep
await sleep(0.1)
```

#### 2.2 `asyncio.Lock()` Usage

**Affected Files**:

- `server/container.py:168`
- `server/services/inventory_mutation_guard.py:42, 45, 48, 70, 74, 77`
- `server/npc/threading.py:206`
- `server/services/room_sync_service.py:53`
- `server/tests/unit/realtime/test_connection_establishment.py:163, 176, 449, 484, 508, 531`
- `server/tests/unit/realtime/test_connection_disconnection.py:153`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
lock = asyncio.Lock()

# ✅ GOOD

from anyio import Lock
lock = Lock()
```

#### 2.3 `asyncio.Event()` Usage

**Affected Files**:

- `server/events/event_bus.py:57`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
event = asyncio.Event()

# ✅ GOOD

from anyio import Event
event = Event()
```

#### 2.4 `asyncio.Queue()` Usage

**Affected Files**:

- `server/events/event_bus.py:52`
- `server/services/nats_service.py:146`
- `server/services/room_sync_service.py:54`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
queue = asyncio.Queue()

# ✅ GOOD

from anyio import create_memory_object_stream
send_stream, receive_stream = create_memory_object_stream(max_buffer_size=100)
```

**Note**: AnyIO uses memory object streams instead of Queue. This requires API changes.

#### 2.5 `asyncio.wait_for()` Usage

**Affected Files**:

- `server/events/event_bus.py:132, 167, 218`
- `server/services/nats_service.py:434, 514`
- `server/infrastructure/nats_broker.py:239`
- `server/realtime/connection_manager_methods.py:660`
- `server/realtime/connection_delegates.py:67`
- `server/database.py:390`
- `server/realtime/monitoring/health_monitor.py:414`
- `server/app/tracked_task_manager.py:131`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
result = await asyncio.wait_for(coro, timeout=5.0)

# ✅ GOOD

from anyio import move_on_after, fail_after
with move_on_after(5.0) as cancel_scope:
    result = await coro
if cancel_scope.cancelled_caught:
    raise TimeoutError()
```

### 3. Task Management Anti-Patterns

#### 3.1 `asyncio.create_task()` Usage

**Rule Violation**: Should use AnyIO's structured concurrency patterns

**Affected Files** (Sample - many more exist):

- `server/services/combat_hp_sync.py:108`
- `server/realtime/messaging/message_broadcaster.py:94`
- `server/services/nats_service.py:805`
- `server/events/event_bus.py:69, 335, 473`
- `server/npc/lifecycle_manager.py:442`
- `server/app/tracked_task_manager.py:62, 70`
- `server/realtime/disconnect_grace_period.py:101`
- `server/services/combat_persistence_handler.py:313`
- `server/commands/admin_shutdown_command.py:292`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
task = asyncio.create_task(coro)

# ✅ GOOD (for fire-and-forget)

from anyio import create_task_group
async with create_task_group() as tg:
    tg.start_soon(coro)

# ✅ GOOD (for tracked tasks - keep existing pattern but use anyio)
# Note: The tracked_task_manager pattern is good, but should use anyio.create_task()

```

#### 3.2 `asyncio.gather()` Usage

**Rule Violation**: Should use AnyIO's TaskGroup for structured concurrency

**Affected Files**:

- `server/realtime/messaging/message_broadcaster.py:199, 256`
- `server/services/user_manager.py:1371`
- `server/services/nats_service.py:434`
- `server/events/event_bus.py:167, 373`
- `server/npc/threading.py:251`
- `server/app/tracked_task_manager.py:217`
- `server/tests/unit/services/test_inventory_mutation_guard.py:381`

**Recommended Fix**:

```python
# ❌ BAD

import asyncio
results = await asyncio.gather(*tasks, return_exceptions=True)

# ✅ GOOD

from anyio import create_task_group
results = []
async with create_task_group() as tg:
    for task in tasks:
        tg.start_soon(lambda t=task: results.append(await t))
```

**Note**: TaskGroup provides better error handling and cancellation semantics.

### 4. Missing Explicit Dependency

**Issue**: `anyio` is not explicitly listed in `pyproject.toml` dependencies, even though it's used transitively (via
`httpx`).

**Impact**:

- Version not pinned
- Could break if transitive dependency changes
- Not clear to developers that anyio patterns should be used

**Recommended Fix**: Add to `pyproject.toml`:

```toml
dependencies = [
    ...
    "anyio>=4.0.0",  # Unified async API for backend-agnostic code
    ...
]
```

### 5. Special Cases Requiring Attention

#### 5.1 Uvicorn Integration

**File**: `server/main.py:299`

**Status**: ✅ **ACCEPTABLE** - Uvicorn manages its own event loop. The `uvicorn.run()` call is appropriate for the
server entry point. Scripts should use `anyio.run()`, but the main server can continue using uvicorn.

#### 5.2 Test Files

**Status**: ⚠️ **REVIEW NEEDED** - Test files use `asyncio` extensively. Consider:

- Using `anyio` in tests for consistency
- Or keeping `asyncio` if pytest-asyncio requires it (verify compatibility)

#### 5.3 Event Bus Queue Migration

**File**: `server/events/event_bus.py`

**Issue**: Uses `asyncio.Queue` which needs migration to AnyIO's memory object streams.

**Complexity**: **HIGH** - Requires API changes:

- `Queue.get()` → `receive_stream.receive()`
- `Queue.put()` → `send_stream.send()`
- `Queue.put_nowait()` → `send_stream.send_nowait()`
- `QueueFull` → `WouldBlock` exception handling

#### 5.4 Tracked Task Manager

**File**: `server/app/tracked_task_manager.py`

**Status**: ⚠️ **PARTIAL** - Good pattern for task tracking, but should use `anyio.create_task()` internally instead of
`asyncio.create_task()`.

## Migration Priority

### High Priority (Entry Points)

1. **All scripts using `asyncio.run()`** - Easy wins, immediate benefits
2. **Add `anyio` to dependencies** - Foundation for migration

### Medium Priority (Core Primitives)

1. **Replace `asyncio.sleep()`** - Straightforward find/replace
2. **Replace `asyncio.Lock()`** - Straightforward find/replace
3. **Replace `asyncio.Event()`** - Straightforward find/replace
4. **Replace `asyncio.wait_for()`** - Requires pattern changes

### Low Priority (Complex Refactoring)

1. **Replace `asyncio.Queue()`** - Requires significant API changes
2. **Replace `asyncio.gather()`** - Requires TaskGroup pattern adoption
3. **Replace `asyncio.create_task()`** - May conflict with tracked_task_manager

## Testing Considerations

Ensure all tests pass after migration

- Verify backend-agnostic behavior (test with both asyncio and Trio backends if possible)
- Performance testing to ensure no regressions
- Integration tests for event bus queue migration

## Recommendations

1. **Immediate**: Add `anyio>=4.0.0` to `pyproject.toml` dependencies
2. **Phase 1**: Migrate all scripts from `asyncio.run()` to `anyio.run()`
3. **Phase 2**: Replace `asyncio.sleep()`, `asyncio.Lock()`, `asyncio.Event()` with anyio equivalents
4. **Phase 3**: Replace `asyncio.wait_for()` with anyio timeout patterns
5. **Phase 4**: Consider migrating `asyncio.Queue()` to memory object streams (requires careful testing)
6. **Phase 5**: Evaluate TaskGroup migration for `asyncio.gather()` usage

## Notes

The codebase has comments mentioning "AnyIO Pattern" but doesn't actually use anyio

- Some patterns (like tracked_task_manager) are good but should use anyio primitives internally
- Migration can be done incrementally without breaking changes
- Consider creating a migration guide for developers
