# Catatonia Check Logic

> 86 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (9 connections)
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
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
- *... and 61 more nodes in this community*

## Relationships

- [Admin Teleport Commands](Admin_Teleport_Commands.md) (16 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (9 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (5 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (5 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Container Open Events](Container_Open_Events.md) (2 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (2 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (2 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 319 (94%)
- INFERRED: 19 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*