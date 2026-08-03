# idle movement npc

> 48 nodes

## Key Concepts

- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_empty_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_no_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_filters_exits_outside_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_weighted_home_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_rooms()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_calculate_distance_to_room_different_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_valid_exits()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_execute_idle_movement_no_exit_selected()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Unit tests for idle movement.  Tests the IdleMovementHandler class.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 23 more nodes in this community*

## Relationships

- [idle npc movement](idle_npc_movement.md) (23 shared connections)
- [npc idle movement](npc_idle_movement.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)
- [realtime maintenance rationale](realtime_maintenance_rationale.md) (1 shared connections)
- [models profession repr](models_profession_repr.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*