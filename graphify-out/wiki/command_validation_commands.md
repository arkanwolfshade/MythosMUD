# command validation commands

> 72 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (9 connections)
- **UUID** (8 connections)
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections)
- **.test_registry_player_id_value_preserves_uuid_and_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_registry_player_id_value_stringifies_non_string_ids()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_tier()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_zero_lcd()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_negative_lcd()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_none()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_fetch_lucidity_record()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 47 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (10 shared connections)
- [request context realtime](request_context_realtime.md) (6 shared connections)
- [player game schema](player_game_schema.md) (5 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (4 shared connections)
- [combat npc services](combat_npc_services.md) (3 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (3 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (2 shared connections)
- [command player state](command_player_state.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 272 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*