# Follow Service Tests

> 57 nodes

## Key Concepts

- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_presence_statistics_impl()** (8 connections) — `server/realtime/connection_statistics.py`
- **.get_player_presence_info()** (5 connections) — `server/realtime/connection_manager.py`
- **.validate_player_presence()** (5 connections) — `server/realtime/connection_manager.py`
- **Any** (5 connections)
- **.get_session_stats()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_presence_statistics()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_online_player_by_display_name()** (4 connections) — `server/realtime/connection_manager.py`
- **test_get_player_presence_info_impl_not_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_player_presence_info_impl_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_player_presence_info_impl_no_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_consistent()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_online_but_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_connections_but_not_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_connection_count_mismatch()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_presence_statistics_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_presence_statistics_impl_no_players()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_found()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_case_insensitive()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- *... and 32 more nodes in this community*

## Relationships

- [Archive Bug Fix](Archive_Bug_Fix.md) (12 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (5 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 177 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*