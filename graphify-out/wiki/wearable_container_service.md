# wearable container service

> 36 nodes

## Key Concepts

- **test_wearable_container_service.py** (62 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **wearable_service()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_wearable_container_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_creates_new()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_unequip_wearable_container_preserves()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_unequip_wearable_container_not_found()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_inventory_full()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_no_room_id()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_existing_id_uuid()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_partial_spill()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_empty_overflow()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player_multiple_containers()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_unequip_wearable_container_empty_allowed_roles()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_dict_items()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_no_spilled_items()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_spilled_items_save_player()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_existing_container_no_metadata()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_existing_container_different_item_instance()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Unit tests for wearable container service.  Tests the WearableContainerService c** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Create WearableContainerService instance.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test WearableContainerService raises error when persistence is None.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container creates new container.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_unequip_wearable_container preserves container.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_unequip_wearable_container returns None when container not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_container_overflow drops to ground when inventory full.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [rate limiter rationale](rate_limiter_rationale.md) (14 shared connections)
- [room game service](room_game_service.md) (8 shared connections)
- [schedule services service](schedule_services_service.md) (5 shared connections)
- [game skill service](game_skill_service.md) (4 shared connections)
- [game room service](game_room_service.md) (4 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (3 shared connections)
- [room service game](room_service_game.md) (2 shared connections)
- [container events rationale](container_events_rationale.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*