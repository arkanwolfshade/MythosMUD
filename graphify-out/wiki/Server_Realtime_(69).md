# Server Realtime (69)

> 24 nodes

## Key Concepts

- **test_connection_cleaner.py** (22 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **test_check_and_cleanup()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_memory_monitor()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **mock_has_websocket_connection()** (2 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
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
- **Create a mock has_websocket_connection callback.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test ConnectionCleaner initialization.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() removes stale players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() does not remove recent players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test prune_stale_players() preserves players with active websockets.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_orphaned_data() cleans up orphaned data.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_dead_connections() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test cleanup_ghost_players() removes ghost players.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test force_cleanup() performs forced cleanup.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Test check_and_cleanup() performs cleanup check.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Relationships

- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (2 shared connections)
- [Server Realtime (45)](Server_Realtime_%2845%29.md) (1 shared connections)
- [Server Realtime (134)](Server_Realtime_%28134%29.md) (1 shared connections)
- [Server Realtime (135)](Server_Realtime_%28135%29.md) (1 shared connections)
- [Server Realtime (136)](Server_Realtime_%28136%29.md) (1 shared connections)
- [Server Realtime (137)](Server_Realtime_%28137%29.md) (1 shared connections)
- [Server Realtime (138)](Server_Realtime_%28138%29.md) (1 shared connections)
- [Server Realtime (139)](Server_Realtime_%28139%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*