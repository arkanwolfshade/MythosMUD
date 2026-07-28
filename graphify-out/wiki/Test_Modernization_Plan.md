# Test Modernization Plan

> 51 nodes · cohesion 0.06

## Key Concepts

- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_presence_statistics_impl()** (8 connections) — `server/realtime/connection_statistics.py`
- **Any** (5 connections)
- **.get_presence_statistics()** (4 connections) — `server/realtime/connection_manager.py`
- **test_get_online_player_by_display_name_impl_case_insensitive()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_found()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_no_name()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_online_player_by_display_name_impl_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_player_presence_info_impl_no_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_player_presence_info_impl_not_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_player_presence_info_impl_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_presence_statistics_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_presence_statistics_impl_no_players()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl_empty_sessions()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_connection_count_mismatch()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_connections_but_not_online()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_consistent()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_validate_player_presence_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- *... and 26 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (10 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 167 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*