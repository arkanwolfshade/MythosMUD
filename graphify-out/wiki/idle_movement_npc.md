# idle movement npc

> 70 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_true()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_false()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_is_npc_in_combat_no_attribute()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_empty_room()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_no_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_filters_exits_outside_subzone()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_all_exits_invalid_subzone_returns_empty()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_empty_dict()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 45 more nodes in this community*

## Relationships

- [idle npc movement](idle_npc_movement.md) (11 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (7 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [player schemas requests](player_schemas_requests.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [command input commands](command_input_commands.md) (1 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 223 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*