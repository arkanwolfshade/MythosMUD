# ContainerRepository and ItemRepository: Review and Full Async Migration Plan

## 1. Review Summary

### 1.1 Current Architecture

**ContainerRepository** (`server/persistence/repositories/container_repository.py`):

- Async facade over **sync** container persistence.
- Every method runs a sync call in a thread pool via `asyncio.to_thread(_sync)`.
- Each sync call opens a **new** psycopg2 connection via `_get_sync_connection()` (context manager), runs the underlying function, then closes the connection.
- Delegates to:
  - `server/persistence/container_persistence.py`: `create_container`, `get_container`, `update_container`, `delete_container`
  - `server/persistence/container_query_helpers.py`: `get_containers_by_room_id`, `get_containers_by_entity_id`, `get_decayed_containers`
- Uses `server/persistence/container_helpers.py`: `fetch_container_items`, `parse_jsonb_column` (called from persistence/query_helpers).

**ItemRepository** (`server/persistence/repositories/item_repository.py`):

- Same pattern: async methods wrap sync functions with `asyncio.to_thread(_sync)`.
- Each call opens a new psycopg2 connection via `_get_sync_connection()`, then closes it.
- Delegates to `server/persistence/item_instance_persistence.py`: `create_item_instance`, `ensure_item_instance`, `item_instance_exists`.

**Underlying sync stack**:

- `container_persistence.py`, `container_query_helpers.py`, `container_helpers.py`: all use **psycopg2** (sync) and `conn.cursor(cursor_factory=RealDictCursor)`.
- `item_instance_persistence.py`: psycopg2 and RealDictCursor.
- No shared connection pool for these sync connections; URL is taken from `get_config().database.url` and converted from `postgresql+asyncpg://` to `postgresql://` for psycopg2.

**Rest of persistence layer**:

- `PlayerRepository`, `RoomRepository`, `HealthRepository`, `ExperienceRepository`, etc. use **SQLAlchemy async** (asyncpg) via `server/database.py`: `get_async_session()`, `get_session_maker()`.
- Single async engine and session factory; no thread pool, no per-call sync connections.

### 1.2 Impact of Current Wrappers

| Aspect | Impact |
|--------|--------|
| **Performance** | Extra thread-pool hop and new connection per call; no connection reuse for container/item operations. |
| **Consistency** | Only container/item code uses sync DB + thread pool; all other repos use async SQLAlchemy. |
| **Complexity** | Two DB stacks (psycopg2 vs asyncpg/SQLAlchemy), URL conversion, and duplicate connection lifecycle logic. |
| **Testing** | Sync modules tested with psycopg2; async repos tested with async sessions. Mixed patterns. |
| **Scalability** | Thread pool can become a bottleneck under load; async end-to-end is preferred. |

### 1.3 Recommendation

Migrate the underlying container and item persistence to **async** so that:

- ContainerRepository and ItemRepository call async implementations directly (no `asyncio.to_thread`).
- Container and item persistence use the same async database access as the rest of the app (SQLAlchemy async + existing session/engine).

---

## 2. Scope of Migration

### 2.1 Functions to Migrate

**Container persistence**

| Module | Function | Used by ContainerRepository |
|--------|----------|-----------------------------|
| `container_persistence.py` | `create_container` | `create_container` |
| `container_persistence.py` | `get_container` | `get_container` |
| `container_persistence.py` | `update_container` | `update_container` |
| `container_persistence.py` | `delete_container` | `delete_container` |
| `container_query_helpers.py` | `get_containers_by_room_id` | `get_containers_by_room_id` |
| `container_query_helpers.py` | `get_containers_by_entity_id` | `get_containers_by_entity_id` |
| `container_query_helpers.py` | `get_decayed_containers` | `get_decayed_containers` |
| `container_helpers.py` | `fetch_container_items` | Used by get_container and query helpers |
| `container_helpers.py` | `parse_jsonb_column` | Pure helper; no I/O (can stay sync or be inlined). |

**Item persistence**

| Module | Function | Used by ItemRepository |
|--------|----------|------------------------|
| `item_instance_persistence.py` | `create_item_instance` | `create_item_instance` |
| `item_instance_persistence.py` | `ensure_item_instance` | `ensure_item_instance` |
| `item_instance_persistence.py` | `item_instance_exists` | `item_instance_exists` |

`get_item_instance` in item_instance_persistence is not currently exposed by ItemRepository; include it in the migration if/when needed.

### 2.2 Callers

- **AsyncPersistenceLayer** (`server/async_persistence.py`): holds `ContainerRepository` and `ItemRepository`; all container/item calls go through this facade.
- **Unit/integration tests**: `server/tests/unit/infrastructure/test_async_persistence.py` and any tests that hit container/item persistence or repos.

No other direct uses of `container_persistence` or `item_instance_persistence` are required for this plan; any remaining sync callers (e.g. legacy or scripts) can be documented and handled in a follow-up (e.g. keep a thin sync wrapper that uses async implementation via `asyncio.run` if necessary).

