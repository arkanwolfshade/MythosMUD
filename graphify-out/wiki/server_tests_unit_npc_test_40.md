# server tests unit npc test

> 60 nodes

## Key Concepts

- **test_idle_movement.py** (36 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **patch** (8 connections)
- **test_is_npc_in_combat_true()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_same_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_current_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_valid_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_empty_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_filters_exits_outside_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_no_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 35 more nodes in this community*

## Relationships

- [server npc idle movement](server_npc_idle_movement.md) (31 shared connections)
- [server tests unit npc test](server_tests_unit_npc_test.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 73 (72%)
- INFERRED: 29 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*