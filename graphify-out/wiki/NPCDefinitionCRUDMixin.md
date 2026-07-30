# NPCDefinitionCRUDMixin

> 21 nodes

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Any** (15 connections)
- **.cleanup_ghost_players()** (9 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_orphaned_data()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._close_and_remove_stale_websocket()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_player_id_from_metadata()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_connections()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Manages connection cleanup and maintenance operations.      This class provides:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return connection IDs that exceed max_connection_age.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Extract player_id from connection metadata if present.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Close stale WebSocket and remove from tracking. Handles None websocket defensive** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up orphaned data that might accumulate over time.          Args:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return set of online player IDs as strings (room._players uses string UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return players in room but not online. Empty if room has no get_players.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Filter to players with zero WebSocket connections (or invalid UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove ghost players from room and log.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up ghost players from all rooms.          This method removes players from** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`

## Relationships

- [Reset database state before each](Reset_database_state_before_each.md) (11 shared connections)
- [real time](real_time.md) (5 shared connections)
- [occupation slots 9()](occupation_slots_9%28%29.md) (5 shared connections)
- [Test check grace period block](Test_check_grace_period_block.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [generate invites](generate_invites.md) (2 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)
- [.get stats()](get_stats%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 94 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*