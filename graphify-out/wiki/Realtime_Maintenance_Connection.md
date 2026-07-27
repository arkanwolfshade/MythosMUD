# Realtime Maintenance Connection

> 16 nodes · cohesion 0.16

## Key Concepts

- **ConnectionCleaner** (28 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_ghost_players()** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._filter_actual_ghost_players()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_online_player_ids()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_potential_ghost_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_ghost_players_from_room()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **connection_cleaner()** (3 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **__init__.py** (3 connections) — `server/realtime/maintenance/__init__.py`
- **Return set of online player IDs as strings (room._players uses string UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return players in room but not online. Empty if room has no get_players.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Filter to players with zero WebSocket connections (or invalid UUIDs).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove ghost players from room and log.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up ghost players from all rooms.          This method removes players from** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Manages connection cleanup and maintenance operations.      This class provides:** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Create a ConnectionCleaner instance.** (1 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **Maintenance components for connection management.  This package provides modular** (1 connections) — `server/realtime/maintenance/__init__.py`

## Relationships

- [[Realtime Maintenance Connection]] (22 shared connections)
- [[Room Occupant Events]] (5 shared connections)
- [[Connection Cleaner Tests]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/realtime/maintenance/__init__.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`

## Audit Trail

- EXTRACTED: 67 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
