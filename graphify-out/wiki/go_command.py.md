# go_command.py

> 80 nodes · cohesion 0.05

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (25 connections) — `server/tests/unit/commands/test_command_validation.py`
- **asyncio** (24 connections)
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (16 connections) — `server/command_handler/catatonia_check.py`
- **_check_all_command_blocks()** (16 connections) — `server/command_handler_unified.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (7 connections)
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **TestCheckAllCommandBlocks** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_PersistenceGetPlayerByName** (5 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **.test_check_catatonia_block_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_fetch_lucidity_record()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 55 more nodes in this community*

## Relationships

- [mapUtils.ts](mapUtils.ts.md) (16 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (6 shared connections)
- [session_factory](session_factory.md) (5 shared connections)
- [QuestService](QuestService.md) (5 shared connections)
- [PopulationStats](PopulationStats.md) (4 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (3 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [DialogueService](DialogueService.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 194 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*