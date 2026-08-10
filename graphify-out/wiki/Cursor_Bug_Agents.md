# Cursor Bug Agents

> 18 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_valid_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Handler for NPC idle movement logic.      This class manages the decision-maki** (1 connections) — `server/npc/idle_movement.py`
- **Test IdleMovementHandler initialization fails without persistence.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when NPC is not alive.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() handles missing in_combat attribute.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When every target fails boundary validation, valid exits dict is empty.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with single exit.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _calculate_distance_to_room() with rooms in same subzone.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test execute_idle_movement() when no valid exits.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test execute_idle_movement() when no exit is selected.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [NPC Movement Integration](NPC_Movement_Integration.md) (19 shared connections)
- [Dual Connection Monitoring Guide](Dual_Connection_Monitoring_Guide.md) (9 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (9 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (4 shared connections)
- [Cursor Skills Arrange](Cursor_Skills_Arrange.md) (3 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (3 shared connections)
- [test_calculate_distance_to_room_different_rooms](test_calculate_distance_to_room_different_rooms.md) (1 shared connections)
- [test_calculate_distance_to_room_same_room](test_calculate_distance_to_room_same_room.md) (1 shared connections)
- [test_execute_idle_movement_no_current_room](test_execute_idle_movement_no_current_room.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)
- [test_get_valid_exits_filters_exits_outside_subzone](test_get_valid_exits_filters_exits_outside_subzone.md) (1 shared connections)
- [test_select_exit_empty_dict](test_select_exit_empty_dict.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 86 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*