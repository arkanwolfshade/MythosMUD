# Server Services (22)

> 83 nodes

## Key Concepts

- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_init()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_duplicate()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_init_custom_params()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- *... and 58 more nodes in this community*

## Relationships

- [Server Api](Server_Api.md) (26 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Monitoring](Server_Monitoring.md) (4 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (3 shared connections)
- [Server Services (88)](Server_Services_%2888%29.md) (3 shared connections)
- [Server Services (72)](Server_Services_%2872%29.md) (3 shared connections)
- [Server Monitoring (2)](Server_Monitoring_%282%29.md) (2 shared connections)
- [Server App](Server_App.md) (1 shared connections)
- [Server Middleware (5)](Server_Middleware_%285%29.md) (1 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (1 shared connections)
- [Server Time](Server_Time.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 262 (92%)
- INFERRED: 22 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*