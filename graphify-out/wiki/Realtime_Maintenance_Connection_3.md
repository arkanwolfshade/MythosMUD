# Realtime Maintenance Connection

> 11 nodes · cohesion 0.22

## Key Concepts

- **Any** (15 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return connection IDs that exceed max_connection_age.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Extract player_id from connection metadata if present.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Close stale WebSocket and remove from tracking. Handles None websocket defensive** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up orphaned data that might accumulate over time.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Initialize the connection cleaner.          Args:             memory_monitor: Me** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [[Realtime Maintenance Connection]] (17 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
