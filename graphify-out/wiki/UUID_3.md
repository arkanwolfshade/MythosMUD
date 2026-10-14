# UUID

> 21 nodes

## Key Concepts

- **UUID** (13 connections)
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **Track a player's combat state. Args: player_id: ID of the player player_name:…** (1 connections) — `server/services/player_combat_service.py`
- **Get a player's combat state. Args: player_id: ID of the player Returns:…** (1 connections) — `server/services/player_combat_service.py`
- **Synchronously check if a player is currently in combat. This is the preferred…** (1 connections) — `server/services/player_combat_service.py`
- **Check if a player is currently in combat. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Get all players currently in combat. Returns: List of player IDs currently in…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat start for a player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Handle NPC death and award XP to the player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Award XP to a player for defeating an NPC. Delegates to LevelService.grant_xp…** (1 connections) — `server/services/player_combat_service.py`
- **Try to get XP reward from persistence lifecycle manager. Returns XP amount if…** (1 connections) — `server/services/player_combat_service.py`
- **Calculate XP reward for defeating an NPC. Args: npc_id: ID of the NPC (UUID…** (1 connections) — `server/services/player_combat_service.py`

## Relationships

- [PlayerCombatService](PlayerCombatService.md) (11 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (2 shared connections)
- [.clear_player_combat_state](clear_player_combat_state.md) (2 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*