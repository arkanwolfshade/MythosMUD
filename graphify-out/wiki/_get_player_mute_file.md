# ._get_player_mute_file

> 7 nodes · cohesion 0.29

## Key Concepts

- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UserManager](UserManager.md) (4 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [._cleanup_player_mutes](_cleanup_player_mutes.md) (1 shared connections)
- [.load_player_mutes](load_player_mutes.md) (1 shared connections)
- [chat_logger](chat_logger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*