---

## 3. Migration Options

### Option A: SQLAlchemy Async (Recommended)

- Implement container and item operations using **SQLAlchemy Core** or existing ORM models with `AsyncSession` from `get_async_session()`.
- Aligns with PlayerRepository, RoomRepository, HealthRepository, etc.
- Reuse existing engine, pool, and session lifecycle from `server/database.py`.
- **Pros**: One stack, consistent patterns, connection pooling, easier to add transactions across repos. **Cons**: May require defining or adapting table mappings if not already present.

### Option B: asyncpg Raw

- Rewrite persistence to use **asyncpg** (raw async driver) with explicit SQL.
- Would require an asyncpg connection pool in addition to (or instead of) SQLAlchemy for these modules, or use SQLAlchemy’s `session.connection()` and run raw SQL (possible but less idiomatic).
- **Pros**: Minimal abstraction, same SQL as today. **Cons**: Two async DB styles (SQLAlchemy vs asyncpg), more custom pool/session handling.

### Option C: Keep Wrappers, Add Sync Connection Pool

- Keep psycopg2 and sync functions; introduce a **sync connection pool** and reuse connections inside `asyncio.to_thread` blocks.
- **Pros**: Smaller change, no rewrite of SQL. **Cons**: Still blocks threads, does not remove the fundamental mismatch with the rest of the async persistence layer.

**Recommendation:** Option A (SQLAlchemy async) for consistency and long-term maintainability.

---

## 4. Full Async Migration Plan

### Phase 1: Preparation (no behavior change)

1. **Audit tables and mappings**
   - Confirm `containers`, `container_contents`, `item_instances`, and related tables are covered by SQLAlchemy metadata/models (e.g. in `server/models/` or schema definitions).
   - If not, add Core `Table` definitions or ORM models and ensure they match current DDL (e.g. from migrations).

2. **Document current SQL and behavior**
   - For each function in `container_persistence`, `container_query_helpers`, `container_helpers`, and `item_instance_persistence`, document:
     - Exact SQL (including JSONB handling, cursor usage).
     - Error handling and validation (e.g. ValidationError, DatabaseError).
     - Return types and any `ContainerData` / dict conversions.
   - Use this as the acceptance criteria for the async versions.

3. **Test coverage**
   - Ensure existing tests for container/item persistence and for ContainerRepository/ItemRepository are sufficient (unit + integration where applicable).
   - Add or tag tests that will validate async behavior (same outcomes as current sync + async entry points).

### Phase 2: Async implementation (container)

1. **Async container helpers**
   - Add async versions of helpers used by container persistence (e.g. `fetch_container_items_async(session, container_id)` using `session.execute(select(...))` and proper JSONB handling).
   - Keep `parse_jsonb_column` as a pure function or move it to a shared util; no I/O change.

2. **Async container persistence**
   - Create `server/persistence/container_persistence_async.py` (or add `async_`-prefixed functions in the same module) implementing:
     - `create_container_async(session, ...)`
     - `get_container_async(session, container_id)`
     - `update_container_async(session, container_id, ...)`
     - `delete_container_async(session, container_id)`
   - Each uses `AsyncSession` from `get_async_session()` (or session passed in by caller). Use SQLAlchemy Core or ORM; preserve existing validation and error handling.

3. **Async container query helpers**
   - Add async versions in `container_query_helpers.py` or a new `container_query_helpers_async.py`:
     - `get_containers_by_room_id_async(session, room_id)`
     - `get_containers_by_entity_id_async(session, entity_id)`
     - `get_decayed_containers_async(session, current_time)`
   - Reuse async `fetch_container_items` and `ContainerData` construction so behavior matches current code.

4. **Wire ContainerRepository to async**
   - Change `ContainerRepository` to use the async persistence and query helpers.
   - Obtain session via `get_async_session()` (or inject a session factory) inside each method; no `_get_sync_connection()`, no `asyncio.to_thread`.
   - Keep the same public method signatures and return types (dict with `items_json`, `metadata_json`, etc.) so AsyncPersistenceLayer and tests need no changes.
   - Remove sync connection context manager and psycopg2 dependency from ContainerRepository.

5. **Tests and backward compatibility**
   - Run existing ContainerRepository and container persistence tests against the new async path.
   - If any code still calls sync `container_persistence` / `container_query_helpers` directly, either migrate those call sites or keep thin sync wrappers that call the async implementation (e.g. `asyncio.run(...)`) until they are removed.

### Phase 3: Async implementation (item)

1. **Async item instance persistence**
   - Add `server/persistence/item_instance_persistence_async.py` (or async functions in the same module):
     - `create_item_instance_async(session, ...)`
     - `ensure_item_instance_async(session, ...)`
     - `item_instance_exists_async(session, item_instance_id)`
     - Optionally `get_item_instance_async(session, item_instance_id)` for future use.
   - Use AsyncSession and SQLAlchemy; preserve validation and error semantics.

