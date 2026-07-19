# Catatonia Check Logic

> 69 nodes · cohesion 0.05

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (16 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (11 connections) — `server/command_handler/command_execution_request.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (4 connections) — `server/command_handler/catatonia_check.py`
- **PlayerLucidity** (4 connections) — `server/command_handler/catatonia_check.py`
- **.test_check_catatonia_block_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_slotted_state_object()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 44 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (10 shared connections)
- [[Command Request App State]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Player Cache]] (5 shared connections)
- [[Command Commands Validation]] (5 shared connections)
- [[Lucidity Database Models]] (2 shared connections)
- [[Grace Period Blocking Tests]] (2 shared connections)
- [[Player Combat XP]] (1 shared connections)
- [[Unified Command Handler]] (1 shared connections)
- [[Commands Command Validation]] (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 260 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
