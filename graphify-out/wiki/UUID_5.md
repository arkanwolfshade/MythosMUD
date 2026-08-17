# UUID

> 29 nodes

## Key Concepts

- **UUID** (15 connections)
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **.save_player()** (4 connections) — `server/services/player_position_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **Track a player's combat state. Args: player_id: ID of the player player_name:…** (1 connections) — `server/services/player_combat_service.py`
- **Get a player's combat state. Args: player_id: ID of the player Returns:…** (1 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state. Args: player_id: ID of the player** (1 connections) — `server/services/player_combat_service.py`
- **Synchronously check if a player is currently in combat. This is the preferred…** (1 connections) — `server/services/player_combat_service.py`
- **Check if a player is currently in combat. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Get all players currently in combat. Returns: List of player IDs currently in…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat start for a player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat end by clearing all players in the combat. Args: combat_id: ID of…** (1 connections) — `server/services/player_combat_service.py`
- **Handle NPC death and award XP to the player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Return True if the NPC rewards path handled the award (success or logged…** (1 connections) — `server/services/player_combat_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (14 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (2 shared connections)
- [_JSONDict](_JSONDict.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (1 shared connections)
- [.change_position](change_position.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 53 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*