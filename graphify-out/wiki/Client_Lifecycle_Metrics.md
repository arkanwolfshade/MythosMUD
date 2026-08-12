# Client Lifecycle Metrics

> 133 nodes

## Key Concepts

- **InventoryMutationGuard** (43 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **.acquire_async()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **.acquire()** (9 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- *... and 108 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (7 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Middleware Metrics Collector](Middleware_Metrics_Collector.md) (1 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (1 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 353 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*