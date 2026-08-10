# Commands Time

> 7 nodes

## Key Concepts

- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`

## Relationships

- [Player Mute Persistence](Player_Mute_Persistence.md) (4 shared connections)
- [chat_logger](chat_logger.md) (1 shared connections)
- [Async Migration Gotchas](Async_Migration_Gotchas.md) (1 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (1 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*