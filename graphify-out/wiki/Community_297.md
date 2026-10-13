# Community 297

> 55 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_async.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (8 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (6 connections)
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **test_acquire_async_cleanup_empty_state()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_concurrent_same_player()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- *... and 30 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 600](Community_600.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (3 shared connections)
- [Community 178](Community_178.md) (3 shared connections)
- [Community 875](Community_875.md) (2 shared connections)
- [Community 701](Community_701.md) (2 shared connections)
- [Community 352](Community_352.md) (2 shared connections)
- [Community 274](Community_274.md) (1 shared connections)
- [Community 791](Community_791.md) (1 shared connections)
- [Community 235](Community_235.md) (1 shared connections)
- [Community 631](Community_631.md) (1 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 92 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*