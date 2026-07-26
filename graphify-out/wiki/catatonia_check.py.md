# catatonia_check.py

> 76 nodes · cohesion 0.04

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (9 connections)
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (8 connections)
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections)
- **.test_check_catatonia_block_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 51 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (14 shared connections)
- [processing.py](processing.py.md) (6 shared connections)
- [get_cached_player](get_cached_player.md) (5 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (4 shared connections)
- [command_input.py](command_input.py.md) (4 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_check_grace_period_block](_check_grace_period_block.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [lucidity.py](lucidity.py.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 283 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*