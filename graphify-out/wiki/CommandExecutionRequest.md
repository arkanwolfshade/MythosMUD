# CommandExecutionRequest

> 72 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
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

- [check alias safety()](check_alias_safety%28%29.md) (9 shared connections)
- [test movement service](test_movement_service.md) (8 shared connections)
- [parse json field()](parse_json_field%28%29.md) (6 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [.add alias()](add_alias%28%29.md) (5 shared connections)
- [.get uuid mapping()](get_uuid_mapping%28%29.md) (4 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [cleanup dead connections()](cleanup_dead_connections%28%29_2.md) (1 shared connections)
- [websocket handler connection](websocket_handler_connection.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 272 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*