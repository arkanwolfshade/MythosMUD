# Test Refactoring Summary

> 33 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **get_cached_player()** (15 connections) — `server/utils/player_cache.py`
- **cache_player()** (13 connections) — `server/utils/player_cache.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **test_player_cache.py** (11 connections) — `server/tests/unit/utils/test_player_cache.py`
- **player_cache.py** (7 connections) — `server/utils/player_cache.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_get_request_state()** (6 connections) — `server/utils/player_cache.py`
- **test_cache_and_get_player()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_multiple()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_overwrite()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_none()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_nonexistent()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Any** (3 connections)
- **.get_player_by_name()** (2 connections) — `server/command_handler/catatonia_check.py`
- **Protocol** (1 connections)
- **Catatonia Checking Logic for MythosMUD.  This module handles checking whether** (1 connections) — `server/command_handler/catatonia_check.py`
- **Minimal persistence surface used by catatonia load path.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Load player for catatonia check, using cache if available.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Unit tests for player_cache utilities.  Tests the player caching functions for r** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test get_cached_player() returns None when no cache exists.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test cache_player() and get_cached_player() operations.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test get_cached_player() returns None for nonexistent key.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- *... and 8 more nodes in this community*

## Relationships

- [Catatonia Check Logic](Catatonia_Check_Logic.md) (11 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (6 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (1 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/utils/test_player_cache.py`
- `server/utils/player_cache.py`

## Audit Trail

- EXTRACTED: 137 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*