# NATS Message Handler Tests

> 14 nodes

## Key Concepts

- **test_command_factories.py** (59 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_command_factory_create_nonexistent_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_pose_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_reply_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_stand_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_cast_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_spells_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Unit tests for command factories.  Tests the CommandFactory class.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test CommandFactory.create_*() methods exist for all command types.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_pose_command delegates to communication factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_reply_command delegates to communication factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_stand_command delegates to exploration factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_cast_command delegates to utility factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_spells_command delegates to utility factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`

## Relationships

- [Mythosmud Obsidian Raw](Mythosmud_Obsidian_Raw.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [test_reconnect_attempts_increment](test_reconnect_attempts_increment.md) (1 shared connections)
- [test_get_stats_no_error](test_get_stats_no_error.md) (1 shared connections)
- [test_disconnect_from_connected](test_disconnect_from_connected.md) (1 shared connections)
- [test_should_idle_move_true_when_not_in_combat_and_probability_succeeds](test_should_idle_move_true_when_not_in_combat_and_probability_succeeds.md) (1 shared connections)
- [test_track_player_presence_new_player](test_track_player_presence_new_player.md) (1 shared connections)
- [test_can_attempt_connection_connected](test_can_attempt_connection_connected.md) (1 shared connections)
- [test_can_attempt_connection_circuit_open](test_can_attempt_connection_circuit_open.md) (1 shared connections)
- [test_time_until_retry_returns_zero_when_not_open](test_time_until_retry_returns_zero_when_not_open.md) (1 shared connections)
- [test_profession_meets_stat_requirements_empty_requirements](test_profession_meets_stat_requirements_empty_requirements.md) (1 shared connections)
- [test_last_connected_time_set](test_last_connected_time_set.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*