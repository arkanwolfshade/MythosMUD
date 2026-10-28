# StatusEffect

> 29 nodes · cohesion 0.13

## Key Concepts

- **NPCMovementIntegration** (52 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (29 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_direct_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_returns_none_without_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_available_exits_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_destination_subzone_from_room_id()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_npc_room_returns_none()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_destination()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_room()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_init_requires_persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_is_npc_in_combat_true()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_blocked_in_combat()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_exception_returns_false()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_to_room_success()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_handles_publish_error()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_publish_movement_events_skips_without_bus()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_update_npc_instance_room_tracking()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_update_room_occupancy_skips_when_already_placed()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_npc_movement()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_npc_movement_npc_not_in_source()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_room_ids_rejects_empty_or_same()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_validate_subzone_boundary()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 4 more nodes in this community*

## Relationships

- [Interaction Design](Interaction_Design.md) (6 shared connections)
- [BaseEvent](BaseEvent.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [Who Command Enhancement](Who_Command_Enhancement.md) (2 shared connections)
- [._publish_attack_event](_publish_attack_event.md) (1 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (1 shared connections)
- [test_process_mortally_wounded_tick_already_dead](test_process_mortally_wounded_tick_already_dead.md) (1 shared connections)
- [test_process_mortally_wounded_tick_caps_at_negative_10](test_process_mortally_wounded_tick_caps_at_negative_10.md) (1 shared connections)
- [test_process_mortally_wounded_tick_publishes_event](test_process_mortally_wounded_tick_publishes_event.md) (1 shared connections)
- [test_process_mortally_wounded_tick_player_not_found](test_process_mortally_wounded_tick_player_not_found.md) (1 shared connections)
- [test_handle_learn_command_success](test_handle_learn_command_success.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 77 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*