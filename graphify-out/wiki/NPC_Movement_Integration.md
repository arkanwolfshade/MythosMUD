# NPC Movement Integration

> 26 nodes

## Key Concepts

- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_true()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_no_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_multiple_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Unit tests for idle movement.  Tests the IdleMovementHandler class.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Create an IdleMovementHandler instance.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test IdleMovementHandler initialization.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when idle movement is disabled.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() respects movement probability (random > threshold fails)** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() when NPC is in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() returns False when NPC is not in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test get_valid_exits() when NPC definition has no sub_zone_id.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When validate_subzone_boundary accepts every target, all directions remain avail** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with multiple exits.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 1 more nodes in this community*

## Relationships

- [Cursor Bug Agents](Cursor_Bug_Agents.md) (19 shared connections)
- [Dual Connection Monitoring Guide](Dual_Connection_Monitoring_Guide.md) (1 shared connections)
- [test_calculate_distance_to_room_different_rooms](test_calculate_distance_to_room_different_rooms.md) (1 shared connections)
- [test_calculate_distance_to_room_same_room](test_calculate_distance_to_room_same_room.md) (1 shared connections)
- [test_execute_idle_movement_no_current_room](test_execute_idle_movement_no_current_room.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)
- [test_get_valid_exits_filters_exits_outside_subzone](test_get_valid_exits_filters_exits_outside_subzone.md) (1 shared connections)
- [test_select_exit_empty_dict](test_select_exit_empty_dict.md) (1 shared connections)
- [test_select_exit_weighted_home_disabled](test_select_exit_weighted_home_disabled.md) (1 shared connections)
- [test_should_idle_move_false_when_registered_in_combat](test_should_idle_move_false_when_registered_in_combat.md) (1 shared connections)
- [test_should_idle_move_not_active](test_should_idle_move_not_active.md) (1 shared connections)
- [test_should_idle_move_probability_fails_when_random_above_threshold](test_should_idle_move_probability_fails_when_random_above_threshold.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*