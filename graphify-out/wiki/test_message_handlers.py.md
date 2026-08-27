# test_message_handlers.py

> 79 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (24 connections) — `server/tests/unit/commands/test_command_validation.py`
- **asyncio** (24 connections)
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (14 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (7 connections)
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
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
- **.test_load_player_for_catatonia_check_from_cache()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_connection_statistics.py](test_connection_statistics.py.md) (8 shared connections)
- [run_flee_effect](run_flee_effect.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (6 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (5 shared connections)
- [Second NPC Combat And Linkdead Findings](Second_NPC_Combat_And_Linkdead_Findings.md) (5 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [Chat Panel](Chat_Panel.md) (2 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (2 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (1 shared connections)
- [Call of Cthulhu Starter Set (source summary)](Call_of_Cthulhu_Starter_Set_source_summary.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 181 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*