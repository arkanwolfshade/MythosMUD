# Community 788

> 21 nodes

## Key Concepts

- **ConnectionCleaner** (27 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **UUID** (10 connections)
- **.prune_stale_players()** (7 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.cleanup_dead_connections()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._cleanup_dead_connections_for_player()** (6 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._remove_stale_player_data()** (5 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._get_players_to_check()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._identify_stale_players()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **.__init__()** (4 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **._is_websocket_dead()** (3 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **server/realtime/maintenance/__init__.py** (3 connections) — `server/realtime/maintenance/__init__.py`
- **Identify players whose last_seen timestamp exceeds the max age. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove all data for a stale player. Args: pid: Player ID to remove…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Remove players whose presence is stale beyond the threshold. Args: last_seen:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return True if websocket appears dead (should be cleaned up).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Return list of player IDs to check (single player or all).** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a single player.** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Clean up dead connections for a specific player or all players. Args:…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Manages connection cleanup and maintenance operations. This class provides: -…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Initialize the connection cleaner. Args: memory_monitor: MemoryMonitor instance…** (1 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **Maintenance components for connection management. This package provides modular…** (1 connections) — `server/realtime/maintenance/__init__.py`

## Relationships

- [Community 843](Community_843.md) (16 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 1328](Community_1328.md) (3 shared connections)
- [Community 591](Community_591.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)
- [Community 910](Community_910.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/__init__.py`
- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 56 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*