# Container Inventory Finders

> 85 nodes · cohesion 0.05

## Key Concepts

- **test_container_helpers_inventory_find.py** (54 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **container_helpers_inventory_find.py** (31 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_wearable_container()** (17 connections) — `server/commands/container_helpers_inventory_find.py`
- **UUID** (16 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_container_in_room()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **create_wearable_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_item_in_inventory()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_inner_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_instance_id()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **_player_for_wearable()** (12 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **try_inner_container_by_id()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_wearable_container_for_put()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_name()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_matching_equipped_containers()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_get_container_pair()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_try_put_container_for_equipped_item()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **check_item_matches_target()** (7 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_uuid()** (5 connections) — `server/commands/container_helpers_inventory_find.py`
- **Player** (5 connections) — `server/commands/container_helpers_inventory_find.py`
- **_component_metadata()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_container_from_equip_dict()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_fallback_create_equipment_container()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **_resolve_inner_uuid()** (4 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_find_wearable_container_falls_back_to_name_slot_match()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- *... and 60 more nodes in this community*

## Relationships

- [[Commands Container Inventory]] (12 shared connections)
- [[Admin Summon Command]] (8 shared connections)
- [[Communication Command Flows]] (5 shared connections)
- [[Container Inventory Ops]] (3 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)
- [[Room Occupancy Class]] (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 407 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