2. **Wire ItemRepository to async**
    - Change `ItemRepository` to call the async item persistence functions.
    - Use `get_async_session()` (or injected session factory); remove `_get_sync_connection()` and `asyncio.to_thread`.
    - Keep public API unchanged.

3. **Tests and backward compatibility**
    - Run existing ItemRepository and item instance persistence tests.
    - Handle any remaining sync callers as in step 8.

### Phase 4: Cleanup

1. **Remove sync path from container/item**
    - Once all callers use async:
      - Remove or deprecate sync functions in `container_persistence.py`, `container_query_helpers.py`, `container_helpers.py` (or mark as legacy and used only by scripts).
      - Remove or deprecate sync functions in `item_instance_persistence.py`.
    - Remove psycopg2 usage from these modules (and from ContainerRepository/ItemRepository if still present).

2. **Dependencies**
    - If no other code uses psycopg2, consider removing it from project dependencies; otherwise leave it for the remaining sync use cases.

3. **Docs and ADR**
    - Update `server/persistence/repositories/README.md` (or equivalent) to state that ContainerRepository and ItemRepository are fully async and use SQLAlchemy async.
    - Add an ADR that records the decision to migrate container/item persistence to async (SQLAlchemy) and the deprecation of the sync wrappers.

### Phase 5: Verification

1. **Integration and performance**
    - Run full test suite (unit + integration).
    - Optionally run a quick load check: many container/item operations in parallel to confirm no thread-pool saturation and improved scalability vs. current wrappers.

---

## 5. File Checklist

| Action | File(s) |
|--------|--------|
| Add/refactor | `server/persistence/container_persistence_async.py` or async functions in `container_persistence.py` |
| Add/refactor | `server/persistence/container_query_helpers_async.py` or async functions in `container_query_helpers.py` |
| Add/refactor | Async helpers in `container_helpers.py` (e.g. `fetch_container_items_async`) |
| Add/refactor | `server/persistence/item_instance_persistence_async.py` or async functions in `item_instance_persistence.py` |
| Modify | `server/persistence/repositories/container_repository.py` – use async persistence, remove to_thread and sync connection |
| Modify | `server/persistence/repositories/item_repository.py` – use async persistence, remove to_thread and sync connection |
| Optional | `server/async_persistence.py` – only if session injection or API changes are desired |
| Tests | `server/tests/unit/infrastructure/test_async_persistence.py`, container/item persistence tests, repository tests |
| Docs | `server/persistence/repositories/README.md`, new ADR for async migration |

---

## 6. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| SQL or behavior difference from current sync code | Strict parity tests (same inputs → same outputs); keep sync implementation until async is validated. |
| Transaction boundaries | Use one async session per logical operation (or per request) where appropriate; document where cross-repo transactions are needed. |
| Regression in callers | Full test suite and targeted tests for AsyncPersistenceLayer container/item methods. |
| Remaining sync callers | Audit for direct use of sync container/item modules; add thin sync wrappers or migrate callers before removing sync code. |

---

## 7. Success Criteria

- ContainerRepository and ItemRepository have no `asyncio.to_thread` and no psycopg2 usage.
- All container and item persistence runs on SQLAlchemy async (same engine/session as other repos).
- Existing tests for container/item persistence and for AsyncPersistenceLayer container/item methods pass.
- Documentation and (optionally) an ADR describe the migration and the removal of the sync wrapper pattern for these repositories.

This plan completes the architecture review task: **Review ContainerRepository and ItemRepository async wrappers and plan full async migration.**

---

## 8. Phase 1 Audit Results (Completed)

- **item_instances**: SQLAlchemy ORM model `ItemInstance` exists in `server/models/item.py` with `__tablename__ = "item_instances"`. Column `metadata_payload` is mapped to DB column `"metadata"`.
- **containers**: No SQLAlchemy ORM/Table for `containers` or `container_contents`. Persistence uses raw psycopg2 and `ContainerData` in `server/persistence/container_data.py`. For full async migration of containers, add SQLAlchemy Core `Table()` definitions or an ORM model and implement async persistence (Phase 2).

---

## 9. Implementation Status

- **Phase 3 (Item) – DONE**: Async item instance persistence and ItemRepository migration are implemented.
  - Added `server/persistence/item_instance_persistence_async.py` with `create_item_instance_async`, `ensure_item_instance_async`, `item_instance_exists_async` using SQLAlchemy AsyncSession and `ItemInstance` table.
  - `server/persistence/repositories/item_repository.py` now uses the async module and `get_session_maker()`; removed `asyncio.to_thread`, `_get_sync_connection()`, and psycopg2.
  - All server tests pass (7259).
- **Phase 2 (Container)**: Not yet implemented; requires async container persistence (e.g. Core Table for `containers`/`container_contents` or new ORM model) and then wiring ContainerRepository.
