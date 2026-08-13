# test_idle_movement.py

> 28 nodes

## Key Concepts

- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_current_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_valid_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_empty_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_no_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_weighted_home_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Unit tests for idle movement. Tests the IdleMovementHandler class.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() returns False when NPC is not in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() handles missing in_combat attribute.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test get_valid_exits() with room having no exits.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test get_valid_exits() when NPC definition has no sub_zone_id.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When every target fails boundary validation, valid exits dict is empty.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When validate_subzone_boundary accepts every target, all directions remain…** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with weighted_home disabled.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _calculate_distance_to_room() with same room.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _calculate_distance_to_room() with different rooms.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _calculate_distance_to_room() with rooms in different subzones.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 3 more nodes in this community*

## Relationships

- [IdleMovementHandler](IdleMovementHandler.md) (19 shared connections)
- [patch](patch.md) (8 shared connections)
- [idle_movement_handler](idle_movement_handler.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_select_exit_empty_dict](test_select_exit_empty_dict.md) (1 shared connections)
- [test_calculate_distance_to_room_same_subzone](test_calculate_distance_to_room_same_subzone.md) (1 shared connections)
- [test_idle_movement_handler_init](test_idle_movement_handler_init.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*