# Loot Generation

> 401 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **container.py** (25 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **ContainerLockState** (14 connections) — `server/models/container.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **environmental_container_loader.py** (13 connections) — `server/services/environmental_container_loader.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- *... and 376 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (128 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (19 shared connections)
- [container events rationale](container_events_rationale.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (12 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [auth users rationale](auth_users_rationale.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (5 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (4 shared connections)
- [Inventory Equip](Inventory_Equip.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 1343 (92%)
- INFERRED: 115 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*