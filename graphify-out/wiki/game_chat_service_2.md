# game chat service

> 36 nodes

## Key Concepts

- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
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
- **test_get_online_player_by_display_name_impl_no_name()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **test_get_session_stats_impl_empty_sessions()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Unit tests for connection statistics.  Tests the connection_statistics module fu** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test get_player_presence_info_impl() returns offline info when player not online** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test get_player_presence_info_impl() returns online info when player is online.** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test get_player_presence_info_impl() handles player with no websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test validate_player_presence_impl() returns consistent when player is consisten** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test validate_player_presence_impl() fixes player marked online but has no conne** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test validate_player_presence_impl() detects player with connections but not mar** (1 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- *... and 11 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (23 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 93 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*