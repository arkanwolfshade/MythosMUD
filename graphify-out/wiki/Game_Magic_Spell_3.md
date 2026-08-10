# Game Magic Spell

> 12 nodes

## Key Concepts

- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_uuids()** (5 connections) — `server/services/user_manager.py`
- **._load_channel_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **Convert timestamp strings in mute_info to datetime objects.** (1 connections) — `server/services/user_manager.py`
- **Convert UUID strings in mute_info to UUID objects.** (1 connections) — `server/services/user_manager.py`
- **Load player mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load channel mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load global mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load mute data for a specific player from JSON file.          Args:** (1 connections) — `server/services/user_manager.py`

## Relationships

- [Player Mute Persistence](Player_Mute_Persistence.md) (16 shared connections)
- [Commands Time](Commands_Time.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*