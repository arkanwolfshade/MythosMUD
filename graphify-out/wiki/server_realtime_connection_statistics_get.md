# server realtime connection statistics get

> 46 nodes

## Key Concepts

- **test_connection_statistics.py** (25 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **validate_player_presence_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_online_player_by_display_name_impl()** (8 connections) — `server/realtime/connection_statistics.py`
- **get_player_presence_info_impl()** (7 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (7 connections) — `server/realtime/connection_statistics.py`
- **get_presence_statistics_impl()** (6 connections) — `server/realtime/connection_statistics.py`
- **Any** (5 connections)
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
- **test_validate_player_presence_impl_online_but_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **Test get_player_presence_info_impl() returns offline info when player not…** (2 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- *... and 21 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*