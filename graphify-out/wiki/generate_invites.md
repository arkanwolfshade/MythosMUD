# generate invites

> 36 nodes

## Key Concepts

- **test_connection_cleaner.py** (22 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **connection_cleaner()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_rate_limiter()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_message_queue()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_cleanup_dead_websocket()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_connection_cleaner_init()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_not_stale()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_with_websockets()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_orphaned_data()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_dead_connections()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_force_cleanup()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Unit tests for connection cleaner.  Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock memory monitor.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock rate limiter.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock message queue.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock cleanup_dead_websocket callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock has_websocket_connection callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 11 more nodes in this community*

## Relationships

- [Player](Player.md) (2 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*