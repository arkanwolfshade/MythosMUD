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

- [player event state](player_event_state.md) (14 shared connections)
- [npc combat service](npc_combat_service.md) (5 shared connections)
- [player cache rationale](player_cache_rationale.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [test_validate_combat_state_in_combat_not_required](test_validate_combat_state_in_combat_not_required.md) (1 shared connections)
- [test_validate_attack_strength_weak_weapon](test_validate_attack_strength_weak_weapon.md) (1 shared connections)
- [test_broadcast_combat_error](test_broadcast_combat_error.md) (1 shared connections)
- [test_combat_validator_init](test_combat_validator_init.md) (1 shared connections)
- [test_validate_attack_strength_target_too_strong](test_validate_attack_strength_target_too_strong.md) (1 shared connections)
- [test_validate_attack_strength_target_significantly_stronger](test_validate_attack_strength_target_significantly_stronger.md) (1 shared connections)
- [test_broadcast_player_mortally_wounded_with_attacker](test_broadcast_player_mortally_wounded_with_attacker.md) (1 shared connections)
- [test_broadcast_player_mortally_wounded_no_attacker](test_broadcast_player_mortally_wounded_no_attacker.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*