# Catatonia Check

> 52 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **get_cached_player()** (13 connections) — `server/utils/player_cache.py`
- **cache_player()** (11 connections) — `server/utils/player_cache.py`
- **test_player_cache.py** (11 connections) — `server/tests/unit/utils/test_player_cache.py`
- **check_catatonia_block()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (7 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (7 connections)
- **player_cache.py** (7 connections) — `server/utils/player_cache.py`
- **_check_catatonia_database()** (6 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (6 connections) — `server/command_handler/catatonia_check.py`
- **_get_request_state()** (6 connections) — `server/utils/player_cache.py`
- **_PersistenceGetPlayerByName** (5 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (5 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (4 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (4 connections) — `server/command_handler/catatonia_check.py`
- **test_cache_and_get_player()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_multiple()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_overwrite()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_none()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_nonexistent()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Any** (3 connections)
- *... and 27 more nodes in this community*

## Relationships

- [Lucidity & Rescue Service](Lucidity_&_Rescue_Service.md) (5 shared connections)
- [Test Request Context](Test_Request_Context.md) (3 shared connections)
- [Test Command Input](Test_Command_Input.md) (2 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Catatonia Registry](Test_Catatonia_Registry.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Test Command Validation](Test_Command_Validation.md) (1 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/utils/test_player_cache.py`
- `server/utils/player_cache.py`

## Audit Trail

- EXTRACTED: 104 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*