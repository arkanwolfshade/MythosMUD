# Client Lifecycle Metrics

> 159 nodes

## Key Concepts

- **InventoryMutationGuard** (43 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **.acquire()** (9 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.begin_mutation()** (5 connections) — `server/services/inventory_service.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- *... and 134 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (35 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (8 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (2 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (2 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Middleware Metrics Collector](Middleware_Metrics_Collector.md) (1 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (1 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 443 (90%)
- INFERRED: 47 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*