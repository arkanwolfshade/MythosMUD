# NPCThreadManager

> 92 nodes

## Key Concepts

- **test_container_helpers_inventory_find.py** (56 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **container_helpers_inventory_find.py** (32 connections) — `server/commands/container_helpers_inventory_find.py`
- **container_helpers_inventory.py** (31 connections) — `server/commands/container_helpers_inventory.py`
- **asyncio** (19 connections)
- **find_wearable_container()** (17 connections) — `server/commands/container_helpers_inventory_find.py`
- **UUID** (16 connections)
- **try_wearable_container_service()** (14 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_container_in_room()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_instance_id()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **create_wearable_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_item_in_inventory()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_inner_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **_player_for_wearable()** (12 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **try_inner_container_by_id()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_wearable_container_service_by_name()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_wearable_container_for_put()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **_get_container_pair()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_matching_equipped_containers()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **_try_put_container_for_equipped_item()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **patch** (8 connections)
- **check_item_matches_target()** (7 connections) — `server/commands/container_helpers_inventory_find.py`
- **container_id()** (6 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_container_uuid()** (5 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_create_wearable_container_fallback_when_equip_returns_non_dict()** (5 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_uses_equip_dict_branch()** (5 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- *... and 67 more nodes in this community*

## Relationships

- [test_character_creation_service.py](test_character_creation_service.py.md) (15 shared connections)
- [ContainerComponent](ContainerComponent.md) (10 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (3 shared connections)
- [GameLogPanel.tsx](GameLogPanel.tsx.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (3 shared connections)
- [ClientLogger](ClientLogger.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_find.py`
- `server/commands/look_container.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 267 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*