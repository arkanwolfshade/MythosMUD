# Magic Command Handlers

> 105 nodes

## Key Concepts

- **InventoryMutationGuard** (43 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
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
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- *... and 80 more nodes in this community*

## Relationships

- [Chat Service Whispers](Chat_Service_Whispers.md) (12 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (11 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (4 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (4 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Middleware Metrics Collector](Middleware_Metrics_Collector.md) (1 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 292 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*