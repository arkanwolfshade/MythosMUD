# .respawn_player_by_user_id

> 18 nodes

## Key Concepts

- **.respawn_player_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **_select_dead_player_for_respawn()** (6 connections) — `server/game/player_respawn_wrapper.py`
- **._load_active_players()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **._load_player_for_delirium_respawn()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **_resolve_respawn_room_data()** (5 connections) — `server/game/player_respawn_wrapper.py`
- **_is_eligible_for_respawn()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (4 connections)
- **Player** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a dead player by user ID. This method handles the complete respawn…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Load the user's character and validate delirium eligibility (lucidity <= -10).** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a delirious player by user ID. This method handles the complete…** (1 connections) — `server/game/player_respawn_wrapper.py`
- **A player is eligible for respawn if dead, or stranded in limbo.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Pick the most-recently-active eligible (dead/limbo) character for this user.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Look up the respawn room, falling back to a placeholder if it's missing.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Initialize with a persistence layer.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Load all non-deleted characters for a user (multi-character support).** (1 connections) — `server/game/player_respawn_wrapper.py`

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (5 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*