# command validation commands

> 84 nodes

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
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **CommandExecutionRequest** (9 connections)
- **request_context.py** (9 connections) — `server/realtime/request_context.py`
- **UUID** (8 connections)
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **CommandExecutionRequest** (3 connections)
- **.test_registry_player_id_value_preserves_uuid_and_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_registry_player_id_value_stringifies_non_string_ids()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 59 more nodes in this community*

## Relationships

- [command handler unified](command_handler_unified.md) (18 shared connections)
- [request context realtime](request_context_realtime.md) (6 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (5 shared connections)
- [player cache rationale](player_cache_rationale.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [command handler processing](command_handler_processing.md) (3 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)
- [command commands validation](command_commands_validation.md) (2 shared connections)
- [commands command validation](commands_command_validation.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 314 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*