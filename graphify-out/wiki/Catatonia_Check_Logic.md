# Catatonia Check Logic

> 70 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
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
- **.test_query_lucidity_record_success()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 45 more nodes in this community*

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (9 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (5 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (4 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (4 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (1 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 258 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*