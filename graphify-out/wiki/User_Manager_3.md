# User Manager

> 16 nodes

## Key Concepts

- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._load_channel_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_uuids()** (4 connections) — `server/services/user_manager.py`
- **._resolve_player_mute_vs_target()** (4 connections) — `server/services/user_manager.py`
- **Convert timestamp strings in mute_info to datetime objects.** (1 connections) — `server/services/user_manager.py`
- **Convert UUID strings in mute_info to UUID objects.** (1 connections) — `server/services/user_manager.py`
- **Load player mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load channel mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load global mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load mute data for a specific player from JSON file. Args: player_id: Player ID…** (1 connections) — `server/services/user_manager.py`
- **Classify mute state for (player_id -> target_id). Removes expired entries. AI:…** (1 connections) — `server/services/user_manager.py`
- **Check if a player has muted another player. Args: player_id: Player ID…** (1 connections) — `server/services/user_manager.py`

## Relationships

- [User Manager](User_Manager.md) (19 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*