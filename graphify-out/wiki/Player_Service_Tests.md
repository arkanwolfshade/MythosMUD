# Player Service Tests

> 12 nodes

## Key Concepts

- **test_combat_validator.py** (50 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_valid()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_attack_strength_success()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_random_error_message()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_random_error_message_unknown_type()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_combat_result_message_failure()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Unit tests for combat validator.  Tests the CombatValidator class for combat com** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test validate_combat_command with valid command.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test validate_attack_strength with successful validation.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test _get_random_error_message returns error message.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test _get_random_error_message with unknown error type.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test get_combat_result_message with failed attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Npc Idle Movement](Npc_Idle_Movement.md) (1 shared connections)
- [handle_player_left_room_impl](handle_player_left_room_impl.md) (1 shared connections)
- [.test_init](test_init.md) (1 shared connections)
- [test_get_player_info_invalid_player_id](test_get_player_info_invalid_player_id.md) (1 shared connections)
- [.test_get_combat_start_messages_single_occupant](test_get_combat_start_messages_single_occupant.md) (1 shared connections)
- [.test_init_with_failover_callback](test_init_with_failover_callback.md) (1 shared connections)
- [.test_on_catatonia_entered_with_uuid](test_on_catatonia_entered_with_uuid.md) (1 shared connections)
- [test_normalize_event_ids_both_provided](test_normalize_event_ids_both_provided.md) (1 shared connections)
- [.test_should_trigger_sanitarium_failover_never_triggered](test_should_trigger_sanitarium_failover_never_triggered.md) (1 shared connections)
- [.test_should_trigger_sanitarium_failover_within_debounce_window](test_should_trigger_sanitarium_failover_within_debounce_window.md) (1 shared connections)
- [test_normalize_event_ids_string_ids](test_normalize_event_ids_string_ids.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*