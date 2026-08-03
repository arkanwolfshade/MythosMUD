# container helpers endpoints

> 87 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.begin_mutation()** (5 connections) — `server/services/inventory_service.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- *... and 62 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (40 shared connections)
- [Inventory Equip](Inventory_Equip.md) (37 shared connections)
- [player event handlers](player_event_handlers.md) (10 shared connections)
- [inventory commands command](inventory_commands_command.md) (10 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (7 shared connections)
- [lucidity active service](lucidity_active_service.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [commands inventory command](commands_inventory_command.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (4 shared connections)
- [npc combat player](npc_combat_player.md) (3 shared connections)

## Source Files

- `server/services/__init__.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 409 (81%)
- INFERRED: 95 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*