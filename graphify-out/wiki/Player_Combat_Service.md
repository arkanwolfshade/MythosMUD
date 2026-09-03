# Player Combat Service

> 25 nodes

## Key Concepts

- **UUID** (15 connections)
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_persistence_fallback()** (6 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **.get_players_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat()** (3 connections) — `server/services/player_combat_service.py`
- **.is_player_in_combat_sync()** (3 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state. Args: player_id: ID of the player** (1 connections) — `server/services/player_combat_service.py`
- **Synchronously check if a player is currently in combat. This is the preferred…** (1 connections) — `server/services/player_combat_service.py`
- **Check if a player is currently in combat. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Get all players currently in combat. Returns: List of player IDs currently in…** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat end by clearing all players in the combat. Args: combat_id: ID of…** (1 connections) — `server/services/player_combat_service.py`
- **Handle NPC death and award XP to the player. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Return True if the NPC rewards path handled the award (success or logged…** (1 connections) — `server/services/player_combat_service.py`
- **Fallback: load player, add XP, save, publish (used without integration in…** (1 connections) — `server/services/player_combat_service.py`
- **Award XP to a player for defeating an NPC. Args: player_id: ID of the player…** (1 connections) — `server/services/player_combat_service.py`
- **Try to get XP reward from persistence lifecycle manager. Returns XP amount if…** (1 connections) — `server/services/player_combat_service.py`
- **Calculate XP reward for defeating an NPC. Args: npc_id: ID of the NPC (UUID…** (1 connections) — `server/services/player_combat_service.py`
- **Clean up stale combat states. Returns: Number of stale states cleaned up** (1 connections) — `server/services/player_combat_service.py`

## Relationships

- [Test Player Combat Service](Test_Player_Combat_Service.md) (15 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (1 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (1 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*