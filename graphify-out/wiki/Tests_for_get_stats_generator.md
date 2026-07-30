# Tests for get stats generator

> 10 nodes

## Key Concepts

- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **._serialize_mute_info_for_json()** (5 connections) — `server/services/user_manager.py`
- **._save_player_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_channel_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_global_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **Convert mute_info datetime and UUID objects to JSON-serializable formats.** (1 connections) — `server/services/user_manager.py`
- **Save player mutes to data dictionary for JSON serialization.** (1 connections) — `server/services/user_manager.py`
- **Save channel mutes to data dictionary for JSON serialization.** (1 connections) — `server/services/user_manager.py`
- **Save global mutes applied by this player to data dictionary for JSON serializati** (1 connections) — `server/services/user_manager.py`
- **Save mute data for a specific player to JSON file.          Args:** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UUID](UUID.md) (16 shared connections)
- [MythosValidationError](MythosValidationError.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*