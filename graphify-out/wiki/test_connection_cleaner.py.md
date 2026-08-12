# test_connection_cleaner.py

> 29 nodes

## Key Concepts

- **test_connection_cleaner.py** (22 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **fixture** (8 connections)
- **connection_cleaner()** (4 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_cleanup_dead_websocket()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_get_async_persistence()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_message_queue()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_rate_limiter()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_cleanup_ghost_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_connection_cleaner_init()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_not_stale()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_prune_stale_players_with_websockets()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Unit tests for connection cleaner. Tests the ConnectionCleaner class.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() does not remove recent players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() preserves players with active websockets.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_ghost_players() removes ghost players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock memory monitor.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock rate limiter.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock message queue.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock cleanup_dead_websocket callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Create a mock has_websocket_connection callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- *... and 4 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (4 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (2 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*