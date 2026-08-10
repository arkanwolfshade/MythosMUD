# Catatonia Check Logic

> 61 nodes

## Key Concepts

- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (9 connections)
- **UUID** (8 connections)
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
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
- **.test_query_lucidity_record_success()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_slotted_state_object()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 36 more nodes in this community*

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (16 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)
- [Async Audit Cursor](Async_Audit_Cursor.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 174 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*