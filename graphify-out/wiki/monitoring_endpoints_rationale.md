# monitoring endpoints rationale

> 32 nodes

## Key Concepts

- **container_helpers_inventory_find.py** (32 connections) — `server/commands/container_helpers_inventory_find.py`
- **UUID** (16 connections)
- **try_wearable_container_service()** (14 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_instance_id()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **create_wearable_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_name()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **_get_container_pair()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_try_put_container_for_equipped_item()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_uuid()** (5 connections) — `server/commands/container_helpers_inventory_find.py`
- **Player** (5 connections)
- **container_id()** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_component_metadata()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_resolve_inner_uuid()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_from_equip_dict()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_fallback_create_equipment_container()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_try_wearable_container_service_finds_component()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_wearable_container_service_swallows_service_error()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_wearable_by_instance_id_match()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_wearable_by_name_slot_metadata()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **_wearable_put_metadata_matches()** (2 connections) — `server/commands/container_helpers_inventory_find.py`
- **_wearable_get_name_slot_matches()** (2 connections) — `server/commands/container_helpers_inventory_find.py`
- **_instance_id_matches_metadata()** (2 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_try_wearable_by_instance_id_empty_id()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_wearable_by_instance_id_no_components()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **Lookups for wearable containers, room containers, and inventory items.  group: i** (1 connections) — `server/commands/container_helpers_inventory_find.py`
- *... and 7 more nodes in this community*

## Relationships

- [container find inventory](container_find_inventory.md) (26 shared connections)
- [combat npc services](combat_npc_services.md) (13 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (6 shared connections)
- [Inventory Equip](Inventory_Equip.md) (4 shared connections)
- [commands communication flows](commands_communication_flows.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 169 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*