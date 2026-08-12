# .load_player_mutes

> 19 nodes

## Key Concepts

- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._load_channel_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **._convert_mute_info_uuids()** (4 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Convert timestamp strings in mute_info to datetime objects.** (1 connections) — `server/services/user_manager.py`
- **Convert UUID strings in mute_info to UUID objects.** (1 connections) — `server/services/user_manager.py`
- **Load player mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load channel mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load global mutes from JSON data into memory.** (1 connections) — `server/services/user_manager.py`
- **Load mute data for a specific player from JSON file. Args: player_id: Player ID…** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management. Uses…** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager. Args: data_dir: Directory for player-specific mute…** (1 connections) — `server/services/user_manager.py`

## Relationships

- [Player Mute Persistence](Player_Mute_Persistence.md) (18 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [._cleanup_player_mutes](_cleanup_player_mutes.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 63 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*